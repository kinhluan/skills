---
name: scheduling-algorithms
description: Job scheduling algorithms for parallel, distributed, and real-time systems. Use for OS scheduling, cloud resource allocation, workflow optimization, and research on heuristic/metaheuristic/ML-based approaches.
metadata:
  tags: ["scheduling", "algorithms", "optimization", "parallel-computing", "real-time", "cloud", "heuristics", "metaheuristics", "machine-learning", "domain-specific"]
---

# Scheduling Algorithms

Comprehensive guide to scheduling algorithms spanning operating systems, parallel/distributed systems, cloud computing, real-time systems, and machine learning-based approaches.

> "Scheduling is the art of allocating scarce resources to competing demands over time."

---

## 1. When to Use

- Designing OS process/thread schedulers
- Allocating tasks in HPC clusters or cloud environments
- Optimizing workflow execution (DAGs, task graphs)
- Research on scheduling optimization and comparison
- Real-time embedded systems with deadlines
- Container orchestration and resource management

---

## 2. Fundamental OS Scheduling Algorithms

### First-Come First-Served (FCFS)

Simplest non-preemptive scheduler.

```
Process queue: P1(24), P2(3), P3(3)
Timeline: | P1(0-24) | P2(24-27) | P3(27-30) |
Waiting times: P1=0, P2=24, P3=27  →  Avg = 17
```

**Pros:** Simple, no starvation  
**Cons:** Convoy effect (short jobs wait behind long ones)  
**Complexity:** O(1) per decision

### Shortest Job First (SJF) / Shortest Remaining Time First (SRTF)

Optimal for minimizing average waiting time.

```
Preemptive (SRTF):
Arrival: P1(0,7), P2(2,4), P3(4,1), P4(5,4)
Timeline: | P1(0-2) | P2(2-4) | P3(4-5) | P2(5-7) | P4(7-11) | P1(11-16) |
```

**Pros:** Minimizes average waiting time  
**Cons:** Requires prediction of burst time; starvation of long jobs  
**Prediction:** Exponential averaging: `τₙ₊₁ = α·tₙ + (1-α)·τₙ`

### Round Robin (RR)

Time-quantum based preemptive scheduling.

```
Quantum = 4, Processes: P1(10), P2(3), P3(5)
Timeline: | P1(0-4) | P2(4-7) | P3(7-11) | P1(11-15) | P3(15-18) | P1(18-20) |
```

**Quantum selection:**
- Too large → FCFS behavior
- Too small → excessive context switches (overhead > 80%)
- Rule of thumb: 80% of CPU bursts should be < quantum

**Complexity:** O(1)  
**Best for:** Time-sharing systems

### Priority Scheduling

```
Priority queue with aging to prevent starvation:
Effective priority = Base priority + (waiting_time / aging_factor)
```

**Starvation fix:** Aging — increase priority of waiting processes over time.

### Multilevel Queue (MLQ)

```
System processes (highest priority, RR q=8)
Interactive processes (RR q=16)
Batch processes (FCFS)
Student processes (lowest priority, RR q=32)
```

Fixed partitions; processes don't move between queues.

### Multilevel Feedback Queue (MLFQ)

Processes can move between queues based on behavior.

```
Q0: RR with q=8ms   → if not done, demote to Q1
Q1: RR with q=16ms  → if not done, demote to Q2
Q2: RR with q=32ms  → if not done, demote to Q3
Q3: FCFS (lowest priority)
```

**Rules:**
1. New jobs enter Q0
2. Job uses full quantum → demoted
3. Job yields before quantum → stays or promoted
4. After waiting in low queue → promoted (aging)

**Best for:** Unknown job characteristics; adapts to I/O-bound vs CPU-bound.

---

## 3. Parallel & Distributed Scheduling

### HEFT (Heterogeneous Earliest Finish Time)

For DAG scheduling on heterogeneous processors.

```
1. Compute upward rank for each task (longest path to exit)
2. Sort tasks by rank (descending)
3. For each task in order:
   - For each processor: compute earliest finish time (EFT)
   - Assign to processor with minimum EFT
   - Use insertion-based scheduling (fill gaps)
```

