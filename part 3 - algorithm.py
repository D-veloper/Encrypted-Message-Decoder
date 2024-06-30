import random
import math
import sys
from answer import is_answer, get_mean_score, alphabet
# You can redefine these functions with the ones you wrote previously.
# Another implementation is provided here.
# from encoding import create_chromosome
from tools import get_score # selection, crossover, mutation

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    string = ''.join([get_letter() for i in range(size)]) #my solution
    return string
    
def score(chrom):
    # floating number between 0 and 1. The better the chromosome, the closer to 1
    # We coded the get_score(chrom) in the previous exercise
    return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score

    sorted_chromosomes_list = sorted(chromosomes_list, key = lambda x:score(x), reverse = True)
    #  * Select the best individuals
    selection = [sorted_chromosomes_list[i] for i in range(math.ceil(GRADED_RETAIN_PERCENT * len(sorted_chromosomes_list)))]

    #  * Randomly select other individuals
    other_individuals = [chromosome for chromosome in sorted_chromosomes_list if chromosome not in selection]
    random.shuffle(other_individuals)

    selection += [other_individuals[i] for i in range(math.ceil(NONGRADED_RETAIN_PERCENT * len(other_individuals)))]
    return selection
    
def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2

    stop_point = int(len(parent1)/2)
    child = parent1[:stop_point] + parent2[stop_point:]

    #  * Return the new chromosome
    #  * Genes should not be moved
    return child
    
def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    i = random.randrange(len(chrom))

    mutated_chromosome = list(chrom)
    mutated_chromosome[i] = get_letter()

    new_chrome = ''.join(mutated_chromosome)

    return new_chrome

def create_population(pop_size, chrom_size):
    # use the previously defined create_chromosome(size) function
    # TODO: create the base population
    base_population = [create_chromosome(chrom_size) for i in range(pop_size)]
    return base_population
    
def generation(population):
    i = 0
    # selection
    # use the selection(population) function created on exercise 2
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # TODO: implement the reproduction
    while len(children) < int(len(select)/2):
        ## crossover
        random.shuffle(select)
        j = i + 1
        parent1 = select[i] # randomly selected
        parent2 = select[j] # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        i += 1
        child = crossover(parent1, parent2)
        
        ## mutation
        # use the mutation(child) function created on exercise 2
        child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children

def algorithm():
    chrom_size = int(input())
    population_size = 200
    
    # create the base population
    population = create_population(population_size, chrom_size)
    
    answers = []
    
    # while a solution has not been found :
    while not answers:
        ## create the next generation
        # TODO: create the next generation using the generation(population) function
        population = generation(population)
        
        ## display the average score of the population (watch it improve)
        # print(get_mean_score(population), file=sys.stderr)
    
        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    
    # TODO: print the solution
    print(answers[0])
    