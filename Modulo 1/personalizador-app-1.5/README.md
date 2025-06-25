# personalizador-app

Este projeto é um pacote chamado `personalizador`, que fornece funcionalidades para manipulação de texto utilizando a biblioteca `rich`. O pacote inclui módulos para layout, criação de painéis, exibição de barras de progresso e aplicação de estilos ao texto.

## Estrutura do Projeto

```
personalizador-app
├── personalizador
│   ├── __init__.py
│   ├── layout.py
│   ├── painel.py
│   ├── progresso.py
│   └── estilo.py
├── cli.py
├── requirements.txt
└── README.md
```

## Módulos

- **personalizador/layout.py**: Contém funções para manipulação de layout, como `centralizar` e `alinhar_direita`.
- **personalizador/painel.py**: Define funções para criar painéis estilizados, como `painel_simples` e `painel_com_titulo`.
- **personalizador/progresso.py**: Implementa funções para mostrar barras de progresso, como `barra_simples` e `barra_longa`.
- **personalizador/estilo.py**: Contém funções para aplicar estilos ao texto, como `negrito` e `colorido`.

## Interface de Linha de Comando

O arquivo `cli.py` fornece uma interface de linha de comando que permite ao usuário interagir com o pacote `personalizador`. Ele utiliza a biblioteca `argparse` para receber argumentos e chamar as funções apropriadas.

## Instalação

Para instalar as dependências do projeto, execute:

```
pip install -r requirements.txt
```

## Uso

Após a instalação, você pode usar a interface de linha de comando para formatar texto. Por exemplo:

```
python cli.py "Seu texto aqui" -m layout -f centralizar
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.