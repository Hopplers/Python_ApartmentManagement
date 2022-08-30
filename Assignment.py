def login():
    flag = True
    while flag:
        print("Log-in Page")
        time.sleep(0.5)
        username = input("Username: ")
        userpw = finduserpw()
        for data in userpw:
            if data[0] == username:
                print("**Forgot password? Enter X in password to change your password!**")
                password = input("Password: ")
                if password.lower() == "x":
                    passwordreset(username)
                    break
                else:
                    if data[1] == password:
                            auditlogin(username)
                            amainmenu(username)
                            pass
                    else:
                        print("Incorrect password, please try again")
                    break
        else:
            print("Incorrect username, please try again")
            continue

def auditlogin(username):
    dnt = currentdatetime()
    data = (dnt + username + " has log in ")
    with open("audit", "a") as record:
        record.write(data + "\n")

def currentdatetime():
    now = datetime.now()
    dnt = now.strftime("[%d/%m/%Y %H:%M:%S] ")
    return dnt

def finduserpw():
    userpw = []
    with open("userpw", "r") as record:
        for line in record:
            item = line.strip().strip(",").split(",")
            userpw.append(item)
        return userpw

def passwordreset(key):
    print("Reset Password")
    time.sleep(0.5)
    userpw = finduserpw()
    for data in userpw:
        while data[0] == key:
            newpw = input("New Password: ")
            passwordstrength(newpw)
            option = input("Do you want to save the new password (1) or change another new password (2) ?\n")
            if option == "1":
                data[1] = newpw
                userpwreplace(userpw)
                print("The password have been changed!")
                time.sleep(0.5)
                print("Redirecting you to Main Menu")
                time.sleep(0.5)
                break
            if option == "2":
                pass

def passwordstrength(password):
    print(password + "hello")

def userpwreplace(newdata):
    with open("userpw", "w") as records:
        for record in newdata:
            for item in record:
                records.write(item + ",")
            records.write("\n")

def amainmenu(username):  # main menu for admin
    print(username, ", Welcome to D&J Tenant Management System")
    flag = True
    i = 1
    while flag:
        if i == 1:
            i = amainmenuselect()

        if i == 2:
            option = input("Which type of New Data?\n1. New Apartment Data\n2. New Tenant Data\n3. New Payment Data\n4. Return to Main Menu\n")
            if option == "1":
                i = new_apartment_data()
            elif option == "2":
                i = new_tenant_data()
            elif option == "3":
                i = new_payment_data()
            elif option == "4":
                i = 1

        if i == 3:
            option = input("Which Data do you wish to search?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Return to Main Menu\n")
            if option == "1":
                i = view_apartment_data()
            elif option == "2":
                i = view_tenant_data()
            elif option == "3":
                i = view_payment_data()
            elif option == "4":
                i = 1

        if i == 4:
            option = input("Which Data do you wish to modify?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Return to Main Menu\n")
            if option == "1":
                i = modify_apartment_data()
            elif option == "2":
                i = modify_tenant_data()
            elif option == "3":
                i = modify_payment_data()
            elif option == "4":
                i = 1

        if i == 5:
            option = input("Which Data do you wish to delete?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Return to Main Menu\n")
            if option == "1":
                i = remove_apartment_data()
            elif option == "2":
                i = remove_tenant_data()
            elif option == "3":
                i = remove_payment_data()
            elif option == "4":
                i = 1

        if i == 6:
            print("Goodbye!")
            username = "hi"
            auditlogout(username)
            time.sleep(0.5)
            break

def amainmenuselect():  #admin main menu select
    option = int(input("Please Select an Option\n1. Enter New Data\n2. Search Current Available Data\n3. Modify Current Available Data\n4. Delete Current Available Data\n5. Log Out \n"))
    if 6 > option > 0:
        i = option + 1
        return i

