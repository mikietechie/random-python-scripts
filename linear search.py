xli = ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'y', 'v']
print(xli)
def linear_search():
    x = input('Enter letter to be searched   :')
    i = 0
    while i<len(xli):
        if xli[i] == x:
            print('item found')
            i=len(xli)
        else:
            i = i+1
            if i== len(xli):
                print('item not found')
linear_search()
