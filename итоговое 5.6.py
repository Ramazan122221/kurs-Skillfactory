masiv = [[" "] * 3 for i in range(3)]
print('первое число отвечает за номер строки, второе число за номер столбца')
print()
def otrisovka():
    print(f'  0 1 2')
    for i in range(3):
        row = " ".join(masiv[i])
        print(f'{i} {row}')

def zapros_peremenih():
    print('Нужно ввести 2 числа от 0 до 2')
    while True:
        a = input("Ваш ход: ").split()
        
        if len(a)!=2:
            print('Введите 2 занчения через пробел от 0 до 2')
            continue
        
        x, y = a
        
        if not(x.isdigit()) or not(y.isdigit()):
            print('Нужно ввести числа')
            continue
        
        x = int(x)
        y = int(y)
        
        if 0>x or x>2 or 0>y or y>2:
            print('Введите числа от 0 до 2')
            continue

        if masiv[x][y] != " ":
            print("Поле занято")
            continue

        return x, y

def win():
    coordinat_win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for coordinat in coordinat_win:
        z = coordinat[0]
        x = coordinat[1]
        c = coordinat[2] 

        if masiv[z[0]][z[1]] == masiv[x[0]][x[1]] == masiv[c[0]][c[1]] != ' ':
            print(f'Выиграл {masiv[c[0]][c[1]]}')
            return True
    return False



k = 0
while True:
    k+=1
    otrisovka()
    if k%2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = zapros_peremenih()

    if k%2 == 1:
        masiv[x][y] = 'X'
    else:
        masiv[x][y] = 'O'

    if win():
        otrisovka()
        break

    if k == 9:
        otrisovka()
        print('Ничья')
        break
    
    
