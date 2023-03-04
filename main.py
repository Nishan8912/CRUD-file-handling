import os

z = 1

while (True):
    print('\n 1. Add Record')
    print('\n 2. Display All Record')
    print('\n 3. Search Student Record by Name')
    print('\n 4. Search Student Record by RollNo')
    print('\n 5. Delete Student Record by Name')
    print('\n 6. Update Student Record')
    print('\n 7. Exit')

    choice = int(input("Enter your choice: "))
    if (choice == 7):
        break
    elif(choice == 1):
        print('\nEnter Student Detail\n')
        name = input('Enter Name: ')
        rollno = input('Enter RollNo: ')
        grade = input('Enter Student Grade: ')
        Fees = input('Enter Student Fees: ')
        gpa = input('Enter student GPA: ')
        file = open('studentfile.txt', 'a')
        file.write(name+"-"+rollno+"-"+grade+"-"+Fees+"-"+gpa+"\n")
        file.close()
    elif(choice == 2):
        print('\n\n List of Present Student Records\n\n')
        print('Name-ROllNO-Grade-Fees-GPA')
        file = open('studentfile.txt', 'r')
        while(True):
            d = file.readline()
            l = len(d)
            if(l == 0):
                break
            print(d.strip())
        file.close()
    elif(choice == 3):
        search = input('Enter student Name to Search: ')
        file = open('studentfile.txt', 'r')
        flag = 0
        while(True):
            t = file.readline()
            l = len(t)
            if l == 0:
                break
            g = t.split("-")
            if (g[0] == search):
                print("\n Record Found")
                print('Name is : ', g[0])
                print('RollNo is : ', g[1])
                print('Grade is : ', g[2])
                print('Fees is : ', g[3])
                print('GPA is : ', g[43])
                flag = 1
                break
        if flag == 0:
            print('\n Record Not Found.')
        file.close()
    elif(choice == 4):
        search = input('Enter student RollNo to Search: ')
        file = open('studentfile.txt', 'r')
        flag = 0
        while(True):
            t = file.readline()
            l = len(t)
            if l == 0:
                break
            g = t.split("-")
            if (g[1] == search):
                print("\n Record Found")
                print('Name is : ', g[0])
                print('RollNo is : ', g[1])
                print('Grade is : ', g[2])
                print('Fees is : ', g[3])
                print('GPA is : ', g[4])
                flag = 1
                break
        if flag == 0:
            print('\n Record Not Found.')
        file.close()
    elif(choice == 5):
        search = input("\n Enter Student Name to Remove Record: ")
        file = open('studentfile.txt', 'r')
        temp = open('temp.txt', 'w')
        h = 0
        flag = 0
        while(True):
            read = file.readline()
            l = len(read)
            if(l == 0):
                break
            g = read.split('-')
            if(g[0] != search):
                temp.write(read)
            if(g[0] == search):
                h = 1
        file.close()
        temp.close()
        if(h == 1):
            print("\n Record deleted successfully!")
            os.remove('studentfile.txt')
            os.rename('temp.txt', 'studentfile.txt')
        elif(h == 0):
            print('\n Record not Found! Unsuccessful Deletion Operation.')
    elif(choice == 6):
        h = 0
        search = input('\n Enter Student Name to Update: ')
        file = open('studentfile.txt', 'r')
        temp = open('temp.txt', 'w')
        flag = 0
        while(True):
            t = file.readline()
            l = len(t)
            if(l == 0):
                break
            g = t.split('-')
            if (g[0] == search):
                print('\n Current Detail is \n', t)
                print("-------------------------------")
                newroll = input(
                    'Want to change rollNo? Enter new detail or Press Enter to Continue: ')
                newgrade = input(
                    'Want to change Grade? Enter new detail or Press Enter to Continue: ')
                newFees = input(
                    'Want to change Fees? Enter new detail or Press Enter to Continue: ')
                newGPA = input(
                    'Want to change GPA? Enter new detail or Press Enter to Continue: ')
                if (len(newroll) == 0):
                    newroll = g[1]
                if (len(newgrade) == 0):
                    newgrade = g[2]
                if (len(newFees) == 0):
                    newFees = g[3]
                if (len(newGPA) == 0):
                    newGPA = g[4]
                temp.write('\n'+g[0]+"-"+newroll+'-' +
                           newgrade+'-'+newFees+'-'+newGPA+'\n')
            else:
                temp.write(t)
        file.close()
        temp.close()
        if(h == 1):
            print('\n Record Updated Successfully!')
            os.remove('studentfile.txt')
            os.rename('temp.txt', 'studentfile.txt')
        elif(h == 0):
            print('\n No such Record exist for the Updation!')
