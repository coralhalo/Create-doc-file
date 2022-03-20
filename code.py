def create_doc_file(read,new):
    '''Reads through a python file and prints the function header without the 
    word  def and the ':'. 
    Looks for any comment starting with three quotation marks and writes the lines without the 
    quotation marks. 
    Doesn't include any comments starting with # . '''
    infile=open(read,"r") #opening the file that this function will read 
    outfile=open(new,"w") #opens another python file where it will store everything. 
    count=0
    for line in infile:
        stripped_line= line.strip()  # getting rid of all the whitespaces for calculation purpose. 
        #outfile.write(stripped)

        if stripped_line.startswith('def'): #looks for function header 
            first_line=stripped_line[4:-2] + '\n' #leaves the word def and colon 
            #print(first_line)
            outfile.write(first_line)
            
        if  stripped_line.startswith("'''") and count==0: #looking for the first quotation marks 
            
            if stripped_line.endswith("'''"):  #if the comment is only one line then this condition executes
                
                com_pos= stripped_line.find("'''") 
                com_pos2= stripped_line.find("'''", com_pos+3)  
                stripped_line= stripped_line[com_pos+3:com_pos2] + '\n'
                outfile.write(stripped_line) 
            else: #this condition works if the comment is not only one line 
                stripped_line= stripped_line.rstrip()
                comment_pos= stripped_line.find("'''")
                stripped_line= stripped_line[comment_pos+3:] +"\n" #stores the first line of comment without the quote marks and breaks the line  
                outfile.write(stripped_line) 
                count+=1    

        elif "'''" in stripped_line  and count !=0: #count not being zero means we are inside the quote marks and looking for the last line 
            com_pos= stripped_line.find("'''")   
            stripped_line= stripped_line[:com_pos] + '\n' #using index to get everything except quote marks
                    
            outfile.write(stripped_line)
            count=2 #prevents from printing all other lines of the code

        elif count==1: #count being 1 means we are inside the quote marks without any quote marks
            stripped_line=stripped_line.rstrip() + '\n'  
            outfile.write(stripped_line) 
           
                   
#testing           

create_doc_file('jam.py','new_file.py')        
