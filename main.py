# make column of type BLOB in the database table and store the binary

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

# print(convertToBinaryData('Python.png'))
# print(convertToBinaryData('pdf.pdf'))

binaryImage = convertToBinaryData('pdf.pdf')

write_file(binaryImage, 'pdf2.pdf')
