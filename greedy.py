def greedy_knapsack(p, w, m):
    assert len(p) == len(w), "p and w differ"

    n = len(p)
    items = list(range(n))
    #Sort the items in descending order of their profit/weight ratio
    items.sort(key=lambda i: p[i] / w[i], reverse=True)

    total_weight = 0
    max_profit = 0

    for i in items:
        if total_weight + w[i] <= m:
            total_weight += w[i]
            max_profit += p[i]
        else:
            remaining_weight = m - total_weight
            fraction = remaining_weight / w[i]
            max_profit += p[i] * fraction
            break
    return int(max_profit)

p = [60, 100, 120]
w = [10, 20, 30]
m = 50

print("Max Profit is",greedy_knapsack(p, w, m))