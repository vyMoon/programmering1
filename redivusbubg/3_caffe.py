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
#used to stop ordering
stopArticle = 0
articles = {
  coffeeKey: 1,
  teaKey: 2,
  cakeKey: 3,
}
prices = {
  coffeeKey: 30,
  teaKey: 50,
  cakeKey: 45,
}

def getNameByArticle(article):
  for dish, art in articles.items():
    if article == art:
      return dish
  return False

#requests a number from user. make sure that it is possible to use value as a number
def getNumber(message):
  while True:
    inp = input(f'{message} ')

    try:
      return int(inp)
    
    except:
      print(f'Ett tal behövs. {inp}  är inte ett tal. Försök igen')
      continue
  

def checkArticle(article):
  return article in [stopArticle, *articles.values()]


def checkAmount(value):
  return value > 0

# request a number and make sure the number is usable further.
# for example request correct value that is more than 0
def getSecureNumber(
    checkFn,
    requestMessage = 'Skriv ett tal',
    errorMessage = 'fel värde. Försök igen'
  ):
  while True:
    value = getNumber(requestMessage)

    if not checkFn(value):
      print(errorMessage)
      continue

    return value

# print out the menu on the screen
def showMenu():
  print('Meny')
  for dish, article in articles.items():
    print(f'{article} = {dish} ({prices[dish]} {currency})')
  print('\n')
  
# requests a list of items, menu article and amount
def getOrderItems():
  print('Välj rätter från menyn. Skriv gärna siffrorna')
  print(f'Skriv {stopArticle} om du är klar med beställningen')
  orderItems = []

  while True:
    # item = requestMenuArticle()
    item = getSecureNumber(
      checkArticle,
      'Vilket rätt du vill ha?',
      'Det finns inget rätt med denna artikel. Försök igen'
    )
    # 0 is stop article
    if item == stopArticle:
      print('Din beställning har skapats \n')
      return orderItems

    amount = getSecureNumber(
      checkAmount,
      'Hur många?',
      'Antal kan inte vara mindre än 1. Försök igen.'
    )
  
    orderItems.append({
      articleKey: item,
      amountKey: amount
    })


def requestMenuArticle():
  # 0 used as a stop article in order to stop order cycle
  availableArticles = [stopArticle, *articles.values()]
  while True:
    article = getNumber('Vilket rätt du vill ha?')

    if not article in availableArticles:
      print(f'Det finns inget rätt med artikel {article}. Försök igen')
      continue

    return article

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
    print(f'{amount}x {dish} - {prices[dish]} {currency}')
  print('------------------------')
  print(f"Totalt: {orderDescription[costKey]}")

def getOrder():
  showMenu()
  orderDescription = getOrderDescription(
    getOrderItems()
  )
  printReceipt(orderDescription)
  return orderDescription

getOrder()