def new_apartment_data():  #function for entering new apartment data
    while True:
        file_name = "apartment"
        apartment_data = []
        apartment_no = input("Enter Apartment No.:")
        apartment_square_footage = input("Enter Apartment Square Footage: ")
        rent_amount = input("Enter Rent Amount: ")
        details_apartment = [apartment_no, apartment_square_footage, rent_amount]
        apartment_data.append(details_apartment)
        savedata(file_name, apartment_data, apartment_no)
        option = input("Do you want to enter another apartment data(1), enter another type of new data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 2
            return i
        elif option == "3":
            i = 1
            return i

def savedata(file_name, data, name):
    datatype = file_name
    with open(file_name, "a") as records:
        for record in data:
            for item in record:
                records.write(item + ",")
            records.write("\n")
        print("Data Saved.")
        auditnewdata(datatype, name)

def auditnewdata(datatype,name):
    dnt = currentdatetime()
    data = (dnt + "new " + datatype + " data for " + name + " has been added")
    with open("audit", "a") as record:
        record.write(data + "\n")

def new_tenant_data():  #function for entering new tenant data
    while True:
        file_name = "tenant"
        tenant_data = []
        id_number = input("Enter Tenant ID No.: ")
        full_name = input("Enter Full Name: ")
        gender = input("Enter Gender: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter address: ")
        city = input("Enter City: ")
        job_history = input("Enter Job History: ")
        current_job = input("Enter Current Job: ")
        date_of_acquisition = input("Enter Date of Acquisition: ")
        apartment_no = input("Enter Apartment No.: ")
        details_tenant = [id_number, full_name, gender, phone_number, address, city, job_history, current_job, date_of_acquisition, apartment_no]
        tenant_data.append(details_tenant)
        savedata(file_name, tenant_data, id_number)
        option = input("Do you want to enter another tenant data(1), enter another type of new data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 2
            return i
        elif option == "3":
            i = 1
            return i

def new_payment_data():  #function for entering new payment data
    while True:
        file_name = "payment"
        payment_data = []
        tenant_id = input("Enter Tenant ID No.: ")
        tenant_name = input("Enter Tenant Name: ")
        apartment_no = input("Enter Apartment No.: ")
        amount_paid = input("Enter Amount Paid: ")
        payment_status = input("Enter Payment Status: ")
        details_payment = [tenant_id, tenant_name, apartment_no, amount_paid, payment_status]
        payment_data.append(details_payment)
        savedata(file_name, payment_data, tenant_id)
        option = input("Do you want to enter another payment data(1), enter another type of new data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 2
            return i
        elif option == "3":
            i = 1
            return i

def view_apartment_data():
    while True:
        file_name = "apartment"
        datatype = file_name
        apartment_list = findrecord(file_name)
        apartment_no = input("Which Apartment No.'s Data do you wish to view? (Enter Apartment No.)\n")
        for aprtmnt_data in apartment_list:
            if aprtmnt_data[0] == apartment_no:
                print("The current data available for the Apartment No. ", apartment_no, " is:\n")
                print("Apartment No.            :", aprtmnt_data[0])
                print("Apartment Square Footage :", aprtmnt_data[1])
                print("Rent Amount              :", aprtmnt_data[2], "\n")
                auditsearchdata(datatype, apartment_no)

        option = input("Do you want to search for another apartment data(1), search for another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 3
            return i
        elif option == "3":
            i = 1
            return i

def findrecord(file_name):
    data = []
    with open(file_name, "r") as record:
        for line in record:
            item = line.strip().strip(",").split(",")
            data.append(item)
        return data

def auditsearchdata(datatype,name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been searched")
    with open("audit", "a") as record:
        record.write(data + "\n")

def view_tenant_data():
    while True:
        file_name = "tenant"
        datatype = file_name
        tenant_list = findrecord(file_name)
        tenant_id_number = input("Which Tenant's Data do you wish to view? (Enter Tenant ID No.)\n")
        for tenantdata in tenant_list:
            if tenantdata[0] == tenant_id_number:
                print("Tenant ID No.        :", tenantdata[0])
                print("Full Tenant Name     :", tenantdata[1])
                print("Tenant Gender        :", tenantdata[2])
                print("Tenant Phone Number  :", tenantdata[3])
                print("Tenant Address       :", tenantdata[4])
                print("Tenant City          :", tenantdata[5])
                print("Tenant Job History   :", tenantdata[6])
                print("Tenant Current Job   :", tenantdata[7])
                print("Date of Acquisition  :", tenantdata[8])
                print("Apartment No.        :", tenantdata[9], "\n")
                auditsearchdata(datatype, tenant_id_number)

        option = input("Do you want to search for another Tenant Data(1), search for another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 3
            return i
        elif option == "3":
            i = 1
            return i

def view_payment_data():
    while True:
        file_name = "payment"
        datatype = file_name
        payment_list = findrecord(file_name)
        tenant_id_number = input("Which Payment Data do you wish to view? (Enter Tenant ID No.)\n")
        for paymentdata in payment_list:
            if paymentdata[0] == tenant_id_number:
                print("Tenant ID No.    :", paymentdata[0])
                print("Tenant Name      :", paymentdata[1])
                print("Apartment No.    :", paymentdata[2])
                print("Amount Paid      :", paymentdata[3])
                print("Payment Status   :", paymentdata[4], "\n")
                auditsearchdata(datatype, tenant_id_number)

        option = input("Do you want to search for another Payment Data(1), search for another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 3
            return i
        elif option == "3":
            i = 1
            return i

def modify_apartment_data():
    while True:
        file_name = "apartment"
        record = findrecord(file_name)
        column = input("Which Apartment Data do you wish to Modify? (Enter Apartment No.)\n")
        selection, replacement = showapdata(record, column)
        replacedata(column, record, selection, replacement, file_name)
        option = input("Do you want to continue modifying Apartment Data(1), modify another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 4
            return i
        elif option == "3":
            i = 1
            return i

def showapdata(record, column):
    for data in record:
        while data[0] == column:
            print("The current data available for the Apartment No. you wish to modify is:\n")
            print("1. Apartment No.            : ", data[0])
            print("2. Apartment Square Footage : ", data[1])
            print("3. Rent Amount              : ", data[2], "\n")
            time.sleep(0.5)
            selection = int(input("Which data do you wish to modify?\n"))
            selection -= 1
            replacement = input("What do you want to replace the data with?\n")
            return selection, replacement

def replacedata(column, record, selection, replacement, file_name):
    datatype = file_name
    for data in record:
        if column == data[0]:
            data[selection] = replacement
            auditmodifydata(datatype, data[0])

    with open(file_name, "w") as records:
        for data in record:
            for item in data:
                records.write(item + ",")
            records.write("\n")

    print("Data Modified")

def modify_tenant_data():
    while True:
        file_name = "tenant"
        record = findrecord(file_name)
        column = input("Which Tenant's Data do you wish to Modify? (Enter Tenant ID No.)\n")
        selection, replacement = showtndata(record, column)
        replacedata(column, record, selection, replacement, file_name)
        option = input("Do you want to continue modifying Tenant Data(1), modify another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 4
            return i
        elif option == "3":
            i = 1
            return i

def auditmodifydata(datatype,name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been modify")
    with open("audit", "a") as record:
        record.write(data + "\n")

def showtndata(record, column):
    for data in record:
        while data[0] == column:
            print("The current data available for the Tenant No. you wish to modify is:\n")
            print("1. Tenant ID No.        :", data[0])
            print("2. Full Tenant Name     :", data[1])
            print("3. Tenant Gender        :", data[2])
            print("4. Tenant Phone Number  :", data[3])
            print("5. Tenant Address       :", data[4])
            print("6. Tenant City          :", data[5])
            print("7. Tenant Job History   :", data[6])
            print("8. Tenant Current Job   :", data[7])
            print("9. Date of Acquisition  :", data[8])
            print("10. Apartment No.       :", data[9], "\n")
            time.sleep(0.5)
            selection = int(input("Which data do you wish to modify?\n"))
            selection -= 1
            replacement = input("What do you want to replace the data with?\n")
            return selection, replacement

def modify_payment_data():
    while True:
        file_name = "payment"
        record = findrecord(file_name)
        column = input("Which Payment Data do you wish to Modify? (Enter Tenant ID No.)\n")
        selection, replacement = showpmdata(record, column)
        replacedata(column, record, selection, replacement, file_name)
        option = input("Do you want to continue modifying Payment Data(1), modify another type of data(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i = 4
            return i
        elif option == "3":
            i = 1
            return i

def showpmdata(record, column):
    for data in record:
        while data[0] == column:
            print("The current data available for the Payment you wish to modify is:\n")
            print("1. Tenant ID No.    :", data[0])
            print("2. Tenant Name      :", data[1])
            print("3. Apartment No.    :", data[2])
            print("4. Amount Paid      :", data[3])
            print("5. Payment Status   :", data[4], "\n")
            time.sleep(0.5)
            selection = int(input("Which data do you wish to modify?\n"))
            selection -= 1
            replacement = input("What do you want to replace the data with?\n")
            return selection, replacement

def remove_apartment_data():
    while True:
        file_name = "apartment"
        apartment_record = findrecord(file_name)
        apartment_no = input("Which Apartment Data do you wish to Delete? (Enter Apartment No.)\n")
        for apdata in apartment_record:
            if apdata[0] == apartment_no:
                print("The matching data for", apartment_no, " is found:\n")
                print("Apartment No.            :", apdata[0])
                print("Apartment Square Footage :", apdata[1])
                print("Rent Amount              :", apdata[2], "\n")
                verification = input("Does the data shown matches your findings? If yes, enter 'X'\n")
                if verification.lower() == "x":
                    confirmation = input("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                    if confirmation.lower() == "x":
                        apartment_record.remove(apdata)
                        deletedata(file_name, apartment_record, apdata[0])
        option = input("Do you want to delete other Apartment Data(1), delete another type of data(2) or return to Main Menu(3)?\n")
        if option == 1:
            continue
        elif option == "2":
            i = 5
            return i
        elif option == "3":
            i = 1
            return i

def deletedata(file_name,record, name):
    datatype = file_name
    with open(file_name, "w") as updateData:
        for data in record:
            for item in data:
                updateData.write(item + ",")
            updateData.write("\n")
        print("Data Deleted")
        auditdeletedata(datatype, name)

def auditdeletedata(datatype,name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been deleted")
    with open("audit", "a") as record:
        record.write(data + "\n")

def remove_tenant_data():
    while True:
        file_name = "tenant"
        tenant_record = findrecord(file_name)
        tnid_no = input("Which Tenant's Data do you wish to Delete? (Enter Tenant ID No.)\n")
        for tndata in tenant_record:
            if tndata[0] == tnid_no:
                print("The matching data for", tnid_no, " is found:\n")
                print("1. Tenant ID No.        :", tndata[0])
                print("2. Full Tenant Name     :", tndata[1])
                print("3. Tenant Gender        :", tndata[2])
                print("4. Tenant Phone Number  :", tndata[3])
                print("5. Tenant Address       :", tndata[4])
                print("6. Tenant City          :", tndata[5])
                print("7. Tenant Job History   :", tndata[6])
                print("8. Tenant Current Job   :", tndata[7])
                print("9. Date of Acquisition  :", tndata[8])
                print("10. Apartment No.       :", tndata[9], "\n")
                verification = input("Does the data shown matches your findings? If yes, enter 'X'\n")
                if verification.lower() == "x":
                    confirmation = input("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                    if confirmation.lower() == "x":
                        tenant_record.remove(tndata)
                        deletedata(file_name, tenant_record,tndata[0])
        option = input("Do you want to delete other Tenant Data(1), delete another type of data(2) or return to Main Menu(3)?\n")
        if option == 1:
            continue
        elif option == "2":
            i = 5
            return i
        elif option == "3":
            i = 1
            return i

def remove_payment_data():
    while True:
        file_name = "payment"
        payment_record = findrecord(file_name)
        tnid_no = input("Which Tenant's Payment Data do you wish to Delete? (Enter Tenant ID No.)\n")
        for pmdata in payment_record:
            if pmdata[0] == tnid_no:
                print("The matching data for", tnid_no, " is found:\n")
                print("1. Tenant ID No.    :", pmdata[0])
                print("2. Tenant Name      :", pmdata[1])
                print("3. Apartment No.    :", pmdata[2])
                print("4. Amount Paid      :", pmdata[3])
                print("5. Payment Status   :", pmdata[4], "\n")
                verification = input("Does the data shown matches your findings? If yes, enter 'X'\n")
                if verification.lower() == "x":
                    confirmation = input("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                    if confirmation.lower() == "x":
                        payment_record.remove(pmdata)
                        deletedata(file_name, payment_record, pmdata[0])
        option = input("Do you want to delete other Payment Data(1), delete another type of data(2) or return to Main Menu(3)?\n")
        if option == 1:
            continue
        elif option == "2":
            i = 5
            return i
        elif option == "3":
            i = 1
            return i

def auditlogout(username):
    dnt = currentdatetime()
    data = (dnt + username + " has log out ")
    with open("audit", "a") as record:
        record.write(data + "\n")

from datetime import datetime
import time
login()
