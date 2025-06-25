from rich.console import Console

console = Console()

def negrito(texto, isArquivo=False):
    """
    Imprime o texto em negrito usando rich.
    Se isArquivo for True, lê o conteúdo do arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    console.print(f"[bold]{conteudo}[/bold]")

def colorido(texto, isArquivo=False):
    """
    Imprime o texto em azul usando rich.
    Se isArquivo for True, lê o conteúdo do arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    console.print(f"[blue]{conteudo}[/blue]")