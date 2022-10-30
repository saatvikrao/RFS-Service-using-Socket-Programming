import os

def get_size(fileobject):
    # go to the end of the file 
    fileobject.seek(0,2) 
    size = fileobject.tell()
    return size


####### for plain text #######
def plain_text_encode(file):
    return
def plain_text_decode(file):
    return


####### for transpose #######
def transpose_encode_decode(file):
    current_file = file.split('.')

    file1 = open(current_file[0] + '1' + current_file[1], 'w')
    file2 = open(file, 'r')

    for line in file2: 
        word = line.split() 

        for i in range(len(word)):
            chr = word[i]
            file1.write(chr[::-1])

            if (i != len(word) - 1): file1.write(' ')
        
        file1.write('\n')

    fsize = get_size(file1)

    file1.truncate(fsize - 1)

    file1.close()
    file2.close()
    os.remove('./' + file)
    os.rename('./' + current_file[0] + '1' + current_file[1], './' + file)


####### for substitue #######
# Caesor cipher 
def substitute_encode(file):
    current_file = file.split('.')

    file1 = open(current_file[0] + '1' + current_file[1], 'w')
    file2 = open(file, 'r')
    file3 = file2.read(1)

    while (file3):
        file1.write(chr((ord(file3) + 2) % 256))

        file3 = file2.read(1)

    file1.close()
    file2.close()
    os.remove('./' + file)
    os.rename('./' + current_file[0] + '1' + current_file[1], './' + file)


def substitute_decode(file):
    current_file = file.split('.')

    file1 = open(current_file[0] + '1' + current_file[1], 'w')
    file2 = open(file, 'r')
    file3 = file2.read(1)

    while (file3):
        file1.write(chr((256 + ord(file3) - 2) % 256))

        file3 = file2.read(1)

    file1.close()
    file2.close()
    os.remove('./' + file)
    os.rename('./' + current_file[0] + '1' + current_file[1], './' + file)

