# Scenario:
# Du driver ett café och vill skapa ett system som genererar kvitto efter flera beställningar.

# Krav:
# A. Menyfunktion
#  Funktion meny() returnerar pris baserat på val:
# o 1 = Kaffe (30 kr)
# o 2 = Te (25 kr)
# o 3 = Kaka (45 kr)

# B. Beställningsloop
# Använda while:
#  Fråga användaren vilken artikel de vill beställa
#  Fråga sedan hur många
#  Lägg till artikel + antal i två listor:
# o artikelns namn
# o antal
# o totalpris (pris * antal)

# C. Kvittoutskrift (egen funktion)
# Funktionen skriv_kvitto() ska skriva:
# 1x Kaffe - 30 kr
# 2x Te - 50 kr
# 1x Kaka - 45 kr
# ------------------------
# Totalt: 125 kr

coffeeKey = 'Kaffe'
teaKey = 'Te'
cakeKey = 'Kaka'

articleKey = 'article'
amountKey = 'amount'

costKey = 'cost'
itemsKey = 'items'

currency = 'kr'
# used to stop ordering
stopArticle = 0
productArticles = {
  coffeeKey: 1,
  teaKey: 2,
  cakeKey: 3,
}

prices = {
  coffeeKey: 30,
  teaKey: 25,
  cakeKey: 45,
}

def getNameByArticle(searchArticle):
  for dishName, article in productArticles.items():
    if searchArticle == article:
      return dishName
  return False

# requests a number from user. make sure that it is possible to use the value as a number
def getNumber(message):
  while True:
    inp = input(f'{message} ')

    try:
      return int(inp)
    except:
      print(f'Ett tal behövs. {inp} är inte ett tal. Försök igen.')
      continue
  

# request a number and make sure the number is valide.
def getValidNumber(
    validatorFn,
    requestMessage = 'Skriv ett tal',
    errorMessage = 'Fel värde. Försök igen'
  ):
  while True:
    value = getNumber(requestMessage)

    if not validatorFn(value):
      print(errorMessage)
      continue

    return value


def articleValidator(article):
  return article in [stopArticle, *productArticles.values()]

def amountValidator(value):
  return value > 0

# print out the menu on the screen
def showMenu():
  print('Meny')
  for name, article in productArticles.items():
    print(f'{article} = {name} ({prices[name]} {currency})')
  print('\n')
  
# requests a list of items, menu article and amount
# uses stopArticle to stop ordering
def getOrderItems():
  print('Välj rätter från menyn. Skriv gärna siffrorna')
  print(f'Skriv {stopArticle} om du är klar med beställningen')
  orderItems = []

  while True:
    item = getValidNumber(
      articleValidator,
      'Vilket rätt du vill ha?',
      'Det finns inget rätt med denna artikel. Försök igen'
    )
    # 0 is stop article
    if item == stopArticle:
      return orderItems

    amount = getValidNumber(
      amountValidator,
      'Hur många?',
      'Antal kan inte vara mindre än 1. Försök igen.'
    )
  
    orderItems.append({
      articleKey: item,
      amountKey: amount
    })


def getOrderDescription(items):
  description = {
    costKey: 0,
    itemsKey: {}
  }

  for item in items:
    dish = getNameByArticle(item[articleKey])

    if not dish:
      raise ValueError('Not existent article')
    
    amount = item[amountKey]
    description[costKey] += prices[dish] * amount

    if dish in description[itemsKey]:
      description[itemsKey][dish] += amount
    else:
      description[itemsKey][dish] = amount

  return description

def printReceipt(orderDescription):
  for dish, amount in orderDescription[itemsKey].items():
    print(f'{amount}x {dish} - {prices[dish] * amount} {currency}')
  print('------------------------')
  print(f"Totalt: {orderDescription[costKey]}")

def getOrder():
  showMenu()
  orderItems = getOrderItems()

  if len(orderItems) == 0:
    print('Inget beställt.')
    return False
  
  print('Din beställning har skapats \n')
  orderDescription = getOrderDescription(orderItems)
  printReceipt(orderDescription)
  return orderDescription

getOrder()
