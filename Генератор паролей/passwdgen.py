import string
import random

class Passwd:

	def start(self):
		your_password = []

		print()
		self.lower_inp = input('Включить строчные буквы? yes/no: ')
		if self.lower_inp == 'yes':
			self.if_lower_inp = int(input('Сколько?: '))
			your_password.extend(random.choices(string.ascii_lowercase, k=self.if_lower_inp))

		print()
		self.upper_inp = input('Включить заглавные буквы? yes/no: ')
		if self.upper_inp == 'yes':
			self.if_upper_inp = int(input('Сколько?: '))
			your_password.extend(random.choices(string.ascii_uppercase, k=self.if_upper_inp))

		print()
		self.russian_inp = input('Включить кирилицу? yes/no: ')
		if self.russian_inp == 'yes':
			self.if_russian_inp = int(input('Сколько?: '))
			your_password.extend(random.choices('йцукенгшщзфывапролдячсмитьбю', k=self.if_russian_inp))

		print()
		self.digits_inp = input('Включить цифры? yes/no: ')
		if self.digits_inp == 'yes':
			self.if_digits_inp = int(input('Сколько?: '))
			your_password.extend(random.choices(string.digits, k=self.if_digits_inp))

		print()
		self.symbol_inp = input('Включить символы? yes/no: ')
		if self.symbol_inp == 'yes':
			self.if_symbol_inp = int(input('Сколько?: '))
			your_password.extend(random.choices(string.punctuation, k=self.if_symbol_inp))

		print()
		self.how_many_passwords = int(input('Сколько паролей сгенерировать?: '))
		print()
		print('Ваши пароли:')
		for _ in range(self.how_many_passwords):
			random.shuffle(your_password)
			print()
			print(''.join(your_password))

password = Passwd()

password.start()