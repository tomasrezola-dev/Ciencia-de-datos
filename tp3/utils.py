from wget import download
import os
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def descarga(csv, name_csv, ej):
    ruta_archivo = os.path.join(name_csv)
    if not os.path.exists(ruta_archivo):
        download(csv)
    else:
        print("No vamos a bajar el archivo porque ya existe")


def box_plot(cuali, cuanti, df):
    df.boxplot(
        column=cuanti,
        by=cuali,
        figsize=(10, 6),
        grid=True,
        patch_artist=True,
        medianprops={'color': 'orange', 'linewidth': 3} # Resalta la línea de la mediana
    )
    plt.title('Distribución de peso por consumo de alcohol', fontsize=14)
    plt.suptitle('')
    plt.xlabel('Consumo de alcohol', fontsize=12)
    plt.ylabel('Peso', fontsize=12)
    ff = df[cuali].cat.codes #convertimos las categorias a numerico para spearman
    sp = ff.corr(df[cuanti], method='spearman')
    if sp >= 0:
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
    plt.figure(figsize=(6, 6))
    plt.scatter(df[cuanti1], df[cuanti2], alpha=0.7)
    plt.xlabel(cuanti1)
    plt.ylabel(cuanti2)
    
    plt.title(f"Relación entre {cuanti1} y {cuanti2}")

    coeficiente_correlacion, p_value = stats.pearsonr(df[cuanti1], df[cuanti2])
    
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