n = input().upper()
original = n

# Replace 'A' with 'T'
result = ''
for ch in n:
    if ch == 'A':
        result += 'T'
    else:
        result += ch
print(result)

# Now replace 'C' with 'G' on the previous result
result2 = ''
for ch in result:
    if ch == 'C':
        result2 += 'G'
    else:
        result2 += ch
print(result2)

# Palindrome check on original input
if original == original[::-1]:
    print("palindrome")
else:
    print("not palindrome")

