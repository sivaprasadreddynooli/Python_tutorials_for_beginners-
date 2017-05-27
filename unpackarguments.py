def health_calculator(age, noofapples, cigars):
    answer = (100-age) + (noofapples * 3.5) - (cigars*2)
    print(answer)

siva_data = [23, 4, 2]
ravi_data = [30,3,7]
tej_data = ['siva',45,2,8,678]
#pass the arguments seperately
health_calculator(siva_data[0],siva_data[1],siva_data[2])
#pass the list directly
health_calculator(*ravi_data)
#pass the partial values from the list
health_calculator(*tej_data[1:4])

