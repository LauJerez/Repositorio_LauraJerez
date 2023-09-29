def lectura():
    f = open('wcm.csv','r',encoding="utf8")
    line = f.readline() 
    for i in line:
        a=i.rstrip('\n').split(',')
        print(a)

