
def bykv(str):
    c = 0
    for i in str:
        if i.isalpha():
            c += 1
    return c
def shifr (z, f, x):
	for d in range(len(s)):
		o = list(s[d])
		for i in range(len(o)):
			if o[i] in z:
					o[i] = z[(z.index(o[i]) + bykv(s[d])*x) % len(z)]
			if o[i] in f:
					o[i] = f[(f.index(o[i]) + bykv(s[d])*x) % len(f)]
		k.append("".join(o))
	print(" ".join(k))

en = list("abcdefghijklmnopqrstuvwxyz")
enb = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
k = []
ru = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
rub = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
print('Добро пожаловать в шифровальную машину Цезаря \nЧто бы вы хотели сделать, зашифровать или дешифровать сообщение?')
if input() in 'зашифроватьЗашифровать':
	x = 1
else:
	x = -1
print('На каком языке сообщение? Русский или английский?')
if input() in "Русскийрусский":
	print('Введите сообщение')
	s = [i for i in input().split(" ")]
	print('Ваше сообщение будет таким:')
	shifr (ru, rub, x)
else:
	print('Введите сообщение')
	s = [i for i in input().split(" ")]
	print('Ваше сообщение будет таким:')
	shifr(en, enb, x)


