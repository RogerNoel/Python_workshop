# est le signe pour commenter le code

# on commence un bloc par l'instruction ":"
# ensuite l'indentation se fait automatiquement, ainsi on reste dans le même bloc
a = 5
if a > 0:
    print("a est positif")
elif a < 0:
    print("a est négatif")
else:
    print("a est neutre")

# un autre exemple avec while

while (a < 10):
    a = a +1
    print(a)