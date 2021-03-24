import math
def queensAttack(n,e,r_q,c_q,g):
    # print(n)
    # print(e)
    # print(r_q)
    # print(c_q)
    # print(g)
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

            # print(vale2,'yyy')

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
    # print(f'total moves : {total}')
    new_arr=list(set(new_arr))
    # print('number of elements are ', len(new_arr))
    # print(new_arr)
    # print('hi r_q is and new_n is',r_q,new_n)


    obs_pos = set()
    # for i in range(len(g)):
    #     obs_pos.append(tuple(g[i]))

    for  i in range(len(g)):
        for j in range(len(new_arr)):
            if tuple(g[i])==new_arr[j]:
                if r_q==g[i][0]:
                    if g[i][1]>c_q:
                        k=g[i][1]
                        while k<=n:
                            obs_pos.add((r_q,k))
                            k+=1
                    else:
                        k=g[i][1]
                        while k>=1:
                            obs_pos.add((r_q,k))
                            k-=1
                elif c_q==g[i][1]:
                    if g[i][0]>r_q:
                        k=g[i][0]
                        while k<=n:
                            obs_pos.add((k,c_q))
                            k+=1
                    else:
                        k=g[i][0]
                        while k>=1:
                            obs_pos.add((k,c_q))
                            k-=1

                else:

                    if g[i][0]>r_q and g[i][1]>c_q:
                        k_row=g[i][0]
                        k_col = g[i][1]
                        while k_col<=n and k_row<=n:
                            obs_pos.add((k_row,k_col))
                            k_row+=1
                            k_col+=1
                    elif g[i][0]>r_q and g[i][1]<c_q:
                        # print('hiyy')
                        k_row = g[i][0]
                        k_col = g[i][1]
                        while k_row<=n and k_col>=1:
                            obs_pos.add((k_row, k_col))
                            k_row += 1
                            k_col -= 1
                    elif g[i][0]<r_q and g[i][1]<c_q:
                        k_row = g[i][0]
                        k_col = g[i][1]
                        while k_row>=1 and k_col>=1:
                            obs_pos.add((k_row, k_col))
                            k_row -= 1
                            k_col -= 1
                    else:
                        k_row = g[i][0]
                        k_col = g[i][1]
                        while k_row >= 1 and k_col <= n:
                            obs_pos.add((k_row, k_col))
                            k_row -= 1
                            k_col += 1
    y_t =len(new_arr)-len(list(obs_pos))
    print(f'ans is {y_t}')
#     # return y_t
#
#
#
#     print(list(obs_pos))
#
#
#
# queensAttack(10000,4,4,[[3,5]])
# # queensAttack(4,4,4,[])
# # queensAttack(5,4,3,[[5,5],[4,2],[2,3]])
# # queensAttack(1,1,1,[])
obstacles = []

with open('input08.txt') as file_handler:
    for line in file_handler:
        obstacles.append(list(map(int, line.rstrip().split())))

# print(obstacles)

# print(fptr)
# nk = fptr.split()
# print(nk)
# n = int(nk[0])
#
# k = int(nk[1])
#
# r_qC_q = input().split()
#
# r_q = int(r_qC_q[0])
#
# c_q = int(r_qC_q[1])
#
# obstacles = []
#
# for _ in range(k):
#     obstacles.append(list(map(int, input().rstrip().split())))

g = obstacles[2:]
# print(g)

queensAttack(obstacles[0][0], 2, obstacles[1][0], obstacles[1][1], g)
# queensAttack(76453, 2, 45635, 65243, [[3,5],[4,5]])