file_name = input("Enter a file name: ")
fp = open(file_name)

def make_list(file_pointer):
    main_list = []
    for line in file_pointer:
        temp = line.split()
        temp[2], temp[3] = int(temp[2]), int(temp[3])
        exam_average = (temp[2] + temp[3])/2
        temp.append(exam_average)
        main_list.append(tuple(temp))
    return main_list

def find_average(master_list, spot):
    ave_sum = 0
    for line in master_list:
        ave_sum += line[spot]
    average = ave_sum/len(master_list)
    return average

def display(master_list, ave1, ave2):
    print("{:<20}{:<8}{:<8}{:<10}".format("Name", "Exam 1", "Exam 2", \
    "Average"))
    for line in master_list:
        print("{:<20}".format(line[0]+" "+line[1]), end="")
        print("{:<8}{:<8}{:<8}".format(line[2], line[3], line[4]))
    print("\n{:<20}{:<8}{:<8}".format("Average for Exams:", ave1, ave2))

student_list = make_list(fp)

exam1_ave = find_average(student_list, 2)
exam2_ave = find_average(student_list, 3)
display(student_list, exam1_ave, exam2_ave)