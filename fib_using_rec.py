print(0)
print(1)
count=2
def fibbrec(prev1,prev2):
    global count
    if(count<19):
        new_fib=prev1+prev2
        prev1=prev2
        prev2=new_fib
        print(new_fib)
        count+=1
        fibbrec(prev1,prev2)
    else:
        return 0
fibbrec(1,0)