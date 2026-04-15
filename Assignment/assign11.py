# *Assignment (09/03/2026)*

# *Assignment Name* : House Price Predictor
# *Description* : Train a Linear Regression model, predict prices, and test with new input.


import numpy as np
from sklearn.linear_model import LinearRegression

area = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)
price = np.array([1000000, 1500000, 2000000, 2400000, 3000000])

model = LinearRegression()
model.fit(area, price)

prediction = model.predict([[1300]])
print("Predicted Price:", prediction[0])