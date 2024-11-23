NF = float('inf')  # Infinity
def floyd_warshall(cost_matrix): 
    num_cities = len(cost_matrix) 
    dist = [[cost_matrix[i][j] for j in range(num_cities)] for i in range(num_cities)] 
    for k in range(num_cities): 
        for i in range(num_cities): 
            for j in range(num_cities): 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
    return dist 

num_cities = int(input("Enter the number of cities: ")) 
cost_matrix = [] 
print(f"Enter the cost matrix ({num_cities} x {num_cities}) row by row (use 'INF' for no direct path):") 
for i in range(num_cities): 
    row = input(f"Row {i+1}: ").split() 
    row = [NF if x == 'INF' else int(x) for x in row]  # Replace INF with float('inf')
    cost_matrix.append(row) 

shortest_paths = floyd_warshall(cost_matrix) 

print("\nShortest paths between all pairs of cities:")
for row in shortest_paths: 
    print(row)
