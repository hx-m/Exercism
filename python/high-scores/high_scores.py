def latest(scores):
    scores.sort(reverse=True)    
    return scores[-2]


def personal_best(scores):
    latest = max(scores)
    return latest

def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
