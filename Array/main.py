def pair_sum_exist(array,target):
  array.sort()
  low = 0
  high = len(array)-1
  while low<=high:
    if(array[low]+array[high] == target):
      return True
    elif(array[low]+array[high]>target):
      high = high - 1
    else:
      low = low + 1
  return False
  # Time complexity O(nlogn)

def index_of_two_sum(array,target):
  ans = []
  aux = []
  for i in range(len(array)):
    aux.append(array[i]-target)
  print(aux)
  print(array)
  for i in range(len(array)):
    for j in range(i+1,len(array)):
      if(array[i]+array[j] == target):
        ans.append(i)
        ans.append(j)
        break;
  return ans
