def is_array_sorted(A):
  # Base Case
  if len(A) == 1:
      return True
  # Cursive Case
  else:
      return A[0] <= A[1] and is_array_sorted(A[1:])

A = [121, 122, 143, 174, 187, 124]
B = [12, 122, 123, 154, 1000, 1002]

print(is_array_sorted(A))
print(is_array_sorted(B))
