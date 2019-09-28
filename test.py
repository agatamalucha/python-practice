names = ["adam", "jan", "tomek", "as", "lukasz"]

names_dict = {"adam": 4, "jan": 3, "tomek": 5}

# 0. Policz ile elementow w liscie za pomoca for loop
# 1. print najdluzsze imie w w liscie
# 2. Lista ktora zmienia sie w dict
# 3. jak policzyc dlugosc stringa


counter = 0

for e in names:
    counter+=1
print (counter)


longest= ""

for e in names:
    if len(e)>len(longest):
        longest=e
    else:
        pass
print (longest)



