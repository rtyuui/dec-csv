def valid_file(given_file):
    """

    :param given_file: name of the supplied file
    :return: if the file is of valid format
    Note: Lazy Check
    """
    if ".csv" not in given_file:
        print("Not a .csv type file? ")
        return False
    else:
        return True


filename = input("Filename: ")
new_filename = filename[0: len(filename) - 4]
#  dec_filename = new_filename + "_decrypted.csv"
new_filename += "_decrypted.lzma"

f = open(filename, "rb")
# ignore first 43 bytes
data_enc = f.read(43)
# save rest of bytes
data = f.read()

empty = b'\x00'


new_data = data[25:]
first_8 = new_data[:8]
rest = new_data[12:]
print(new_data)
new_file = open(new_filename, "wb")
# insert 6 bytes in between 
new_file.write(first_8 + empty * 6 + b'\x11' + b'\x13' + rest) 
# save & finish
new_file.close()
f.close()

