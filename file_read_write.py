#!/usr/bin/env python3

# Create a file and write some content to it
file = open("input.txt", "w")
file.write("Hello World!")
file.write("This is my Python file read and write assignment.")
file.write("Hope I pass this test!")
file.close()

# Read the content of input.txt
file = open("input.txt", "r")
content = file.read()
file.close()

print("Original Content (input.txt):")
print(content)

# Modify content (convert to uppercase)
modified_content = content.upper()

# Write modified content into a new file
file = open("output.txt", "w")
file.write(modified_content)
file.close()

print(" Modified Content has been written to output.txt")


# Error Handling Lab 

try:
    #  Ask the user for a filename
    filename = input("file_read_write: ")

    # Step 6: Try reading the file
    file = open(filename, "r")
    content = file.read()
    print("File content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")

finally:
    print(" File operation completed.")
