print('Привет. \n Я покажу тебе простой математический трюк. \n Какое бы число ты не ввёл, ряд арифметических операций превратит его в 4.')
number = int(input('Введи число'))
number2 = number*2
number3 = number*2+8
number4 = (number*2+8)//2
number5 = (number*2+8)//2 - number
print('Число', number,'умножаем на 2, что равно',number2)
print('К числу',number2,'прибавляем 8, что в сумме даёт',number3)
print('Число',number3,'делим на 2, что в сумме даёт',number4)
print('А затем отнимаем от числа',number4, 'загаданное число', number, 'и получаем в результате:', number5)
