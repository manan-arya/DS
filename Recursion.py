class Recursion:
    def fact(self,n):
        if n<=1:
            return 1
        return n*self.fact(n-1)

    def isSorted(self,arr):
        if len(arr)<=1:
            return True
        if arr[0] < arr[1]:
            return self.isSorted(arr[1:])
        else:
            return False


