text = input("Enter the firstline of a nursery rhyme: ")
print("Text length: ", len(text))

start = int(input("Enter a starting number: "))
end   = int(input("Enter an end number: "))

print("Part:", text[start:end])