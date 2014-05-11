# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

    checked=[]
    frontier=[[0,init[0],init[1]]]
    while(True):
        
        checked.extend([f[1:] for f in frontier])
        newFrontier=frontier
        frontier=[]
        print "round\n"
        for f in newFrontier:
            currentCost=f[0]
            for move in delta:
                # Check the move is valid
                newYpos=f[1]+move[0]
                newXpos=f[2]+move[1]
                newPos=[newYpos,newXpos]

                InBoundaryY= (newYpos>=0) and (newYpos<=len(grid)-1)
                InBoundaryX= (newXpos>=0) and (newXpos<=len(grid[0])-1)
                if not (InBoundaryY and InBoundaryX): continue
                if (not newPos in checked) and (not newPos in [i[1:] for i in frontier]) and (not newPos in [j[1:] for j in newFrontier])and grid[newYpos][newXpos]==0:
                    newCostPos=[currentCost+cost, newYpos, newXpos]
                    if newPos==goal:
                        return newCostPos
                    else:
                        print newCostPos
                        frontier.append(newCostPos)
        if frontier==[]: return 'fail'

print search()