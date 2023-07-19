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
        # listOfMoney.insert(i,random.randint(0,1))
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

# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

# while(number>0):        
#     count+=number%10
#     number = number//10
# print(count)

def UserInput(text):
    print(text)
    value = input()
    for i in range(len(value)-1):
        if value[i]== ".":
            value = float(value)
            return value
    if  isinstance(value, str):
        value = int(value)
        return value
# number = UserInput("Введите число: ")
# count = 0
# def SumOfNumber(number,count):
#     while (number-number%1)<number:
#         number*=10
#     while(number>0):        
#         count+=number%10
#         number = number//10
#     print(count)
    
# SumOfNumber(number,count)


# задача 3 необязательная

# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).
# number = UserInput("Введите число: ")
# list = []*number
# def all_divisors(number,list):
#     i = 1
#     j = 0
#     while i<=number//2  or i==number:
#         if number%i==0:
#             list.insert(j, i)
#             j+=1
#         i+=1
#     list.insert(j,number)
#     return list
# print(all_divisors(number,list))




