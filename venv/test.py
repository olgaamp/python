a = 2
b = 2



class Model:
    value = 3

def x(a):
    a = a + 1


x(a)

c = Model()
d = c

print(id(c))
print(c.value)

c.value = 4 

print(id(d))
print(d.value)
print(id(a))
print(id(b))

