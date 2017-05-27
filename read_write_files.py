
fw = open('sample.txt','w')
fw.write('i am siva prasad reddy\n')
fw.write('i am from kadapa , vempalli')
fw.close()

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
