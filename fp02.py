import re
string_a_comparar = "Ola, eu tenho 245 anos"
pattern = re.compile(r'\d{3}')
s = re.findall(pattern, string_a_comparar)
print(s)