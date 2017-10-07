print('Hello, Django girls!')
if 3 > 2:
    print('it work!')
if 5 > 2:
    print('5 est effectivement plus grand que 2')
else:
    print (" 5 n'est pas plus grand  que 2")
name= 'Marjane'
if name== 'Marjane':
    print ('hey Marjane!')
elif name == 'sonja':
    print('hey! sonja')
else:
    print('hey anonymous!')

volume = 57
if volume < 20:
    print("c'est plutôt calme.")
elif 20 <= volume < 40:
    print("Une jolie musique de fond.")
elif 40 <= volume < 60:
    print( "Parfait,je peux entendre tous les détails du morceau.")
elif 60 <= volume < 80:
    print("Parfait pour la fête!")
elif 80 <= volume < 100:
    print("Un peu trop fort!")
else:
    print("Au secours! Mes oreilles! :(")

def hi(name):
    print('Hi' + name + '!' )

girls =['Rachel,Phoebe,Ola,Monica,Marjane']
for name in girls:
     hi(name)
     print('Next girl')

for i in range (1,6):
    print(i)
