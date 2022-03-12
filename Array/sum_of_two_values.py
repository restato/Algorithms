# https://www.educative.io/m/sum-of-two-values
def find_sum_of_two(A, val):
  found_values = set()
  for a in A:
    if val - a in found_values: # 🔑
      return True
    found_values.add(a) # 🔑 check visited
  return False

v = [5, 7, 1, 2, 8, 4, 3]
test = [3, 20, 1, 2, 7]

for i in range(len(test)):
  output = find_sum_of_two(v, test[i])
  print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))
