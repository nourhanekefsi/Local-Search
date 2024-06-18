import random as r

def bestK(cost, neighbors, k, p):
    if p < 0.2:
        a = 0
        b = 0.2
    elif p < 0.4:
        a = 0.2
        b = 0.4
    elif p < 0.6:
        a = 0.4
        b = 0.6
    elif p < 0.8:
        a = 0.6
        b = 0.8
    else:
        a = 0.8
        b = 1
    a *= sum(cost) / len(cost)
    b *= sum(cost) / len(cost)
    sC = []
    s = []
    i = 0
    while i < len(cost) and len(s) < k:
        if cost[i] <= b and cost[i] >= a:
                sC.append(cost[i])
                s.append(neighbors[i])
        i += 1
    return sC, s


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
        true = True
        while true:
            p = r.random()
            costCurrents, currents = bestK(costs, neighbors, k, p)
            if len(currents) == k:
                true = False 
    return currents[costCurrents.index(0)]
            
k = 7
probleme = Problem(k)
print(Local_beam_Search(probleme, k))
