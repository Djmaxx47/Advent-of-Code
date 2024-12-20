conditions = []
update_groups = []
middlenumList = []
incorrect_middle_nums = []

with open(r"C:\Users\Msb12\Downloads\dependencies.txt", "r") as file:
    read = file.read()
    for fsplit in read.strip().split("\n"):
        if "|" in fsplit:
            trueSplit = fsplit.split("|")
            cond1 = int(trueSplit[0])
            cond2 = int(trueSplit[1])
            conditions.append((cond1, cond2))

with open(r"C:\Users\Msb12\Downloads\update_groups.txt", "r") as file2:
    read2 = file2.read()
    lineSplit = read2.strip().split("\n")

    for line in lineSplit:
        if line:
            numbers = [int(x) for x in line.split(",")]
            real = True
            for rule in conditions:
                cond1, cond2 = rule
                if cond1 in numbers and cond2 in numbers:
                    pos_cond1 = numbers.index(cond1)
                    pos_cond2 = numbers.index(cond2)
                    if pos_cond1 > pos_cond2:
                        real = False
                        break
            
            if real == False:
                numbers_list = numbers.copy()
                n = len(numbers_list)
                changes_made = True
                while changes_made:
                    changes_made = False
                    for rule in conditions:
                        before, after = rule
                        if before in numbers_list and after in numbers_list:
                            pos_before = numbers_list.index(before)
                            pos_after = numbers_list.index(after)
                            if pos_before > pos_after:
                                numbers_list[pos_before], numbers_list[pos_after] = numbers_list[pos_after], numbers_list[pos_before]
                                changes_made = True
                
                middle_index = len(numbers_list) // 2
                middle_num = numbers_list[middle_index]
                incorrect_middle_nums.append(middle_num)

print(f"Number of incorrect sequences fixed: {len(incorrect_middle_nums)}")
print(f"Middle numbers from fixed sequences: {incorrect_middle_nums}")
print(f"Sum of middle numbers from fixed sequences: {sum(incorrect_middle_nums)}")
