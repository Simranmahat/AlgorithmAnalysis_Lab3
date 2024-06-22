def brute_01_knapsack(p, w, m):
    assert len(p) == len(w), "p and w differ"

    n = len(p)
    max_profit = 0
    total_weight = m
    soln = ''
    for i in range(2**n):
        s = bin(i)[2:].rjust(n, '0')
        profit = sum((int(s[j])) * p[j] for j in range(n))
        weight = sum((int(s[j])) * w[j] for j in range(n))
    
        if profit > max_profit and weight <= total_weight:
            max_profit = profit
            soln = s

    return max_profit

p = [60, 100, 120]
w = [10, 20, 30]
m = 50
print("Max Profit is",brute_01_knapsack(p, w, m))