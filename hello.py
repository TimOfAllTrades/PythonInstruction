import csv

#with open('Book1.csv', newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)

file = open('Book1.csv')
reader = csv.reader(file)
data = list(reader)

#print(data[5][3])

#for line in data:
#    if int(line[0]) > 2:
#        print(line)

a=3
b=4
print(a+b)

print(a+b)

