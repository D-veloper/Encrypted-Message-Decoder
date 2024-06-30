
from answer import get_answer

def get_score(chrom):
    key = get_answer()
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
    count = 0
    for i in range(len(key)):
        if chrom[i] == key[i]:
            count += 1
    
    score = count/len(key)

    return score
    