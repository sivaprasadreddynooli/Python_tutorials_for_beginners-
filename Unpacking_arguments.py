def health_calculator(age,apples,cigs_day):
    answer = (100-age) + (apples * 3) - (cigs_day * 2)
    print(answer)



health_calculator(27,10,2)
#we can also send the data as list
data1 = [12,5,0]
health_calculator(data1[0],data1[1],data1[2])



#below, we send the list name as the parameter to the function
data = [35,12,5]
#append "*" to the list name and send it as a parameter to the function
health_calculator(*data)

