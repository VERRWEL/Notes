import random

GENES = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_!"#%&/()=?@${[]}+'''
POPULATION_SIZE = 100
TARGET = '123456789'

def MakeIndividual(): # membuat satu individu
    single_rand_gene = []
    for i in range(len(TARGET)):
        single_rand_gene.append(random.choice(GENES))
    return single_rand_gene


def JoinChar(unjoined_indiv): # mengkombinasi masing-masing char dalam variabel 'TARGET' menjadi string
    joined_indiv = ''.join(unjoined_indiv)
    return joined_indiv

def SeparateChar(joined_indiv): # memisahkan masing-masing char menjadi list
    unjoined_indiv = list(joined_indiv)
    return unjoined_indiv

def FillPopulation(): #memenuhi populasi
    individuals = {}
    for i in range(POPULATION_SIZE):
        individuals[JoinChar(MakeIndividual())] = 0
    return individuals

def CalcFitness(initial_population): #mengkalkulasikan poin fitness masing masing individu

    #print original dict individual
    print("uncalculated :")
    for a,b in initial_population.items():
        print(a, b)
    print("\n")

    temp_dict_keys = list(initial_population.keys())
    calculated_population = {}

    for qi in temp_dict_keys:
        fitness = 0
        sep_key = SeparateChar(qi)
        for char in sep_key:
            if char == TARGET[sep_key.index(char)]:
                fitness += 1
            else:
                fitness = fitness

        calculated_population[qi] = fitness
    return calculated_population
        

    
for a,b in CalcFitness(FillPopulation()).items():
    print(a,b)