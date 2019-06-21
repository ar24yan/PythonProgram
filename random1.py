from random import *

z = []
for i in range(5):
    z.append(random())
print(z)

a = []
for i in range(5):
    a.append(randint(50, 100))
print(a)

b = [2,3,4,5,6]
shuffle(b)
print(b)

c = []
for j in range(5):
    c.append(uniform(5,10))
print(c)

l = []
list = ["Ayran", "Golu", "Raja", "Raju"]
for i in range(5):
    l.append(choice(list))
print(l)


