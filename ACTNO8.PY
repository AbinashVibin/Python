city=[]
for i in range(5):
    C = input('Enter a C:')
    city.append(C)

print('citiesin the array:', city)
print('length of the array:', len(city))
city.append('Hong')
print('cities after +"Hong":',city)
city.pop(0)
print('remove the first element of th city:',city)
city.reverse()
print('reverse the word city:', city)