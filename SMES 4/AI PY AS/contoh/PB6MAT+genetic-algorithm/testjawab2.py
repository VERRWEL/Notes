import random

GENES = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_!"#%&/()=?@${[]}+'''
POPULATION_SIZE = 994
TARGET = 'Kecerdasan Buatan 4PTI52'

def MakeIndividual(): # membuat satu individu
    single_rand_gene = []
    for i in range(len(TARGET)):
        single_rand_gene.append(random.choice(GENES))
    return single_rand_gene

def JoinChar(unjoined_indiv): # mengkombinasi masing-masing char menjadi string
    joined_indiv = ''.join(unjoined_indiv)
    return joined_indiv

def SeparateChar(joined_indiv): # memisahkan masing-masing char menjadi list
    unjoined_indiv = list(joined_indiv)
    return unjoined_indiv

def FillPopulation(): #membuat populasi awal
    individuals = {}
    for i in range(POPULATION_SIZE):
        individuals[JoinChar(MakeIndividual())] = 0
    return individuals

def CalcFitness(population): #mengkalkulasikan poin fitness masing masing individu

    temp_dict_keys = list(population.keys())
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

def SortPopulation(unsorted_calc_population): #mengurutkan masing masing individu berdasarkan poin fitness
    fitness_sorted_population = sorted(unsorted_calc_population.items(), key=lambda x: x[1], reverse=True)
    return dict(fitness_sorted_population)

def Selection(population_tobe_selected): # memilih 2 individu untuk menjadi parent
    candidate1 = random.choice(list(population_tobe_selected.keys()))
    candidate2 = random.choice(list(population_tobe_selected.keys()))
    while candidate2 == candidate1:
        candidate2 = random.choice(list(population_tobe_selected.keys()))
    candidate3 = random.choice(list(population_tobe_selected.keys()))
    while candidate3 == candidate2 or candidate3 == candidate1:
        candidate3 = random.choice(list(population_tobe_selected.keys()))
    candidate4 = random.choice(list(population_tobe_selected.keys()))
    while candidate4 == candidate3 or candidate4 == candidate2 or candidate4 == candidate1:
        candidate4 = random.choice(list(population_tobe_selected.keys()))

    #print(f"candidates: \n{candidate1}\n{candidate2}\n{candidate3}\n{candidate4}")

    #tournament selection
    if population_tobe_selected[candidate1] > population_tobe_selected[candidate2]:
        parent1 = candidate1
    else:
        parent1 = candidate2
    if population_tobe_selected[candidate3] > population_tobe_selected[candidate4]:
        parent2 = candidate3
    else:
        parent2 = candidate4

    two_parents = [parent1, parent2]
    return two_parents

def Crossover(parent1, parent2): # fungsi kawin silang
    parent1 = list(parent1)
    parent2 = list(parent2)
    parent1_stay = []
    parent1_sepr = []
    parent2_stay = []
    parent2_sepr = []
    
    #print(f"parent1 {parent1} \nparent2 {parent2}")

    crossover_point = random.randint(1, len(parent1) - 1)
    #print(f"crossover point : {crossover_point}")

    for indx in range(0,crossover_point):
        parent1_stay.append(parent1[indx])
    for indx in range(crossover_point, len(parent1)):
        parent1_sepr.append(parent1[indx])
    for indx in range(0,crossover_point):
        parent2_stay.append(parent2[indx])
    for indx in range(crossover_point, len(parent2)):
        parent2_sepr.append(parent2[indx])

    for element in parent1_sepr:
        parent2_stay.append(element)
    for element in parent2_sepr:
        parent1_stay.append(element)

    #print(f"{parent1_stay}  \n{parent2_stay}")
    return JoinChar(parent1_stay), JoinChar(parent2_stay)

def MakingNextGeneration(prevgen): # fungsi membuat generasi selanjutnya
    newgen = {}

    while len(newgen) < POPULATION_SIZE:
        tmpsel = Selection(prevgen)
        newgen[Crossover(tmpsel[0], tmpsel[1])[0]] = 0

    # mutation
    newgenlist = list(newgen.keys())
    def mutate(iteration):

        mutation_rate = 0.3
        if iteration == POPULATION_SIZE:
            return
        else:
            mutation_point = random.randint(0, len(newgenlist[iteration]) - 1)
            
            if random.random() < mutation_rate:
                to_mutate = SeparateChar(newgenlist[iteration])
                to_mutate[mutation_point] = random.choice(GENES)
                #print(newgenlist)
                #print(f"choosen : {newgenlist.index(newgenlist[iteration])}")
                #print(f"before mutation {newgenlist[iteration]}")
                #print(f"after mutation {JoinChar(to_mutate)}")
                #print(f"mutation point {mutation_point}")

                newgen[JoinChar(to_mutate)] = 0
                newgen.pop(newgenlist[iteration])

            mutate(iteration + 1)
    mutate(0)

    newgen = SortPopulation(CalcFitness(newgen))

    return newgen

# MAIN PROGRAM
if __name__ == "__main__":
    firstgen = SortPopulation(CalcFitness(FillPopulation())) 
    #print(f"first generation {firstgen}")
    if list(firstgen.values())[0] == len(TARGET):
        print(list(firstgen.keys())[0])
    else:
        got = 0
        generation = 0
        while got != len(TARGET):
            nextgen = MakingNextGeneration(firstgen)
            got = list(nextgen.values())[0]
            firstgen = nextgen
            generation += 1
            print(f"generation {generation} | {list(nextgen.keys())[0]} | fitness {got}")
