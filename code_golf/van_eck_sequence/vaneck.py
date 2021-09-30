x = 0
iterator = 1
a = []
b = []
print(0)
a.append(x)
while iterator <= 1001:
    last = (iterator - 1) in b
    if last == False:
        x = 0
        a.append(x)
        b.append(x)
        print(x)

    else:
        while a[last] != x:
            if a[last] != x:
                last -= 1
            else:
                x = a[last]
                y = iterator - last
                a.append(y)
                print(y)
            l
        

    iterator += 1
