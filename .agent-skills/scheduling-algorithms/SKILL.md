---
name: scheduling-algorithms
description: Job scheduling algorithms for parallel and distributed systems
metadata:
---

# Scheduling Algorithms

Algorithms and techniques for job scheduling in parallel and distributed systems.

## When to Use

- Designing scheduling systems for multi-core or distributed environments
- Research on scheduling optimization
- Comparing heuristic vs. metaheuristic approaches

## Algorithm Categories

### Heuristic Algorithms

Fast, rule-based approaches that provide good (not optimal) solutions.

#### HEFT (Heterogeneous Earliest Finish Time)

```
1. Compute upward rank for each task
2. Sort tasks by rank (descending)
3. For each task in order:
   - Assign to processor that minimizes EFT
   - Use insertion-based scheduling
```

**Complexity:** O(n² × m) where n=tasks, m=processors

**Best for:** Heterogeneous systems with known execution times

#### Min-Min Algorithm

```
1. For each unmapped task:
   - Find minimum completion time on each machine
2. Select task with overall minimum time
3. Assign to that machine
4. Repeat until all tasks mapped
```

**Complexity:** O(n² × m)

**Best for:** Load balancing in homogeneous systems

#### Max-Min Algorithm

```
Same as Min-Min, but select task with MAXIMUM minimum time
```

**Best for:** Reducing makespan when long tasks exist

### Metaheuristic Algorithms

Stochastic optimization for complex search spaces.

#### Genetic Algorithm (GA)

```python
# Pseudocode
population = initialize_population()
for generation in range(max_generations):
    fitness = evaluate(population)
    parents = selection(population, fitness)
    offspring = crossover(parents)
    offspring = mutate(offspring)
    population = survivor_selection(population, offspring)
return best_solution(population)
```

**Key Components:**
- Encoding: Task-to-machine mapping
- Crossover: Order-based, position-based
- Mutation: Swap, insertion, scramble

#### Variable Neighborhood Search (VNS)

```python
# Pseudocode
solution = initial_solution()
while not stopping_condition():
    for k in range(k_max):
        solution_prime = shake(solution, k)
        solution_double_prime = local_search(solution_prime)
        if improvement(solution_double_prime, solution):
            solution = solution_double_prime
            break  # Reset to first neighborhood
return solution
```

**Neighborhoods:**
- N1: Swap two tasks
- N2: Insert task at different position
- N3: Reverse subsequence

#### Ant Colony Optimization (ACO)

```python
# Pseudocode
initialize_pheromones()
while not stopping_condition():
    for ant in range(num_ants):
        solution = construct_solution(pheromones, heuristics)
        solution = local_search(solution)
    update_pheromones(solutions, evaporation_rate)
return best_solution
```

**Pheromone Update:**
```
τ_ij = (1 - ρ) × τ_ij + Σ(1 / L_k) for best solutions
```

## Hybrid Approaches

### GA-VNS Hybrid

```
1. Use GA for global search
2. Apply VNS as local search operator
3. VNS refines offspring before population update
```

**Benefits:**
- GA explores search space
- VNS exploits promising regions

### ACO-GA Hybrid

```
1. ACO constructs initial solutions
2. GA operators (crossover, mutation) diversify
3. Pheromone update from best GA solutions
```

## Performance Metrics

| Metric | Description |
|--------|-------------|
| Makespan | Total completion time (max) |
| Flow Time | Sum of completion times |
| Load Balance | Variance in machine utilization |
| Speedup | Sequential time / Parallel time |

## Research Directions

- **Unrelated Parallel Machines**: Different execution times per machine
- **Heterogeneous Multi-core**: Varying CPU capabilities
- **Energy-aware Scheduling**: Minimize power consumption
- **Dynamic Scheduling**: Tasks arrive online

## Resources

- [Scheduling Theory Handbook](https://www.scheduling-handbook.com/)
- Topalouglu et al. - "GA-VNS for Parallel Machine Scheduling"
