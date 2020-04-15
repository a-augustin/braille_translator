#Student name: Alisha Augustin
#Lab section: ENGR 132-002

braille_table = {"a": [[1, 0], [0, 0], [0, 0]],
                 "b": [[1, 0], [1, 0], [0, 0]],
                 "c": [[1, 1], [0, 0], [0, 0]],
                 "d": [[1, 1], [0, 1], [0, 0]],
                 "e": [[1, 0], [0, 1], [0, 0]],  
                 "f": [[1, 1], [1, 0], [0, 0]],
                 "g": [[1, 1], [1, 1], [0, 0]],
                 "h": [[1, 0], [1, 1], [0, 0]],
                 "i": [[0, 1], [1, 0], [0, 0]],
                 "j": [[0, 1], [1, 1], [0, 0]], 
                 "k": [[1, 0], [0, 0], [1, 0]],
                 "l": [[1, 0], [1, 0], [1, 0]],
                 "m": [[1, 1], [0, 0], [1, 0]],
                 "n": [[1, 1], [0, 1], [1, 0]],
                 "o": [[1, 0], [0, 1], [1, 0]], 
                 "p": [[1, 1], [1, 0], [1, 0]],
                 "q": [[1, 1], [1, 1], [1, 0]],
                 "r": [[1, 0], [1, 1], [1, 0]],
                 "s": [[0, 1], [1, 0], [1, 0]],
                 "t": [[0, 1], [1, 1], [1, 0]], 
                 "u": [[1, 0], [0, 0], [1, 1]],
                 "v": [[1, 0], [1, 0], [1, 1]],
                 "w": [[0, 1], [1, 1], [0, 1]],
                 "x": [[1, 1], [0, 0], [1, 1]],
                 "y": [[1, 1], [0, 1], [1, 1]], 
                 "z": [[1, 0], [0, 1], [1, 1]]} 
def decode (file_name):
    plain_text = ""
    a = open(file_name)
    b = a.read()
    c = b.split("\n")
    TopLine = c[0].split(" ")
    MiddleLine = c[1].split(" ")
    BottomLine = c[2].split(" ")
    for i in range(0,len(TopLine),2):
      top2 = [int(TopLine[i]),int(TopLine[i+1])]
      middle2 = [int(MiddleLine[i]),int(MiddleLine[i+1])]
      bottom2 = [int(BottomLine[i]),int(BottomLine[i+1])]
      letter_to_add = [top2,middle2,bottom2]
      for j in braille_table:
        if braille_table[j] == letter_to_add:
            plain_text = plain_text + j
    return plain_text

def encode (plain_text):
    matrix1 = []
    line1 = ""
    line2 = ""
    line3 = ""
    for i in plain_text:
        matrix1.append(braille_table[i])
    for column in matrix1:
        line1 = line1 + str(column[0][0]) + " " + str(column[0][1]) + " "
        line2 = line2 + str(column[1][0]) + " " + str(column[1][1]) + " "
        line3 = line3 + str(column[2][0]) + " " + str(column[2][1]) + " "
    print()
    print(line1)
    print(line2)
    print(line3)




if __name__ == "__main__":
    
    """ English to Braille"""
    plain_text = input ("Enter plain text: ")
    encode (plain_text)
    
    """Braille to English """
    file_name = input ("Enter file name: ")
    plain_text = decode (file_name)
    print (plain_text)
    

    
