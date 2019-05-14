import random
arr=[]
for i in range(1,100):
    arr.append(random.randint(100,1000))
for n in arr:
    print(n)
len = len(arr)
print("The length of array is" , len)
sum=sum(arr)
avg=sum/len
print("The average of array is" , avg)
max=max(arr)
print("The maximum value in list is ", max)
min=min(arr)
print("The minimum value in list is ", min)
