class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        man_to_woman = [-1] * n
        woman_to_man = [-1] * n
        proposal_index = [0] * n
        
        # women's ranking of men
        preference_rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for i, m in enumerate(women[w]):
                preference_rank[w][m] = i
        
        free_men = list(range(n))
        
        while free_men:
            man = free_men.pop(0)
            woman = men[man][proposal_index[man]]
            proposal_index[man] += 1
            
            if woman_to_man[woman] == -1:
                woman_to_man[woman] = man
                man_to_woman[man] = woman
            else:
                current_man = woman_to_man[woman]
                
                if preference_rank[woman][man] < preference_rank[woman][current_man]:
                    woman_to_man[woman] = man
                    man_to_woman[man] = woman
                    free_men.append(current_man)
                else:
                    free_men.append(man)
        
        return man_to_woman