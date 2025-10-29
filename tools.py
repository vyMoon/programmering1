def isPositiveNumber(n) -> bool:
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

def getOrdinalNumber(num) -> str:
  lastDigit = int(str(num)[-1])
  postfix = ''

  match lastDigit:
    case 1:
      postfix = 'st'
    case 2:
      postfix = 'nd'
    case 3:
      postfix = 'rd'
    case _:
      postfix = 'th'
    
  return f'{num}{postfix}'

def getSetNumbers(amount):
  numbers = []

  for i in range(amount):
    numbers.append(
      requestNumber(f'Give me the {getOrdinalNumber(i + 1)} number')
    )
  
  return numbers

def sumArray(numbers):
  sum = 0
  for i in numbers:
    sum += i
  return sum

def getOperatorCalc():
  allowedOperators = ['+', '-', '*', '/']

  print('Provide an operator from list of possible operators. The list is bellow')

  for i in allowedOperators:
    print(i)
  
  while True:
    candidate = input('Provide operator ')

    if candidate in allowedOperators:
      return candidate
    else:
      print('You can chose only from the list of allowed operators. See the list above and try one more time')

def getCalcResult(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  
  return False
