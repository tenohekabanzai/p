try:
    f = open('test3.txt')
except Exception as e:
    print(e)
    print('Sorry file does not exist')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finallly..........')