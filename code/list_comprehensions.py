nums = [1,2,3,4,5,6,7,8,9,10]

# l = []
# for i in nums:
#     l.append(i)

sq = map(lambda i : i*i,nums)
l = map(lambda i : i,nums)

cube = [i*i*i for i in nums if i%2 ==0]

print(list(l))
print(list(sq))
print(list(cube))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
tl = [(i,j) for i in "abcd" for j in range(4)];
print(list(tl))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
names = ['Abc','Def',"ghi",'jkl']
age = [10,11,12,13,14,15,16,17];

l2 = zip(names,age);
print(list(l2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
set1 = {i for i in nums};
print(set(set1));
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def gen_func(nums):
    for i in nums:
        yield i*i

mg = gen_func(nums);

ltx = [i for i in mg];
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(ltx)

for i in mg:
    print(i);
    