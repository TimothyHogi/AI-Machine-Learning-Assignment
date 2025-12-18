import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Load the dataset from the data folder
file_path = 'data/GCB2022v27_MtCO2_flat.csv'
df = pd.read_csv(file_path)

# 2. Filter for 'Global' data to see the world trend
global_emissions = df[df['Country'] == 'Global'].copy()

# 3. Prepare Features (X) and Target (y)
# We use 'Year' to predict 'Total' emissions
X = global_emissions[['Year']]
y = global_emissions['Total']

# 4. Split data into Training and Testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and Train the Model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Evaluate
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {error:.2f} MtCO2")

# 7. Visualization for your Report
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='green', label='Actual Emissions', alpha=0.5)
plt.plot(X, model.predict(X), color='red', linewidth=2, label='ML Forecast Trend')
plt.title('SDG 13: Global CO2 Emissions Forecast')
plt.xlabel('Year')
plt.ylabel('MtCO2')
plt.legend()
plt.grid(True)
plt.savefig('emissions_trend.png') # This saves a screenshot for your GitHub!
plt.show()