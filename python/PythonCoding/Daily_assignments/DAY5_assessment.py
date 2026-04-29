'''user_input = input("Enter some text: ")

with open("output.txt", "w") as file:
    file.write(user_input)

with open("output.txt", "r") as file:
    contents = file.read()

print("\nContents of output.txt:")
print(contents)'''


with open("sample.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words_in_line = line.split()
    word_count += len(words_in_line)
    char_count += len(line)

print(f"Number of lines: {line_count}")
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")