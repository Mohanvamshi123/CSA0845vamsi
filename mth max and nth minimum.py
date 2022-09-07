def getMin(arr, n):
 res = arr[0]
 for i in range(1, n):
   res = min(res,arr[i])
 return res
# Function to find maximum element
def getMax(arr, n):
 res = arr[0]
 for i in range(1, n):
 res = max(res, arr[i])
 return res
# Function to get Sum
def findSum(arr, n):
 min = getMin(arr, n)
 max = getMax(arr, n)
 return min + max
# Function to get product
def findProduct(arr, n):
 min = getMin(arr, n)
 max = getMax(arr, n)
 return min * max
# Driver Code
if _name_ == "_main_":

 arr = [ 12, 1234, 45, 67, 1 ]
 n = len(arr)
 # Sum of min and max element
 print("Sum = " , findSum(arr, n))
32
 # Product of min and max element
 print("Product = " , findProduct(arr, n))
