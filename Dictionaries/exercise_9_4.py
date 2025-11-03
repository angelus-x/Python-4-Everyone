# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# https://www.py4e.com/tools/pythonauto/static/files/mbox-short.txt?_=1762166321521


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

mail=dict()


for lines in handle:
    if not lines.startswith('From '): continue
    lines=lines.split()
    address=lines[1]
    #print(address)
    mail[address]=mail.get(address,0)+1

#print(mail)


final_email=None
final_count=None

for address,count in mail.items():
    if final_count is None or count > final_count:
        final_email = address
        final_count = count
        
print(final_email,final_count)        
   
