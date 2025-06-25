"""
Módulo de estilo usando Rich.
"""

from rich.console import Console

console = Console()

def texto_colorido(texto, isArquivo=False):
    """
    Exibe o texto em azul e negrito.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(texto, style="bold blue")

def texto_sombreado(texto, isArquivo=False):
    """
    Exibe o texto em vermelho e itálico.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(texto, style="italic red")
