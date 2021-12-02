input = int(input("input: "))
index = 2

for bawah in range (1,input+1):
    for samping in range (1,2*input) :
        if bawah+samping == input+1 or samping-bawah == input-1:
            print ("*", end="")
        elif bawah == input and samping != index:
            print ("*",end="")
            index = index+2
        else:
            print (end=" ")
    print ()