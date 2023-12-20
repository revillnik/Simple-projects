from random import *

ch = '0123456789'
bu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bm =  'abcdefghijklmnopqrstuvwxyz'
pu = '!#$%&*+-=?@^_'
s = ''

print('Добро пожаловать в программу по генерации безопасных паролей \nВведите количество  паролей, которые вам нужно сгенерировать')
while True:
	n = int(input()) 	# количество паролей
	if n < 1:
		print('Неподходящее число')
	else:
		break
	
	
print('Введите длину пароля')
while True:
	f = int(input()) 	# длина пароля
	if f < 1:
		print('Неподходящее число')
	else:
		break

print('включать ли цифры в пароль?')
c = input() 	# включать ли цифры в пароль
print('включать ли прописные буквы в пароль?')
pb = input() 	# включать ли прописные буквы в пароль
print('включать ли строчные буквы в пароль?')
ct = input() 	# включать ли строчные буквы в пароль
print('включать ли символы в пароль?')
ci = input() 	# включать ли символы в пароль
print('включать ли неоднозначные символы в пароль?')
nc = input() 	# включать ли неоднозначные символы в пароль

if c.lower() in 'нетno':
	ch = ''
if pb.lower() in 'нетno':
	bu = ''
if ct.lower() in 'нетno':
	bm = ''
if ci.lower() in 'нетno':
	pu = ''

z = ch+bu+bm+pu

if nc.lower() in 'нетno':
	for i in 'il1Lo0O':
		z = z.replace(i, '')

def generate_password(length):
	global s, z
	for i in range (length):
		o = randrange (0,int(len(z)))
		s = s + z[o]
	print (s)
	s = ''

print('Ваши пароли:')

for i in range (n):
	generate_password(f)	
