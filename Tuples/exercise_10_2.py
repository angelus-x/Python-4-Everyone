# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts={}
for line in handle:
    if not line.startswith("From "):continue
    lines=line.split()
    date=lines[5]
    hours=date.split(":")[0]
    counts[hours]=counts.get(hours,0)+1

#print(counts)#Prints out dictionary

#print(sorted(counts))#Sort they key, but discards the value

new_list=[]
for key,value in counts.items():
    tuple=(key,value)
    new_list.append(tuple)
   
storage=sorted(new_list)

for k,v in storage:
    print(k,v)
