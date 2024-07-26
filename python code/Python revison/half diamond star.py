# Function to print the 
# half diamond star pattern 
def halfDiamondStar(N): 
	
	# Loop to print the upper half 
	# diamond pattern 
	for i in range(N): 

		for j in range(0, i + 1): 
			print("*", end = "") 
		print() 

	# Loop to print the lower half 
	# diamond pattern 
	for i in range(1, N): 

		for j in range(i, N): 
			print("*", end = "") 
		print() 

 
N = 5; 

# Function Call 
halfDiamondStar(N); 



