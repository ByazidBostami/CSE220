#print 1-4
def one_To_four(i):
    if i > 4:
        return 
    else:
        one_To_four(i+1)
        print(i)
one_To_four(1)