**Complexity:** O(n² × m) where n=tasks, m=processors  
**Best for:** Heterogeneous systems with known execution times  
**Limitation:** Static; assumes known execution times

### Min-Min Algorithm

```
1. For each unmapped task:
   - Find minimum completion time (CT) on each machine
2. Select task with overall minimum CT
3. Assign to that machine
4. Update machine availability; repeat until all mapped
```

**Complexity:** O(n² × m)  
**Best for:** Load balancing in homogeneous systems  
**Weakness:** Favors short tasks; long tasks may starve

### Max-Min Algorithm

Same as Min-Min, but select task with **MAXIMUM** minimum completion time.

**Best for:** Reducing makespan when long tasks exist  
**Trade-off:** May hurt load balancing

### Suffrage Algorithm

```
For each task, compute: suffrage = second_best_CT - best_CT
Select task with maximum suffrage (most "hurt" by not getting best machine)
Assign to its best machine
```

**Best for:** Better balance between Min-Min and Max-Min

---

## 4. Metaheuristic Algorithms

### Genetic Algorithm (GA)

```python
# Pseudocode
population = initialize_population(size=N)
for generation in range(max_generations):
    fitness = [evaluate(chromosome) for chromosome in population]
    parents = tournament_selection(population, fitness, k=3)
    offspring = []
    for i in range(0, len(parents), 2):
        child1, child2 = order_crossover(parents[i], parents[i+1])
        child1 = swap_mutation(child1, prob=0.1)
        child2 = insert_mutation(child2, prob=0.1)
        offspring.extend([child1, child2])
    population = elitism_replacement(population, offspring, elite_size=2)
return best_solution(population)
```

**Encoding:** Task-to-machine mapping (permutation or direct)  
**Crossover:** Order-based (OX), Partially mapped (PMX), Position-based  
**Mutation:** Swap, insertion, scramble, inversion  
**Selection:** Tournament, roulette wheel, rank-based

**Parameters:**
| Parameter | Typical Range |
|---|---|
| Population size | 50-200 |
| Crossover rate | 0.7-0.9 |
| Mutation rate | 0.01-0.1 |
| Generations | 100-1000 |

### Particle Swarm Optimization (PSO)

```python
# Pseudocode
particles = initialize_swarm(N, dim=num_tasks)
velocities = random_velocities(N, dim)
pbest = particles.copy()
gbest = best(pbest)

for iteration in range(max_iter):
    for i, particle in enumerate(particles):
        velocities[i] = w*velocities[i] \
            + c1*r1*(pbest[i] - particle) \
            + c2*r2*(gbest - particle)
        particles[i] = update_position(particle, velocities[i])
        if fitness(particles[i]) < fitness(pbest[i]):
            pbest[i] = particles[i]
    gbest = best(pbest)
return gbest
```

**Best for:** Continuous optimization spaces; fast convergence  
**Parameters:** w (inertia), c1 (cognitive), c2 (social)

### Variable Neighborhood Search (VNS)

```python
# Pseudocode
solution = initial_solution()
while not stopping_condition():
    for k in range(1, k_max+1):
        solution_prime = shake(solution, k)      # random neighbor in Nk
        solution_double_prime = local_search(solution_prime)
        if fitness(solution_double_prime) < fitness(solution):
            solution = solution_double_prime
            k = 1  # Reset to first neighborhood
return solution
```

**Neighborhoods:**
- N1: Swap two tasks
- N2: Insert task at different position
- N3: Reverse subsequence (2-opt)
- N4: Move task to different machine

### Ant Colony Optimization (ACO)

```python
# Pseudocode
initialize_pheromones(tau_0)
for iteration in range(max_iter):
    solutions = []
    for ant in range(num_ants):
        solution = construct_solution(pheromones, heuristic_info)
        solution = local_search(solution)  # optional
        solutions.append(solution)
    update_pheromones(solutions, evaporation_rate=rho)
    # Elitist: extra pheromone on best solution
return best_solution(solutions)
```

