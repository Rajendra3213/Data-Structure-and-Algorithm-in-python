# Replace ___ with your code

def compute_hash(string, base = 256, prime = 101):
    
    hash_value = 0

    for index, char in enumerate(string):
        
        ascii_value = ord(char)
        exponent = len(string) - index - 1
        term = (ascii_value * pow(base, exponent)) % prime
        
        hash_value = (hash_value + term) % prime

    return hash_value

def rabin_karp(text, pattern, base = 256, prime = 101):
    # write your code here
    pattern_length = len(pattern)
    text_length = len(text)
 
    # hash of the pattern text (substring)
    pattern_hash = compute_hash(pattern)
    
    # hash of a substring that has the same length as the pattern
    substring_hash = compute_hash(text[: pattern_length])
    
    # initialize a list to store occurrences of the pattern in text
    occurrences = []
    
    # pre-compute the highest power of base
    # this is needed to update the hash for the next substring
    highest_base_pow = pow(base, pattern_length - 1) % prime
 
    # loop through all possible substrings of text with pattern length
    for i in range(text_length - pattern_length + 1):
        
        # compare hash of substring and pattern
        if pattern_hash == substring_hash:
            
            # double check to confirm match
            if all(text[i + j] == pattern[j] for j in range(pattern_length)):
                occurrences.append(i)
                
        # update the hash of the next substring using the previous hash
        if i < text_length - pattern_length:
            
            # update the rolling hash for the next substring
            # remove first character's hash and add next character's hash-based
            substring_hash = (substring_hash - ord(text[i]) * highest_base_pow) * base
            substring_hash = (substring_hash + ord(text[i + pattern_length])) % prime
            
    return occurrences

text = input()
pattern = input()
occurrences = rabin_karp(text, pattern)

for occurrence in occurrences:
    end_index = occurrence + len(pattern)-1
    print(f"Matching pattern: index {occurrence} to {end_index}.")