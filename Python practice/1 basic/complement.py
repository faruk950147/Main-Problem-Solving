# find complement of a number
# complement of a number is the number with all the bits inverted
# for example, the complement of 5 is 2
# 5 in binary is 101
# 2 in binary is 010

def FindComplement(num):
    binary = bin(num)[2:]
    complement = "" 
    for bit in binary:
        if bit == "1":
            complement += "0"
        else:
            complement += "1"
    return int(complement, 2) # convert binary to decimal and 2 is base of binary
    
a = 1
print(FindComplement(a))
    
    