**Pheromone update:**
```
τ_ij = (1 - ρ) × τ_ij + Σ(1 / L_k) for all ants k that used edge (i,j)
```

**Best for:** Combinatorial optimization; works well with scheduling constraints

### Simulated Annealing (SA)

```python
# Pseudocode
T = T_max
solution = initial_solution()
while T > T_min:
    for _ in range(iterations_per_temp):
        neighbor = generate_neighbor(solution)
        delta = fitness(neighbor) - fitness(solution)
        if delta < 0 or random() < exp(-delta / T):
            solution = neighbor
    T = alpha * T  # cooling, alpha ∈ [0.95, 0.999]
return solution
```

**Best for:** Escaping local optima; simple to implement

---

## 5. Hybrid Approaches

### GA-VNS Hybrid

```
1. GA explores global search space
2. VNS acts as local search operator within GA loop
3. After crossover/mutation, apply VNS to offspring
4. VNS refines before population evaluation
```

**Benefits:** GA diversity + VNS exploitation

### ACO-GA Hybrid

```
1. ACO constructs diverse initial population
2. GA operators (crossover, mutation) explore
3. Pheromone update incorporates best GA solutions
4. Feedback loop between both methods
```

### Memetic Algorithm (MA)

GA + local search embedded in every generation.

```
for generation in generations:
    population = genetic_operators(population)
    for individual in population:
        individual = local_search(individual)  # Lamarckian learning
    population = selection(population)
```

---

## 6. Machine Learning-Based Scheduling

### Reinforcement Learning (RL) Scheduling

```python
# RL formulation for scheduling
State:  [machine_loads, task_queue, current_time]
Action: assign_task_to_machine(task_id, machine_id)
Reward: -makespan  or  -energy  or  +throughput

# Common algorithms
- DQN (Deep Q-Network): discrete action space
- PPO (Proximal Policy Optimization): stable policy gradient
- A3C (Asynchronous Advantage Actor-Critic): parallel training
```

**State representation:**
- Machine features: CPU, memory, load, queue length
- Task features: runtime estimate, deadline, priority, dependencies
- System features: time, energy consumption

**Reward shaping:**
```
R = -α·makespan - β·energy + γ·deadline_met - δ·starvation
```

### Neural Network Predictors

Predict task execution times to improve scheduling decisions.

```python
# LSTM/Transformer for runtime prediction
features = [task_type, input_size, historical_runtimes, system_load]
predicted_runtime = model.predict(features)
# Use predicted_runtime in HEFT/Min-Min instead of static estimates
```

### Graph Neural Networks (GNN) for DAG Scheduling

```python
# Task graph as graph
nodes = tasks with features (execution_time, priority)
edges = dependencies with features (data_size, communication_cost)

# GNN encoder → node embeddings
embeddings = GNN(task_graph)

# Policy network → scheduling decisions
action_probs = policy_network(embeddings, machine_states)
selected_action = sample(action_probs)
```

**Best for:** Complex dependency structures; learns communication patterns

### Neural Architecture Search (NAS) for Scheduling

Auto-design scheduling policies:
```
Search space: RL policy architectures (LSTM, Transformer, GNN)
Controller: RNN samples architectures
Evaluator: Train RL agent, measure makespan/energy
```

---

## 7. Real-Time Scheduling

### Earliest Deadline First (EDF)

Dynamic priority; highest priority to task with nearest deadline.

```
Schedulability test (sufficient for periodic tasks on single CPU):
Σ(Ci / Ti) ≤ 1   (utilization bound)

Where Ci = worst-case execution time, Ti = period
```

**Pros:** Optimal for preemptive uniprocessor; simple  
**Cons:** Priority inversion; complex on multiprocessor

### Rate Monotonic (RM) / Rate Monotonic Scheduling (RMS)

Static priority; shorter period → higher priority.

```
Schedulability test (sufficient):
Σ(Ci / Ti) ≤ n(2^(1/n) - 1)   → approaches ln(2) ≈ 0.693 as n→∞

Exact test: Response time analysis
Ri = Ci + Σ[j∈hp(i)] ⌈Ri / Tj⌉ × Cj
```

