"""This module processes sings based on certain conditions."""
def fun(n,s):
    """Process the string based on whether n is even or odd."""
    if n%2==0:
        i=0
        j=len(s)-1
        while s[i]==s[j] and i<j:
            # print(i,j)
            i+=1
            j-=1

        if i>=j:
            return s

        if ord(s[i])<ord(s[j]):
            return s
	else:
            return s[::-1]+s
    else:
        i=0
        j=len(str)-1
        while s[i]!=s[j] and i<=j:
            i+=1
            j-=1
        if i>=j:
            return s
        if ord(s[i])>=ord(s[j]):
            return s
        else:
	    return s[::-1]+s


for _ in range(int(input())):
    no = int(input())
    # n,m,k = map(lambda x: int(x), input().split())
    inp_s=input()

    print(fun(no,inp_s))
