n = int(input("Enter the number of rows"))  
# outer loop represent the number of rows  
for i in range(0, n):  
    # inner loop to represent the number of columns   
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
   
        print()