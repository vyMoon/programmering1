# while True:
#   stopWord = 'stop'
#   text = input(f'Write smth in order to repeat it, or write {stopWord} to stop the programme.')

#   if text != stopWord:
#     print('The programme is stopped')
#     break

#   print(text)


# text = 'jensens'
# sCount = 0
# for i in range(0, len(text)):
  
#   if (text[i] == 's'):
#     sCount += 1

# print(sCount)


# i  = 0 
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# def vowelCounter():
#   vowels = ['a', 'i', 'e', 'o', 'u', 'y', 'å', 'ö', 'ä']
#   text = input('write a text in order to count vowels')
#   vowelCounter = 0

#   for text in text:
#     print(text)
#   #   if text[i].lower() in vowels:
#   #     vowelCounter += 1
#   # print(vowelCounter)
#   print(text)

# vowelCounter()

# it = 'string'.__iter__()
# print(it.__repr__())


# while it.__length_hint__():
#   print(it.__length_hint__())
#   print('next', it.__next__())
#   print(it.__length_hint__())
# print('the string is over')




def requestPass():
  pas = 'python123'

  while True:
    inpt = input('write the password ')

    if inpt == pas:
      print('You have the access')
      break

    print('password is incorrect')

# requestPass()

from tools import requestNumber

def gasConsum():
  distance = requestNumber('How many kilometers have you driven', True)
  gasConsummation = requestNumber('HOw much gas have been used', True)

  consummationPerMil = round((gasConsummation / distance) * 10, 2 )
  print(consummationPerMil)
  if consummationPerMil > 1:
    print('Bilen drar mycket bränsle')
  else:
    print('Bra bränsleekonomi')


# gasConsum()

def speedComparison():
  maxSpeed = requestNumber('What is allowed speed?', True)
  speed = requestNumber('What is your speed', True)
  diff = speed - maxSpeed

  if diff > 0 :
    print('Du kör för fort!')
    if diff >= 30:
      print('Du riskerar böte!')
  else:
    print('Du hller hastighetsgränsen')

speedComparison()