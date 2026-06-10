"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
total_count = 0
vowels = ["a", "e", "i", "o", "u"]

with open("file_reading_practice/sowpods.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        
        has_all_vowels = True
        for v in vowels:
            if v not in word:
                has_all_vowels = False
                break
                
        if has_all_vowels:
            print(word)
            total_count += 1

print("Total words with all vowels:", total_count)