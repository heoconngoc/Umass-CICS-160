def is_prime(num):
  for i in range (2, int(num**(1/2))+1):
    if num % i == 0:
      return False
  return True

def are_relatively_prime(num1, num2):
  return find_GCD(num1, num2) == 1
    
def find_GCD(num1, num2):
  if num2 == 0:
    return num1
  else:
    return find_GCD(num2, num1%num2)

def primes(num):
  lst = []
  for i in range (2,num+1):
    if is_prime(i):
      lst.append(i)
  return lst

def prime_decomposition(num):
  lst = []
  while num != 1:
    for i in range(2, num+1):
      if is_prime(i) and num % i == 0:
        lst.append(i)
        num = num // i
        break
  return lst

def has_prime_decomposition_of_size_2_and_factors_are_different(num):
  lst = prime_decomposition(num)
  if len(lst) != 2:
    return False
  if lst[0] == lst[1]:
    return False
  return True



