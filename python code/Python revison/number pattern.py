# Function 
def numpat(n):
    
    # initialising starting number 
    num = 1

    # outer loop of rows
    for i in range(0, n):
    
        # re assigning num
        num = 1
    
        # inner loop of columns
            
        for j in range(0, i+1):
        
                # printing number
            print(num, end=" ")
        
            # incrementing number at each column
            num = num + 1
    
        # ending line after each row
        print("")

n = 5
numpat(n)