**Best for:** Periodic tasks with fixed priorities; simple implementation

### Deadline Monotonic (DM)

Like RM but priority based on relative deadline (not period).

**When deadline < period:** DM outperforms RM.

### Multiprocessor Real-Time

```
Partitioned: Assign tasks to specific CPUs, then use uniprocessor EDF/RM
Global: Single ready queue, tasks migrate between CPUs
Semi-partitioned: Mostly fixed, some tasks migrate

Partitioned schedulability: Bin-packing (First Fit, Best Fit) + EDF/RM
```

---

## 8. Cloud & Container Scheduling

### Kubernetes Scheduler

```yaml
# Scheduling pipeline
1. Predicates (filter): nodeSelector, affinity, taints/tolerations, resources
2. Priorities (score): LeastRequested, BalancedResourceAllocation, InterPodAffinity
3. Bind: Assign pod to selected node
```

**Extending:**
- Scheduler framework plugins (Filter, Score, Reserve, Permit, PreBind, PostBind)
- Custom schedulers (schedulerName in pod spec)

### Borg (Google)

```
Cell: cluster of machines
Job: collection of tasks with same binary
Task: single running instance

Scheduling:
1. Feasibility checking (resources, constraints)
2. Scoring (minimize preemptions, spread across failure domains)
3. Optimistic concurrency control

Features:
- All-or-nothing scheduling (gang scheduling for MPI)
- Resource estimation (fine-grained CPU/memory)
- Preemption with priority classes
```

### YARN (Hadoop)

```
ResourceManager: Global scheduler
NodeManager: Per-node agent
ApplicationMaster: Per-application scheduler

Scheduling policies:
- FIFO
- Capacity Scheduler (queues with guaranteed capacity)
- Fair Scheduler (max-min fairness across pools)
```

### Apache Mesos

Two-level scheduling:
```
1. Resource offers: Mesos master offers resources to frameworks
2. Framework acceptance: Framework accepts/rejects offers

Benefits: Multiple frameworks (Hadoop, Spark, MPI) share cluster
Trade-off: Frameworks may reject many offers (allocation delay)
```

---

## 9. Workflow & DAG Scheduling

### Critical Path Method (CPM)

```
1. Forward pass: compute earliest start/finish times
2. Backward pass: compute latest start/finish times
3. Slack = LS - ES (or LF - EF)
4. Critical path: tasks with zero slack
```

**Best for:** Static project scheduling; identifies bottlenecks

### List Scheduling

```
1. Compute priorities (e.g., upward rank, critical path)
2. Maintain ready list (tasks whose predecessors are done)
3. While ready list not empty:
   - Select highest priority ready task
   - Assign to processor minimizing finish time
   - Update ready list
```

**HEFT** is a specific list scheduling algorithm.

### Data Placement Strategies

```
Co-location: Place task near its data (data locality)
Replication: Replicate hot data across nodes
Staging: Pre-fetch data before task starts

Metrics:
- Data transfer time = data_size / bandwidth
- Makespan = max(finish_time) across all tasks
```

---

## 10. Energy-Aware Scheduling

### DVFS (Dynamic Voltage and Frequency Scaling)

```
Power ∝ V² × f   (voltage squared × frequency)
Energy = Power × Time

Trade-off: Lower frequency → lower power but longer execution
Optimal: Find frequency that minimizes energy while meeting deadline
```

### Energy-Efficient HEFT (E-HEFT)

```
Extension of HEFT with energy constraint:
1. Compute EFT at minimum frequency (lowest energy)
2. If deadline violated, increase frequency of critical path tasks
3. Iteratively adjust until deadline met with minimal energy
```

### Thermal-Aware Scheduling

```
Avoid hot spots by distributing tasks to balance temperature:
- Temperature prediction via thermal model
- Migrate tasks from hot to cool processors
- Co-schedule cool + hot tasks to average out
```

---

## 11. Performance Metrics

