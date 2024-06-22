def brute_func_knapsack(p, w, m):
    assert len(p) == len(w), "p and w differ"
    n = len(p)
    max_profit = 0
    total_weight = m
    soln = ''
    for i in range(2**n):
        s = bin(i)[2:].rjust(n, '0')
        profit = 0
        weight = 0
        for j in range(n):
            if s[j] == '1':
                profit += p[j]
                weight += w[j]
            elif s[j] == '0':
                pass
        # Calculate fractional weight for '0' elements in s
        if weight > total_weight:
            continue
        fraction = (total_weight - weight) / sum(w[j] for j in range(n) if s[j] == '0')
        profit += fraction * sum(p[j] for j in range(n) if s[j] == '0')
        weight += fraction * sum(w[j] for j in range(n) if s[j] == '0')
        
        if profit > max_profit:
            max_profit = profit
            soln = s
    return int(max_profit)

p = [60, 100, 120]
w = [10, 20, 30]
m = 50
print("Max Profit is",brute_func_knapsack(p, w, m))