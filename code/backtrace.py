n =       #  n元
x = [0]*n # 初始化一个解
X = []    # 一组解

def conflict(k):
  global 
  
  if 冲突：
      return True
  else: return False

#子集树  
def function(k):
  global
  
  if k>=n: #成功结束，判断条件由具体情况而定
      print(x)
      # X.append(x) 保存多组解
  else:
      for i in range(m): # m个状态
          x[k] = i
          if not conflict(k): #剪枝
              function(k+1) #递归实现回溯
              
#排列树
def function(k):
  global
  
  if k>=n: #大多数是超出最后的元素
      print(x)
      # X.append(x) 保存多组解
  else:
      for i in range(m): # m个状态
          x[k],x[i] =  x[i],x[k]
          if not conflict(k): #剪枝
              function(k+1) #递归实现回溯
          x[i], x[k] = x[k], x[i] # 回溯
