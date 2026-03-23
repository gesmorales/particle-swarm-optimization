# Particle Swarm Optimization

## Description
Particle Swarm Optimization (PSO) is a population-based metaheuristic algorithm inspired by the collective behavior of social organisms such as bird flocks and fish schools. It was first introduced by James Kennedy and Russell Eberhart in 1995 and has since become a widely used technique for solving complex optimization problems.

PSO operates by initializing a group of candidate solutions, called particles, within a search space. Each particle has a position and velocity and evaluates its performance using a predefined fitness function. During the optimization process, each particle keeps track of its personal best position (pBest) and is also influenced by the best solution found by the entire swarm (gBest). The particles iteratively update their velocities and positions based on these two factors, enabling them to explore and exploit the search space efficiently (Abualigah, 2025).

One of the main strengths of PSO is its simplicity and ease of implementation, as it requires only a few parameters compared to other optimization algorithms. It is also computationally efficient and demonstrates fast convergence in many applications. However, PSO may suffer from premature convergence and can become trapped in local optima, particularly in complex or high-dimensional problems (Sharma et al., 2026).

Recent studies have focused on improving PSO through hybridization with other algorithms, adaptive parameter tuning, and multi-swarm strategies. These enhancements aim to improve solution diversity and avoid stagnation. As a result, PSO continues to be applied in various domains, including machine learning, engineering design, healthcare, and energy systems (Casas-Ordaz et al., 2026).

## Traveling Salesman Problem (Particle Swarm Optimization Example 1)

### Overview
tsp.py - this project implements Particle Swarm Optimization (PSO) to solve the Traveling Salesman Problem (TSP). The goal of TSP is to find the shortest possible route that visits a set of cities exactly once and returns to the starting point.

PSO is a population-based optimization algorithm inspired by swarm intelligence. In this implementation, each particle represents a candidate solution (a route), and the algorithm iteratively improves these solutions by learning from both individual and collective experiences.

### How It Works
* Each particle is a permutation of cities (a possible route).
* The fitness function calculates the total distance of the route.
* Each particle tracks:
  * Personal Best (pBest) – best route it has found
  * Global Best (gBest) – best route found by the swarm
* Instead of traditional velocity, swap operations are used to update routes.
* The swarm iteratively improves solutions to minimize total distance.

### Features
* Random city generation
* Distance-based fitness evaluation
* PSO adapted for permutation problems
* Route visualization using Matplotlib

### Output
* Best route (sequence of cities)
* Minimum distance found
* Visualization of the optimized route

## SVM Hyperparameter Tuning (Particle Swarm Optimization Example 2)

### Overview
svm.py - this project implements Particle Swarm Optimization (PSO) to automatically tune the hyperparameters of a Support Vector Machine (SVM) model. The goal is to improve classification performance by finding optimal values for key parameters.

Traditional methods such as grid search can be computationally expensive. In contrast, PSO provides a more efficient, population-based search strategy inspired by swarm intelligence.

### Problem Statement
Selecting optimal hyperparameters for SVM, particularly:
- C (Regularization Parameter)
- Gamma (Kernel Coefficient)

is crucial for achieving high model accuracy. This project uses PSO to search for the best combination of these parameters.

### How It Works
- Each particle represents a candidate solution: [C, gamma]
- The fitness function evaluates model accuracy
- Each particle updates based on:
- Personal Best (pBest)
- Global Best (gBest)
- The swarm iteratively improves to maximize classification accuracy

### Dataset
This implementation uses the Breast Cancer dataset from scikit-learn, a widely used benchmark dataset for binary classification.

### Features
- PSO-based hyperparameter tuning
- Automatic optimization of SVM parameters
- Simple and efficient implementation
- Easily extendable to other datasets

## Summary
PSO is a powerful and flexible optimization technique that leverages collective intelligence to efficiently search for optimal solutions in complex problem spaces.

## References
Abualigah, L. (2025). Particle Swarm Optimization: Advances, Applications, and Experimental Insights. Computers, Materials & Continua, 82(2), 1539–1592. https://doi.org/10.32604/cmc.2025.060765

Casas-Ordaz, A., Haro, E. H., Beltran, L. A., Alvarez, O., Mousavirad, S. J., Pérez-Cisneros, M., & Oliva, D. (2026). Particle swarm optimization: A survey of innovations over the last 10 years. Computer Science Review, 60, 100910. https://doi.org/10.1016/j.cosrev.2026.100910

Sharma, R., Matharu, J. S., & Parmar, K. S. (2026). A survey on Particle Swarm Optimization: Evolution, adaptations and practical implementations. Applied Soft Computing, 186, 114016. https://doi.org/10.1016/j.asoc.2025.114016
