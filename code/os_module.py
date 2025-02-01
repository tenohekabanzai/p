import os;

# get the current working directory
print(os.getcwd())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#change current working directory
os.chdir(r'C:\Users\bypt-lenovo2\Desktop\p');
print(os.getcwd())
# list all directories
print(os.listdir())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# create nested directories

#check if folder exists
if not os.path.isdir(r'dir1/dir1_1'):
    #create directory/directories
    os.makedirs('dir1/dir1_1')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# delete directories
if os.path.isdir(r'dir1/dir1_1'):
    os.removedirs('dir1/dir1_1')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

os.rename()