def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    content = []
    for l in lines:
        if l != '\n':
            content.append(l.replace("\n", " "))
    return content
