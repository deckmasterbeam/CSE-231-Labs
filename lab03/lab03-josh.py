exit_condition = 0

while exit_condition == 0:
    input_str = input("Input a word (Input 'quit' to quit): ")
    input_str = input_str.lower()
    
    if input_str == "quit":
        exit_condition = 1
    else:
        vowel_spot = 0    
        exit_condition2 = 0
        while exit_condition2 == 0:
            if (input_str[vowel_spot] == "a"):
                exit_condition2 = 1
            elif (input_str[vowel_spot] == "e"):
                exit_condition2 = 1
            elif (input_str[vowel_spot] == "i"):
                exit_condition2 = 1
            elif (input_str[vowel_spot] == "o"):
                exit_condition2 = 1
            elif (input_str[vowel_spot] == "u"):
                exit_condition2 = 1
            else:
                vowel_spot += 1
        
        if vowel_spot == 0:
            print(input_str," translates to ",input_str+"way")
        else:
            print(input_str," translates to  ",input_str[vowel_spot:]+input_str[:vowel_spot]+"ay")
        