# cook your dish here
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 
t=int(input())
for i in range(t) :
    n=int(input())
    string=input()
    sstr=list(string)
    for j in range(n) :
            if sstr[j]=='A' :
                sstr[j]='T'
            elif sstr[j]=='T' :
                sstr[j]='A'
            elif sstr[j]=='C' :
                sstr[j]='G'
            else :
                sstr[j]='C'
    sstr2=listToString(sstr)    
    print(sstr2)
    