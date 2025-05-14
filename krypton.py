from collections import deque as dq
d=dq([])
uid=0
def shiv(target,pos,tree):
    
    while d:
        
        el=d.popleft()
        
        if tree[el]==target:
            pp=el*(p-1)+pos
            return pp
        
        if left(el)!=-1:
            d.append(left(el))
            
        if right(el)!=-1:
            d.append(right(el))
        

def left(ind):
    v=(ind*2)+1
    if v<len(tree):
        return v
    return -1
    
def right(ind):
    v=(ind*2)+2
    if v<len(tree):
        return v
    return -1
    
p=int(input("enter number of parameters"))
params=[]
tree=[]
branches=[]

for i in range(p-1):
    z=input("enter attribute")
    params.append(z)

def pushdata(uid,params,tree,branches):
    print(f"you unique identifier is {uid}")
    tree.append(uid)
    if len(tree)<1:
        d.append(0)
    uid+=1
    for i in range(len(params)):
        z=input(f"enter value for {params[i]}")
        branches.append(z)
    print(tree)
    print(branches)
    return uid
        
def query(params,tree,branches):
    v=int(input("enter unique identifier"))
    
    v1=input("enter attribute to search")
    
    v2=params.index(v1)
    
    op=shiv(v1,v2,tree)
    print(f"{v1} of {v} is {op}")    
    
op1=pushdata(uid,params,tree,branches)
op2=pushdata(op1,params,tree,branches)
query(params,tree,branches)
    


        
    
    
    
    

    
