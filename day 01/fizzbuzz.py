# using modulus
def fizzbuzz_soln1(num):
    output = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output


# without using modulus
def fizzbuzz_soln2(num):
    output = []
    fizzCount = 0
    buzzCount = 0
    for i in range(1, num + 1):
        fizzCount += 1
        buzzCount += 1
        if fizzCount == 3 and buzzCount == 5:
            output.append("FizzBuzz")
            fizzCount = 0
            buzzCount = 0
        elif buzzCount == 5:
            output.append("Buzz")
            buzzCount = 0
        elif fizzCount == 3:
            output.append("Fizz")
            fizzCount = 0
        else:
            output.append(str(i))
    return output


# using hashmap and string
def fizzbuzz_soln3(num):
    output = []
    fizz_buzz = {3: "Fizz", 5: "Buzz"}
    for i in range(1, num + 1):
        s = ""
        for key in fizz_buzz:
            if i % key == 0:
                s += fizz_buzz[key]
        if s == "":
            s = str(i)
        output.append(s)
    return output

print(fizzbuzz_soln3(15))
