"""
Módulo de layout usando Rich.
"""

from rich.console import Console
from rich.align import Align

console = Console()

def exibir_layout_simples(texto, isArquivo=False):
    """
    Exibe o texto centralizado.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(Align.center(texto))

def exibir_layout_esquerda(texto, isArquivo=False):
    """
    Exibe o texto alinhado à esquerda.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(Align.left(texto))
