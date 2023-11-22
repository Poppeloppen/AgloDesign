import numpy as np
from sys import stdin


def knapsack_1_0_recursive(weights: list[int], vals: list[int], capacity: int, n: int) -> int:
    """Recursive algorithm to find the maximum value that can be packed obtained by packing
    'n' items with values and weights specified by 'vals' and 'weights' into a knapsack of size
    'capacity'
    """
    #Base case
    if n == 0 or capacity == 0:
        return 0

    #If adding item will exceed capacity of bag, do not pack it
    elif weights[n-1] > capacity:
        return knapsack_1_0_recursive(weights=weights, vals=vals, capacity=capacity, n=(n-1))
        
    else:
        exclude = knapsack_1_0_recursive(weights=weights, vals=vals, capacity=capacity, n=(n-1))
        include = vals[n-1] + knapsack_1_0_recursive(weights=weights, vals=vals, capacity=capacity-weights[n-1], n=(n-1))

        return max(exclude, include)



def knapsack_1_0_iterative(weights: list[int], vals: list[int], capacity: int, n: int) -> tuple[int, list[list[int]]]:
    """Iterative dynamic programming algorithm using memoization to find the maximum value that can be obtained by packing
    'n' items with values and weights specified by 'vals' and 'weights' into a knapsack of size 'capacity'. 
    """
    #Memoization array (size: (n+1)x(W+1) --> +1 due to base case)
    M = [[-1] * (capacity+1) for _ in range(n+1)]

    #initialize first row and column as 0 --> base case
    #Cannot get any value when there is NO ITEMS
    for w in range(capacity+1):
        M[0][w] = 0
    
    #Cannot get any value when there is NO CAPACITY
    for i in range(n+1):
        M[i][0] = 0
    
    for i in range(1, n+1): #Skipping base cases
        for w in range(1, capacity+1): 
            
            #Base case (NOTE: this is redundant since base case is already taken care of)
            #if i == 0 or w == 0:
            #    M[i][w] = 0
    
            #If adding item will exceed capacity of bag, do not pack it
            if weights[i-1] > w:
                M[i][w] = M[i-1][w]
                
            else:
                include_item = vals[i-1] + M[i-1][w-weights[i-1]]
                exclude_item = M[i-1][w]
                M[i][w] = max(include_item,exclude_item)


    return M[n][capacity], M



def knapsack_optimal_packing_from_M(M: list[list[int]], weights: list[int], vals: list[int], capacity: int, n: int) -> list[int]:
    """Returns the indecies of the items that yields the optimal value when packing a knapsack
    (note: the indicies are based on 0-indexing, so might be neccesary to add 1)
    """
    optimal_value =  M[n][capacity]    

    current_capacity = capacity
    optimal_included_items = []
    for i in range(n, 0, -1):

        if optimal_value <= 0:
            break
        
        #If you can get the maximum value without packing the current item i 
        # (but by packing the previous item i-1) -> do not pack i
        if optimal_value == M[i - 1][current_capacity]:
            continue

        else:
            #Pack the prior item
            included_item = i-1 
            optimal_included_items.append(included_item)

            optimal_value -= vals[i-1]
            current_capacity -= weights[i-1]

    return optimal_included_items





def main():

    C, n = map(int, stdin.readline().split())

    all_weights = []
    all_values = []
    for i in range(n):
        value_i, weight_i = map(int, stdin.readline().split())
        all_values.append(value_i)
        all_weights.append(weight_i)
    

    res, M = knapsack_1_0_iterative(weights=all_weights, vals=all_values, capacity=C, n=n)
    res2 = knapsack_1_0_recursive(weights=all_weights, vals=all_values, capacity=C, n=n)
    print(res)
    print(res)

    optimal_packing = knapsack_optimal_packing_from_M(M=M, weights=all_weights, vals=all_values, capacity=C, n=n)
    print(*optimal_packing)

    return




if __name__ == "__main__":
    main()