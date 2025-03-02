import random

GENES = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_!"#%&/()=?@${[]}+'''
POPULATION_SIZE = 100
TARGET = 'Matkul Bamngke'

#make initial population

def MakeGenome():
    single_rand_gene = []
    for i in range(len(TARGET)):
        single_rand_gene.append(random.choice(GENES))
    return single_rand_gene


def MakeIndividual():
    single_generated_individual = []
    for i in range(POPULATION_SIZE):
        single_generated_individual.append(MakeGenome())
    return single_generated_individual

def JoinChar():
    list_joined_indiv = []
    for gene in MakeIndividual():
        single_joined_indiv = ''.join(gene)
        list_joined_indiv.append(single_joined_indiv)

    for indiv in list_joined_indiv:
        print(indiv)

#memisahkan masing-masing char dalam variabel 'TARGET' menjadi list
def SplitTARGET():
    list_split_target = []
    for char in TARGET:
        list_split_target.append(char)
    return list_split_target


def CalculateFitness():
    compare = SplitTARGET()