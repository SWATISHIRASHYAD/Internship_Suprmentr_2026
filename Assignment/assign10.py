
# *Assignment (03/03/2026)*

# *Assignment Name* : Build Your First Dataset
# *Description* : Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

study_hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
marks = np.array([35, 40, 50, 60, 70, 80])

df = pd.DataFrame({
    "StudyHours": study_hours.flatten(),
    "Marks": marks
})

print(df)

model = LinearRegression()
model.fit(study_hours, marks)

prediction = model.predict([[7]])
print("Predicted Marks for 7 hours study:", prediction[0])