import os;

path = os.getcwd();
path = path+r"\files";
os.chdir(path)
print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = f"{f_num}_{f_title}{f_ext}"
    os.rename(f,new_name)