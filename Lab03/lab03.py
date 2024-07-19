def integerDivision(n, k):
    if n >= k:
        return integerDivision(n - k, k) + 1
    else:
        return 0


def collectEvenInts(listOfInt):
    if not listOfInt: 
        return []
    else:
        first = listOfInt[0]
        rest = listOfInt[1:]
        if first % 2 == 0:  
            return [first] + collectEvenInts(rest)  
        else:
            return collectEvenInts(rest)  


def countVowels(someString):
    vowels = "AEIOUaeiou"
    if not someString: 
        return 0
    else:
        first = someString[0]
        rest = someString[1:]
        if first in vowels: 
            return 1 + countVowels(rest) 
        else:
            return countVowels(rest) 
        

def reverseString(s):
    if s == "": 
        return s
    else:
        first = s[0]
        rest = s[1:]
        return reverseString(rest) + first  


def removeSubString(s, sub):
    if s == "":  
        return s
    elif s.startswith(sub):  
        return removeSubString(s[len(sub):], sub)  
    else:
        return s[0] + removeSubString(s[1:], sub)  


