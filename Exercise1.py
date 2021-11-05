a=int(input("Give me a number"))
odd_sum=0
sum_even=0
count=0
for i in range(1,a+1):
    if i%2==1:
        odd_sum+=i
    if i%2==0:
        sum_even+=i
        count+=1
print("Odd numbers sum:",odd_sum,"\nEven numbers avarage:",sum_even/count)
