# Function names 'is_anagram' takes two string as its parameters.
#It returns True if the string are anagrams, and False otherwise.

#E.g, is_anagram("typhoon", "opython") should return True
# While the call is_anagram("Alice", "Bob") should return False.

def is_anagram(a, b): 
    auth = False if len([i for i in list(a) if i not in list(b)]) >= 1 else True
    return auth

print(is_anagram("typhoon", "opython")) #True
print(is_anagram("typhozon", "opython")) #False
print(is_anagram("typhhozon", "opython")) #False

print(is_anagram("Alice", "Bob")) #False
