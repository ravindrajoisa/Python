try:
    fn = open('textfun.txt')
    fn.write('testing')
except IOError:
    print('File doesn\'t exist')
else:
    print('All well')
