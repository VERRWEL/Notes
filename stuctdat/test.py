Ge = {
    "AB" : 1,
    "CD" : 2,
    "EF" : 0,
    "GH" : 4
}


for i in Ge.keys():
    if Ge[i] < 1:
        del Ge[i]

for key, value in Ge.items():
    print(key, ":", value)