'''
Q. alternativel merge two strings
i/p
Bhima
ABCDEOLM
o/p
BAhBiCmDaEOLM

'''

def alternate_merge(s1, s2):
    result = []
    n = min(len(s1), len(s2))
    for i in range(n):
        result.append(s1[i])
        result.append(s2[i])
    if len(s1) > len(s2):
        result.append(s1[n:])
    elif len(s2) > len(s1):
        result.append(s2[n:])
    return ''.join(result)

s1 = "Bhima"
s2 = "ABCDEOLM"

print(alternate_merge(s1, s2))
	

