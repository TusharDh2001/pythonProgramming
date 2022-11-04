port textwrap
'''
def wrap(string, max_width):
    k=0
    for i in string:
        if i != None:
            print(i,end='')
        elif i==None:
            return
        k=k+1
        if(k%4==0):
            print()
    return
'''
def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
