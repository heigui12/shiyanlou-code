a = 0
b = '7'

while a < 100:
    a = a + 1
    
    if a % 7 == 0:
        continue
    elif str(a).find(b) == 1:
        continue
    else:
        print(a)
    

