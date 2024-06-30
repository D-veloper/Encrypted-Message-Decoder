def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2

    stop_point = int(len(parent1)/2)
    child = parent1[:stop_point] + parent2[stop_point:]

    #  * Return the new chromosome
    #  * Genes should not be moved
    return child