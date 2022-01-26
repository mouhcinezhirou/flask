import pandas as pd
import numpy as np

def Methode_Coutmin(n,m,name):
    C=[]
    T=[]
    CT=1
    A3=[]
    df = pd.read_excel(name)
    df = df.dropna(how='all', axis='columns') 
    a = df[df.columns[1:]].values
    while len(A3)!=1:
        TAB_COUT=np.delete(np.delete(a,slice(m,m+1),1),n,0)
        for i in range(n):
            x=min(TAB_COUT[i])
            T.append(x)
        z=min(T)
        A3=TAB_COUT.tolist()
        t=fnd(A3,z)
        if a[n][t['col']-1]>=a[t['row']-1][m] :
            y=a[t['row']-1][m]
            a[n][t['col']-1]=a[n][t['col']-1]-a[t['row']-1][m]
            a=np.delete(a,t['row']-1,0)
            n=n-1
        else:
            y=y=a[n][t['col']-1]
            a[t['row']-1][m]=a[t['row']-1][m]-a[n][t['col']-1]
            a=np.delete(a,slice(t['col']-1,t['col']),1)
            m=m-1
        T=[]
        C.append((z,y))
    for i in range(len(C)):
        CT=CT+C[i][0]*C[i][1]
    #print(f'le cout total de cette operation est: {CT}')
    return CT

def Methode_NordOuest(n,m,name):
    C=[]
    CT=1
    df = pd.read_excel(name)
    df = df.dropna(how='all', axis='columns')    
    print(df)
    a = df[df.columns[1:]].values
    print(a)
    c=0
    while np.shape(a)!=(1,2):
        print("a[c][m],a[n][c] --> " , c,m,n,c)
        x=min(a[c][m],a[n][c])
        y=a[0][0]
        if a[c][m]>a[n][c] :
            a[c][m]=a[c][m]-a[n][[c]]
            a=np.delete(a,0,1)
            m=m-1
        else:
            a[n][c]=a[n][c]-a[c][m]
            a=np.delete(a,0,0)
            n=n-1
        C.append((x,y))
    for i in range(len(C)):
        CT=CT+C[i][0]*C[i][1]
    #print(f'le cout total de cette operation est: {CT}')
    return CT


def f_reg(n,m,name):
    Y=[]
    C=[]
    T=[]
    CT=1
    A4=[]
    a=np.zeros((n+2,m+2))
    #r=np.zeros((n+2,m+2))
    #l=0
    df = pd.read_excel(name)
    df = df.dropna(how='all', axis='columns') 
    df["regret"] = 0
    row = dict()
    for item in df.columns:
        row[item] = 0
    df = df.append(row, ignore_index=True)
    a = df[df.columns[1:]].values
    #print(a)
    a=calculregret(a,m,n)
    #print(a)
    Lr=regretvide(a,n,m)
    while(len(A4)!=1):
        A1=np.delete(a,slice(m+1,m+2),1)
        A2=np.delete(A1,slice(m,m+1),1)
        A3=np.delete(A2,n+1,0)
        A4=np.delete(A3,n,0)
        L1=A4.tolist()
        Lr=regretvide(a,n,m)
        m3=maxregret(Lr,a)
        S=fnd(Lr,m3)
        #print(S)
        x=minrowcol(L1,S,m,n)
        Lv=valeurminavide(a,S,n,m)
        t=fnd(Lv,x)
        #print(t)
        if a[n][t['col']-1]>=a[t['row']-1][m] :
            y=a[t['row']-1][m]
            a[n][t['col']-1]=a[n][t['col']-1]-a[t['row']-1][m]
            a=np.delete(a,t['row']-1,0)
            n=n-1
            #print(a)

        else:
            y=y=a[n][t['col']-1]
            a[t['row']-1][m]=a[t['row']-1][m]-a[n][t['col']-1]
            a=np.delete(a,slice(t['col']-1,t['col']),1)
            m=m-1
            #print(a)
        T=[]


        C.append((x,y))
    #print(len(C))
    #print(C)
    for i in range(len(C)):
        CT=CT+C[i][0]*C[i][1]
    return CT

def maxregret(Lr,a):
    Y=[]
    for i in range(len(Lr)-2):
        Y.append(a[i][np.shape(Lr)[1]-1])
    m1=max(Y)
    Y=[]
    for i in range(np.shape(Lr)[1]-2):
        Y.append(a[len(Lr)-1][i])
    m2=max(Y)
    Y=[]
    return max(m1,m2)


    
def minrowcol(L1,S,m,n):
    Y=[]
    if S['col']==m+2:
        p=min(L1[S['row']-1])
    else:
        p=0
        for i in range(S['row']-2):
            Y.append(L1[i][S['col']-1])
        p=min(Y)
        Y=[]
    return p
    
    
def calculregret(a,m,n):
    Y=[]
    A1=np.delete(a,slice(m+1,m+2),1)
    A2=np.delete(A1,slice(m,m+1),1)
    A3=np.delete(A2,n+1,0)
    A4=np.delete(A3,n,0)
    L1=A4.tolist()
    if len(A4)!=1:
        for i in range (np.shape(L1)[1]):
            for j in range(len(L1)):
                Y.append(L1[j][i])
            m1=min(Y)
            Y.remove(m1)
            m2=min(Y)
            a[n+1][i]=m2-m1
            Y=[]
    if np.shape(A4)[1]!=1:
        for i in range(len(L1)):
            for j in range (np.shape(L1)[1]):
                Y.append(L1[i][j])
            m1=min(Y)
            Y.remove(m1)
            m2=min(Y)
            a[i][m+1]=m2-m1
            Y=[]
    return a
    
    
def valeurminavide(a,S,n,m):
    v=np.zeros((n,m))
    if S['col']==m+2:
        for i in range (m):
            v[S['row']-3][i]=a[S['row']-3][i]
    else:
        for i in range(n):
            v[i][S['col']-1]=a[i][S['col']-1]
    Lv=v.tolist()
    return Lv


def regretvide(a,n,m):
    A1=np.delete(a,slice(m+1,m+2),1)
    A2=np.delete(A1,slice(m,m+1),1)
    A3=np.delete(A2,n+1,0)
    A4=np.delete(A3,n,0)
    L1=A4.tolist()
    r=np.zeros((n+2,m+2))
    for i in range (np.shape(L1)[1]):
        r[n+1][i]=a[n+1][i]
    for i in range(len(L1)):
        r[i][m+1]=a[i][m+1]
    Lr=r.tolist()
    return Lr
    
    
def fnd(l,value):
    for i,v in enumerate(l):
        if value in v:
            return {'row':i+1,'col':v.index(value)+1}