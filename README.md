# Análise de <Municipios> com dados do <IBGE> (<2026>)

## Problema

<Uma frase. A pergunta que você queria responder, e por que ela te interessou.>

## Dados e fonte

- Órgão: <INEP>
- Base: <nome exato da base>
- Ano de referência: <2026>
- Link: <(https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html)>

## Decisões

<descartei cabeçalho e rodapé porque não são registros municipais; 
o numero de população estimada veio com um formato que usava pontos para separar milhares, então voltei o arquivo
para o Excel e formatei os números da forma correta, sem separação
decidi por considerar Brasilia como municipio
>

## Resultados

1. <Pergunta 1>: <resposta numérica>
2. <Pergunta 2>: <resposta numérica>
3. <Pergunta 3>: <resposta numérica>

## Conclusões

<O que esses números significam em uma frase. Depois, uma limitação do dado,
por exemplo: "os valores são estimativas com data de referência, não contagem
censitária, então comparações entre anos exigem cautela".>

## Como rodar

Rodar `python semana01/analise_municipios.py` na raiz do projeto.