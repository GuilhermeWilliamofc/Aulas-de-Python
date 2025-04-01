from Aula22Desafio107Modulos.titulo import titulo
from Aula22Desafio107Modulos import moeda

titulo(107)

n = float(input('Digite o Preço: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentarporcento(n, 10)}')
print(f'Diminuindo 13%, temos R${moeda.diminuirporcento(n, 13)}')
