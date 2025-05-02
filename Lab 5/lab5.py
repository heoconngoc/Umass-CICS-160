def search(lst:list, e:int):
  if not lst:
    return False
  if lst[0] == e:
    return True
  else:
    return search(lst[1:], e)

print(search([1,2,3,4,5,4],0))
print(search([1,2,3,4,5,4],5))

def count(lst:list, e:int): 
  res = 0
  if not lst:
    return 0
  if len(lst)==1:
    if lst[0]==e:
      return 1
    else:
      return 0
  else: 
    mid = len(lst)//2
  return count(lst[:mid],e) + count(lst[mid:],e)

print(count([1,1,2,2,0,1],1))