word = "Zero days on the cruise "  
file_name = "zerodays.md"  

with open(file_name, 'w') as file:
    for _ in range(5000):
        file.write(word + "\n")

print(f"File '{file_name}' has been written with 5000 lines of '{word}'.")

# now you got zero days 
