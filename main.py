# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
     
    # the sorted strings are checked
    if(sorted(word)== sorted(anagram)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
word ="below"
anagram ="elbow"
find_anagram(word, anagram)
