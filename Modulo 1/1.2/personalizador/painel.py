"""
Módulo de painel usando Rich.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto, isArquivo=False):
    """
    Exibe o texto dentro de um painel simples.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(Panel(texto))

def painel_decorado(texto, isArquivo=False):
    """
    Exibe o texto dentro de um painel decorado com borda dupla.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
    console.print(Panel(texto, border_style="green", title="Painel Decorado"))
