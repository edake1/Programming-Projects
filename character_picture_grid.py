grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(grid[0][0], grid[1][0], grid[2][0], grid[3][0],grid[4][0],grid[5][0],grid[6][0],grid[7][0],grid[8][0])

for item in range(len(grid[0])):
        print()
        for suck in range(len(grid)):
                print(grid[suck][item], end='')


# newString = ''
# newString1 = '\n'
# newString2 = '\n'
# newString3 = '\n'
# newString4 = '\n'
# newString5 = '\n'
# for i in range(len(grid)):
#     newString += str(grid[i][0])
#
#     newString1 += str(grid[i][1])
#
#     newString2 += str(grid[i][2])
#
#     newString3 += str(grid[i][3])
#
#     newString4 += str(grid[i][4])
#
#     newString5 += str(grid[i][5])
#
# print(newString + newString1 + newString2 + newString3 + newString4 + newString5)


# print('\n'.join(map(''.join, zip(*grid))))


# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         print(grid[i][j],end='')
#     print('')


# def final(grid_solve, count):
#     empty = ""
#     for i in grid_solve:
#         empty += i[count]
#
#     return empty
#
#
# total = 0
#
# while total != len(grid[0]):
#     print(final(grid, total))
#     total += 1


# for x in range (0,6):
#     for y in range (0,9):
#         print (grid[y][x], end='')
#     print ('')
#
#
# b=len(grid)
# for y in range(b-3):
#     print('\n')
#     for x in range(b):
#         print(grid[x][y], end=' ')


# def printer(grid):
#     for m in range(len(grid[0])):
#         print()
#         for n in range(len(grid)):
#             print (grid[n][m],end="")
#             n+=1
#         m +=1
#
