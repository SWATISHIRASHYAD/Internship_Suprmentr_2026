# *Assignment (18/03/2026)*

# *Assignment Name* : Customer Segmentation
# *Description* : Perform K-Means clustering on a mall dataset and describe customer groups.

import pandas as pd
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "Income": [15, 16, 17, 60, 62, 64, 120, 122, 125],
    "Score": [39, 40, 41, 70, 72, 75, 20, 22, 25]
})

model = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = model.fit_predict(df)

print(df)