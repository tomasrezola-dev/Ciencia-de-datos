from wget import download
import os
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import seaborn as sns
import pandas as pd

def descarga(csv, name_csv, ej):
    ruta_archivo = os.path.join(name_csv)
    if not os.path.exists(ruta_archivo):
        download(csv)
    else:
        print("No vamos a bajar el archivo porque ya existe")


def box_plot(cuali, cuanti, df, ord=False):
    df.boxplot(
        column=cuanti,
        by=cuali,
        figsize=(10, 6),
        grid=True,
        patch_artist=True,
        medianprops={'color': 'orange', 'linewidth': 3} # Resalta la línea de la mediana
    )
    plt.title(f"Relación entre {cuali} y {cuanti}")
    plt.suptitle('')
    plt.xlabel(cuali, fontsize=12)
    plt.ylabel(cuanti, fontsize=12)

    if ord:
        ff = df[cuali].cat.codes #convertimos las categorias a numerico para spearman
        sp = ff.corr(df[cuanti], method='spearman')
    if ord and sp >= 0:
        plt.text(
            x=0.95, y=0.95,
            s=(f'spearman: {round(sp, 4)}'),
            transform=plt.gca().transAxes,
            fontsize=11,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(
                boxstyle='round,pad=0.5', 
                facecolor='white', 
                edgecolor='orange', 
                alpha=0.9
            ) 
        )
    plt.show()


def scatter_plot(cuanti1, cuanti2, df):

    df_limpio = df[[cuanti1, cuanti2]].dropna()
    plt.figure(figsize=(6, 6))
    plt.scatter(df_limpio[cuanti1], df_limpio[cuanti2], alpha=0.7)
    plt.xlabel(cuanti1)
    plt.ylabel(cuanti2)
    
    plt.title(f"Relación entre {cuanti1} y {cuanti2}")

    coeficiente_correlacion, p_value = stats.pearsonr(df_limpio[cuanti1], df_limpio[cuanti2])
    
    plt.legend([f"Correlación: {coeficiente_correlacion:.4f}"], loc="upper left")

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def histograma(df, cuanti, cajas=20):
    datos_limpios = df[cuanti].dropna()
    
    plt.figure(figsize=(8, 5))
    
    plt.hist(datos_limpios, bins=cajas, color='steelblue', edgecolor='black', alpha=0.8)
    
    plt.title(f"Distribución de {cuanti}")
    plt.xlabel(cuanti)
    plt.ylabel("Frecuencia")
    
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def heatmap(df, val=True):
    correlation_matrix = df.corr(numeric_only=val)

    # imprimimos la matriz como un heatmap
    plt.figure(figsize=(16,12))
    sns.heatmap(correlation_matrix, vmin=-1.0, vmax=1.0, center=0.0, annot=True, cmap= 'coolwarm')
    plt.show()


def test_chi_cuadrado(df, var_nominal1, var_nominal2):
    # 1. Creamos la tabla de contingencia (frecuencias cruzadas ignorando nulos)
    tabla_contingencia = pd.crosstab(df[var_nominal1], df[var_nominal2])
    
    res = stats.chi2_contingency(tabla_contingencia)
    
    chi2 = float(res[0])        # type: ignore
    p_val = float(res[1])       # type: ignore
    grados_libertad = int(res[2]) # type: ignore
    
    print(f"Test de Chi-cuadrado entre {var_nominal1} y {var_nominal2} ---")
    print(f"Estadístico Chi2: {chi2:.4f}")
    print(f"P-value: {p_val:.5f}")
    print(f"Grados de libertad: {grados_libertad}\n")
    
    if p_val < 0.05:
        print("✅ Resultado: Hay evidencia estadística de asociación (las variables NO son independientes).")
    else:
        print("⚠️ Resultado: No se rechaza la hipótesis de independencia (no hay asociación significativa).")


def graficar_tendencia_temporal(col_year, col_valor, df):
    """
    Agrupa los datos por año, calcula la media y el desvío estándar,
    y grafica la tendencia temporal con un intervalo de confianza sombreado.
    """
    # 1. Agrupar por año y calcular las métricas estadísticas
    # agg() nos permite calcular múltiples cosas a la vez para cada año
    df_agrupado = df.groupby(col_year)[col_valor].agg(['mean', 'std', 'count']).reset_index()
    
    # Opcional: Filtrar años con muy pocos registros (ej. menos de 3) 
    # para evitar que un solo dato suelto distorsione el desvío estándar (que daría NaN)
    df_agrupado = df_agrupado[df_agrupado['count'] > 2].dropna(subset=['std'])

    # 2. Configurar el gráfico
    plt.figure(figsize=(10, 6))
    
    # Eje X e Y principal (La media)
    x = df_agrupado[col_year]
    y_mean = df_agrupado['mean']
    y_std = df_agrupado['std']
    
    # 3. Dibujar la línea de la media (μ)
    plt.plot(x, y_mean, color='#1f77b4', linewidth=2.5, label=r'Media ($\mu$)')
    
    # 4. Dibujar el área sombreada del desvío estándar (μ ± σ)
    plt.fill_between(x, 
                     (y_mean - y_std), 
                     (y_mean + y_std), 
                     color='#1f77b4', alpha=0.2, 
                     label=r'Desvío Estándar ($\mu \pm \sigma$)')
    
    # 5. Detalles estéticos
    plt.title(f'Tendencia Histórica de {col_valor} por Año', fontsize=14)
    plt.xlabel('Año de Lanzamiento', fontsize=12)
    plt.ylabel('Duración (Minutos)', fontsize=12)
    
    # Limitar el eje Y inferior a 0 (las películas no tienen duración negativa)
    plt.ylim(bottom=0)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


def barras(col_cat, df):
    # Calcula las frecuencias directamente
    frecuencias = df[col_cat].value_counts()
    
    # Crea el gráfico
    plt.figure(figsize=(8, 5))
    plt.bar(frecuencias.index.astype(str), frecuencias.values, color='#1f77b4', edgecolor='black')
    
    # Etiquetas y título
    plt.title(f'Distribución de {col_cat}')
    plt.xlabel('Categorías')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45, ha='right')
    
    # Ajusta los márgenes y muestra el gráfico
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt

def barras_binarias(columnas_binarias, df):
    """
    Grafica la frecuencia de múltiples columnas binarias (ej: géneros).
    """
    # Sumamos los 1s de cada columna y ordenamos de mayor a menor
    frecuencias = df[columnas_binarias].sum().sort_values(ascending=False)
    
    # Creamos el gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(frecuencias.index, frecuencias.values, color='#1f77b4', edgecolor='black')
    
    # Etiquetas y título
    plt.title('Frecuencia de Géneros')
    plt.xlabel('Géneros')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()