| Metric | Formula | Goal |
|--------|---------|------|
| **Makespan** | max(Ci) where Ci = completion time of task i | Minimize |
| **Flow Time** | Σ(Ci - ri) where ri = release time | Minimize |
| **Weighted Flow Time** | Σ(wi × (Ci - ri)) | Minimize |
| **Tardiness** | Σ max(0, Ci - di) where di = deadline | Minimize |
| **Lateness** | Σ(Ci - di) | Minimize |
| **Load Balance** | std(machine_utilization) | Minimize |
| **Speedup** | Tsequential / Tparallel | Maximize |
| **Efficiency** | Speedup / m (processors) | Maximize (≤1) |
| **Energy** | Σ(Poweri × runtime_i) | Minimize |
| **SLA Violations** | Count of missed deadlines / total | Minimize |

---

## 12. Algorithm Comparison

| Algorithm | Type | Complexity | Best For | Limitation |
|-----------|------|------------|----------|------------|
| FCFS | OS | O(1) | Simple systems | Convoy effect |
| SJF/SRTF | OS | O(n log n) | Min avg waiting | Starvation, prediction needed |
| Round Robin | OS | O(1) | Time-sharing | Quantum tuning |
| MLFQ | OS | O(1) | Mixed workloads | Parameter tuning |
| HEFT | Heuristic | O(n²m) | Heterogeneous DAGs | Static, needs estimates |
| Min-Min | Heuristic | O(n²m) | Homogeneous load balance | Favors short jobs |
| Max-Min | Heuristic | O(n²m) | Reducing makespan | Poor load balance |
| GA | Metaheuristic | O(G·N·n) | Complex search spaces | Slow, parameter tuning |
| PSO | Metaheuristic | O(I·N·n) | Continuous spaces | Premature convergence |
| VNS | Metaheuristic | O(I·k·LS) | Local refinement | Depends on neighborhoods |
| ACO | Metaheuristic | O(I·A·n) | Combinatorial | Slow convergence |
| SA | Metaheuristic | O(I·T) | Escaping local optima | Cooling schedule tuning |
| EDF | Real-time | O(log n) | Dynamic priorities | Priority inversion |
| RM/RMS | Real-time | O(1) | Fixed priorities | Utilization bound ~69% |
| RL (DQN/PPO) | ML | Training | Dynamic environments | Needs training data |
| GNN | ML | Training | Complex DAGs | High compute for training |

---

## 13. Python Implementation Examples

### Round Robin Scheduler

```python
from collections import deque
from dataclasses import dataclass

@dataclass
class Process:
    pid: str
    burst_time: int
    arrival_time: int = 0

def round_robin(processes: list[Process], quantum: int) -> dict:
    """Round Robin scheduling with metrics."""
    queue = deque(sorted(processes, key=lambda p: p.arrival_time))
    time = 0
    completion_times = {}
    waiting_times = {}
    turnaround_times = {}
    remaining = {p.pid: p.burst_time for p in processes}

    while queue:
        current = queue.popleft()
        if remaining[current.pid] <= quantum:
            time += remaining[current.pid]
            remaining[current.pid] = 0
            completion_times[current.pid] = time
            turnaround_times[current.pid] = time - current.arrival_time
            waiting_times[current.pid] = turnaround_times[current.pid] - current.burst_time
        else:
            time += quantum
            remaining[current.pid] -= quantum
            # Re-queue (in real OS, check for new arrivals)
            queue.append(current)

    avg_waiting = sum(waiting_times.values()) / len(waiting_times)
    avg_turnaround = sum(turnaround_times.values()) / len(turnaround_times)

    return {
        "completion_times": completion_times,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
    }

# Usage
processes = [
    Process("P1", 24, 0),
    Process("P2", 3, 0),
    Process("P3", 3, 0),
]
result = round_robin(processes, quantum=4)
print(f"Avg waiting: {result['avg_waiting']:.2f}")
```

### HEFT Scheduler (Simplified)

