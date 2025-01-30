my_list = [0,1,2,3,4,5,6,7,8,9]

print (my_list)
print (my_list[-1])
print (my_list[-2])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(my_list[0:4])
print(my_list[3:8])
print(my_list[1:-2])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print entire list
print(my_list[:])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print all values from idx = 2 to second last idx skipping one in b/w
print(my_list[2:-1:2]);
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# no values printed as increment in left direction pointer makes out of bounds
print(my_list[2:-1:-1]);
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start from last indexx and print till index 2+1 ie 3
print(my_list[-1:2:-1]);
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# reverse printing the list
print(my_list[::-1]);
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# printing the list
print(my_list[::1]);
