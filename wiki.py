from googlesearch import search 
import os
v = '\033[1;31m'
b = '\033[1;97m'
while True:
	
    print(f'{v}wikipedia')
    print('powered by: stephen')
    print()

    quero = input(f'{b}qual sua pesquisa:  ')

    query = quero + 'wikipedia'

    for resultado in search(query):
        print(resultado) 
        print()
        print()
        print()
    
    reset = input('0 to reset: ')
    if reset== '0':

        os.system('clear')
        continue