def hashing(input_):
    output = []
    for i in range(0, len(input_)):
        code = ord(input_[i]) % (len(input_)*(i+1))
        output.append(code)
    return output

def hashing2(input_):
    total = 0
    for i in range(0, len(input_)):
        code = ord(input_[i]) % (len(input_)*(i+1))
        total += code
    return total

print(hashing(input("input: ")))
print(hashing2(input("input: ")))
