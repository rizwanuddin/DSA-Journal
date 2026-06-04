# Print a name N times using recursion

class Solution:
    def print_name(self, name, count, N):
        if count == N:#base case
            return
        print(name)
        self.print_name(name, count + 1, N)
if __name__=="__main__":
    sol = Solution()
    N = 5
    name = "Rizzu"
    sol.print_name(name, 0, N)            
## Now the static recirsive function way to do it

class Solution:
    @staticmethod
    def print_name(name, count, N): 
        # we dont need self here as we are not using any
        # instance variable, instance variable is the variable
        #  which is specific to an object, here we are not using
        #  any object specific variable, so we can make it static method. 
        # eg count and N are not specific to any object, they are just parameters which are passed to the function, 
        # so we can make it static method.
        if count == N:
            return
        print(name)
        Solution.print_name(name, count + 1, N) #we need to call the function using class name as it is static method
if __name__=="__main__":
    N = 5
    name = "Rizzu"
    Solution.print_name(name, 0, N) #we need to call the function using class name as it is static method        
    

