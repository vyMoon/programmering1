# Scenario:
# I denna övning ska du hjälpa flygplatsens personal att sortera bagage efter vikt.
# Krav:
# A. Inmatning
#  Använd while-loop för att mata in väskvikter tills användaren skriver “stop”.
# B. Funktioner
# Skapa tre funktioner:
# 1. totalvikt(lista)
# 2. sortera_vikt(lista)
# Den ska sortera väskor i:
# lätt (< 10 kg)
# normal (10–20 kg)
# tung (> 20 kg)
# 3. rapport() som skriver:
# Total vikt: 274 kg
# Lätta väskor: 4
# Normala väskor: 7
# Tunga väskor: 2
# C. Extra krav (svårare)
#  Skriv även ut medelvikt per väska.
#  Skriv ut tungaste väskan.

lightKey = 'light'
normalKey = 'normal'
heavyKey = 'heavy'

def getBaggageList():
  stopWord = 'stop'
  baggage = []

  print('Create a list of the baggage. Write the weight (in kg) of every bag one by one.')

  while True:
    next = input('Provide the weight of the next bag ')

    try:
      weight = int(next)

      if weight < 1:
        print(f'Weight should be more than 0. {weight} is provided')
        continue

      baggage.append(weight)

    except:
      if next == stopWord:
        print('The list of the baggage is created')
        return baggage
      
      print(f'Weight should be a number. {next} is not a number. Try again')
      continue

def getTotalWeight(arr):
  return sum(arr)

def sortByWeight(arr):
  baggage = {
    lightKey: [],
    normalKey: [],
    heavyKey: [],
  }

  for item in arr:
    if item < 10:
      baggage['light'].append(item)
    elif 10 <= item <= 20:
        baggage['normal'].append(item)
    elif item > 20:
        baggage['heavy'].append(item)
  
  return baggage

def rapport(baggage):
  totalWeight = getTotalWeight(baggage)
  sortedBaggage = sortByWeight(baggage)
  print(f'Total vikt: {totalWeight}')
  print(f'Lätta väskor: {len(sortedBaggage[lightKey])}')
  print(f'Normala väskor: {len(sortedBaggage[normalKey])}')
  print(f'Tunga väskor: {len(sortedBaggage[heavyKey])}')

  print(f'Medelvikt per väska: {totalWeight / len(baggage)}')
  print(f'tungaste väskan: {max(baggage)}')


def baggageControl():
  rapport(
    getBaggageList()
  )

baggageControl()