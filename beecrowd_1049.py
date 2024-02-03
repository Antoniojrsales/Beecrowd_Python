tipo_animal = input('Digite qual o tipo de Animal abaixo\n'
                        'Vertebrado\n'
                        'Invertebrado\n').lower()
print()
tipo_especie = input('Digite qual o tipo de Especie abaixo\n'
                        'Vertebrado\n'
                        'Ave\n'
                        'Mamifero\n'
                        'Invertebrado\n'
                        'Inseto\n'
                        'Anelideo\n').lower()
print()
tipo_cadeia = input('Digite qual o tipo de Cadeia alimentar abaixo\n'
                        'Carnivoro\n'
                        'Onivoro\n'
                        'Herbivoro\n'
                        'Hematofago\n').lower()
print()


if tipo_animal == 'vertebrado' and tipo_especie == 'ave' and tipo_cadeia == 'carnivoro':
    print('aguia')
elif tipo_animal == 'vertebrado' and tipo_especie == 'ave' and tipo_cadeia == 'onivoro':
    print('pomba')
elif tipo_animal == 'vertebrado' and tipo_especie == 'mamifero' and tipo_cadeia == 'onivoro':
    print('homem')
elif tipo_animal == 'vertebrado' and tipo_especie == 'mamifero' and tipo_cadeia == 'herbivoro':
    print('vaca')

elif tipo_animal == 'invertebrado' and tipo_especie == 'inseto' and tipo_cadeia == 'hematofago':
    print('pulga')
elif tipo_animal == 'invertebrado' and tipo_especie == 'inseto' and tipo_cadeia == 'herbivoro':
    print('lagarta')
elif tipo_animal == 'invertebrado' and tipo_especie == 'anelideo' and tipo_cadeia == 'hematofago':
    print('sanguessuga')
elif tipo_animal == 'invertebrado' and tipo_especie == 'anelideo' and tipo_cadeia == 'onivoro':
    print('minhoca')
else:
    print('Opcao invalida')

#forma melhorada#
    
'''tipo_animal = input().lower()
tipo_especie = input().lower()
tipo_cadeia = input().lower()

if tipo_animal == 'vertebrado':
    if tipo_especie == 'ave':
        if tipo_cadeia == 'carnivoro':
            print('aguia')
        elif tipo_cadeia == 'onivoro':
           print('pomba') 
    
    if tipo_especie == 'mamifero':
        if tipo_cadeia == 'onivoro':
            print('homem')
        elif tipo_cadeia == 'herbivoro':
           print('vaca')

if tipo_animal == 'invertebrado':
    if tipo_especie == 'inseto':
        if tipo_cadeia == 'hematofago':
            print('pulga')
        elif tipo_cadeia == 'herbivoro':
            print('lagarta') 

    if tipo_especie == 'anelideo':
        if tipo_cadeia == 'hematofago':
            print('sanguessuga')
        elif tipo_cadeia == 'onivoro':
            print('minhoca') '''



