
print("WELCOME TO THE PATTERN GENERATOR")
print("menu:\n1.right angled triangle \n2.inverted right angled triangle\n3.pyramid\n4inverted pyramid\n5.diamond pattern\n6.triangle aligned to right\n7.sand glass\n8.hollow pyramid\n9.hollow diamond\n10.number pyramid\n")
pat=input("enter your choice of pattern:\t")
match pat:
    case "1":
        rows=5
        for i in range(1,rows+1):
            print("*" * i)
    case "2":
        rows=5
        for i in range(rows,0,-1):
            print("*" * i)
    case "3":
        rows=5
        for i in range(1, rows+1):
            print(" " * (rows-i)+ "*" * (2*i-1))
    case "4":
        rows=5
        for i in range(rows,0,-1):
            print(" " * (rows-i)+"*" * (2*i-1))
    case "5":
        rows=5
        for i in range(1,rows+1):
            print(" "*(rows-i)+"*"*(2*i-1))
        for i in range(rows-1,0,-1):
            print(" "*(rows-i)+ "*"*(2*i-1))
    case "6":
        rows=5
        for i in range(1,rows+1):
            print(" "*(rows-i)+"*"*i)
    case "7":
        rows=5
        for i in range(rows,0,-1):
            print(" "*(rows-i)+"*"*(2*i-1))
        for i in range(2, rows+1):
            print(" "*(rows-i)+"*"*(2*i-1))
    case "8":
        rows=5
        for i in range(1,rows+1):
            if i==1 or i==rows:
                print(" "*(rows-i)+"*"*(2*i-1))
            else:
                print(" "*(rows-i)+"*"+" "*(2*i-3)+"*")
    case "9":
        rows=5
        for i in range(1,rows+1):
            if i==1:
                print(" "*(rows-i)+"*")
            else:
                print(" "*(rows-i)+"*"+" "*(2*i-3)+"*")
        for i in range(rows-1,0,-1):
            if i==1:
                print(" "* (rows-i)+"*")
            else:
                print(" "*(rows-i)+"*"+" "*(2-i-3)+"*")
    case "10":
        rows=5
        for i in range(1, rows+1):
            print(" "*(rows-i)+" ".join(str(j) for j in range(1,i+1)))
    case _:
        print("invalid choice")   