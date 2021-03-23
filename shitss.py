import math 
def queensAttack(n,r_q, c_q):
    #counting diagonal elements
    #counting for left
    new_n = math.floor(n/2)
    new_arr=[]
    # if n%2==0:
    if n-r_q<n-c_q:
            # this is for this diagnoal '/'
            # print('hi')
            # print('n-r_q',n-r_q)
            # print('n-c_q',n-c_q,n)
            val1 = n-r_q
            val2 = c_q-1
            vale1 = val1+val2
            # print(vale1,val1,val2,1)
            if vale1==0:
                # print('enterred ')
                i=r_q 
                j=c_q
                k=0
                while k<n:
                    if i==r_q and j==c_q:
                        i-=1
                        j+=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i-=1
                    j+=1
                    k+=1
            k=0
            i=r_q-val2
            j=1
            while k<=vale1:
                    if i==r_q and j==c_q:
                        i+=1
                        j+=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i+=1
                    j+=1
                    k+=1
               
    elif n-c_q<n-r_q:
            val1 = n-c_q
            val2=r_q-1
            vale1 = val1+val2
            # print(vale1,val1,val2,2)
            if vale1==0:
                # print('enterred ')
                i=r_q 
                j=c_q
                k=0
                while k<n:
                    if i==r_q and j==c_q:
                        i+=1
                        j-=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i+=1
                    j-=1
                    k+=1
            k=0
            i=1
            j=c_q-val2
            while k<=vale1:
                    if i==r_q and j==c_q:
                        i+=1
                        j+=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i+=1
                    j+=1
                    k+=1
            
            
    else:
            vale1=n-1
            # print(vale1)
            if c_q==n and r_q==n:
                k=0
                i=r_q
                j=c_q
                while k<=vale1:
                    if i==r_q and j==c_q:
                        i-=1
                        j-=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i-=1
                    j-=1
                    k+=1
            elif c_q==1 and r_q==1:
                k=0
                i=r_q
                j=c_q
                while k<=vale1:
                    if i==r_q and j==c_q:
                        i+=1
                        j+=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i+=1
                    j+=1
                    k+=1
            else:
                k=0
                i=1
                j=1
                while k<=vale1:
                    if i==r_q and j==c_q:
                        i+=1
                        j+=1
                        k+=1
                        continue
                    new_arr.append((i,j))
                    i+=1
                    j+=1
                    k+=1
                        
                    
                
                
        # this is for this diagnoal '\'
    if c_q==8 or c_q==1:
            vale2 = abs(c_q-r_q)
            
            print(vale2,'yyy')
            
            if c_q==1:
                k=0
                i=r_q-1
                j =2
                while k<vale2:
                    new_arr.append((i,j))
                    i-=1
                    j+=1
                    k+=1
            elif c_q==8:
                k=0
                i=r_q+1
                j=n-1
                while k<vale2:
                    new_arr.append((i,j))
                    i+=1
                    j-=1
                    k+=1
            
                
    elif r_q<=new_n:
            # print('hi')
            val1=c_q-1
            val2 = r_q-1
            vale2 = val1+val2
            k=0
            i=r_q+val1
            j=1
            while k<=vale2:
                if i==r_q and j==c_q:
                    i-=1
                    j+=1
                    k+=1
                    continue
                new_arr.append((i,j))
                i-=1
                j+=1
                k+=1
            # print(vale2,val1,val2,3)
    
    elif r_q>new_n:
            # print('hi r_q is and new_n is',r_q,new_n)
            val1 = n-r_q
            val2 = n-c_q
            vale2=val1+val2
            k=0
            i=r_q+val1
            j=c_q-val1
            while k<=vale2:
                if i==r_q and j==c_q:
                    i-=1
                    j+=1
                    k+=1
                    continue
                new_arr.append((i,j))
                i-=1
                j+=1
                k+=1
                
            
            # print(vale2,val1,val2,4)
    diagonal_move = vale1+vale2
    # print(diagonal_move,vale2)
    #vertical length
    val1 = n-r_q
    val2 = r_q-1
    vale_ver  = val1+val2
    k=0
    i=r_q
    j=1
    while k<=vale_ver:
        if i==r_q and j==c_q:
            j+=1
            k+=1
            continue
        new_arr.append((i,j))
        j+=1
        k+=1
    # print(vale_ver)
    #horizontal length
    val1 = n-c_q
    val2 = c_q-1
    vale_hor = val1+val2
    k=0
    i=1
    j=c_q
    while k<=vale_ver:
        if i==r_q and j==c_q:
            i+=1
            k+=1
            continue
        new_arr.append((i,j))
        i+=1
        k+=1
    # print(vale_hor)
    total = diagonal_move + vale_ver + vale_hor
    print(f'total moves : {total}')
    new_arr=list(set(new_arr))
    print('number of elements are ', len(new_arr))
    print(new_arr)
    # print('hi r_q is and new_n is',r_q,new_n)
    
    # Code for obstrcution
    
    # for i in range(len(k))
        
            
            
queensAttack(8,1,4)
