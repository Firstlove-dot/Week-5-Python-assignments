
filename = input("Enter the file name .i.e file.txt :")
try:
    # Open the file for reading
    infile = open(filename, "r")
    content = infile.read()
    infile.close()

    # Modify the content (make everything uppercase)
    modified_content = content.upper()

    # Save into a new file
    new_filename = "modified_" + filename
    outfile = open(new_filename, "w")
    outfile.write(modified_content)
    outfile.close()

    print("File processed successfully! Saved as:", new_filename)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)