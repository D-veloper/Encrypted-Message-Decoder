import random
from answer import get_score
import math # my code
    
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
