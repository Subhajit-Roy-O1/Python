def printJobSequencing(arr1,t):
    n=len(arr1)
    for i in range(n):
        for j in range(n-1-i):
            if(arr1[j][2]<arr1[j+1][2]):
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                
                result = [False]*t
                
                job = ['-1']*t
                
                for i in range(len(arr1)):
                    for j in range(min(t-1,arr1[i][1]-1),-1,-1):
                        if(result[j] is False):
                            result[j] = True
                            job[j] = arr1[i][0]
                            break
                        
    return job


     
 
    

arr_1=[[1,4,20],
       [2,1,10],
       [3,1,40],
       [4,1,30]]
lol=arr_1
job=printJobSequencing(arr_1,4)

li=[]
for i in job:
    if(int(i)>0):
        li.append(i)
t=0
for i in li:
    t+=lol[i-1][2]

print(len(li),t) 