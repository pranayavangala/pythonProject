x = ('apple' , 'orange', 'pear')
y = list(x)
y[1] = ('grape')
x = tuple(y)
print(x)
'''
Customer1= {'username': 'john-sea', 'online': 'false',
'friends':100}
print(Customer1)
'''
new_dict = {
 'brand': 'Honda',
 'model': 'Civic',
 'year': 1995
}
print(new_dict)

for x in new_dict:
 print(x)
#print all values in the dictionary
for x in new_dict:
 print(new_dict[x])
#loop through both keys and values
for x, y in my_dict.items():
 print(x, y)