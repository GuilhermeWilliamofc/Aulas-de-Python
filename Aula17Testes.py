num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
if 0 in num:
    num.remove(0)
else:
    print('Não achei o número 0')
print(num)
print(f'Essa lista tem {len(num)} elementos')
