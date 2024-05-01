# Replace ___ with your code

def compute_lps_array(pattern):
    lps = [0]
    c = 0
    for i in range(1, len(pattern)):
        if pattern[c] == pattern[i]:
            c = c + 1 
        elif pattern[i] == pattern[0]:
            c = 1
        else:
            c = 0
        lps.append(c)
    return lps

def kmp(text, pattern):
    occurences= []
    i = 0
    j = 0
    # write your code here
    lps = compute_lps_array(pattern)
    while i < len(text):
        if pattern[j] == text[i]:
            i+=1
            j+=1
            if j < len(pattern)-1:
                occurences.append(i-j)
                j = lps[j-1]
        else:
            #if mismatch
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
    return occurences



        

text = input()
pattern = input()
occurrences = kmp(text, pattern)

for occurrence in occurrences:
    end_index = occurrence+len(pattern)-1
    print(f"Matching pattern: index {occurrence} to {end_index}.")