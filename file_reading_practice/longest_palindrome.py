"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
longest_palindromes = []
max_length = 0

with open("file_reading_practice/sowpods.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        
        if word == word[::-1]:
            word_len = len(word)
            
            if word_len > max_length:
                max_length = word_len
                longest_palindromes = [word]
            elif word_len == max_length:
                longest_palindromes.append(word)

print("Longest palindrome length:", max_length)
for p in longest_palindromes:
    print(p)