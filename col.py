size = 5
count = 1
string = '.X...OX...OX...OXOO.OX...'
result = 'unknown'

for i in range(len(string)):
    if i + size*4 < size*size:
        if(string[i] == 'X' or string[i] == 'O'):
            for j in range(i, i+size*5,size):
                if count == 5:
                    if string[i] == "X":
                        result = 'Black'
                    if string[i] == "O":
                        result = 'White'
                    break
                if (string[i] == string[j]):
                    count = count + 1
            count = 1
                
print(result)