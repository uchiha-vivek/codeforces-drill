

def seive(n):
    prime = [True for i in range(n+1)]
    p:int=2
    while(p*p<=n):
        if(prime[n]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        
        p+=1

    for p in range(2,n+1):
        if prime[p]:
            print(p)


if __name__=="__main__":
    print(seive(20))