def solve_puzzle(Board, Source, Destination):
    #initialize memoization matrix of same size as board to all 0s
    memo = []
    for i in range(len(Board)):
        memo.append([])
        for j in range(len(Board[i])):
            memo[i].append(0)

    #initialize start tile to 1
    memo[Source[0]][Source[1]] = 1

    k = 1
    while memo[Destination[0]][Destination[1]] == 0:
        #expand memoization until end is found
        dead_end = True
        for i in range(len(memo)):
            for j in range(len(memo[i])):
                if memo[i][j] == k:
                    #up
                    if i > 0 and memo[i-1][j] == 0 and Board[i-1][j] == '-':
                        memo[i-1][j] = k+1
                        dead_end = False
                    #right
                    if j < len(memo[i])-1 and memo[i][j+1] == 0 and Board[i][j+1] == '-':
                        memo[i][j+1] = k+1
                        dead_end = False
                    #down
                    if i < len(memo)-1 and memo[i+1][j] == 0 and Board[i+1][j] == '-':
                        memo[i+1][j] = k+1
                        dead_end = False
                    #left
                    if j > 0 and memo[i][j-1] == 0 and Board[i][j-1] == '-':
                        memo[i][j-1] = k+1
                        dead_end = False
        k += 1
        #break loop if destination is unreachable
        if dead_end == True:
            break

    #Backtrack from destination to find path
    if memo[Destination[0]][Destination[1]] == 0:
        return None
    else:
        directions = ""
        i = Destination[0]
        j = Destination[1]
        path = [(i, j)]
        k = memo[i][j]
        while k > 1:
            #up
            if i > 0 and memo[i-1][j] == k-1:
                i = i-1
                path.insert(0, (i, j))
                directions = "D" + directions
                k -= 1
            #right
            elif j < len(memo[i])-1 and memo[i][j+1] == k-1:
                j = j+1
                path.insert(0, (i, j))
                directions = "L" + directions
                k -= 1
            #down
            elif i < len(memo)-1 and memo[i+1][j] == k-1:
                i = i+1
                path.insert(0, (i, j))
                directions = "U" + directions
                k -= 1
            #left
            elif j > 0 and memo[i][j-1] == k-1:
                j = j-1
                path.insert(0, (i, j))
                directions = "R" + directions
                k -= 1
            else:
                print("error with backtracking for path")
                break
        output = (path, directions)
    return output

Puzzle = [
 ['-', '-', '-', '-', '-'],
 ['-', '-', '#', '-', '-'],
 ['-', '-', '-', '-', '-'],
 ['#', '-', '#', '#', '-'],
 ['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0,2), (2,2)))

print(solve_puzzle(Puzzle, (0,0), (4,4)))

print(solve_puzzle(Puzzle, (0,0), (4,0)))