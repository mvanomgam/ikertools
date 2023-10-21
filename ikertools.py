# iterators are data types that can be used in afor loop.
# 1. Product - This is a Mathematical Cartesian Product 
#       1       2       3
# 1   (1,1)   (1,2)   (1,3)
# 2   (2,1)   (2,2)   (2,3)
# 3   (3,1)   (3,2)   (3,3)

from itertools import product

a = [1, 2, 3]
b = [1, 2, 3]

prod = product(a, b)
print(f"\n{list(prod)}")

a = [1, 2, 3]
b = [1, 2, 3]

prod = product(a, b, repeat=2)
print(f"\n{list(prod)}")

# 2. Permutations - Number of ways a given list can be ordered.

from itertools import permutations

a = [1, 2, 3]

perm = permutations(a)
print(f"\n{list(perm)}")

a = [1, 2, 3]

perm = permutations(a, 2)
print(f"\n{list(perm)}")

# 3. Combinations - umber of ways a given list can be ordered with no repetitions. 

from itertools import combinations

a = [1, 2, 3, 4]

comb = combinations(a, 2)
print(f"\n{list(comb)}")

a = [1, 2, 3, 4]

comb = combinations(a, 3)
print(f"\n{list(comb)}")

from itertools import combinations_with_replacement

a = [1, 2, 3, 4]

comb_wr = combinations_with_replacement(a, 2)
print(f"\n{list(comb_wr)}")

a = [1, 2, 3, 4]

comb_wr = combinations_with_replacement(a, 3)
print(f"\n{list(comb_wr)}")

# 4. Accumulator 

from itertools import accumulate

a = [1, 2, 3, 4]

acc = accumulate(a)
print(f"\n{a}")
print(f"\n{list(acc)}")

import operator

a = [1, 2, 3, 4]

acc = accumulate(a, func=operator.mul)
print(f"\n{a}")
print(f"\n{list(acc)}")

a = [1, 2, 5, 3, 4]

acc = accumulate(a, func=max)
print(f"\n{a}")
print(f"\n{list(acc)}")

# 5. Groupby

from itertools import groupby

def less_than_3(x):
  return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=less_than_3)

for key, value in group_obj:
  print(' ')
  print(key, list(value))

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x<3)

for key, value in group_obj:
  print(' ')
  print(key, list(value))

persons = [{"name": "cecilia", "age": 20},
           {"name": "sanele", "age": 20},
           {"name": "mvano", "age": 25},
           {"name": "luvo", "age": 30}]

group_obj = groupby(persons, key=lambda x: x['age'])

for key, value in group_obj:
  print(' ')
  print(key, list(value))
  
# 6. Infinite iterators 

from itertools import count, cycle, repeat

# infinite loop that starts at n and add 1
print(' ')
for i in count(10):
  print(i)
  # breaking the loop
  if i == 15:
    break

# print the same thing for an infinite number of times  
a = [1, 2, 3]

print(' ')
for i in cycle(a):
  print(i)
  # breaking the loop
  if i == 3:
    break

# repeat something called x and stop after n repetitions
a = [1, 2, 3]

print(' ')
for i in repeat(1, 10):
  print(i)
  
