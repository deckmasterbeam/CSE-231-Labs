def open_file(file_name):
    '''Opens up a file from a user input, reprompts if file isn't found 
    Value: name of file
    Returns: file pointer'''
    while True:
        try:
            fp = open(file_name)
            return fp
        except FileNotFoundError:
            print("Error! File Not Found.")
            file_name = input("Enter a file name: ")
            
def read_file(fp):
    main_dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    total = 0
    for line in fp:
        line = line.strip()
        if line[0] == "0":
            continue
        first_digit = line[0]
        main_dict[first_digit] += 1
        total += 1
        
    return main_dict, total
    
def percentages(main_dict, total):
    percentages_list = [0,0,0,0,0,0,0,0,0,0,0]
    for key in main_dict:
        percentages_list[int(key)] = (main_dict[key]/total)*100
    return percentages_list
    
def display(percentages_list):
    benford_list = ["(30.1%)","(17.6%)", "(12.5%)", "( 9.7%)", "( 7.9%)", \
    "( 6.7%)", "( 5.8%)", "( 4.1%)", "( 4.6%)"]
    loop_counter = 1    
    
    print("{:>7} {:>7} {:>7}".format("Digit", "Percent", "Benford"))
    while loop_counter < len(percentages_list)-1:
        print("{:>7}: {:>7.1f}% {:>7}".format(loop_counter, percentages_list[loop_counter], benford_list[loop_counter-1]))
        loop_counter += 1        
         
given_file = input("Enter a file name: ")
pointer = open_file(given_file)
best_dict, total_digits = read_file(pointer)
per_list = percentages(best_dict, total_digits)
display(per_list)