
def delete_contacts():
    Heading = ['Name', 'Email Address', 'Mobile Number', 'Address']
    mobile = input("\nEnter the Mobile Number to Delete a Contact : ")
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
        print(mobile_numbers)
        x=0
        for i in mobile_numbers:
            if mobile==i:
                x=mobile_numbers.index(mobile)
                print(f"\nAlert!! This information will be deleted \n")
                print("*********************************************************************************")
                print(f"Contact Information => {Heading[0]} : {all_contacts[x][0]},{Heading[1]} :{all_contacts[x][1]} and {Heading[2]} :{all_contacts[x][2]}")
                print("**********************************************************************************")
                yn = input("Are you sure (Y/N) : ".lower())
                if yn == "y":
                    m = all_contacts.pop(x)
                    with open("all_contacts.csv", "w+", newline='') as myfile:
                        change_file = csv.writer(myfile)
                        for i in range(len(all_contacts)):
                            change_file.writerow(all_contacts[i])
                        myfile.close()
                    print(m, ".... is deleted")
              
             
                else:
                    print("Wrong input, Try Again (Y/N)")
                  
    file.close()
    

    
   
        
        
        


