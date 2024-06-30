import random
from answer import alphabet

def get_letter():
    return random.choice(alphabet)
    
def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    i = random.randrange(len(chrom))

    mutated_chromosome = list(chrom)
    mutated_chromosome[i] = get_letter()

    new_chrome = ''.join(mutated_chromosome)

    return new_chrome
