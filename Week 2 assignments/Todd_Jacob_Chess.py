x = 0
y = 1
while x < 64:
    y = y * 2
    x = x + 1

print(y,"amount of grains")
print(int(y*50/1000),"amount of grain in grams")    #y amount of grain * 50 mg per grain / 1000 converting to grams
print(254806*1000/y,"meters high in grain")     #254806 amount of square KM, 1000 converting to meters, lets say the grain is 1 square meter
