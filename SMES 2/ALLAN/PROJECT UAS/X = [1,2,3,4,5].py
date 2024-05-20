a = {"b" : 2}
b = {"a" : 1}

gogo =[a,b]
l = max(list(a.values()) + (list(b.values()))) 

for y in gogo:
    for i in y:
        if (y[i]) == l:
            x = i
print(l, "as max val", x, "as the key")