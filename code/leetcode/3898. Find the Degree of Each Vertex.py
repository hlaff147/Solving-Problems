def findDegrees(matrix):
    # matrix =
    # [
    # [0,1,1]
    # [1,0,1]
    # [1,1,0]
    # ]
    result = []
    for i in range(len(matrix)):
        print(matrix[i])
        loopCountConnection = 0
        for j in range(len(matrix[i])):
            print(matrix[i][j])
            if matrix[i][j] == 1:
                loopCountConnection += 1
        result.append(loopCountConnection)
        loopCountConnection = 0
    return result


matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print(findDegrees(matrix))
