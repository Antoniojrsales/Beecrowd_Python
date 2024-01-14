tempo = int(input('Digite o tempo gasto na viagem: '))
velocidade = int(input('Digite a velocidade media na viagem: '))
consumo = int(input('Digite a media de consumo km/l: ')) 
media_consumo = tempo * velocidade / consumo
print(f'Uma viagem de {tempo} hrs em velocidade de {velocidade} km/h com o consumo media de {consumo} km/l vc gastara de combustivel a quantia de {media_consumo:.3f} Lts')