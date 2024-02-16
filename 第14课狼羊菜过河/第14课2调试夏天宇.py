a=2
b=-1
c=-1
M=[a,b,c]
N=[]
#数据 用数字来判断前进
#---------
def move(x,y,list1,list2,j,k):
    print(f'将{y}从{j}移到{k}')
    i=list1.index(x)#直接搜索list1列表里的元素
    list1.pop(i)#弹出值
    list2.append(x)#不能用i
for i in range(4):
    m=sum(M)#求和
    
    if  m==0 or  m==2 :
        move(a,"羊",M,N,"河1","河2")

    elif m==-2 :
        move(b,"狼",M,N,"河1","河2")

    else:
        move(c,"菜",M,N,"河1","河2")

    n=sum(N)#求和判断
    if  n==1 :
        move(a,"羊",N,M,"河2","河1")
'''
ls.index(1)#直接查找ls里面的元素
sum()#求和  可以求列表和  可以加上numpy库进行数组相加
'''
        
        
       
