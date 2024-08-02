def removeCharacter(str,n):
    if n>len(str):
        return ""
    
    result=""

    for index,char in enumerate(str):
        if index<n-1 :
            result+=char
        if index>=n-1 :
            break

    return result

# using an inbuilt method

def removeCharacters2(str,n):
    if n>len(str):
        return ""
    
    return str[:n-1]

str=input("Enter the string : ")
n=int(input("Enter the number of characters to remove : "))

result=removeCharacter(str,n)

print(f"After removing characters : {result}")
