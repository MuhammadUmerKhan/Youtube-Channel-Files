data = ['This is Line 1\nThis is Line 2\nThis is Line 3']


with open('Example.txt', 'w') as myFile:
    contentWriting = myFile.writelines(data)