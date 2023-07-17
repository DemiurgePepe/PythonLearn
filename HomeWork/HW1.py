# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random
# def searchMoney():
#     n = int(input())
#     listOfMoney = []
#     number = 0
#     eagle =0
#     for i in range(0,n): 
#         listOfMoney.insert(i,random.randint(0,1))
#         if listOfMoney[i]==1:
#             number=number+1
#             print(number)
#         else:
#             eagle=eagle+1
#     if eagle>number:
#         print(f"Нужно перевернуть {number} решек")
#     elif eagle<number:
#         print(f"Нужно перевернуть {eagle} гербов")
#     elif eagle==number:
#         print(f"Нужно перевернуть {eagle} гербов или {number} решек")
#     print(listOfMoney)
# searchMoney()








# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# x = random.randint(1,1000)
# y = random.randint(1,1000)
# s = x+y
# p = x*y
# print(x)
# print(y)
# print(s)
# print(p)
# firstNumber=(s-int((s**2-4*p)**0.5))//2
# secondNumber=(s+int((s**2-4*p)**0.5))//2
# print(f"Первое число  равняется {firstNumber}, второе {secondNumber}")




# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input())
# array= []
# for i in range(1,n):
#     if 2**i<n:
#         array.insert(i-1,2**i)
# print(array)





