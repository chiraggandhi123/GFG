#code

def get_number(arr,n,s):

    sum=0
    flag=0
    start=0
    for i in range(n):
        sum=sum+arr[i]
        
        while(sum>s):
            sum=sum-arr[start]
            start=start+1
        
        if(sum==s):
            flag=1
            print(start+1,end=' ')
            print(i+1)
            break
    
    if flag==0:
        print(-1)
    

t=int(input())
while(t):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    get_number(arr,n,s)
    #print(out[0],out[1])
    #print(type(get_number(arr,n,s)))
    t=t-1
    
    #solvable in O (n+m)