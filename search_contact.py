
def search_contact():
    mobile = input("\nEnter the Mobile Number : ")
    import csv
    all_contacts = []
    with open('all_contacts.csv', 'r') as file:
        myfile = csv.reader(file)
        for row in myfile:
            all_contacts.append(row)
        mobile_numbers=[]
        msg="Mobile not Foundn"
        for i in all_contacts:
            mobile_numbers.append(i[2])
        
        for i in mobile_numbers:
            if mobile==i:
                msg="Mobile is allready used" 
                   
    file.close()
    print("_______________________")
    print (msg)
    print("------------------------")
    
           



