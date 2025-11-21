# Uppgift: Ändra listan och kör igen. Vad händer?

# tal = [1, 1, 1, 1, 1]
# summa = 0 
# for num in tal:
#   summa += num
# print("Summan är:", summa)


# Skriv ut varje tecken i en sträng
# Uppgift: Gör så att programmet också skriver tecknets position i texten.

text = "Python"

# for bokstav in text:
#   print(bokstav)

# for index in range(len(text)):
#   print(f'letter position: {index}, letter - {text[index]}')


# Övning 3 – Enkel räkneräknare
# Uppgift: Ändra så att den räknar ned från 10 till 1.

# räknare = 0

# while räknare < 5:
#   print("Räknare =", räknare)
#   räknare += 1

# räknare = 10

# while räknare > 0:
#   print("Räknare =", räknare)
#   räknare -= 1


# Övning 4 – Gissa talet
# Uppgift: Lägg till en räknare som visar hur många försök användaren behövde.

# hemligt_tal = 7
# gissning = int(input("Gissa talet mellan 1 och 10: "))
# counter = 1

# while gissning != hemligt_tal:
#   print("Fel! Försök igen.")
#   counter += 1
#   gissning = int(input("Gissa talet: "))
  
# print("Rätt gissat!")
# print(f'You have done {counter} attempts')


# Övning 5 – Skapa och ändra en lista
# Uppgift: Ta bort första frukten med pop(0) och skriv ut listan igen.

# frukter = ["äpple", "banan", "päron"]
# frukter.append("apelsin")
# print(frukter)
# frukter.pop(0)
# print(frukter)


# Övning 6 – Del-listor (slicing)
# Uppgift: Skriv ut de sista tre elementen och listan baklänges med slicing.

# nummer = [10, 20, 30, 40, 50, 60]
# print(nummer[1:4]) # [20, 30, 40]
# print(nummer[-3:])
# print(nummer[::-1])

# for i in range(len(nummer), 0, -1):
#   print(nummer[i - 1: i])


# Övning 7 – Räkna ut medelvärde med for-loop och lista
# Uppgift: Lägg till en while-loop som låter användaren mata
# in egna tal tills de skriver 'stop'.

def createArray():
  tal = []
  stopWord = 'stop'
  print('Provide a number.')
  print(f'if you are happy woth the provided numbers, provide the stop word: \'{stopWord}\'')

  while True:
    inp = input('What is next? ')

    if inp == stopWord:
      print('Ok I am starting to count the average value')
      return tal

    try:
      num = int(inp)
      tal.append(num)
    except ValueError:
      print(f'I expect to have a number or \'{stopWord}\'')
      print(f'{inp} is none of them. Try one more time')

def getAverageValue(arr):
  if len(arr) == 0:
    print('Err tha array is empty')
    return False
  
  summa = 0

  for t in arr:
    summa += t

  return summa / len(arr)


# print("Medelvärdet är:", getAverageValue(createArray()))


# def gett(text, onlyPositive = False):
#   while True:
#     inp = input(f'{text} ')
#     try:
#       num = int(inp)

#       if onlyPositive and num <=0:
#         print('this time you should provide a number that is grater tahn 0.')
#         print('Try one more time')
#         continue
      
#       return num

#     except ValueError:
#       print(f'You should provide a number. {inp} is not a number')
#       print('Try one more time')

def gett(text, onlyPositive = False):
  while True:
    inp = input(f'{text} ')

    try:
      num = int(inp)

      if onlyPositive and num <= 0:
        print('Only positive, try one more time')
        continue

      return num
    
    except ValueError:
      print(f'{inp} is not a number . try one more time')

print(gett('Provide a number', True))

