import random as r


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
        bestC = 1000000
        s = []
        for i in range(8):
            for j in range(8):
                if j != state[i]:
                    sT = [0]*8
                    for k in range(8): 
                        if k != i: 
                            sT[k] = state[k] 
                        else: 
                            sT[k] = j
                    c = - Problem.value(self, sT)
                    if c < bestC:
                        s = []
                        s.append(sT)
                        bestC = c
        return s[0]
    
def HILL_CLIMBING(problem):
    current = problem.initial
    print( "\n\ninitial, ", - problem.value(current),"state=",current)
    while True:
        neighbor = problem.bestSuccessor(current)
        c1 = problem.value(neighbor)
        print("neighbor", - c1, neighbor)
        if c1 <= problem.value(current):
            print("\nresult, c=",- problem.value(current), "state", current)
            return current
        current = neighbor
def random_restart_hill_climbing(problem):
    goal = False
    while not goal:
        state = HILL_CLIMBING(problem)
        if problem.isGoal(state):
            goal = True
    print("final Result",state)

#s =[7, 2, 6, 3, 1, 4, 0, 5]
#s1 = [4, 5, 6, 3, 4, 5, 6, 5]
probleme = Problem()
#print(probleme.value(s1))
random_restart_hill_climbing(probleme)