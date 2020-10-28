f = open('D:\\file.text','w')
for i in range(1,1001):
    if i%2==0:
        f.write(i)
        f.close()
