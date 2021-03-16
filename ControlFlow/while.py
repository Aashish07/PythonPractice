# While loop falls under the category of indefinite iteration. 
# Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance. 

    # # Python program to illustrate 
    # # while loop 
    # count = 0
    # while (count < 3):	 
    #     count = count + 1
    #     print("Hello Geek") 

    # print() 

    # # checks if list still 
    # # contains any element 
    # a = [1, 2, 3, 4] 
    # while a: 
    #     print(a.pop()) 

# -----------------------Single statement while block---------------------------
    # If there are multiple statements in the block that makes up the loop body, they can be separated by semicolons (;).

        # # Python program to illustrate 
        # # Single statement while block 
        # count = 0
        # while (count < 5): count += 1; print("Hello Geek") 

# ------------------------Loop Control Statements----------------------
    # Continue Statement: It returns the control to the beginning of the loop. 

        # # Prints all letters except 'e' and 's' 
        # i = 0
        # a = 'geeksforgeeks'

        # while i < len(a): 
        #     if a[i] == 'e' or a[i] == 's': 
        #         i += 1
        #         continue
        #     print('Current Letter :', a[i]) 
        #     i += 1

    # Break Statement: It brings control out of the loop. 
        # break the loop as soon it sees 'e' 
        # # or 's' 
        # i = 0
        # a = 'geeksforgeeks'

        # while i < len(a): 
        #     if a[i] == 'e' or a[i] == 's': 
        #         i += 1
        #         break
        #     print('Current Letter :', a[i]) 
        #     i += 1

    # Pass Statement: We use pass statement to write empty loops.

        # # An empty loop 
        # a = 'geeksforgeeks'
        # i = 0

        # while i < len(a): 
        # 	i += 1
        # 	pass
        # print('Value of i :', i) 

    # while-else loop 
        # while loop executes the block until a condition is satisfied
        # Note: The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

        # # Python program to demonstrate 
        # # while-else loop 
        # i = 0
        # while i < 4: 
        #     i += 1
        #     print(i) 
        # else: # Executed because no break in for 
        #     print("No Break\n") 

        # i = 0
        # while i < 4: 
        #     i += 1
        #     print(i) 
        #     break
        # else: # Not executed as there is a break 
        #     print("No Break") 





