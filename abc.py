TESTCASES = 5
ALPHABET = {"A", "B", "C"}
LOCATION = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2], 4 : [1, 0], 5 : [1, 1], 6 : [1, 2], 7 : [2, 0], 8 : [2, 1], 9 : [2, 2]} # a dictionary of the indexes of each number
pieces = [["", "", ""], ["", "", ""], ["", "", ""]] # a 2d list of all of the puzzle pieces

def filled(): # returns whether the board is filled
    for i in pieces:
        if (i.count("") > 0):
            return False
    return True

def findRow(n): # row num
    return pieces[n]

def findCol(n): # col num
    return [pieces[i][n] for i in range(len(pieces))]

def uniqueAnswer(row, col): # returns the possible answer/s
    r = findRow(row)
    c = findCol(col)
    given = set(r + c)
    unique = ALPHABET - given
    return unique

def printPieces():
    print(pieces[0][0] + pieces[0][1] + pieces[0][2] + pieces[1][0] + pieces[1][1] + pieces[1][2] + pieces[2][0] + pieces[2][1] + pieces[2][2])


def solve():
    info = list(input().split(", ")) # all of the given information
    for i in range(1, int(info[0]) * 2 + 1, 2): # puts all of the information into the pieces
        alphab = info[i + 1]
        loc = int(info[i])
        pieces[LOCATION[loc][0]][LOCATION[loc][1]] = alphab
    while (not filled()):
        for row in range(len(pieces)):
            for col in range(len(pieces[0])):
                u = uniqueAnswer(row, col)
                if (len(u) == 1):
                    pieces[row][col] = list(u)[0]
    printPieces()
                

for i in range(TESTCASES):
    solve()
    pieces = [["", "", ""], ["", "", ""], ["", "", ""]]

'''
SAMPLE INPUT
3, 1, A, 3, C, 8, A
3, 1, A, 6, C, 8, B
3, 1, B, 6, B, 9, C
2, 1, C, 5, B
2, 3, B, 7, A

OUTPUT
ABCBCACAB
ACBBACCBA
BCACABABC
CABABCBCA
CABBCAABC
'''
