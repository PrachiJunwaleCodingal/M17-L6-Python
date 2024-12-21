#ACP-Checking Alphabets

x = input("Enter character:")   
if len(x)>1:
    print("\nWrite only 1 character to check")
else:
    if (x>='a' and x<='z' ) or (x>='A' and x<='Z'):
        print(x+ " is alphabet.")
    else:
        print(x+ " is not alphabet.")