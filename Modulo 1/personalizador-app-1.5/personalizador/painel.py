from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto, isArquivo=False):
    """
    Exibe um painel simples com o texto fornecido.
    Se isArquivo for True, lê o conteúdo do arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    console.print(Panel(conteudo))

def painel_com_titulo(texto, titulo="Título", isArquivo=False):
    """
    Exibe um painel com um título e o texto fornecido.
    Se isArquivo for True, lê o conteúdo do arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    console.print(Panel(conteudo, title=titulo))