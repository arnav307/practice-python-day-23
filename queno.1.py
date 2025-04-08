def counts(filename):
    with open(filename, 'r') as inputfile:
        files = inputfile.read()
        count=0
        for char in files:
            if char !=' 'and char!='\n':    
                count+=1
        print(count)
        
        
counts('file.txt')