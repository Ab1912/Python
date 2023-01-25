# Nested for loop
'''
*				
*	*			
*	*	*		
*	*	*	*	
*	*	*	*	* 
'''
'''
*	*	*	*	*
*	*	*	*	
*	*	*		
*	*			
*				
'''
'''
ABCDE
ABCDE
ABCDE
ABCDE
'''
for a in range(0,6,1):
    for b in range(a):
        print("*",end="")
    print("")

print('------------------')
for a in range(5,0,-1):
    for b in range(a):
        print('*',end='')
    print('')
print('-------------------')

for a in range(65,70,1): # Ascii range for alphabet(A-Z(65-91),a-z(97-122))
    for b in range(65,70,1):
        print(chr(b),end='') # chr is used for alphabets
    print('')
print('-------------------')