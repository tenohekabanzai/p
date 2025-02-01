f = open('text.txt','r') # opened file in read only mode
print(f.name) # get filename
print(f.mode) # get mode
f.close()

print('_____________________________________________________________________________')
print('_____________________________________________________________________________')

with open('text.txt','r') as x:
    f_contents = x.read(); # reads entire file    
    print(f_contents,' ')
    print('_____________________________________________________________________________')
    x.seek(0); #brings pointer to first line of file
    f_line1 = x.readline()
    f_line2 = x.readline()
    f_line3 = x.readline()
    print(f_line1,' ')
    print(f_line2,' ')
    print(f_line3,' ')
    x.close()
print('_____________________________________________________________________________')
print('_____________________________________________________________________________')

with open('text.txt','r') as y:
    # printing all lines in a file
    for line in y:
        print(line,' ')
    y.close()

with open('test2.txt','w') as z:
    # writing to file
    z.write("Hello World\n")
    z.write("Hello World\n")
    z.close();

with open('text.txt','r') as rf:
    with open('test3.txt','w+') as wf:
        content = rf.read();
        wf.write(content)
        print('------------------------------------------------------------------------')
        #printing file that was written upon
        wf.seek(0)
        for line in wf:
            print(line,' ')
        wf.close();
    rf.close();

### File Objects
with open('seal.jpg','rb') as rf:
    with open('seal_copy.jpg','wb') as wf:
        # break jpg file in to binary blocks of 4096 bits
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size);
        while len(rf_chunk) >0:
            #write the file into another block by block
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)