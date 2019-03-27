# 非递归遍历

# 前序遍历
def preOrder(root):
	'''
	根左右，先将根值加入result，不断往stack压入左节点直到左节点为空
	弹出最后一个左节点，若其右节点不为空，则将指针指向其右节点，往stack压入右节点，访问其左节点
	'''
	result = []
	stack = []
	cur = root
	while cur or stack:
		while cur != None:
			result.append(cur.val)
			stack.append(cur)
			cur = cur.left
		elem = stack.pop()
		if elem.right != None:
			cur = elem.right
	return result

# 中序遍历
def inOrder(root):
	'''
	左根右，先将根节点压入stack，然后不断访问左节点，往stack压入左节点直到左节点为空
	弹出最后一个左节点，若其右节点不为空，则将指针指向其右节点，往stack压入右节点，不断访问其左节点
	'''
	result = []
	stack = []
	cur = root
	while cur or stack:
		while cur != None:
			stack.append(cur)
			cur = cur.left
		elem = stack.pop()
		result.append(elem.val)
		if elem.right != None:
			cur = elem.right
	return result

# 后序遍历
def postOrder(root):
	'''
	左右根，将其它当成是根右左的反转
	'''
	result = []
	stack = []
	cur = root
	while cur or stack:
		while cur != None:
			result.append(cur.val)
			stack.append(cur)
			cur = cur.right
		elem = stack.pop()		
		if elem.left != None:
			cur = elem.left
	return result[::-1]

# 层次遍历，队列
def levelOrder(root):
	result=[]
	queue = [root]
	while queue :
		cur = queue[0]
		queue = queue[1:]
		result.append(cur.val)
		if cur.left != None:
			queue.append(cur.left)
		if cur.right != None:
			queue.append(cur.right)
	return result
