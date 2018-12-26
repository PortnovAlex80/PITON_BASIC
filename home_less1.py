'__author__ = Суслов Олег Александрович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


print ("решение первой задачи")
print ()
numb=45673
Numbs=[]
i=0
while i < len(str(numb)):
    Numbs.append(int((str(numb))[i]))
    i=i+1
Maxnumb = max(Numbs)
print("Максимальное значение цифры в числе "+ str(numb)+" равно -",Maxnumb)
print ()
print ()


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


print ("решение второй задачи")
print ()
a = input ("Введите первое число = ")
b = input ("Введите второе число = ")
Massiv=[]
Massiv.append(a)
Massiv.append(b)
print("Первое значение = ",a)
print("Второе значение = ",b)
print("Меняем значения местами!!!")
a=Massiv[1]
b= Massiv[0]
print("Теперь первое значение = ",a)
print("Теперь второе значение = ",b)
print ()
print ()


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


import math

print ("решение третьей задачи")
print ()
print ("Решаем уравнение вида: ax² + bx + c = 0") 

a = float(input ("Введите значение коэффициента а = "))
b = float(input ("Введите значение коэффициента b = "))
c = float(input ("Введите значение коэффициента c = "))

diskr = b**2-4*a*c

if diskr >0:
    koren1 = (-b+math.sqrt(diskr))/(2*a)
    koren2 = (-b-math.sqrt(diskr))/(2*a)
    print ("Дискриминант положительный, корни вещественные и различны!!")
    print ("Первый корень: =", koren1)
    print ("Второй корень: =", koren2)

elif diskr ==0:
    koren = (-b/(2*a))
    print ("Дискриминант равен 0, корни вещественные и одинаковы!!")
    print ("Первый и второй корени: =", koren)
    
    
elif diskr<0:
    print ("Дискриминант отрицательный, корни комплексные!!")
    print ("Первый корень: =", str(-b/2*a)+"+"+"("+str((math.sqrt(-diskr))/2*a)+"*i)")
    print ("Второй корень: =", str(-b/2*a)+"-"+"("+str((math.sqrt(-diskr))/2*a)+"*i)")
     
print ()
print ()


# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

print ("решение четвертой задачи")
print ()
a=1
while bool(a)==True:
    if bool(a**2)== True and bool(a*2) == True and bool(a>999999)==True:
        print ("Искомое значение перменной = ", a)
        break
    else:
        a= a+1
    

