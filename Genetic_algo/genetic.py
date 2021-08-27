from copy import deepcopy
from random import random, randint
from sys import exit, argv


"""
BIG TODOS:
Implement loading, find theoretical lower bound, and:
All three types of crossover
Order vs cycle crossover
PMX vs CX
Simple crossover strategies failings
Try different mutation strategies
"""
"""
Loading and formatting distance data
"""
# Loads data from file cities.csv
data = []
with open("cities.csv", "r+") as file:
    for line in file.readlines():
        data.append(str(line).strip())

# Formats data into 2D array with ints in every position
for a in range(len(data)):
    data[a] = data[a].split()
    for b in range(len(data[a])):
        data[a][b] = int(data[a][b].strip(","))

"""
Defining functions for the main genetic algo loop
Fitness- Determined by subtracting the solution from the theoretical lower bound of the equation, and adding that
         negative value to 1000. 
"""
# Letter to number mapper
## City names (letters) are mapped to specific cells within the data and this function converts between the two
## Note: For a more versatile implementation, perhaps load the below letters in via CSV
letters = ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
def demapper(letter):
    for a in range(len(letters)):
        if letter == letters[a]:
            return a


# Solution conversion function
## Converts a solution of cities (letters) to visit into the respective distances between those cities
### TODO: MAYBE CHANGE TO DO ONE AT A TIME IN THE FUTURE
def converter(solutions):
    out_solutions = [[None for a in range(len(solutions[0]))] for b in range(len(solutions))]
    for a in range(len(solutions)):
        last_letter = None
        # Loading from data is row first, then column - technically shouldn't matter given nature of data
        for b in range(len(solutions[a])):
            letter = solutions[a][b]
            if last_letter is None:
                out_solutions[a][b] = data[demapper('X')][demapper(letter)]
            else:
                out_solutions[a][b] = data[demapper(last_letter)][demapper(letter)]
            last_letter = letter
        out_solutions[a].append(data[demapper(last_letter)][demapper('X')])
    return out_solutions


# Evaluation function
## Evaluates the lengths of letter solutions in a list and returns the list, sorted from best-performing to worst
## Also checks to see if the termination condition has been met - current condition is reaching fitness of 1000
def evaluate(solutions):
    finished = False
    ABC_solutions = converter(solutions)
    for a in range(len(ABC_solutions)):
        total = 0
        for num in ABC_solutions[a]:
            total += num
        solutions[a] = [solutions[a], total]
        if total <= 1400:
            finished = True
    if finished:
        solutions = sorted(solutions, key=lambda l:l[1])
        print(solutions[0])
        print(f"Highest total found: {solutions[0][1]}")
        print(f'ENDING: Goal length reached, ending program')
        with open("Best_solutions.txt", "a") as file:
            for solution in solutions:
                file.write(str(solution) + '\n')
        exit(0)
    return sorted(solutions, key=lambda l:l[1])


# Fitness calculation function
## Calculates the fitness of every solution in a list given the length of the tour
# TODO: Consider calculating and hard-coding the lower bound for this problem
lower_bound = 1000
def gym(solutions):
    solutions = deepcopy(solutions)
    for solution in solutions:
        solution[1] = lower_bound - solution[1] + 2500
    return solutions


# Wheel creation function
## Creates a roulette wheel which is used for many types of sampling - TODO: Describe how it works
def wheeler(solutions):
    wheel = []
    totalfit = 0
    for solution in gym(solutions):
        totalfit += solution[1]
    top = 0
    for solution in gym(solutions):
        f = solution[1]/totalfit
        wheel.append((top, top+f, solution[0]))
        top += f
    return wheel


# Binary search for sorting through the wheel
## Has to be done for the SUS to work, could work around it but I'm lazy
def binSearch(wheel, num):
    mid = len(wheel)//2
    low, high, answer = wheel[mid]
    if low<=num<=high:
        return answer
    elif high < num:
        return binSearch(wheel[mid+1:], num)
    else:
        return binSearch(wheel[:mid], num)


# Stochastic Universal Sampling Function
## Selects N number of solutions from the total number of solutions using stochastic universal sampling
def SUS(wheel, N):
    stepSize = 1.0/N
    answer = []
    r = random()
    answer.append(binSearch(wheel, r))
    while len(answer) < N:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
    return answer


# Cycle Crossover Function
## Performs cycle crossover by ensuring that every city maintains the position it had in at least one of the parents
def cycle_crossover(solutions): # TODO: See if this is actually working properly
    children = []
    for p1 in solutions:
        for p2 in solutions:
            if p1 != p2:
                child = []
                p2_reversed = deepcopy(p2)
                p2_reversed.reverse()
                for a in range(len(p1)):
                    if p1[a] == p2_reversed[a]:
                        child.append(p2[a])
                    else:
                        child.append(p1[a])
                children.append(child)
    return children


