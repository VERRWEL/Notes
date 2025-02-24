import random

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}+'''
POPULATION_SIZE = 100
TARGET = 'Matkul Bamngke'

#make initial population

def MakeGenome():
    x = []
    for i in range(len(TARGET)):
        x.append(random.choice(GENES))
    return x


def MakeIndividual():
    y = []
    for i in range(POPULATION_SIZE):
        y.append(MakeGenome())
    return y

for i in MakeIndividual():
    print(i)
print(f"total individual/chromosome : {len(MakeIndividual())}")
