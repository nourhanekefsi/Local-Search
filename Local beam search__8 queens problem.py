import random as r

def bestK(cost, neighbors, k):
    for i in range(len(cost) - 1):
        for j in range(i+1, len(cost)):
            if cost[j] < cost[i]:
                cost[i], cost[j] = cost[j], cost[i]
                neighbors[i], neighbors[j] = neighbors[j], neighbors[i]
    return cost[0:k], neighbors[0:k]


def lessThan(cost, c):
    for i in range(len(cost)):
        if c < cost[i]:
            return True, i 
    return False, -1

class Problem:
    def __init__(self, k):
        self.initial = []
        self.costInitial = []
        for _ in range(k):
            state=[8]*8
            for i in range(8):
                state[i] = r.randint(0,7)
            self.initial.append(state)
            self.costInitial.append(-self.value(state))
    
    def value(self, state):
        TLc = [0]*8
        c = 0
        for i in range(8):
            TLc[state[i]] += 1
        for i in range(8):
            if TLc[i] > 1:
                c += ( (TLc[i]-1) * TLc[i] ) / 2
        for i in range(8):
            for j in range(i+1, 8):
                if (j - i == state[j] - state[i] and j > i and state[j] > state[i]) or (j - i == state[i] - state[j] and i < j and state[j] < state[i]):
                    c += 1
        return -c
        
    def isGoal(self, state):
        c = Problem.value(self, state)
        if c == 0:
            return True
        return False
    
    def bestSuccessor(self, state):
        Cost = []
        s = []
        for i in range(8):
            for j in range(8):
                if j != state[i]:
                    sT = [0]*8
                    for z in range(8): 
                        if z != i: 
                            sT[z] = state[z]
                        else: 
                            sT[z] = j
                    c = - Problem.value(self, sT)
                    s.append(sT[:])
                    Cost.append(c)
        return s, Cost
    
def Local_beam_Search(problem, k):
    currents = problem.initial
    costCurrents = problem.costInitial
    while 0 not in costCurrents:
        neighbors = []
        costs = []
        for c in currents:
            neighbor, cost = problem.bestSuccessor(c)
            for i in range(len(neighbor)):
               neighbors.append(neighbor[i])
               costs.append(cost[i])
        costCurrents, currents = bestK(costs, neighbors, k)
    return currents[costCurrents.index(0)]
            
k = 7
probleme = Problem(k)
print(Local_beam_Search(probleme, k))
