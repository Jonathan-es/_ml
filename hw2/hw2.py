import random

locations = [
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

def calcDist(pt1, pt2):
    return ((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) ** 0.5

def routeDist(route):
    total = 0
    size = len(route)
    for i in range(size):
        total += calcDist(locations[route[i]], locations[route[(i + 1) % size]])
    return total

def swapRoute(route):
    tempRoute = route[:]
    a, b = sorted(random.sample(range(len(route)), 2))
    tempRoute[a:b+1] = reversed(tempRoute[a:b+1])
    return tempRoute

def hillClimb(route, costFunc, neighborFunc, maxTries=10000):
    tries = 0
    bestRoute = route
    bestCost = costFunc(route)
    print("Starting Route Cost:", bestCost, route)

    while tries < maxTries:
        newRoute = neighborFunc(route)
        newCost = costFunc(newRoute)

        if newCost < bestCost:
            route = newRoute
            bestCost = newCost
            bestRoute = route
            tries = 0
            print("Finding best route...", bestCost, route)
        else:
            tries += 1

    print("Best Route:", bestCost, bestRoute)
    return bestRoute

bestPath = hillClimb(list(range(len(locations))), routeDist, swapRoute)
