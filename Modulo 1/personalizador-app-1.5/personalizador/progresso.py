from rich.progress import track
import time

def barra_simples(texto, isArquivo=False):
    """
    Mostra uma barra de progresso simples usando o rich.
    Se isArquivo for True, lê o conteúdo do arquivo e itera sobre as linhas.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()
    else:
        conteudo = texto.splitlines() if '\n' in texto else [texto]
    for _ in track(conteudo, description="Processando..."):
        time.sleep(0.02)

def barra_longa(texto, isArquivo=False):
    """
    Mostra uma barra de progresso longa usando o rich.
    Se isArquivo for True, lê o conteúdo do arquivo e mostra parte dele na descrição.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    descricao = (conteudo[:20] + "...") if len(conteudo) > 20 else conteudo
    for _ in track(range(10), description=descricao):
        time.sleep(0.2)