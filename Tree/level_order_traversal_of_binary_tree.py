# Using two queues
def level_order_traversal(root):
  if root == None:
    return

  queues = [deque(), deque()]

  current_queue = queues[0]
  next_queue = queues[1]
  
  current_queue.append(root)
  level_number = 0

  # 🔑
  while current_queue:
    temp = current_queue.popleft()
    print(str(temp.data) , end = " ")

    if temp.left != None:
      next_queue.append(temp.left)

    if temp.right != None:
      next_queue.append(temp.right)

    if not current_queue:
      print()
      level_number += 1
      current_queue = queues[level_number % 2] 
      next_queue = queues[(level_number + 1) % 2]
  print()
  
arr = [100,50,200,25,75,350]
root = create_BST(arr)
print("\nLevel Order Traversal:\n", end = "")
level_order_traversal(root)
