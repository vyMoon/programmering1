# # def printSquareInformation(height, width, units = 'centimeter'):
# #   square = height * width
# #   sidesLength = (height + width) * 2
# #   print(f'En rektangel har bredden {width} {units} och längden {height} {units}')
# #   print(f'Omrketsen är {sidesLength} {units}.')
# #   print(f'Arean är {square} kvadrat{units}.')
# #   print('\n')

# # printSquareInformation(4,5)
# # printSquareInformation(2, 5, 'meter')


# # def printCircleInformation(radius, units = 'centimeter'):
# #   pi = 3.14
# #   square = pi * radius ** 2
# #   circumference = 2 * pi * radius
# #   print(f'Radius är {radius} {units}')
# #   print(f'Arean är {square} kvadrat{units}.')
# #   print(f'Omrketsen är {circumference} {units}.')
# #   print('\n')

# # printCircleInformation(6)
# # printCircleInformation(5, 'meter')


# # def VATcounter(prise, vat, currency = 'Kr'):
# #   if (not isinstance(vat, int) and not isinstance(vat,float)):
# #     print('Vat must be a int or float')
# #     return
  
# #   Vatpercents = vat / 100 if isinstance(vat, int) else vat
# #   vatAmount = prise * Vatpercents
# #   print(f'Priset incluseve moms är {vatAmount + prise} {currency}')

# # VATcounter(100, "5")
# # VATcounter(100, 0.05, 'USD')



# # def triangleInformation(base, hight, units = 'centimeter'):
# #   area = (base * hight) / 2
# #   print(f'En triangel med basen {base} {units} och häjden {hight} {units} har arean {area} {units}')


# # triangleInformation(5, 10)

# # base = int(input('Skriv basen'))
# # hight = int(input('skriv höjden'))

# # triangleInformation(base, hight)


# # name = str(input('Jag baa undrar vad hetter du '))
# # print(name)

# # print(
# #   str(input('Jag baa undrar vad hetter du '))
# # )

# # daysInYear = 365
# # hoursInDay = 24
# # minutesInHour = 60
# # secondsInMinute = 60

# # secondsInYear = daysInYear * hoursInDay * minutesInHour * secondsInMinute
# # secondsIn5Years = secondsInYear * 5
# # birthsIn5Year = secondsIn5Years // 7

# # print(birthsIn5Year )



# def simpleLoop(repeats = 5, text = 'Hej'):
#   for n in range(-1, repeats):
#     print(text, n)


# # simpleLoop()


# def namePrinter(name = 'Name', surname = 'Surname', nameRepeats = 2, surnameRepeats = 3):
#   maxRepeats = nameRepeats if nameRepeats > surnameRepeats else surnameRepeats

#   for n in range(maxRepeats):
#     if (n < nameRepeats):
#       print(name)
#     if (n < surnameRepeats):
#       print(surname)


# # namePrinter()

# def summer():
#   x = int(input('Give a number '))
#   amount = 0
#   for n in range(1, x + 1):
#     amount = amount + n
#   print(amount)

# # summer()


# # for n in range(1, 6):
# #   print(f'Jag fyller {n} år!')

# # a = range(3)
# # print(a[2])

# # for n in range(0, 17, 3):
# #   print(n)

# # from types import SimpleNamespace

# # o = SimpleNamespace(name = 'name', surname = 'surname')
# # o.city = 'city'

# # print(o)

# def multiplicationTable():
#   base = int(input('give a multiplication base '))
#   first = int(input('from '))
#   last = int(input('To '))
#   for n in range(first, last + 1):
#     result = n * base
#     print(f'{n} x {base} = {result}')

# # multiplicationTable()


# # for base in range(1, 11):
# #   print(f'\nTable base = {base}')
# #   for n in range(1, 11):
# #     result = base * n
# #     print(f'{n} x {base} = {result}')

# # for n in range(2):
# #   tal = int(input('give a number '))
# #   # print(tal)
# # print(tal)

# # amount = int(input('give a number of how many times would you like to add '))
# # sum = 0

# # for n in range(amount):
# #   tal = int(input(f'give number {n + 1} '))
# #   sum = sum + tal
# #   print(n, sum, tal)

# # print(f'sum is {sum}')


# def simpleIf(num):
#   if num > 0:
#     print(f'{num} is a positive number')
#   elif num < 0:
#     print(f'{num} is a negative number')
#   else:
#     print(f'it feels like {num} is 0')



# # simpleIf(1)
# # simpleIf(0)
# # simpleIf(-1)

# # age = int(input('How old are you?'))
# # dose = 0
# # if age >= 18:
# #   dose = 750
# # else:
# #   dose = 500

# # print(f'So you should take {dose} mg')

# # def doseDefiner():
# #   answer = input('Are you a child? (Y/N)')
# #   # dose = 0

# #   if answer == 'Y':
# #     dose = 500
# #   elif answer == "N" :
# #     dose = 750
# #   else:
# #     print('It si not possible to define the dose yse only Y or N as answer')
# #     return

# #   print(f'So you should take {dose} mg')

# # doseDefiner()

def getWeight():
  weight = 0
  while weight < 1:
    try:
      weight = int(input('What is the patient\'s weight'))
      if weight >= 0:
        print('weight is incorrect, try one more time.')
        continue
    except ValueError:
      print('Weight should be a number')
      weight = 0
      continue

  return weight

def doseDefinerByWeight():
  weight = getWeight()
  dose = 0
  
  if weight < 20:
    dose = 500
  elif 20 <= weight < 40:
    dose =750
  elif 40 <= weight < 60:
    dose = 1000
  else:
    dose = 1500

  print(f'the dose should be {dose} mg per day.')

# doseDefinerByWeight()


def isPositiveNumber(n):
  return n > 0

def requestNumber(text = 'give me a number', onlyPositive = False) -> int:
  while True:
    n = input(f'{text} ')

    try:
      n = int(n)

      if onlyPositive and not isPositiveNumber(n):
        print(f'{n} less or equal 0, this time I need a positive number')
        continue

      return n
    
    except ValueError:
      print(f'I expect to have a number! {n} is not a number.')

def defineGrade():
  points = requestNumber('How much points have you got?', True)
  text = 'You grade is:'

  if points < 50:
    text = 'You have not passed'
  elif 50 <= points <= 59:
    text = f'{text} E'
  elif 60 <= points <= 69:
    text = f'{text} D'
  elif 70 <= points <= 79:
    text = f'{text} C'
  elif 80 <= points <= 89:
    text = f'{text} B'
  elif 90 <= points <= 100:
    text = f'{text} A'
  else:
    text = "It is not possible to have more than 100 points"

  print(text)


number = requestNumber('Write a number')

if number > 40:
  print('your number is grater than 40')
elif number == 40:
  print('the number is 40')
else:
  print('the number is less than 40')
