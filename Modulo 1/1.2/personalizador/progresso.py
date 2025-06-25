"""
Módulo de progresso usando Rich.
"""

from rich.progress import track
import time

def barra_de_progresso(texto, isArquivo=False):
    """
    Simula progresso com 10 passos.
    """
    for _ in track(range(10), description="Processando..."):
        time.sleep(0.1)

def progresso_por_linha(texto, isArquivo=False):
    """
    Mostra progresso por linha de texto.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            linhas = file.readlines()
    else:
        linhas = texto.split("\n")
    for linha in track(linhas, description="Exibindo linhas..."):
        print(linha.strip())
        time.sleep(0.1)
