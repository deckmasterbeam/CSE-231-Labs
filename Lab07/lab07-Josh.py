"""
def open_file():
    exit_bool = False
    while exit_bool != True:
        try:
            file_name = ""
            file_name = input("Enter a file name: ")
            fp = open(file_name)
        except FileNotFoundError:
            print("Error. Please try again")
            continue
        exit_bool = True
    return fp
    
def line_isolate(file_input, line_number):
    line_number_local = 0
    line_contents_local = ""
    for line_number_local,line_contents_local in enumerate(file_input):
        if line_number_local == line_number-1:
            line_contents_local = line_contents_local.split()
            break
    return line_contents_local

file = open_file()
line_1 = line_isolate(file, 1)
print(line_1)
"""

list_1 = [("a",3),("c",1),("b",2)]

list_1 = sorted(list_1)

print(len(list_1))