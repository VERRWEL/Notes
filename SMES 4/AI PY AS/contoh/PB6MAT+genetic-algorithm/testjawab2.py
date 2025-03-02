import random

#GENES = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_!"#%&/()=?@${[]}+'''
GENES = '1234567890'
POPULATION_SIZE = 10
TARGET = '12345'

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
FP = FillPopulation()

def CalcFitness(initial_population): #mengkalkulasikan poin fitness masing masing individu

    temp_dict_keys = list(initial_population.keys())
    calculated_population = {}

    for qi in temp_dict_keys:
        fitness = 0
        iteration = 0
        sep_key = SeparateChar(qi)
        for char in sep_key:
            if char == TARGET[iteration]:
                fitness += 1
            else:
                fitness = fitness

            iteration += 1
        calculated_population[qi] = fitness
        
    return calculated_population

def SortPopulation(calculated_population): # mengurutkan masing masing individu secara descending berdasarkan poin fitness
    fitness_sorted_population = sorted(calculated_population.items(), key=lambda x: x[1], reverse=True)
    return dict(fitness_sorted_population)


print(f"Target = {TARGET}")
print("\nUnsorted population : ")
for a,b in CalcFitness(FP).items():
    print(a,b)

print("\nSorted population : ")
for a,b in SortPopulation(CalcFitness(FP)).items():
    print(a,b)