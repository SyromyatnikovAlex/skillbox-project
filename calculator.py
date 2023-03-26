while True:
	num_1 = float(input('Введите первое число: '))
	num_2 = float(input('Введите второе число: '))
	operation = input('Какую операцию хотите провести: +, -, *, /. Выход "0": ')
	if operation == '+':
		result = num_1 + num_2
		print(num_1, '+', num_2, '=', result)
		print()
	elif operation == '-':
		result = num_1 - num_2
		print(num_1, '-', num_2, '=', result)
		print()
	elif operation == '*':
		result = num_1 * num_2
		print(num_1, '*', num_2, '=', result)
		print()
	elif operation == '/':
		result = num_1 / num_2
		print(num_1, '/', num_2, '=', result)
		print()
	elif operation == '0':
		print('Завершение работы...')
		print()
		break
	else:
		print('Некорректный ввод. Попробуйте еще раз.')
		print()