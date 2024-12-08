my_list_1 = [12, 10, 13, 4, 1, 5]
my_list_2 = [6, 1, 7, 8, 10]

my_list_1.extend(my_list_2)
my_list_1.sort()

print(my_list_1)

length = len(my_list_1)
print(length)

position_of_median = (len(my_list_1)+1)/2
position_of_median = int(position_of_median)

position_of_q1 = (len(my_list_1)+1)/4
position_of_q1 = int(position_of_q1)

position_of_q2 = (len(my_list_1)+1) *3/4
position_of_q2 = int(position_of_q2)

print("Median:", my_list_1[position_of_median-1])
print("Q1:", my_list_1[position_of_q1-1])
print("Q2:", my_list_1[position_of_q2-1])