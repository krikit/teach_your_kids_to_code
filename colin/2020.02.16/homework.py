message = input("Enter a message to encode or decode: ")
output = ""
for letter in message:
    if 'A' <= letter <= 'M' or 'a' <= letter <= 'm':
        value = ord(letter) + 13
    elif 'N' <= letter <= 'Z' or 'n' <= letter <= 'z':
        value = ord(letter) - 13
    letter = chr(value)
    output += letter
print("Output message: ", output)
