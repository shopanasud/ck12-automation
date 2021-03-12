print("Hi")
a = [1,"s",{"l": "g"}]
b = (1,"sd",{"h": "g"})
a[0] = 2
x, y, z = b
# b[0] = 2
print(a[0])
print(a[1])
print(a[2])
print("+++++++++++++++++++++")
print("b : ", b)
print(x)
print(y)
print(z)
for item in b:
    a.append(item)
print(a)