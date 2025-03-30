def mochila_gulosa(values, weights, w):
    n = len(values)

    r = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    r.sort(reverse=True)
    
    total_value = 0
    current_weight = 0 

    for ratio, value, weight in r:
        if current_weight + weight <= w:
            total_value += value
            current_weight += weight
        else:
            fraction = (w - current_weight) / weight
            total_value += value * fraction
            break
    
    return total_value

values = [2, 3, 5, 4]
weights = [40, 50, 100, 90]
w = 8
print("Valor máximo: ", mochila_gulosa(values, weights, w))