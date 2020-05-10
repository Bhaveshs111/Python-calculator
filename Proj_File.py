def myfile(text):
    f=open("project.txt",'a+')
    f.write(text)
    f.write('\n')
    f.close()

