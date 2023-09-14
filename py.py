import random
from pokemonDB import typeList

random.shuffle(typeList)

for item in typeList:
    print(item)