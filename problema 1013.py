numero = list(map(int, input().split()))

if numero[0] > numero[1] and numero[0] > numero[2]:
    print(f'{numero[0]} eh maior')
elif numero[2] > numero[0] and numero[2] > numero[1]:
    print(f'{numero[2]} eh maior')
else:
    print(f'{numero[1]} eh maior')