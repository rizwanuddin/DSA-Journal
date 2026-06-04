##difference between them is that in
# parameterized recursion,
# we are passing the intermediate result (multi) 
# as a parameter to the recursive function, whereas in functional recursion,
# we are returning the intermediate result from the recursive function and using it in the next call. 
# In parameterized recursion, we are using an extra variable (multi) to store the intermediate result,
# whereas in functional recursion, we are not using any extra variable to store the intermediate result.
# and parameterized recursion prints inside the function and functional recursion returns the result and we print it outside the function.
# also parameterized is less reusable as it is specific to the problem, whereas functional recursion is more reusable as it can be used for other problems as well.
## Parameterized Recursion
class FactorialFinder:
    def factorial(self, N, current, multi):
        if current > N :
            print(multi)
            return
        multi *= current
        self.factorial(N, current+1, multi)

if __name__== "__main__":
    N = 5
    sol = FactorialFinder()
    sol.factorial(N, 1, 1)

## Now the Functional Recursion way to do it
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
if __name__== "__main__":
    N = 5
    print(factorial(N)) 
