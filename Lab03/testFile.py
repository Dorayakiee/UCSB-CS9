# testFile.py

def test_integerDivision():
    from lab03 import integerDivision
    assert integerDivision(25, 5) == 5
    assert integerDivision(27, 5) == 5
    assert integerDivision(25, 1) == 25
    assert integerDivision(25, 2) ==12
    


def test_collectEvenInts():
    from lab03 import collectEvenInts
    assert collectEvenInts([1, 2, 3, 4, 5, 6]) == [2,4,6]
    assert collectEvenInts([7, 3, 9, 1]) == []
    assert collectEvenInts([2, 4, 6, 8]) == [2,4,6,8]
    assert collectEvenInts([1,2,3,4]) == [2,4]

def test_countVowels():
    from lab03 import countVowels
    assert countVowels("hello") == 2 
    assert countVowels("world") == 1
    assert countVowels("OpenAI") == 4
    assert countVowels("python") == 1
    assert countVowels("") == 0
    assert countVowels("AEIOU") == 5
    assert countVowels("aeiou") == 5

def test_reverseString():
    from lab03 import reverseString
    assert reverseString("hello") == "olleh"
    assert reverseString("world") == "dlrow"
    assert reverseString("OpenAI") == "IAnepO"
    assert reverseString("python") == "nohtyp"
    assert reverseString("") == ""  
    assert reverseString("a") == "a"
    assert reverseString("ab") == "ba"



def test_removeSubString():
    from lab03 import removeSubString
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("ababcc", "abc") == "abc"
    assert removeSubString("hello", "l") == "heo"
    assert removeSubString("world", "or") == "wld"
    assert removeSubString("OpenAI", "e") == "OpnAI"
    assert removeSubString("python", "py") == "thon"
    assert removeSubString("aaaaa", "aa") == "a"
    assert removeSubString("aabbcc", "ab") == "abcc"


