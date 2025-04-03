from Modulos.Aula22Desafio107Modulos.titulo import titulo
import urllib
import urllib.request

titulo(114)

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    # print(site.read()) aparece o código html do site
