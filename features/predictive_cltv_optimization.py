
# predictive_cltv_optimization.py
# TARIRO Studio: Predictive Customer Lifetime Value (CLTV) Optimization

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

class CLTVOptimizer:
    def __init__(self, customer_data):
        self.customer_data = customer_data
        self.cltv_model = self._train_cltv_model()

    def _train_cltv_model(self):
        """
        Trains a predictive model to estimate Customer Lifetime Value (CLTV).
        This is a simplified example; real-world CLTV models are more complex.
        """
        print("Training CLTV prediction model...")

        # Example: Assuming customer_data has 'Recency', 'Frequency', 'Monetary', 'CLTV_Actual' columns
        # In a real scenario, features would be engineered and CLTV_Actual would be calculated over time
        if not isinstance(self.customer_data, pd.DataFrame):
            # Create a dummy DataFrame for demonstration if none is provided
            data = {
                'Recency': np.random.randint(1, 365, 100),
                'Frequency': np.random.randint(1, 20, 100),
                'Monetary': np.random.rand(100) * 1000 + 50,
                'CLTV_Actual': np.random.rand(100) * 5000 + 100
            }
            self.customer_data = pd.DataFrame(data)

        X = self.customer_data[['Recency', 'Frequency', 'Monetary']]
        y = self.customer_data['CLTV_Actual']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        print(f"CLTV Model trained. Mean Absolute Error: {mae:.2f}")
        return model

    def predict_cltv(self, new_customer_features):
        """
        Predicts CLTV for new or existing customers based on their features.
        """
        if not isinstance(new_customer_features, pd.DataFrame):
            new_customer_features = pd.DataFrame([new_customer_features])

        predicted_cltv = self.cltv_model.predict(new_customer_features)
        print(f"Predicted CLTV: {predicted_cltv[0]:.2f}")
        return predicted_cltv[0]

    def optimize_marketing_strategy(self, customer_segments, budget_allocation):
        """
        Optimizes marketing strategies based on predicted CLTV for different customer segments.
        """
        print("Optimizing marketing strategy based on CLTV...")
        optimized_allocations = {}
        for segment, features in customer_segments.items():
            predicted_cltv = self.predict_cltv(features)
            # Simple rule: allocate more budget to higher CLTV segments
            allocation_factor = predicted_cltv / 1000 # Scaling factor
            optimized_allocations[segment] = budget_allocation * allocation_factor
        
        # Normalize allocations if needed (sum to 100%)
        total_allocated_factor = sum(optimized_allocations.values())
        if total_allocated_factor > 0:
            for segment in optimized_allocations:
                optimized_allocations[segment] = (optimized_allocations[segment] / total_allocated_factor) * budget_allocation
        
        print(f"Optimized Marketing Allocations: {optimized_allocations}")
        return optimized_allocations

# Example usage:
if __name__ == "__main__":
    # Example customer data (replace with real data for actual use)
    example_customer_data = pd.DataFrame({
        'Recency': [10, 50, 120, 30, 200, 15, 70, 90, 180, 25],
        'Frequency': [5, 2, 1, 8, 1, 10, 3, 4, 2, 7],
        'Monetary': [500, 200, 100, 800, 50, 1200, 300, 450, 150, 900],
        'CLTV_Actual': [2500, 800, 300, 4000, 150, 6000, 1500, 2200, 600, 4500]
    })

    cltv_optimizer = CLTVOptimizer(customer_data=example_customer_data)

    # Predict CLTV for a new customer
    new_customer = {'Recency': 20, 'Frequency': 6, 'Monetary': 750}
    new_customer_df = pd.DataFrame([new_customer])
    predicted_cltv = cltv_optimizer.predict_cltv(new_customer_df)
    print(f"\nPredicted CLTV for new customer: {predicted_cltv:.2f}")

    # Optimize marketing strategy for segments
    customer_segments_example = {
        "High_Value_Loyal": pd.DataFrame([{'Recency': 10, 'Frequency': 15, 'Monetary': 1500}]),
        "New_Potential": pd.DataFrame([{'Recency': 5, 'Frequency': 1, 'Monetary': 50}]),
        "Churn_Risk": pd.DataFrame([{'Recency': 180, 'Frequency': 2, 'Monetary': 100}]),
    }
    total_marketing_budget = 100000.0 # Example budget

    optimized_allocations = cltv_optimizer.optimize_marketing_strategy(
        customer_segments_example,
        total_marketing_budget
    )
    print("
Optimized Marketing Budget Allocations:")
    for segment, allocation in optimized_allocations.items():
        print(f"{segment}: ${allocation:.2f}")
