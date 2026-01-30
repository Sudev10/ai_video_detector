import numpy as np

edge_strengths = [
    1.37, 1.42, 5.52, 5.58, 5.55, 5.60, 5.61, 5.65,
    4.54, 4.86, 4.52, 5.73, 1.51, 6.75, 8.02, 8.88,
    9.57, 9.88, 10.11, 10.08, 10.18, 10.29, 10.36,
    1.71, 10.53, 10.52, 10.62, 10.91, 11.17, 11.43,
    11.42, 11.42, 11.40, 2.07, 2.69, 3.54, 4.38,
    5.01, 5.35
]

mean = np.mean(edge_strengths)
std = np.std(edge_strengths)
cv = std / mean

print("Mean:", mean)
print("Std deviation:", std)
print("Consistency score (CV):", cv)
