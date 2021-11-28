for x in range(1,151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101,1):
    if x % 10 == 0 :
        print("Coding Dojo")
    elif x % 5 == 0 :
        print("coding")
    else:
        print(x)

sum = 0
for x in range(500001):
    if x % 2 != 0:
        sum += x
print(sum)


for x in range(2018, 0 , -4):
    if x % 2 == 0:
        print(x)

def three_num(low_num, high_num, mult):
    for x in range(low_num, high_num +1,1):
        if x % mult == 0:
            print(x)
        
three_num(2, 9, 3)