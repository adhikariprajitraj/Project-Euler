sum1=0
sum2 = 0
for i in range (1,101):
    sum1 = sum1+ i**2
    sum2 = sum2+i

final_sum = sum2 ** 2
diff = final_sum - sum1
print(diff)

