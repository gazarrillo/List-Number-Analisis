#Obtaining Path from User
path = input('Enter File Path Here (must be a .txt): ')
#Initializing List
nlist = []
#Opening File
rfile = open(path, 'r')
#Reading File
for linefromfile in rfile:
    nlist.append(int(linefromfile))
rfile.close()
#Calculating Min, Max, Sum, Length, and Average
min_nlist = min(nlist)
max_nlist = max(nlist)
sum_nlist = sum(nlist)
len_nlist = len(nlist)
avg_nlist = sum_nlist/len_nlist
#Intro
print('The following numbers were read from the file:')
#Printing Numbers in List
for i in range (len_nlist):
    print(nlist[i])
#Printing Results
print('The lowest number in the list is: ' + str(min_nlist))
print('The highest number in the list is: ' + str(max_nlist))
print('The total of all numbers in the list is: ' + str(sum_nlist))
print('The average of all numbers in the list is: ' + str(avg_nlist))
