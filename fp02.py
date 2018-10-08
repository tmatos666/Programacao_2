import re

#Ex1
"""string_a_comparar = ["abcdefg", "abcde", "abc"]
pattern = re.compile("abc")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex2
"""string_a_comparar = ["abcd123efg", "ab123cde", "123abc"]
pattern = re.compile("123")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex3
"""string_a_comparar = ["cat.", "896.", "?=+.","abc1"]
pattern = re.compile(r"...\.")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex4
"""string_a_comparar = ["can", "man", "fan","dan","ran","pan"]
pattern = re.compile("[cmf]an")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex5
"""string_a_comparar = ["hog", "dog", "bog"]
pattern = re.compile("[^b]og")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex6
"""string_a_comparar = ["Ana", "Bob", "Cpc","aax","bby","ccz"]
pattern = re.compile("[A-Z][n-p][a-c]")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex7
"""string_a_comparar = ["wazzzzzup", "wazzzup", "wazup"]
pattern = re.compile("waz{3,5}up")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex8
"""string_a_comparar = ["aaaabcc", "aabbbbc", "aacc", "a"]
pattern = re.compile("aa+b*c+")
#significa 1 ou mais aa´s, 0 ou mais b´s e 1 ou mais c's
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex9
"""string_a_comparar = ["1 file found?", "2 files found?", "24 files found?", "No files found."]
pattern = re.compile(r"\d+ files? found\?")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""


#Ex10
"""string_a_comparar = ["1.   abc", "2.    abc", "3.     abc", "4.abc"]
pattern = re.compile(r"\d\.\s+abc")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex11
"""
string_a_comparar = ["Mission: successful", "Last Mission: unsuccessful", "Next Mission: successful upon capture of target"]
pattern = re.compile("^Mission: successful$")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex12
"""string_a_comparar = ["file_record_transcript.pdf", "file_07241999.pdf", "testfile_fake.pdf.tmp"]
pattern = re.compile(r"^(file_.+)\.pdf")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""