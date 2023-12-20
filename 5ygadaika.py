from random import *

word_list = ["тасовка", "полет", "самолет", "вертолет", "собака", "лошадь", "пуська", "программа"]
word = word_list[randrange(0, len(word_list))]
print(word)
def human(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]
def play(s):
    tries = 6
    str = "_ " * (len(word))
    naz = ["_"] * len(word)
    slovo = list(word)
    print("Давайте играть в угадайку слов!")
    print(human(tries))
    print("Осталось количество попыток - ", tries)
    print(str)
    while "".join(naz) != word:
        print("Введите одну русскую букву")
        byk = input()
        while len(byk) != 1 or byk.lower() not in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
            print("Попробуйте еще раз!")
            byk = input()
        if byk in slovo:
            while byk.lower() in slovo:
                naz[slovo.index(byk)] = slovo[slovo.index(byk)]
                slovo[slovo.index(byk)] = " "
            print(" ".join(naz))
        else:
            tries = tries - 1
            print("У вас осталось попыток - ", tries)
            print(human(tries))
            if tries == 0:
                c = False
                return c
    c = True
    return c
while 1>0:
	k = play(word)
	if k == True:
		print('Вы прошли игру!')
	else:
		print('Вы проиграли! :(')
	print('Желаете повторить?')
	j = input()
	if j.lower() in 'даyes':     
		word = word_list[randrange(0, len(word_list))]
		continue
	else:
		print('До новых встреч!')
		break