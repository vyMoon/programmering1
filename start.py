# def printSquareInformation(height, width, units = 'centimeter'):
#   square = height * width
#   sidesLength = (height + width) * 2
#   print(f'En rektangel har bredden {width} {units} och längden {height} {units}')
#   print(f'Omrketsen är {sidesLength} {units}.')
#   print(f'Arean är {square} kvadrat{units}.')
#   print('\n')

# printSquareInformation(4,5)
# printSquareInformation(2, 5, 'meter')


# def printCircleInformation(radius, units = 'centimeter'):
#   pi = 3.14
#   square = pi * radius ** 2
#   circumference = 2 * pi * radius
#   print(f'Radius är {radius} {units}')
#   print(f'Arean är {square} kvadrat{units}.')
#   print(f'Omrketsen är {circumference} {units}.')
#   print('\n')

# printCircleInformation(6)
# printCircleInformation(5, 'meter')


# def VATcounter(prise, vat, currency = 'Kr'):
#   if (not isinstance(vat, int) and not isinstance(vat,float)):
#     print('Vat must be a int or float')
#     return
  
#   Vatpercents = vat / 100 if isinstance(vat, int) else vat
#   vatAmount = prise * Vatpercents
#   print(f'Priset incluseve moms är {vatAmount + prise} {currency}')

# VATcounter(100, "5")
# VATcounter(100, 0.05, 'USD')



# def triangleInformation(base, hight, units = 'centimeter'):
#   area = (base * hight) / 2
#   print(f'En triangel med basen {base} {units} och häjden {hight} {units} har arean {area} {units}')


# triangleInformation(5, 10)

# base = int(input('Skriv basen'))
# hight = int(input('skriv höjden'))

# triangleInformation(base, hight)


# name = str(input('Jag baa undrar vad hetter du '))
# print(name)

# print(
#   str(input('Jag baa undrar vad hetter du '))
# )

# daysInYear = 365
# hoursInDay = 24
# minutesInHour = 60
# secondsInMinute = 60

# secondsInYear = daysInYear * hoursInDay * minutesInHour * secondsInMinute
# secondsIn5Years = secondsInYear * 5
# birthsIn5Year = secondsIn5Years // 7

# print(birthsIn5Year )



def simpleLoop(repeats = 5, text = 'Hej'):
  for n in range(-1, repeats):
    print(text, n)


# simpleLoop()


def namePrinter(name = 'Name', surname = 'Surname', nameRepeats = 2, surnameRepeats = 3):
  maxRepeats = nameRepeats if nameRepeats > surnameRepeats else surnameRepeats

  for n in range(maxRepeats):
    if (n < nameRepeats):
      print(name)
    if (n < surnameRepeats):
      print(surname)


# namePrinter()

def summer():
  x = int(input('Give a number '))
  amount = 0
  for n in range(1, x + 1):
    amount = amount + n
  print(amount)

# summer()


# for n in range(1, 6):
#   print(f'Jag fyller {n} år!')

# a = range(3)
# print(a[2])

# for n in range(0, 17, 3):
#   print(n)

# from types import SimpleNamespace

# o = SimpleNamespace(name = 'name', surname = 'surname')
# o.city = 'city'

# print(o)

def multiplicationTable():
  base = int(input('give a multiplication base '))
  first = int(input('from '))
  last = int(input('To '))
  for n in range(first, last + 1):
    result = n * base
    print(f'{n} x {base} = {result}')

# multiplicationTable()


# for base in range(1, 11):
#   print(f'\nTable base = {base}')
#   for n in range(1, 11):
#     result = base * n
#     print(f'{n} x {base} = {result}')

# for n in range(2):
#   tal = int(input('give a number '))
#   # print(tal)
# print(tal)

# amount = int(input('give a number of how many times would you like to add '))
# sum = 0

# for n in range(amount):
#   tal = int(input(f'give number {n + 1} '))
#   sum = sum + tal
#   print(n, sum, tal)

# print(f'sum is {sum}')


print( not not 1)
print(3 != 5)
print('string' != 'String')
print(not True)


