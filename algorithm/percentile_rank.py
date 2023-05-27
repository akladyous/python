# https://en.wikipedia.org/wiki/Percentile_rank
# https://www.educba.com/percentile-rank-formula/


# da controllare ancora!!!!!


scores_list = [2, 3, 3, 5, 7, 9, 1, 1, 11, 2]
def pr(scores, frequency):
    cf : cumulative_frequency = 0
    n = len(scores)
    for score in sorted(scores_list):
        if score <= frequency:
            cf += 1
    return ((cf-(0.5 * frequency))/n)*100

print(pr(scores_list,11))
