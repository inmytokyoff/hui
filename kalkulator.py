while True:   
    print('Введите первое число: ')
    a = int(input(''))
    print('Введите второе число: ')
    b = int(input('')) 
    c = input('Введите знак "+" "-" "*" "/" : ')
    if c == '+' :
        print(a+b)
    elif c == '-' :
        print(a-b)
    elif c == '*' :
        print(a*b)
    elif c == '/' and b != 0 :
        print(a/b)
    else :
        print('Ошибка!')
    break
        