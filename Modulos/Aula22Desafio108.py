from Aula22Desafio107Modulos.titulo import titulo
from Aula22Desafio107Modulos import moeda

titulo(108)

n = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.formatacaomoeda(n)} é {moeda.formatacaomoeda(moeda.metade(n))}')
print(f'O dobro de {moeda.formatacaomoeda(n)} é {moeda.formatacaomoeda(moeda.dobro(n))}')
print(f'Aumentando 10%, temos {moeda.formatacaomoeda(moeda.aumentarporcento(n, 10))}')
print(f'Diminuindo 13%, temos {moeda.formatacaomoeda(moeda.diminuirporcento(n, 13))}')