# Mutation function
## Creates N number of mutated solutions based upon the solutions given to it - mutation is Twors
## TODO: Add other types of mutation
def radiation(solutions, N):
    children = []
    for a in range(N):
        child = solutions[randint(0, len(solutions)-1)]
        l1 = randint(0, len(child)-1)
        l2 = randint(0, len(child)-1)
        child[l1], child[l2] = child[l2], child[l1] # TODO: Make sure this code works - it should
        children.append(child)
    return children


# Starting pool of children function
## Generates N number of random tours to populate the initial tour, use if not loading in old tours
def starting_pool(N):
    solutions = []
    while len(solutions) < N:
        solution = []
        cities = deepcopy(letters)
        cities.remove('X')
        while len(solution) < (len(letters)-1):
            solution.append(cities.pop(randint(0, len(cities)-1)))
        solutions.append(solution)
    return solutions


# Sanity check function
## Ensures that there are no duplicate cities within a selection of tours
def sanity(solutions):
    checked_solutions = []
    for solution in solutions:
        sane = True
        cities = []
        for letter in solution:
            if letter in cities:
                # print('ERROR: INSANE SOLUTION')
                # print('TYPE: OVERLAPPING CITIES')
                # print(solution)
                # print(cities)
                sane = False
            else:
                cities.append(letter)
        if len(cities) == 20 and sane:
            checked_solutions.append(cities)
        else:
            pass
            # print('ERROR: INSANE SOLUTION')
            # print('TYPE: NOT ALL LETTERS INCLUDED')
            # print(solution)
            # print(cities)
    return checked_solutions


""""
Main genetic algorithim loop

Each generation is made up of at least 100 individuals, around 50 of them should be produced from the crossover, 
and the rest from mutation. - Hypothetically

Two startup options:
1 - Create random tours and train
2 - Load a list of old tours to train
"""
if len(argv) != 2:
    raise SystemError("Usage: python genetic.py n\nn=1: Create pool at runtime\nn=2: Load pool at runtime from load_solutions.txt")
# Startup option 1 - Creating random tours
if argv[1] == '1':
    solutions = starting_pool(100)

# Startup option 2 - Loading a list of old tours
# TODO: Implement loading lists of old tours, and selection between the two startup options
if argv[1] == '2':
    solutions = []
    with open("load_solutions.txt", "r+") as file:
        for line in file.readlines():
            for letter in deepcopy(line.strip()):
                pass
                # Fix this later
    print(solutions)
raise NotImplementedError

# Main loop - Commented prints are for debugging purposes
generation = 0
best_solution = 100000000000
best_generation = []
last_gens = [100000000000 for a in range(100)]
gens_counter = 0
while True:
    generation += 1
    # Evaluating the fitness of every solution
    # print('Starting solutions:')
    solutions = evaluate(solutions)
    # print('\nEvaluation format:')
    # print(solutions)
    if best_solution > solutions[0][1]:
        best_solution = solutions[0][1]
        best_generation = solutions

    print(f'Generation:{generation}, Current best solution length: {best_solution}, '
          f'Generation size: {len(solutions)}, Generation best: {solutions[0][1]}')

    # Resets to best generation if the last 100 generations have gone nowhere - Mixed results at 15
    last_gens[gens_counter] = solutions[0][1]
    progress = False
    for total in last_gens:
        if total <= best_solution:
            progress = True
    if not progress:
        print('NOTICE: Best generation not exceeded in last fifteen generations, reverting')
        solutions = best_generation
    if gens_counter == 99:
        gens_counter = 0
    else:
        gens_counter += 1

    # Creating a wheel for the SUS
    wheel = wheeler(solutions)
    # print('\nWheel format:')
    # print(wheel)

    # Performing SUS on the solutions
    solutions = SUS(wheel, 50)
    # print('\nSUS:')
    # print(solutions)

    # Performing crossover on the selected solutions to make new solutions
    solutions = cycle_crossover(solutions)
    # print('CX:')
    # print(len(solutions))

    # Removing duplicate solutions from the bred solutions
    novel_solutions = []
    for solution in solutions:
        R_solution = deepcopy(solution)
        solution.reverse()
        if R_solution not in novel_solutions and solution not in novel_solutions:
            novel_solutions.append(R_solution)
    solutions = novel_solutions
    # print('After Duplicates removed:')
    # print(len(solutions))

    # Removing insane solutions from the bred solutions
    solutions = sanity(solutions)
    # print('Sanity check:')
    # print(len(solutions))

    # Check to see if the number of sane, non-duplicate solutions is dangerously low for some reason
    if len(solutions) < 50:
        print('WARNING: Length of solutions very low')
        print(f'WARNING: Current solutions length : {len(solutions)}')

    # Mutating the current solutions in order to fill the entire generation
    if len(solutions) < 150:
        mutants = radiation(solutions, 150-len(solutions))
    else:
        mutants = radiation(solutions, 30)
    for mutant in mutants:
        solutions.append(mutant)
    # print('Mutation:')
    # print(len(solutions))
