from Aula22Desafio107Modulos.titulo import titulo
from Aula22Desafio107Modulos import moeda

titulo(10)

n = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.formatacaomoeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.formatacaomoeda(n)} é {moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos {moeda.aumentarporcento(n, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuirporcento(n, 13, True)}')
