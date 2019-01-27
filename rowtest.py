size = 5
count = 1
string = 'X...XOXOO..OOOOOXXOX.OX..'
result = 'unknown'

for i in range(len(string)):
    if (string[i] == 'X' or string[i] == "O"):
        if(i+5 <= size*size):
            for j in range(i,i+size,1):
                print(count, string[i])
                if(count == 5):
                    if string[i] == "X":
                        result = 'Black'
                    if string[i] == "O":
                        result = 'White'
                    break
                if(string[i] == string[j]):
                    count = count + 1
            count = 1
        

print(result)