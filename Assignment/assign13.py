# *Assignment (07/03/2026)* 
# *Assignment Name* : KNN in Real Life 
# *Description* : Explain Netflix-like recommendations using KNN and create a small similarity example.

# KNN works by finding users with similar preferences.
# For example, if two users watch similar movies, 
# KNN recommends movies liked by one user to the other based on similarity distance.

from sklearn.neighbors import NearestNeighbors
import numpy as np

users = np.array([
    [5, 4, 0, 1],
    [4, 5, 1, 0],
    [0, 1, 5, 4],
    [1, 0, 4, 5]
])

model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(users)

target_user = np.array([[5, 5, 0, 0]])
distances, indices = model.kneighbors(target_user)

print("Nearest Users Index:", indices)
print("Distances:", distances)