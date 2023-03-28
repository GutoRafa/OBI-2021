i = 0
num_vitorias = 0
while i < 6:
    x = input()
    if x == 'V':
        num_vitorias += 1
    i += 1
grupo = [-1,3,3,2,2,1,1]
print(grupo[num_vitorias])