from time import sleep

# Para o cabeçário padrão

def cabecario(titulo):
    print('-'*(len(titulo)+2))
    print(titulo.center(len(titulo)+2))
    print('-' * (len(titulo)+2))

def cabecario_jokenpo(titulo):
    print('=-' * (len(titulo)))
    print(f'{" "*2} {titulo}')
    print('=-' * (len(titulo)))

def jokenpo():
    for c in range (1):
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!')
        sleep(0.5)
