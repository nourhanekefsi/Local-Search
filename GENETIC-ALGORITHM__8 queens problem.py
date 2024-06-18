import random as r


def mutate(child):
    i = r.randint(0, len(child) -1)
    j = r.randint(0,len(child)-1)
    child[i] = j
    return child


def REPRODUCE(parent1, parent2):
    i = r.randint(0, len(parent1) - 2)
    child=[]
    child.extend(parent1[:i])
    child.extend(parent2[i:])
    return child

def WEIGHTED_RANDOM_CHOICES(population, weights, k):
    parents = [-1]
    while -1 in  parents or len(parents) < k:
        p = r.random()
        p = int(p * 10)
        a = (p - 1)*10 if p % 2 == 1  else p*10 
        b = a + 20
        j = 0
        for _ in range(k):
            for i in range(j, len(weights)):
                if weights[i] < b and weights[i] >= a :
                    if -1 in parents:
                        parents = [] 
                    parents.append(population[i])
                    break
            j = i + 1
    return (parents[i] for i in range(k))

def fitness(population):
    cost = []
    for p in population:
        TLc = [0]*8
        c = 0
        for i in range(8):
            TLc[p[i]] += 1
        for i in range(8):
            if TLc[i] > 1:
                c += ( (TLc[i]-1) * TLc[i] ) / 2
        for i in range(8):
            for j in range(i+1, 8):
                if (j - i == p[j] - p[i] and j > i and p[j] > p[i]) or (j - i == p[i] - p[j] and i < j and p[j] < p[i]):
                    c += 1
        cost.append(28 - c)
        w = [0]*len(cost)
        for i in range(len(cost)):
            w[i] =(cost[i] / sum(cost)) * 100

    return w

def GENETIC_ALGORITHM(population, fitness): 
    z = 0
    weights = fitness(population)
    print("weignts",weights," population ",population)
    while z < 100:
        population2 = []
        for _ in range(len(population)):
            parent1, parent2 = WEIGHTED_RANDOM_CHOICES(population, weights, 2)
            print("parents",parent1,parent2)
            child = REPRODUCE(parent1, parent2)
            print("child",child)
            p = r.random()
            if p < 0.1:
                child = mutate(child)
            population2.extend([child[:]])
        population = []
        population.extend(population2[:])
        weights = fitness(population)
        z += 1

    return population[weights.index(min(weights))]


population = [[r.randint(0,7) for _ in range(8)] for _ in range(2)]
print(GENETIC_ALGORITHM(population, fitness))
