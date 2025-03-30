def greedy_fractional_knapsack(values, weights, W):
    n = len(values)
    
    # Calculate value/weight ratio for each item
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Sort items based on ratio in non-increasing order
    ratios.sort(reverse=True)
    
    total_value = 0  # Initialize total value
    current_weight = 0  # Initialize current weight
    
    # Loop through all items
    for ratio, value, weight in ratios:
        if current_weight + weight <= W:
            # Add entire item
            total_value += value
            current_weight += weight
        else:
            # Add fraction of item
            fraction = (W - current_weight) / weight
            total_value += value * fraction
            break
    
    return total_value


# Example Usage
values1 = [60, 100, 120]
weights1 = [10, 20, 30]
W1 = 50
print("Maximum value in knapsack (Greedy Approach) =", greedy_fractional_knapsack(values1, weights1, W1))  # Output: 240

values2 = [40, 100, 50, 60]
weights2 = [20, 10, 40, 30]
W2 = 50
print("Maximum value in knapsack (Greedy Approach) =", greedy_fractional_knapsack(values2, weights2, W2))  # Output: 210
