# Gerador de Tabela de Parser SLR, LR e LALR

## Qual o propósito deste projeto?
O objetivo deste projeto é criar o backend de uma aplicação que irá gerar tabelas para os parsers SLR, LR e LALR.

## Por que este projeto existe?
Estudando a disciplina de compiladores, descobri que possuo certa dificuldade na geração das tabelas. Acredito que implementar uma ferramenta capaz de gerar as tabelas automaticamente, seguindo passo a passo do que eu faria à mão, irá me permitir entender melhor o funcionamento do algoritmo e me dará um método de checar as respostas dos exercícios que fiz e que não possuem gabaritos.

## Quais são as rotas desta API?
- /table/<parser_type>
    - parser_type pode ser slr, lr ou lalr
- /execute

## Quais informações devem estar contidas no request da API?
- Uma lista indicando quais caracteres são as variáveis
- Uma lista indicando quais caracteres são os terminais
- Uma lista com as produções da linguagem

## Comandos importantes:
- Salvar requisitos: ```pip freeze > requirements.txt```
