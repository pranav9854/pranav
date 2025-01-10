def extract_pattern(s):
    substrings = []
    
    for i in range(len(s) - 2):
    
        if s[i] == s[i + 3]:
            
            substrings.append(s[i:i + 4])  
    
    return substrings
input_string = "abacab"
result = extract_pattern(input_string)
print(result)  
