import random as r
import math 

class Problem:
    def __init__(self):
        state=[8]*8
        for i in range(8):
            state[i] = r.randint(0,7)
        self.initial = state
    
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
        successor = state[:]
        column = r.randint(0, 7)
        line = r.randint(0, 7)
        successor[column] = line
        return successor
    
def simulated_annealing(problem, schedule):
    current = problem.initial
    t = 1
    
    t = 1
    while True:
        T = schedule(t)
        if T == 0:
            return current
        
        neighbor = problem.bestSuccessor(current)
        delta_E = problem.value(neighbor) - problem.value(current)
        
        if delta_E > 0 or 0.04 > math.exp(delta_E / T):
            current = neighbor
        
        t += 1

def schedule(t):
    return 100 - t  



problem = Problem()
solution = simulated_annealing(problem, schedule)
print("Solution trouvée: ", solution)
print("Valeur de la solution: ", -problem.value(solution))