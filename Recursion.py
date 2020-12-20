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

    #backtracking starts
    def append_at_front(self,arr,bit):
        return [bit+ item for item in arr]
    def all_bit_strings(self,n):
        if n <= 0:
            return []
        if n == 1:
            return ["0","1"]
        else:
            return [self.all_bit_strings(self,n-1),self.all_bit_strings(self,n-1)+"0"]


