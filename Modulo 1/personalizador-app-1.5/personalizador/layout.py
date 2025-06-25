from rich.console import Console
from rich.align import Align

console = Console()

def centralizar(texto):
    console.print(Align.center(texto))

def alinhar_direita(texto):
    console.print(Align.right(texto))