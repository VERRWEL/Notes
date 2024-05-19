x = {
    "1": 1,
    "2": 2,
    "3": 3
}

def dilite(b):

    if len(x) == 0:
        return 0
    else:
        x.pop(b)

print(x)
c = x.copy()
for i in c:
    dilite(i)

print(x)
