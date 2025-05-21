prev1=0
prev2=1
for fibb in range(18):
    new_fib=prev1+prev2
    prev1=prev2
    prev2=new_fib
    print(new_fib)