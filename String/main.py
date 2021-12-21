def is_palindrome(string):
  rev_string = string[::-1]
  if(string == rev_string):
    return True
  else:
    False

def sub_string(string):
  count = 0
  for i in range(len(string)):
    for j in range(i,len(string)):
      if is_palindrome(string[i:j+1]):
        count = count + 1
  print(count)

