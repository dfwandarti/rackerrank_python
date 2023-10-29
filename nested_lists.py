# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    all_scores = []
    scores_only = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_scores.append([name, score])
        scores_only.add(score)
        
    sorted_scores = list(scores_only)
    sorted_scores.sort()
    second_score = sorted_scores[1]
    names = [tuple[0] for tuple in all_scores if tuple[1] == second_score]
    names.sort()
    for name in names:
        print(name)
