import argparse
from personalizador.layout import centralizar, alinhar_direita
from personalizador.painel import painel_simples, painel_com_titulo
from personalizador.progresso import barra_simples, barra_longa
from personalizador.estilo import negrito, colorido

modulos = {
    "layout": {
        "centralizar": centralizar,
        "alinhar_direita": alinhar_direita
    },
    "painel": {
        "painel_simples": painel_simples,
        "painel_com_titulo": painel_com_titulo
    },
    "progresso": {
        "barra_simples": barra_simples,
        "barra_longa": barra_longa
    },
    "estilo": {
        "negrito": negrito,
        "colorido": colorido
    }
}

def main():
    parser = argparse.ArgumentParser(description="Personalizador de texto com Rich.")
    parser.add_argument("texto", help="Texto ou caminho para arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo")
    parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(),
                        help="Escolha o módulo: layout, painel, progresso, estilo")
    parser.add_argument("-f", "--funcao", required=True,
                        help="Escolha a função do módulo selecionado")

    args = parser.parse_args()

    # Execução da função escolhida
    if args.funcao in modulos[args.modulo]:
        funcao = modulos[args.modulo][args.funcao]
        funcao(args.texto, args.arquivo)
    else:
        print(f"Função inválida! Use uma destas: {list(modulos[args.modulo].keys())}")

if __name__ == "__main__":
    main()