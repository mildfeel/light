import turtle as t
a=2
b=-1
c=-1
M=[a,b,c]
N=[]
t.register_shape("100.gif")#登记 画笔变成狼
t1=t.Turtle()
t1.shape("100.gif")
t1.up()
t1.goto(-200,200)

t.register_shape("100.gif")#登记 画笔变成羊
t2=t.Turtle()
t2.shape("100.gif")
t2.up()
t2.goto(-200,0)

t.register_shape("100.gif")#登记 画笔变成菜
t3=t.Turtle()
t3.shape("100.gif")
t3.up()
t3.goto(-200,-100)


def move(x,y,list1,list2,j,k):
    print(f'将{y}从{j}移到{k}')
    i=list1.index(x)
    list1.pop(i)
    list2.append(x)
    
for i in range(4):
    m=sum(M)
    
    if  m==0 or  m==2 :
        move(a,"羊",M,N,"河1","河2")
        t2.pd()
        t2.goto(200,0)
        

    elif m==-2 :
        move(b,"狼",M,N,"河1","河2")
        t1.pd()
        t1.goto(200,200)
    else:
        move(c,"菜",M,N,"河1","河2")
        t3.pd()
        t3.goto(200,-100)
    n=sum(N)
    if  n==1 :
        move(a,"羊",N,M,"河2","河1")
        t2.pd()
        t2.goto(-200,0)


t.done()
