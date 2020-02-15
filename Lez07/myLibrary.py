def isIntero(s):
    s = s.strip()
    if s[0:1] in '+-': 
        s=s[1:]
    return s.isdecimal()

def isPari(n):
    return n%2==0
