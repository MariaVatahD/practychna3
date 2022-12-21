word = input("Введіть слово: ")

for word in word:
    if "A" in word:
        for i in range(7):  #A
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

    if "B" in word:
        for i in range(7):  #B
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or i == 2 or j == 3 or j == 4:
                        row = row + "*"   
            print(row)

    if "C" in word:
        for i in range(7):  #C
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 3 or i == 4:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)   

    if "D" in word:
        for i in range(7):  #D
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)       

    if "E" in word:
        for i in range(7):  #E
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 3:
                    if j == 0 or j == 1 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "F" in word:
        for i in range(7):  #F
            row = ""
            for j in range(5):  
                if i == 0:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 3:
                    if j == 0 or j == 1 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " " 
                if i == 6:
                    if j == 0:
                        row = row + "*"
            print(row) 

    if "G" in word:
        for i in range(7):  #G
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 5 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 2:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "H" in word:
        for i in range(7):  #H
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:    
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

    if "I" in word:
        for i in range(7):  #I
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "    
            print(row)

    if "J" in word:
        for i in range(7):  #J
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "    
                if i == 6:
                    if j == 0 or j == 1:
                        row = row + "*"
                    if j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "K" in word:
        for i in range(7):  #K
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 4:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 1 or j == 3 or j == 4:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " "        
            print(row)

    if "L" in word:
        for i in range(7):  #L
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0:    
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

    if "T" in word:
        for i in range(7):  #T
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "O" in word:
        for i in range(7):  #O
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)

    if "U" in word:
        for i in range(7):  #U
            row = ""
            for j in range(5):    
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)

    if "V" in word:
        for i in range(7):  #V
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 6:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3:
                        row = row + " "
            print(row)

    if "M" in word:
        for i in range(7):  #M
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 0 or j == 1 or j == 3 or j == 4 :
                        row = row + "*"
                    if j == 2:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 3:
                        row = row + " "
                    if j == 2 or j == 0 or j == 4:
                        row = row + "*"
                    
            print(row)

    if "P" in word:
        for i in range(7):  #P
            row = ""
            for j in range(5):
                if i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 1 or i == 2:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 0 or i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)

    if "S" in word:
        for i in range(7):  #S
            row = ""
            for j in range(5):
                if i == 0 or i == 3 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)

    if "W" in word:
        for i in range(7):  #W
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 2:
                        row = row + " "  
                    
            print(row)

    if "X" in word:
        for i in range(7):  #X
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 3:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "N" in word:
        for i in range(7):  #N
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 0 or j == 1 or j == 4:
                        row = row + "*"
                    if j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
            print(row)

    if "R" in word:
        for i in range(7):  #R
            row = ""
            for j in range(5):
                if i == 0 or i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
            print(row)

    if "Y" in word:
        for i in range(7):  #Y
            row = ""
            for j in range(5):
                if i == 0 or i == 1:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 2 :
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)

    if "Q" in word:
        for i in range(7):  #Q
            row = ""
            for j in range(5):
                if i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0:
                        row = row + " "
                if i == 6:
                    if j == 1 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 0 or j == 3:
                        row = row + " "
            print(row)

    if "Z" in word:
        for i in range(7):  #Z
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1:
                    if j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 0:
                        row = row + " "
                if i == 2:
                    if j == 3:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 4 or j == 0:
                        row = row + " " 
                if i == 3:
                    if j == 2:
                        row = row + "*"
                    if j == 1 or j == 4 or j == 3 or j == 0:
                        row = row + " "
                if i == 4:
                    if j == 1:
                        row = row + "*"
                    if j == 4 or j == 2 or j == 3 or j == 0:
                        row = row + " "
                if i == 5:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)
