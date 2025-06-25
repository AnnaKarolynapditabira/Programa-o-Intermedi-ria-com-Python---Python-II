import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

funcoes_disponiveis = {
    "layout": ["exibir_layout_simples", "exibir_layout_esquerda"],
    "painel": ["painel_simples", "painel_decorado"],
    "progresso": ["barra_de_progresso", "progresso_por_linha"],
    "estilo": ["texto_colorido", "texto_sombreado"]
}

parser = argparse.ArgumentParser(description="Personalizador de texto com Rich")
parser.add_argument("entrada", help="Texto ou caminho para o arquivo")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que a entrada é um arquivo")
parser.add_argument("-m", "--modulo", choices=modulos.keys(), required=True, help="Módulo a ser usado")
parser.add_argument("-f", "--funcao", required=True, help="Função do módulo")

args = parser.parse_args()

modulo = modulos.get(args.modulo)
funcoes = funcoes_disponiveis[args.modulo]

if args.funcao not in funcoes:
    print(f"Função inválida. Escolha entre: {funcoes}")
else:
    func = getattr(modulo, args.funcao)
    func(args.entrada, args.arquivo)
