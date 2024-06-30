import random
from answer import alphabet

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    string = ''.join([get_letter() for i in range(size)]) #my solution
    return string
    