# Set up our data structures
DICT = {}
infile = open("wordlist.txt", 'r')
for word in infile:  # `word`` goes through each line in the file
    DICT[word.strip()] = 0
    # Creates an entry with key `word` and value 0 (for the count)
print("Number of words in DICT", len(DICT))
infile.close()  # close the file after we're done with it

WORDLIST = []
for key in DICT:  # put the DICT keys into WORDLIST
    WORDLIST.append(key)
print("Number of words in WORDLIST", len(WORDLIST))


infile = open("peter_pan.txt", 'r')
book = infile.read()
infile.close()
words = book.split()

from time import time

# Algorithm 1 - Lists
start = time()

counter = 0
for word in words:
    word = word.strip("\"\'()[]{},.?<>:;-").lower()
    if word in WORDLIST:
        counter += 1
end = time()
print("counter", counter)
print("Time elapsed with WORDLIST (in seconds):", end - start)

# Algorithm 2 - Dictionary
start = time()
counter = 0

for word in words:
    word = word.strip("\"\'()[]{},.?<>:;-").lower()
    if word in DICT:
        counter += 1
end = time()
print("counter", counter)
print("Time elapsed with DICT (in seconds):", end - start)

