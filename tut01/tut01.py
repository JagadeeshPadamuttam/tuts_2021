
print("my name is Jagadeesh Padamuttam.and my roll no is :1901EE27")

def meraki_helper(n):
    """This will detect meraki number"""
    if (n<0):
        print("Yes","this a meraki number",n)
        return 1
#cast the given elements in input into string to calculate the number of digits in each element of input
    string_of_n=str(n)
#now calculate length of string
    length_of_string=len(string_of_n)-1
    x=0 
    for x in range(0,length_of_string):
        v=int(string_of_n[x])
        w=int(string_of_n[x+1])-int(string_of_n[x])
        if (abs(w)==1):
        
            continue
        else:
            print("No !","this not a meraki number",n)
            return 0
    print("Yes","this is a meraki number",n)
    return 1

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_count=0
non_meraki_count=0
for y in input:
    if(meraki_helper(y)):
        meraki_count+=1
    else:
        non_meraki_count+=1
print("The given input contains number  of meraki numbers" ,meraki_count,",")
print("the given input contains number of non meraki numbers",non_meraki_count)