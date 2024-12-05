def view_all_contacts():
    import csv
    all_contacts = []
    space = " "
    print(f"Seriol No{space:<2}Name{space:<22}Email Address{space:<15}Mobile Number{space:<5}Address")
    print("=============================================================================================================")
    with open('all_contacts.csv', 'r',) as file:
        myfile = csv.reader(file)
        i=1
        for row in myfile:
            print(f"{i:<11}{row[0]:<26}{row[1]:<29}{row[2]:<18}{row[3]}")
            i += 1
        print("--------------------------------------------------------------------------------------------------------------")