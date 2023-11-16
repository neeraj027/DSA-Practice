total_days=int(input('Enter number of day(s):'))
temperature=[]
temp=0
total=0
for i in range(total_days):
    temp=int(input(f'Enter high temperature of day {i+1}:'))
    temperature.append(temp)
    total+=temp
print(temperature)
avg=total/total_days
print(avg)
count=0
for i in temperature:
    if i>avg:
        count+=1
print(f'Total day(s) higher than avg is/are {count}')