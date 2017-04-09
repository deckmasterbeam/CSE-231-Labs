def build_map(in_file, scores_dic):
    line_counter = 0
    line_list = []
    for line_counter, line in enumerate(in_file):
        if line_counter != 0:
            line_list = line.split()
            for word in line_list:            
                word = word.strip().lower()
            if line_list[0] not in scores_dic:
                scores_dic[line_list[0]] = 0
            scores_dic[line_list[0]] += int(line_list[1])
    return scores_dic

def dic_sort(scores_dic):
    sorted_list = []
    for item in scores_dic:
        sorted_list.append((item, scores_dic[item]))
    sorted_list = sorted(sorted_list, key=str)
    return sorted_list

def display_dic(sorted_list):
    print("{:<10}{:<6}".format("Name", "Total"))    
    for item in sorted_list:
        print("{:<10}{:<6}".format(item[0], item[1]))
                
scores_dic = {}
fp1 = open(input("Enter a file name: "), "r")
fp2 = open(input("Enter another file name: "))

scores_dic = build_map(fp1, scores_dic)
scores_dic = build_map(fp2, scores_dic)

sorted_list = dic_sort(scores_dic)

display_dic(sorted_list)