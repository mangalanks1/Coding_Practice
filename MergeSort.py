
def merge(A,B):
  # Merge ascending sorted lists A and B into C
  n1 = len(A)
  n2 = len(B)
  C=[]
  
  i, j = (0,0)
  while i< n1 and j < n2:
    if A[i] <= B[j]:
      C.append(A[i])
      i = i+1
    elif A[i] > B[j]:
      C.append(B[j])
      j=j+1
  if i == n1-1: 
    C.append(B[j::])
  else: 
    C.append(A[i::]]
  return(C)
                 
def mergesort(x):
  n = len(x)
  mid = int(n/2)
  if n==0 or n==1: return x
  else:
    a = mergesort(x[0:mid])
    b = mergesort(x[mid::])
    C = merge(a,b)
    return C

if name == '__main__':
  x = [1,4,7,4,9,22,66,88,6,66,100]
  print("Jumbled Array is", x)
  print(mergesort(x))
  
             
