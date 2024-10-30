"""Roman to Integer
Symbol  Value
I		1
V		5
X		10
L		50
C		100
D		500
M		1000
"""


def integerValue(c: str):
    if c == "I":
        return 1
    if c == "V":
        return 5
    if c == "X":
        return 10
    if c == "L":
        return 50
    if c == "C":
        return 100
    if c == "D":
        return 500
    if c == "M":
        return 1000
    return -1


def romanToInteger(S):
    n = len(S) 
    # print(f"len: {n}")
    output = 0
    for i in range(n):
        curr = integerValue(S[i])
        if i + 1 < n:
            next = integerValue(S[i + 1])
            if curr >= next:
                output = output + curr
            else:
                output = output - curr
        else:
            output = output + curr
        # print(f"curr: {curr}\tnext: {next}\toutput: {output}")

    return output


print(f"Output: {romanToInteger("XL")}")
print(f"Output: {romanToInteger("MCMIV")}")
print(f"Output: {romanToInteger("MCMXCIV")}")
