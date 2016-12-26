#here is the way , how to unpack the lists
#here the number of variables should be equal to the number of items in the list
data,item,price = ['December 25th','milk',8.98]
print(item)


def drop_first_last(grades):
    #the below statement will take and first elements aside and will assign remaining elements to the *middle
    #from which we can access the remaining elements
    first,*middle,last = grades
    avg = sum(middle)/len(middle)
    print(avg)


drop_first_last([65,78,95,34,89])
drop_first_last([12,12,23,45,67,86,34,54,98,29])