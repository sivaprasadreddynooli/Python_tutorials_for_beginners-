#the function "open" will help a file either to create or open a already present file
#the second parameter 'w' will help in creating the file if not present , will open to append the text if already present
#  and 'r' will help in reading the file
#you can name anything to the file like fw,fr
fw = open('sample.txt','w')
fw.write('i am siva reddy nooli\n')
fw.write('i am from kadapa , veluma\n')
fw.close()

fr = open('sample.txt','r')
data = fr.read()
print(data)
fr.close()
