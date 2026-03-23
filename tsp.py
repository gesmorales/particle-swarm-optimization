import numpy as np
import random
import matplotlib.pyplot as plt

# -----------------------------
# Generate random cities
# -----------------------------
def generate_cities(n):
    return np.random.rand(n, 2) * 100

# -----------------------------
# Distance calculation
# -----------------------------
def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        city1 = cities[route[i]]
        city2 = cities[route[(i + 1) % len(route)]]
        dist += np.linalg.norm(city1 - city2)
    return dist

# -----------------------------
# Particle class
# -----------------------------
class Particle:
    def __init__(self, num_cities):
        self.position = list(range(num_cities))
        random.shuffle(self.position)
        self.best_position = list(self.position)
        self.best_distance = float('inf')

    def evaluate(self, cities):
        dist = total_distance(self.position, cities)
        if dist < self.best_distance:
            self.best_distance = dist
            self.best_position = list(self.position)

# -----------------------------
# Swap operator (for permutation)
# -----------------------------
def swap_sequence(p1, p2):
    swaps = []
    temp = list(p1)
    for i in range(len(p1)):
        if temp[i] != p2[i]:
            swap_idx = temp.index(p2[i])
            swaps.append((i, swap_idx))
            temp[i], temp[swap_idx] = temp[swap_idx], temp[i]
    return swaps

def apply_swaps(position, swaps, prob):
    new_pos = list(position)
    for (i, j) in swaps:
        if random.random() < prob:
            new_pos[i], new_pos[j] = new_pos[j], new_pos[i]
    return new_pos

# -----------------------------
# PSO algorithm
# -----------------------------
def pso_tsp(cities, num_particles=30, iterations=200, w=0.5, c1=1, c2=2):
    num_cities = len(cities)
    swarm = [Particle(num_cities) for _ in range(num_particles)]

    gbest_position = None
    gbest_distance = float('inf')

    for _ in range(iterations):
        for particle in swarm:
            particle.evaluate(cities)

            if particle.best_distance < gbest_distance:
                gbest_distance = particle.best_distance
                gbest_position = list(particle.best_position)

        for particle in swarm:
            swaps_pbest = swap_sequence(particle.position, particle.best_position)
            swaps_gbest = swap_sequence(particle.position, gbest_position)

            new_position = apply_swaps(particle.position, swaps_pbest, c1)
            new_position = apply_swaps(new_position, swaps_gbest, c2)

            particle.position = new_position

    return gbest_position, gbest_distance

# -----------------------------
# Visualization
# -----------------------------
def plot_route(cities, route):
    ordered = cities[route]
    ordered = np.vstack([ordered, ordered[0]])  # return to start

    plt.figure()
    plt.scatter(cities[:, 0], cities[:, 1])
    plt.plot(ordered[:, 0], ordered[:, 1])
    plt.title("Best Route Found by PSO")
    plt.show()

# -----------------------------
# Run Example
# -----------------------------
if __name__ == "__main__":
    cities = generate_cities(20)
    best_route, best_distance = pso_tsp(cities)

    print("Best Distance:", best_distance)
    print("Best Route:", best_route)

    plot_route(cities, best_route)
