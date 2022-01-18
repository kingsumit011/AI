# Program 2: Write a program to solve the 8-Puzzle problem using DFID (Depth First Iterative Deepening) Strategy.
import copy
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]


class Data:
    '''data class store 2D matrix mat of size n*n
        emptyPos(value 0) coordinate , lastMove'''
    def __init__(self , mat, emptyPos , lastMove):  
        self.mat = mat
        self.emptyPos = emptyPos
        self.lastMove = lastMove
        self.next = []

    def __eq__(self, other):
        return (self.mat == other.mat ) if (isinstance(other,Data)) else False
    def test(self ):
        return self.mat == final.mat

    def genrateNew(self):
        '''4 move in each direction and store in next'''
        for i in range(4):
            x= self.emptyPos[0] + row[i]
            y = self.emptyPos[1] + col[i]
            if(
                (0<=x<n)
                and (0<=y<n)
                and i!=self.lastMove
            ):
                bpX =self.emptyPos[0]
                bpY = self.emptyPos[1]
                child = copy.deepcopy(self)
                self.mat[bpX][bpY], child.mat[x][y] = child.mat[x][y], self.mat[bpX][bpY]
                child.emptyPos = [x,y]
                child.lastMove = i-2 if i > 1 else i+2
                self.next.append(child)


def solve(temp):
    global depth
    depth = -1
    while True:
        depth += 1
        result = DBDFS(temp, depth)
        if(result) : 
            print(f" SOLUTION FOUND \n AT DEPTH BOUND {depth} \n")
            break
        else:
            print(f" SOLUTION NOT FOUND \n CURRENT DEPTH BOUND {depth} \n")
            

def DBDFS( start, N):
    if(N <0 ): return False
    if(start.test()): return True
    start.genrateNew()
    return any((DBDFS(i , N-1)) for i in start.next)


def inputMatrix():
    mat = []
    for x in range(n):
        a = []
        for y in range(n):
            a.append(int(input(f"Tell The element at position {x} , {y} ")))
            if(a[-1]==0): emptyPos = [x,y]
        mat.append(a)
    return Data(mat , emptyPos , -1)

if __name__ == '__main__' :
    global n , final , temp
    n = int(input("Enter the value of "))
    print("Enter the element of intial matrix: ")
    temp = inputMatrix()
    print("Enter the element of intial matrix: ")
    final = inputMatrix()
    solve(temp)
