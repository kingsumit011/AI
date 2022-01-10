import random
import copy

n = 3
 
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]


initial = [ [ 1, 2, 3 ],
            [ 8,7,4 ],
            [ 0, 6,5 ] ]

f = [ [ 1, 2, 3 ],
     [ 8, 0, 4 ],
     [ 7, 6, 5 ] ]
          
open = []
closed = []
numStep = 0

class Data:
    '''data class store 2D matrix mat of size n*n
        emptyPos(value 0) coordinate , lastMove'''
    def __init__(self , mat, emptyPos , lastMove):  
        self.mat = mat
        self.emptyPos = emptyPos
        self.lastMove = lastMove
    
    def __eq__(self, other):
        if(isinstance(other,Data)):
            return (self.mat == other.mat ) 
        return False

def moveGenration(cur):
    '''4 move in each direction and check is it possible'''
    for i in range(4):
        if (
            (0 <= cur.emptyPos[0] + row[i] < n)
            and (0 <= cur.emptyPos[1] + col[i] < n)
            and i != cur.lastMove
        ):
            child = genrateNew(cur , i)
            if child not in closed: 
                open.append(child)
                if test(child) : return True
    return False

def genrateNew(curr ,i):
    '''genrate new object od data class'''
    bpX = curr.emptyPos[0]
    bpY = curr.emptyPos[1]

    child = copy.deepcopy(curr)

    x= curr.emptyPos[0] + row[i]
    y = curr.emptyPos[1] + col[i]

    child.mat[bpX][bpY], child.mat[x][y] = child.mat[x][y], child.mat[bpX][bpY]
    child.emptyPos = [x,y]
    child.lastMove = i-2 if i > 1 else i+2
    return child
def test(child):
    global numStep
    print(F'current  : {child.mat}')
    numStep += 1
    return child == final


def solve():
    while(open):
        index = random.randint(0,len(open)-1)
        if(moveGenration(open[index])) : 
            # print( "output : " + closed[-1] )
            print( "Solution Found \n  No OF Steps Taken : " + str(numStep))
            return
        else : 
            print( " No OF Steps Taken : " +str(numStep) )
            closed.append(open.pop(index))
    print("Solution not Fount \n No of steps taken " + str(numStep))

final = Data(f,0,0)
open = [Data(initial ,[1,1],-1)]
solve()

# def inputMatrix():
#     mat = []
#     for x in range(n):
#         a = []
#         for y in range(n):
#             a.append(int(input(f"Tell The element at position {x} , {y} ")))
#             if(a[-1]==0): emptyPos = [x,y]
#         mat.append(a)
#     return Data(mat , emptyPos , -1)
# if __name__ == '__main__' :
#     global final
#     n = int(input("Enter the value of "))
#     print("Enter the element of intial matrix: ")
#     open.append(inputMatrix())
#     print("Enter the element of intial matrix: ")
#     final = inputMatrix()
#     solve()
