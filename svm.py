import numpy as np
import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# -----------------------------
# Load dataset
# -----------------------------
data = datasets.load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Fitness function
# -----------------------------
def fitness_function(params):
    C, gamma = params

    # Avoid invalid values
    if C <= 0 or gamma <= 0:
        return 0

    model = SVC(C=C, gamma=gamma)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    return acc

# -----------------------------
# Particle class
# -----------------------------
class Particle:
    def __init__(self):
        self.position = np.array([
            random.uniform(0.1, 100),   # C
            random.uniform(0.0001, 1)   # gamma
        ])
        self.velocity = np.random.rand(2)
        self.best_position = self.position.copy()
        self.best_score = 0

    def evaluate(self):
        score = fitness_function(self.position)

        if score > self.best_score:
            self.best_score = score
            self.best_position = self.position.copy()

# -----------------------------
# PSO algorithm
# -----------------------------
def pso(num_particles=20, iterations=30, w=0.5, c1=1.5, c2=1.5):
    swarm = [Particle() for _ in range(num_particles)]

    gbest_position = None
    gbest_score = 0

    for _ in range(iterations):
        for particle in swarm:
            particle.evaluate()

            if particle.best_score > gbest_score:
                gbest_score = particle.best_score
                gbest_position = particle.best_position.copy()

        for particle in swarm:
            r1, r2 = np.random.rand(2)

            cognitive = c1 * r1 * (particle.best_position - particle.position)
            social = c2 * r2 * (gbest_position - particle.position)

            particle.velocity = w * particle.velocity + cognitive + social
            particle.position = particle.position + particle.velocity

    return gbest_position, gbest_score

# -----------------------------
# Run PSO
# -----------------------------
best_params, best_score = pso()

print("Best Accuracy:", best_score)
print("Best Parameters:")
print("C =", best_params[0])
print("Gamma =", best_params[1])
