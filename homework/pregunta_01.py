"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Leer archivo CSV con índice temporal
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Estilo personalizado por categoría de medio
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "green",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    # Crear figura
    plt.figure(figsize=(10, 6))

    for col in df.columns:
        # Línea principal
        plt.plot(
            df.index,
            df[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

        # Añadir valor inicial
        start_year = df.index[0]
        start_val = df[col].loc[start_year]
        plt.scatter(start_year, start_val, color=colors[col], zorder=zorder[col])
        plt.text(
            start_year - 0.2,
            start_val,
            f"{col} {start_val} %",
            ha="right",
            va="center",
            color=colors[col],
        )

        # Añadir valor final
        end_year = df.index[-1]
        end_val = df[col].loc[end_year]
        plt.scatter(end_year, end_val, color=colors[col], zorder=zorder[col])
        plt.text(
            end_year + 0.2,
            end_val,
            f"{col} {end_val} %",
            ha="left",
            va="center",
            color=colors[col],
        )

    # Ajustes de ejes
    plt.title("How people get their news", fontsize=16)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.xticks(df.index)

    # Guardar imagen
    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()

if __name__ == "__main__":
    pregunta_01()

    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
