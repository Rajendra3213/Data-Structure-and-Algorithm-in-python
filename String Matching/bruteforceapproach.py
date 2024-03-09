# Replace ___ with your code

def brute_force(text, pattern):
    # write your code here
    occurances = []
    for i in range(0,len(text)):
        for j in range(0,len(pattern)):
            match = text[i+j] == pattern[j]
            if not match:
                break
            if j == len(pattern)-1:
                occurances.append(i);
    return occurances
        

text = input()
pattern = input()
occurrences = brute_force(text, pattern)
for occurrence in occurrences:
    end_index = occurrence+len(pattern)-1
    print(f"Matching pattern: index {occurrence} to {end_index}.")