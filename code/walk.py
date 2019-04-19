maze = [[1,1,1,1,1,1,1,1,1,1],
        [0,0,1,0,1,1,1,1,0,1],
        [1,1,0,1,0,1,1,0,1,1],
        [1,0,1,1,1,0,0,1,1,1],
        [1,1,1,0,0,1,1,0,1,1],
        [1,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,0,1,1,1,1,0],
        [1,1,1,1,1,0,1,1,1,1]]

m,n = 8,10
entry = (1,0)
path = [entry]
paths = []
step = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def conflict(nx,ny):
    global m,n,maze
    if 0<=nx<m and 0<=ny<n and maze[nx][ny]==0:
        return False
    return True

def walk(x,y): #输入一个状态
    global m,n,entry,path,paths,maze,step

    if (x,y)!=entry and (x%(m-1)==0 or y%(n-1)==0):
        paths.append(path[:])
    else:
        for i,j in step:
            nx,ny = x+i,y+j
            path.append((nx,ny))            
            if not conflict(nx,ny):
                maze[nx][ny] = 2
                walk(nx,ny)
                maze[nx][ny] = 0
            path.pop()

def show(path):
    global maze
    
    import pprint, copy
    
    maze2 = copy.deepcopy(maze)
    
    for p in path:
        maze2[p[0]][p[1]] = 2 # 通路
        
    pprint.pprint(maze)  # 原迷宫
    print()
    pprint.pprint(maze2) # 带通路的迷宫


# 测试
walk(1,0)
print(paths[-1], '\n') # 看看最后一条路径
show(paths[-1])
