def create_matrix():
    size = int(input(""))
    if size < 2:
        return None
    

    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = input(f"")
            if (value == "f"):
                value = float("inf")
            else:
                value = int(value)
            row.append(value)
        matrix.append(row)


    return matrix

def bell_algorithm(matrix, startingVertex):

    distanceMatrix = [float("inf")] * len(matrix)
    distanceMatrix[startingVertex] = 0


    for _ in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #print(f"{i} -> {j} = {matrix[i][j]}
                if distanceMatrix[j] > distanceMatrix[i] + matrix[i][j]:
                    distanceMatrix[j] = distanceMatrix[i] + matrix[i][j]


    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != float("inf") and distanceMatrix[i] != float("inf") and distanceMatrix[j] != None and distanceMatrix[i] != None:
                if distanceMatrix[j] > distanceMatrix[i] + matrix[i][j]:
                    distanceMatrix = [None] * len(matrix)
                    print(f"Node {startingVertex}: {distanceMatrix}")
                    return
                    


    print(f"Node {startingVertex}: {distanceMatrix}")
    pass

#result_matrix = [
#    [0,-1],
#    [1,0]
#]


#result_matrix = [
#                [0, float("inf"), 3, float("inf")],
#                [2, 0, float("inf"),float("inf")],
#                [float("inf"), 7, 0, 1],
#                [6, float("inf"), float("inf"), 0]
#               ]

result_matrix = create_matrix()
for i in range (len(result_matrix)):
    bell_algorithm(result_matrix, i)

