numbers = [2,3,45,8,56,5,6,5,2,0,2,1,6,2,3]

## This is my first code on python
# Based on Selection Sort

for i in range(len(numbers)):
    temp = i    
    for j in range(i+1,len(numbers)) :
        if(numbers[j]<numbers[temp]) :
            temp = j 
    numbers[i],numbers[temp] = numbers[temp],numbers[i]      

print(numbers)


