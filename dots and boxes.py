##state_mat=[0 for x in range(5)]
##for k in range(5):
##    l=[int(i) for i in input().split()]
##    state_mat[k]=l

state_mat=[[0 for x in range(5)] for x in range(5)]

#player_id = int(input())

rounds=10

while rounds:
    rounds-=1
    sparse_box=False
    brim_box=False
    sx=sy=bx=by=int()

    def count_edges(n):
        k=4
        bits=[]
        while k:
            k-=1
            bits.insert(0,int(n%2))
            n=n/2
        counter=0
        for i in bits:
            if(i==1):
                counter+=1
        return counter

    def get_edge(n):
        k=4
        bits=[]
        while k:
            k-=1
            bits.insert(0,int(n%2))
            n=n/2
        for i in range(4):
            if(bits[i]==0):
                return i

    def update( a , b ,e):
        k=4
        bits=[]
        n=state_mat[a][b]
        while k:
            k-=1
            bits.insert(0,int(n%2))
            n=n/2
        bits[e]=1
        temp=8
        sum_=0
        for i in range(4):
            bits[i]=temp*bits[i]
            sum_+=bits[i]
            temp=temp/2
        state_mat[a][b]=sum_
            


    for i in range(5):
        for j in range(5):
            edges=count_edges(state_mat[i][j])
            if(edges==3):
                brim_box=True
                bx,by=i,j
            elif(edges<3):
                sparse_box=True
                sx,sy=i,j

    if(brim_box):
        e=get_edge(state_mat[bx][by])
        #print("changing ",bx,by,e)
        print(bx,by,e)
        #print(state_mat[bx][by])
        update(bx,by,e)
        #print("updated state is ",state_mat[bx][by])
        
    if(sparse_box):
        e=get_edge(state_mat[sx][sy])
        #print("changing ",sx,sy,e)
        print(sx,sy,e)
        #print(state_mat[sx][sy])
        update(sx,sy,e)
        #print("updated state is ",state_mat[sx][sy])

            
