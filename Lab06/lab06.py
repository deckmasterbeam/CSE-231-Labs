def file_to_list(file):
    height_list, weight_list, name_list = [], [], []
    line_number = 0
    line = ""
    for line_number,line in enumerate(file):
        temp = 0
        if line_number >= 1:
            temp = str(line[:10])
            name_list.append(temp)
            temp = float(line[12:16])
            height_list.append(temp)
            temp = float(line[24:29])
            weight_list.append(temp)
    return height_list, weight_list, name_list

def minimum(list_local):
    while_counter, minimum_local = 0, 10000000    
    while while_counter < len(list_local):
        if (list_local[while_counter] < minimum_local):
            minimum_local = list_local[while_counter]
        while_counter += 1
    return minimum_local
    
def maximum(list_local):
    while_counter, maximum_local = 0, -10000000    
    while while_counter < len(list_local):
        if (list_local[while_counter] > maximum_local):
            maximum_local = list_local[while_counter]
        while_counter += 1
    return maximum_local

def bmi_calculator(height_list, weight_list):
    while_counter = 0
    bmi_list = []
    temp = 0
    while while_counter < len(height_list):
        temp = weight_list[while_counter]/(height_list[while_counter]**2)
        bmi_list.append(temp)
        while_counter += 1
    return bmi_list
    
def average(list_local):
    while_counter, ave = 0,0
    while while_counter < len(list_local):
        ave += list_local[while_counter]
        while_counter += 1
    ave = ave/len(list_local)
    return ave
    
def display(name_list, height_list, weight_list, bmi_list, height_ave, \
weight_ave, bmi_ave, height_min, weight_min, bmi_min, height_max, weight_max, \
bmi_max):
    index = 0
    print("Name        Height(m)   Weight(kg)   BMI")
    while index <= 7:
        print(name_list[index], " {:.2f}        {:.2f}       {:.2f}"\
        .format(height_list[index], weight_list[index], bmi_list[index]))
        index += 1
    print("")
    print("{:<12}{:<12.2f}{:<12.2f}{:<126.2f}".format("Average",height_ave,\
    weight_ave, bmi_ave))
    print("Max         {:.2f}        {:.2f}       {:.2f}".format(height_max,\
    weight_max, bmi_max))
    print("Min         {:.2f}        {:.2f}       {:.2f}".format(height_min,\
    weight_min, bmi_min))
    
    
list_bmi, list_height, list_name = [], [], []
min_height, min_weight, min_bmi, max_height, max_weight, max_bmi = 0,0,0,0,0,0
ave_weight, ave_height, ave_bmi = 0,0,0
fp = open("data.txt", "r")

list_height, list_weight, list_name = file_to_list(fp)

min_height = minimum(list_height)
min_weight = minimum(list_weight)
max_height = maximum(list_height)
max_weight = maximum(list_weight)

list_bmi = bmi_calculator(list_height, list_weight)
min_bmi = minimum(list_bmi)
max_bmi = maximum(list_bmi)

ave_weight = average(list_weight)
ave_height = average(list_height)
ave_bmi = average(list_bmi)

display(list_name, list_height, list_weight, list_bmi, ave_height, ave_weight,\
ave_bmi, min_height, min_weight, min_bmi, max_height, max_weight, max_bmi)
