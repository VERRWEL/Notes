
#finding minimum
"""
ls = [10,11,76,9,5,7]
now = ls[0]
for temp in ls:
    if temp < now:
        now = temp

print(now)
"""
dik = {
    'P1' : [0,7],
    'P2' : [2,4],
    'P3' : [4,1],
    'P4' : [5,4]

}
"""
now = list(dik.values())[0][1]
for temp in list(dik.keys()):
    print("hadeuha ", dik[temp][1])
    if dik[temp][1] < now:
        now = dik[temp][1]
"""

"""
now = list(dik.keys())[0]
# now becomes P1
for temp in list(dik.keys()):
    if dik[temp][1] < dik[now][1]:
        now = temp
print(now)
"""

tmp = []
for i in list(dik.keys()):
    tmp.append(dik[i][1])

print(sum(tmp))