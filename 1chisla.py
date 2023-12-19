from random import *

n = randint(1, 10)
print(n)
print("Добро пожаловать в числовую угадайку :)")


def diapazon(k):
    if k > 100 or k < 0:
        print("Оно не входит в заданный диапазон")
        return False
    else:
        return True

o = int(input("Введите число от 1 до 100 \n"))
while diapazon(o) == False:
    o = int(input("Введите число от 1 до 100 \n"))

while True:
     if o < n:
           print('Ваше число меньше загаданного, попробуйте еще разок')       
     elif o > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
     elif o == n:
        print('Вы прошли игру, желаете повторить?')
        s = input()
        if s in 'yesда':
            n = randint(1, 100)
            print(n)
        else:
            print('Спасибо за игру')
            break
     o = int(input("Введите число от 1 до 100 \n"))
     while diapazon(o) == False:
        o = int(input("Введите число от 1 до 100 \n"))



    
      