```python
from dataclasses import dataclass, field
from typing import Optional
import math

@dataclass
class Task:
    id: str
    exec_times: dict[str, float]  # machine_id -> time
    predecessors: list[str] = field(default_factory=list)
    successors: list[str] = field(default_factory=list)

@dataclass
class Machine:
    id: str
    avail_time: float = 0.0

@dataclass
class DAG:
    tasks: dict[str, Task]
    machines: list[Machine]

    def upward_rank(self, task_id: str, memo: dict) -> float:
        if task_id in memo:
            return memo[task_id]
        task = self.tasks[task_id]
        avg_exec = sum(task.exec_times.values()) / len(task.exec_times)
        if not task.successors:
            rank = avg_exec
        else:
            max_succ = max(
                self.upward_rank(sid, memo) + avg_exec  # simplified comm cost
                for sid in task.successors
            )
            rank = avg_exec + max_succ
        memo[task_id] = rank
        return rank

def heft(dag: DAG) -> dict[str, str]:
    """HEFT scheduling. Returns task -> machine mapping."""
    # Compute upward ranks
    memo = {}
    ranks = {tid: dag.upward_rank(tid, memo) for tid in dag.tasks}
    sorted_tasks = sorted(dag.tasks, key=lambda t: ranks[t], reverse=True)

    schedule = {}  # task_id -> machine_id
    task_finish = {}  # task_id -> finish_time

    for task_id in sorted_tasks:
        task = dag.tasks[task_id]
        best_machine = None
        best_finish = math.inf

        for machine in dag.machines:
            # Earliest start time considering predecessors
            est = machine.avail_time
            for pred_id in task.predecessors:
                pred_finish = task_finish[pred_id]
                # Simplified: assume communication cost is 0 if same machine
                # In full HEFT, add communication cost here
                est = max(est, pred_finish)

            eft = est + task.exec_times[machine.id]
            if eft < best_finish:
                best_finish = eft
                best_machine = machine

        schedule[task_id] = best_machine.id
        task_finish[task_id] = best_finish
        best_machine.avail_time = best_finish

    return schedule

# Usage
dag = DAG(
    tasks={
        "T1": Task("T1", {"M1": 4, "M2": 5}, successors=["T2", "T3"]),
        "T2": Task("T2", {"M1": 3, "M2": 2}, predecessors=["T1"]),
        "T3": Task("T3", {"M1": 2, "M2": 3}, predecessors=["T1"]),
    },
    machines=[Machine("M1"), Machine("M2")],
)
schedule = heft(dag)
print(schedule)  # {'T1': 'M1', 'T2': 'M2', 'T3': 'M1'}
```

---

## 14. Research Directions

- **Multi-objective optimization:** Makespan + energy + cost simultaneously (NSGA-II, MOEA/D)
- **Online/dynamic scheduling:** Tasks arrive during execution; no prior knowledge
- **Serverless scheduling:** Cold start optimization, function chaining, resource right-sizing
- **Edge computing:** Latency-aware scheduling with constrained resources
- **Quantum-inspired scheduling:** Quantum annealing, QAOA for combinatorial optimization
- **Federated scheduling:** Privacy-preserving distributed scheduling decisions
- **Carbon-aware scheduling:** Schedule compute during low-carbon intensity periods

---

## 15. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| DAG scheduling | `python-development` | Implementation in Python |
| RL scheduling | `federated-learning-dqn` | DQN, PPO training |
| Cloud scheduling | `kubernetes-orchestration` | K8s scheduler internals |
| Energy optimization | `evolutionary-architecture` | Fitness functions for energy |
| Experiment design | `research-design` | Benchmark methodology |
| Results presentation | `paper-writing` | Scheduling paper structure |

---

## References

- [Scheduling Theory Handbook](https://www.scheduling-handbook.com/)
- Topalouglu et al. — "GA-VNS for Parallel Machine Scheduling"
- Buttazzo, G.C. — *Hard Real-Time Computing Systems* (EDF, RM)
- Verma et al. — "Large-scale cluster management at Google with Borg"
- Vavilapalli et al. — "Apache Hadoop YARN: Yet Another Resource Negotiator"
- Mao et al. — "Resource Management with Deep Reinforcement Learning"
- Mirhoseini et al. — "A Graph Placement Methodology for Fast Chip Design" (GNN scheduling)
