a = [2, 3, 4, 7]
b = a[:] #esse [:] é importante pra criar cópias de listas!
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
