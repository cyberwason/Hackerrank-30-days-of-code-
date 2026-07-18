# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())

for a0 in range(t):
    s = input().strip()
    
    even_chars = s[0::2]
    odd_chars = s[1::2]
    
    print(even_chars, odd_chars)