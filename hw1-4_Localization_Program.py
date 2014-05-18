colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
x=len(colors[0])
y=len(colors)

p=[[0.05 for j in range(x) ] for i in range(y)]
world=[colors[i][j] for i in range(y) for j in range(x)]
#print world

def sense(p, Z):
    q=[]
    p=[p[i][j] for i in range(y) for j in range(x)]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    q=[ q[i*x:i*x+x] for i in range(y)]
    return q

def move(p, U):
    q = []
    for i in range(y):
        for j in range(x):
            s = (1-p_move) * p[i][j]
            s = s + p_move * p[(i-U[0]) % y][(j-U[1]) % x]
            q.append(s)
    q=[ q[i*x:i*x+x] for i in range(y)]
    return q

for i in range(len(motions)):
    p=move(p,motions[i])
    p=sense(p,measurements[i])
    


#Your probability array must be printed 
#with the following code.

show(p)




