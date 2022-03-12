def find_missing(input):
  # calculate sum of all elements 
  # in input list
  sum_of_elements = sum(input)
  
  # There is exactly 1 number missing 
  n = len(input) + 1
  actual_sum = (n * ( n + 1 ) ) / 2 # 👏
  return actual_sum - sum_of_elements


def test(n):
  missing_element = random.randint(1, n)
  v = []
  for i in range(1, n):
    if i != missing_element:
      v.append(i)
