def change_contacts():
    import csv
    all_contacts = []
    Heading = ['Name', 'Email Address', 'Mobile Number', 'Address']
    with open('all_contacts.csv', 'r') as file:
        myfile = csv.reader(file)
        for row in myfile:
            all_contacts.append(row)

        edit_record = int(input("\nEnter the Record You Want to Edit =>Serial No. (1-" + str(len(all_contacts)) + ") : "))

        for i in range(len(all_contacts[0])):
            newDatails = input(f"Enter {Heading[i]} : ")
            all_contacts[edit_record - 1][i] = newDatails

        print("\nHere is the Line Going to be Changed bellow:".title())
        print("**********************************************")
        for i in all_contacts[edit_record-1]:
           print(i,end="   ")
        
        
        yn = input("Are you sure (Y/N : )".title())
        if yn.lower() == "y":
            with open("all_contacts.csv", "w+",newline='') as myfile:
                change_file = csv.writer(myfile)
                for i in range(len(all_contacts)):
                    change_file.writerow(all_contacts[i])
            myfile.close()
        elif yn == "n":
            print("Ok, No problem")
        else:
            print("Wrong input, Try Again (Y/N")