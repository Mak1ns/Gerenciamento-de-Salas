import pandas as pd
import os

PASTA_DATA = "data"

def ler_csv(nome_arquivo):
    caminho = os.path.join(PASTA_DATA, nome_arquivo)
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    return pd.read_csv(caminho)

def salvar_csv(df, nome_arquivo):
    caminho = os.path.join(PASTA_DATA, nome_arquivo)
    df.to_csv(caminho, index=False)