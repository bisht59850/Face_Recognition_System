# ascii=ord('a')
# print(ascii)

# print("Enter a String: ",end="")
text = input()
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)


print(ord('Vijay v'))