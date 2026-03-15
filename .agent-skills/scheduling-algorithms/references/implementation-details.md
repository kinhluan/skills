# Personal Research Implementation: Scheduling Algorithms

This document contains the heuristic and metaheuristic logic for parallel and distributed job scheduling.

## 1. Heuristic Algorithms (Fast)

### HEFT (Heterogeneous Earliest Finish Time)
```
1. Compute upward rank for each task
2. Sort tasks by rank (descending)
3. For each task in order:
   - Assign to processor that minimizes EFT
   - Use insertion-based scheduling
```

### Min-Min & Max-Min
- **Min-Min:** Select task with overall minimum completion time. Good for load balancing.
- **Max-Min:** Select task with maximum minimum completion time. Good for reducing makespan when long tasks exist.

## 2. Metaheuristic Algorithms (Search)

### Genetic Algorithm (GA)
```python
population = initialize_population()
for generation in range(max_generations):
    fitness = evaluate(population)
    parents = selection(population, fitness)
    offspring = crossover(parents)
    offspring = mutate(offspring)
    population = survivor_selection(population, offspring)
return best_solution(population)
```

### Variable Neighborhood Search (VNS)
```python
solution = initial_solution()
while not stopping_condition():
    for k in range(k_max):
        solution_prime = shake(solution, k)
        solution_double_prime = local_search(solution_prime)
        if improvement(solution_double_prime, solution):
            solution = solution_double_prime
            break
return solution
```

### Ant Colony Optimization (ACO)
```python
initialize_pheromones()
while not stopping_condition():
    for ant in range(num_ants):
        solution = construct_solution(pheromones, heuristics)
        solution = local_search(solution)
    update_pheromones(solutions, evaporation_rate)
return best_solution
```

## 3. Hybrid Approaches

### GA-VNS Hybrid
1. Use GA for global exploration.
2. Use VNS as a local search operator to refine offspring.

### ACO-GA Hybrid
1. ACO constructs high-quality initial pheromone trails.
2. GA operators (crossover/mutation) maintain population diversity.
