def Khayyam_Pascal():
    n=int(input('n?'))
    list=[]
    for i in range(1,n+1):
        if i==1:
            list.append(1)
            print(list)
        if i==2:
            list.append(1)  
            print(list)
        if i>=3:
            list.insert(i-2,list[i-3]+list[i-2])
            j=3
            while i>3 and j<i: 
                list[i-j]=list[i-j]+list[i-j-1] 
                j=j+1
            print(list)                    
               
Khayyam_Pascal()
