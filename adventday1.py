def bigboy_file(filename):
    with open(filename, "r") as file:
        content = file.read().replace('\n', '').replace(' ', '').strip()
        
        numbers = []
        i = 0
        while i + 5 <= len(content):
            numbers.append(int(content[i:i+5]))
            i += 5
        
      
        first_list = numbers[::2]  
        second_list = numbers[1::2]  
        
        return first_list, second_list
    
    
first_list, second_list = bigboy_file("adventday1.txt")
first_list.sort()
second_list.sort()

total_diff = []
for i in range(min(len(first_list), len(second_list))):
    summ = abs(first_list[i] - second_list[i])
    total_diff.append(summ)

true_sum = sum(total_diff)

print("The true sum is " , true_sum)


similar_num = []


for j in range(len(first_list)):
    for i in range(len(second_list)):
        if first_list[j] == second_list[i]:
            similar_num.append(first_list[j])



similarSum = sum(similar_num)
print("Similar number sum is " ,similarSum)
