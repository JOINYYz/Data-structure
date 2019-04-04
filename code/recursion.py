# 1、阶乘
def f(n):
  if n==1:
    return 1
  return f(n-1)*n

# 2、猴子吃桃
'''
一只小猴子第一天摘下若干个桃子，并吃了一半。感觉到吃的还不瘾，于是又多吃了一个；
第二天早上，又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上,都吃了前一天剩下的一半零一个。
到了第10天早上想再吃时，却发现只剩下一个桃子了。
请问第一天共摘了多少？
'''
def f(n):
  if n==10:
    return 1
  return (f(n+1)+1)*2

print(f(1))

# 3、将一个数逆序放入列表中 如：1234----[4,3,2,1]
l = '1234'
length = len(l)
li = []
def f(length):
  if length == 0:
    return li
  li.append(l[length-1])
  return f(length-1)
  
print (f(length))

# 4、
