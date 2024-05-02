# Name:Shahmir Alam

def myDynamicProgramming(n, c, V, W):
    '''
    Implement Knapsack Dynamic Programming function under here.
    Input:
    n: Number of items - int
    c: Capacity of the Knapsack - int
    V: List of Values of each item - list[int]
    W: List of Weights of each item - list[int]
    return:
    Z: Optimal choice of items for the given constraints - list[int]
    DP: Dynamic Programming table generated while calculation - list[list[int]]
    '''
    # Initialize DP matrix with zeros
    DP = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    # Initialize Z array to track the chosen items
    Z = [0] * n

    for i in range(1, n + 1):
        for w in range(1, c + 1):
            if W[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - W[i - 1]] + V[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]

    # Backtrack to find the optimal choice of items
    i, w = n, c
    while i > 0 and w > 0:
        if DP[i][w] != DP[i - 1][w]:
            Z[i - 1] = 1
            w -= W[i - 1]
        i -= 1

    return Z, DP

# Example usage
n = 3
V = [5, 8, 12]
W = [4, 5, 10]
c = 11

Z, DP = myDynamicProgramming(n, c, V, W)
for row in DP:
    print(row)
print("Z =", Z)





