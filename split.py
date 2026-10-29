n=int(input())
arr=list(map(str, input().split()))
count=0
suffix=input()
for i in range(n):
    if(suffix in arr[i]):
        count+=1
print(count)
