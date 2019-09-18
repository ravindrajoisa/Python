try:
    fn = open('fryfile.txt', 'w')
    fn.write('testing')
finally:
    print('Knock Knock')
    fn.close()
