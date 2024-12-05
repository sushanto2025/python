def validate_mobile(mobile):
    import csv
    all_contacts = []
    with open('all_contacts.csv', 'r') as file:
        myfile = csv.reader(file)
        for row in myfile:
            all_contacts.append(row)
        mobile_numbers=[]
        msg="\nMobile not Found\n"
        for i in all_contacts:
            mobile_numbers.append(i[2])
        
        for i in mobile_numbers:
            if mobile==i:
                msg=f"\nMobile is allready used \n"
                return False
            return True              
    file.close()

def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False
            
def add_contacts():
        name = input("Enter Name : ").title()
        
        while True:
            user_email=input("Enter email :")
            if validate_email(user_email):
                print("Valid Email")
                break
            else:
                print("Invalid Email. Please Check Format")

        while True:
            try:
                mobile = int(input("Enter Mobile Number: "))
            except ValueError:
                print("Mobile number must be integer")

            if validate_mobile(mobile):
                break
            

        address=input("Enter Address :")
        


        import csv
        with open('all_contacts.csv','a', newline='') as myfile:
            myfilewriter=csv.writer(myfile)
            myfilewriter.writerow([name,user_email,mobile,address])
            print("\nContact info added successfully\n")
        myfile.close()
    

