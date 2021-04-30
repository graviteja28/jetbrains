n = "         "


def pritgrid(n):
    print("---------")
    for i in range(0, 8, 3):
        print("|", end=" ")
        for j in n[i:i + 3]:
            print(j, end=" ")
        print("|")
    print("---------")


def check(n):
    x, y = 0, 0
    if n[0] == n[1] == n[2] == 'X' or n[3] == n[4] == n[5] == 'X' or n[6] == n[7] == n[8] == 'X' or n[0] == n[3] == n[6] == 'X' or n[1] == n[4] == n[7] == 'X' or n[2] == n[5] == n[8] == 'X' or n[0] == n[4] == n[8] == 'X' or n[2] == n[4] == n[6] == 'X':
        x = 1
    if n[0] == n[1] == n[2] == 'O' or n[3] == n[4] == n[5] == 'O' or n[6] == n[7] == n[8] == 'O' or n[0] == n[3] == n[6] == 'O' or n[1] == n[4] == n[7] == 'O' or n[2] == n[5] == n[8] == 'O' or n[0] == n[4] == n[8] == 'O' or n[2] == n[4] == n[6] == 'O':
        y = 1
    if x == 1:
        return 2
    elif y == 1:
        return 3
    else:
        return 4


pritgrid(n)
x = 1
count = 0
n11 = input("Enter the coordinates:\n").split()
if len(n11) == 1:
    n1, n2 = n11[0], "ravi"
else:
    n1, n2 = n11[0], n11[1]
k1 = None
while x != 0:
    if n1.isdigit() and n2.isdigit():
        while x != 0:
            if int(n1) < 4 and int(n2) < 4:
                if int(n1) == 1:
                    k1 = int(n2) - 1
                elif int(n1) == 2:
                    k1 = int(n2) + 2
                elif int(n1) == 3:
                    k1 = int(n2) + 5
                if n[k1] in 'XO':
                    print("This cell is occupied! Choose another one!")
                    n11 = input("Enter the coordinates:\n").split()
                    if len(n11) == 1:
                        n1, n2 = n11[0], "ravi"
                    else:
                        n1, n2 = n11[0], n11[1]
                    break
                if count % 2 == 0:
                    if int(n1) == 1:
                        n = n[:int(n2) - 1] + 'X' + n[int(n2):]
                    elif int(n1) == 2:
                        n = n[:int(n2) + 2] + 'X' + n[int(n2) + 3:]
                    elif int(n1) == 3:
                        n = n[:int(n2) + 5] + 'X' + n[int(n2) + 6:]
                    pritgrid(n)
                else:
                    if int(n1) == 1:
                        n = n[:int(n2) - 1] + 'O' + n[int(n2):]
                    elif int(n1) == 2:
                        n = n[:int(n2) + 2] + 'O' + n[int(n2) + 3:]
                    elif int(n1) == 3:
                        n = n[:int(n2) + 5] + 'O' + n[int(n2) + 6:]
                    pritgrid(n)
                count += 1
                print(count)
                x1 = check(n)
                if x1 == 2:
                    print("X wins")
                    x = 0
                    break
                elif x1 == 3:
                    print("O wins")
                    x = 0
                    break
                elif x1 == 4 and count > 8:
                    print("Draw")
                    x = 0
                    break
                if count > 8:
                    x = 0
                else:
                    n11 = input("Enter the coordinates:\n").split()
                    if len(n11) == 1:
                        n1, n2 = n11[0], "ravi"
                    else:
                        n1, n2 = n11[0], n11[1]
                    break
            else:
                print("Coordinates should be from 1 to 3!")
                n11 = input("Enter the coordinates:\n").split()
                if len(n11) == 1:
                    n1, n2 = n11[0], "ravi"
                else:
                    n1, n2 = n11[0], n11[1]
                break
    else:
        print("You should enter numbers!")
        n11 = input("Enter the coordinates:\n").split()
        if len(n11) == 1:
            n1, n2 = n11[0], "ravi"
        else:
            n1, n2 = n11[0], n11[1]
