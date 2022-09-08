def login():
    while True:
        flag = False
        file_name = "userpw"
        print("Log-in Page")
        time.sleep(0.5)
        username = characters_val("Username: ")
        userpw = findrecord(file_name)
        for data in userpw:
            if data[0] == username:
                if data[1] == "":
                    flag = True
                    print("Welcome new user")
                    time.sleep(0.5)
                    while flag:
                        passwrd = noempty_val("As a startup, please insert a desirable password for your account\n")
                        passwordstrength(passwrd)
                        option = options_val("Do you want to save the password(1) or use another password(2)?\n", 2)
                        if option == 1:
                            data[1] = passwrd
                            replacedatatofile(file_name, userpw)
                            print("Password saved!")
                            auditsetup(username)
                            time.sleep(0.5)
                            print("Redirecting you to Log In page")
                            time.sleep(0.5)
                            break
                        elif option == 2:
                            pass
                else:
                    password = noempty_val("Password: ")
                    flag = True
                    if data[1] == password:
                        auditlogin(username)
                        if data[2] == "superadmin":
                            smainmenu(username)
                            break
                        elif data[2] == "admin":
                            amainmenu(username)
                            break
                        elif data[2] == "tenant":
                            tmainmenu(username)
                            break
                    else:
                        print("Incorrect password, please try again")
                        time.sleep(0.5)
                    break
        if not flag:
            print("Incorrect username, please try again")
            time.sleep(0.5)
            continue

def auditsetup(username):
    dnt = currentdatetime()
    data = (dnt + username + " has set up his/her account ")
    with open("audit", "a") as record:
        record.write(data + "\n")

def auditlogin(username):
    dnt = currentdatetime()
    data = (dnt + username + " has log in ")
    with open("audit", "a") as record:
        record.write(data + "\n")

def currentdatetime():
    now = datetime.now()
    dnt = now.strftime("[%d/%m/%Y %H:%M:%S] ")
    return dnt

def smainmenu(username):  # main menu for super admin
    status = "superadmin"
    print(username, ", Welcome to D&J Tenant Management System\n")
    time.sleep(0.5)
    i = 1
    while True:
        if i == 1:
            i = smainmenuselect()

        elif i == 2:
            i = view_audit_log()

        elif i == 3:
            i = new_user(status, None)

        elif i == 4:
            i = userpasswordreset(status)

        elif i == 5:
            print("Goodbye!")
            auditlogout(username)
            time.sleep(0.5)
            break


def smainmenuselect():
    option = options_val("Please select an option\n1. View Audit Log\n2. Add New Admin\n3. Change Username or Password\n4. Log out\n", 4)
    i = option + 1
    return i

def view_audit_log():
    file_name = "audit"
    record = findrecord(file_name)
    print("These are the recent 20 records in audit log:\n")
    for data in record[-20:]:
        print(data[0])
    random = noempty_val("\nEnter anything to continue\n")
    print("Redirecting you to Main Menu")
    i = 1
    return i

def new_user(status,username):
    while True:
        position = None
        file_name = "userpw"
        if status == "superadmin":
            position = "admin"
            username = characters_val("Enter the new Username you want to create\n")
        elif status == "admin":
            position = "tenant"
        records = findrecord(file_name)
        for lines in records:
            if lines[0] == username:
                print("This username has been taken, please enter another username")
                time.sleep(0.5)
                break
        else:
            data = []
            details = [username, "", position]
            data.append(details)
            savedata(file_name, data, username, position)
            i = 1
            return i

def amainmenu(username):  # main menu for admin
    status = "admin"
    print(username, ", Welcome to D&J Tenant Management System\n")
    time.sleep(0.5)
    i = 1
    while True:
        if i == 1:
            i = amainmenuselect()

        elif i == 2:
            option = options_val("Which type of New Data?\n1. New Apartment Data\n2. New Tenant Data\n3. New Payment Data\n4. Return to Main Menu\n", 4)
            if option == 1:
                i = new_apartment_data()
            elif option == 2:
                i = new_tenant_data(status)
            elif option == 3:
                i = new_payment_data()
            elif option == 4:
                i = 1

        elif i == 3:
            option = options_val("Which Data do you wish to search?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Payment Status\n5. Return to Main Menu\n", 5)
            if option == 1:
                i = view_apartment_data()
            elif option == 2:
                i = view_tenant_data()
            elif option == 3:
                i = view_payment_data()
            elif option == 4:
                i = viewpaymentstatus()
            elif option == 5:
                i = 1

        elif i == 4:
            option = options_val("Which Data do you wish to modify?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Return to Main Menu\n", 4)
            if option == 1:
                i = modify_apartment_data()
            elif option == 2:
                i = modify_tenant_data()
            elif option == 3:
                i = modify_payment_data()
            elif option == 4:
                i = 1

        elif i == 5:
            option = options_val("Which Data do you wish to delete?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Return to Main Menu\n", 4)
            if option == 1:
                i = remove_apartment_data()
            elif option == 2:
                i = remove_tenant_data()
            elif option == 3:
                i = remove_payment_data()
            elif option == 4:
                i = 1

        elif i == 6:
            i = userpasswordreset(status)

        elif i == 7:
            print("Goodbye!")
            auditlogout(username)
            time.sleep(0.5)
            break

def amainmenuselect():  #admin main menu select
    option = options_val("Please select an option\n1. Enter New Data\n2. Search Current Available Data\n3. Modify Current Available Data\n4. Delete Current Available Data\n5. Change Username or Password\n6. Log Out \n", 6)
    i = option + 1
    return i

def tmainmenu(username):
    status = "tenant"
    print(username, ", Welcome to D&J Tenant Management System\n")
    i = 1
    while True:
        if i == 1:
            i = tmainmenuselect()

        elif i == 2:
            option = options_val("Which Data do you wish to search?\n1. Apartment Data\n2. Tenant Data\n3. Payment Data\n4. Payment Status\n5. Return to Main Menu\n", 5)
            if option == 1:
                i = view_apartment_data()
            elif option == 2:
                i = view_tenant_data()
            elif option == 3:
                i = view_payment_data()
            elif option == 4:
                i = viewpaymentstatus()
            elif option == 5:
                i = 1

        elif i == 3:
            i = userpasswordreset(status)

        elif i == 4:
            print("Goodbye!")
            auditlogout(username)
            time.sleep(0.5)
            break

def tmainmenuselect():
    option = options_val("Please select an option\n1. Search Current Available Data\n2. Change Username or Password\n3. Log Out \n", 3)
    i = option + 1
    return i


def new_apartment_data():  #function for entering new apartment data
    while True:
        file_name = "apartment"
        apartment_data = []
        apartment_no = noempty_val("Enter Apartment No.:")
        if isAvailable(file_name, 0, apartment_no):
            print("This data has already been added, enter other data")
        else:
            date_of_acquisition = date_val("Enter Date of Acquisition(DD/MM/YY): ")
            apartment_square_footage = numbers_val("Enter Apartment Square Footage: ")
            rent_amount = numbers_val("Enter Rent Amount: ")
            details_apartment = [apartment_no, date_of_acquisition, apartment_square_footage, rent_amount]
            apartment_data.append(details_apartment)
            savedata(file_name, apartment_data, apartment_no, "")
            option = options_val("Do you want to enter another apartment data(1), enter another type of new data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 2
                return i
            elif option == 3:
                i = 1
                return i

def isAvailable(file_name, position, text):
    data = text
    records = findrecord(file_name)
    for lines in records:
        if lines[position] == data:
            return True
    return False

def savedata(file_name, data, name, status):
    datatype = file_name
    with open(file_name, "a") as records:
        for record in data:
            for item in record:
                records.write(item + ",")
            records.write("\n")
        if datatype != "userpw" and datatype != "paymentstatus":
            auditnewdata(datatype, name)
            print("Data Saved.")
            time.sleep(0.5)
        elif datatype == "userpw":
            auditnewuser(status, name)
            print("New username, " + name + " is created")
            time.sleep(0.5)
        elif datatype == "paymentstatus":
            auditpaystatus(name)
            print("Payment Status updated")
            time.sleep(0.5)


def auditnewdata(datatype, name):
    dnt = currentdatetime()
    data = (dnt + "new " + datatype + " data for " + name + " has been added")
    with open("audit", "a") as record:
        record.write(data + "\n")

def auditnewuser(status, name):
    dnt = currentdatetime()
    data = (dnt +"new user " + name + " has been added as " + status)
    with open("audit", "a") as record:
        record.write(data + "\n")

def auditpaystatus(name):
    dnt = currentdatetime()
    data = (dnt + "payment status for " + name + " has been updated")
    with open("audit", "a") as record:
        record.write(data + "\n")

def new_tenant_data(status):  #function for entering new tenant data
    while True:
        file_name = "tenant"
        tenant_data = []
        newnumb = newnumbgen("tenant_count")
        id_number = "TN" + newnumb
        full_name = characters_val("Enter Full Name: ")
        if isAvailable(file_name, 1, full_name):
            print("The data for " + full_name + " has already been added, please enter other name")
            time.sleep(0.5)
            continue
        else:
            gender = characters_val("Enter Gender: ")
            phone_number = numbers_val("Enter Phone Number: ")
            address = noempty_val("Enter address: ")
            city = characters_val("Enter City: ")
            job_history = characters_val("Enter Job History: ")
            current_job = characters_val("Enter Current Job: ")
            while True:
                apartment_no = noempty_val("Enter Apartment No.: ")
                if not isAvailable("apartment", 0, apartment_no):
                    print("This Apartment no. does not exist, please re-enter the Apartment no.")
                    time.sleep(0.5)
                    continue
                else:
                    date_of_rent = date_val("Enter Date of Rent(DD/MM/YY): ")
                    details_tenant = [id_number, full_name, gender, phone_number, address, city, job_history, current_job, apartment_no, date_of_rent]
                    tenant_data.append(details_tenant)
                    savedata(file_name, tenant_data, id_number, "")
                    new_user(status, full_name)
                    option = options_val("Do you want to enter another tenant data(1), enter another type of new data(2) or return to Main Menu(3)?\n", 3)
                    if option == 1:
                        break
                    elif option == 2:
                        i = 2
                        return i
                    elif option == 3:
                        i = 1
                        return i

def newnumbgen(file_name):
    lines = fileline(file_name)
    newnumb = str(lines + 1)
    with open(file_name, "a") as records:
        records.write(newnumb + "\n")
    return newnumb

def fileline(file_name):
    lines = 0
    with open(file_name, "r") as records:
        for line in records:
            lines += 1
    return lines

def new_payment_data():  #function for entering new payment data
    while True:
        file_name = "payment"
        payment_data = []
        newnumb = newnumbgen("payment_count")
        payment_id = "PM" + newnumb
        tenant_id = nosymbols_val("Enter Tenant ID No.: ")
        if not isAvailable("tenant", 0, tenant_id):
            print("This Tenant ID no. does not exist, please re-enter the Tenant ID no.")
            time.sleep(0.5)
            continue
        else:
            while True:
                apartment_no = noempty_val("Enter Apartment No.: ")
                if not isAvailable("apartment", 0, apartment_no):
                    print("This Apartment No. does not exist, please re-enter the Apartment No.")
                    time.sleep(0.5)
                    continue
                else:
                    amount_paid = numbers_val("Enter Amount Paid: ")
                    payment_month = month_val("Enter Payment Month (MM/YY): ")
                    details_payment = [payment_id, tenant_id, apartment_no, amount_paid, payment_month]
                    payment_data.append(details_payment)
                    savedata(file_name, payment_data, tenant_id, "")
                    paymentstatus(payment_month, tenant_id, apartment_no, amount_paid)
                    option = options_val("Do you want to enter another payment data(1), enter another type of new data(2) or return to Main Menu(3)?\n", 3)
                    if option == 1:
                        break
                    elif option == 2:
                        i = 2
                        return i
                    elif option == 3:
                        i = 1
                        return i

def paymentstatus(payment_month, tenant_id, apartment_no, amount_paid):
    flag = False
    data = []
    rentalfee = None
    file_name = "paymentstatus"
    paystatus_records = findrecord(file_name)
    apartment_records = findrecord("apartment")
    for lines in apartment_records:
        while apartment_no == lines[0]:
            rentalfee = lines[3]
            break

    for lines in paystatus_records:
        while payment_month == lines[0] and tenant_id == lines[1] and apartment_no == lines[2]:
            total_paid = int(lines[4]) + int(amount_paid)
            lines[4] = str(total_paid)
            if int(lines[4]) >= int(lines[3]):
                lines[5] = "paid"
            else:
                pass
            replacedatatofile(file_name, paystatus_records)
            auditpaystatus(tenant_id)
            print("Payment Status updated")
            time.sleep(0.5)
            flag = True
            break

    if not flag:
        if int(amount_paid) >= int(rentalfee):
            paymentstatus = "paid"
        else:
            paymentstatus = "unpaid"
        details = (payment_month, tenant_id, apartment_no, rentalfee, amount_paid, paymentstatus)
        data.append(details)
        savedata(file_name,data, tenant_id,"")

def view_apartment_data():
    while True:
        flag = False
        file_name = "apartment"
        datatype = file_name
        apartment_list = findrecord(file_name)
        apartment_no = noempty_val("Which Apartment No.'s Data do you wish to view? (Enter Apartment No.)\n")
        for aprtmnt_data in apartment_list:
            if aprtmnt_data[0] == apartment_no:
                print("The current data available for the Apartment No. ", apartment_no, " is:\n")
                print("Apartment No.            :", aprtmnt_data[0])
                print("Date of Acquisition.     :", aprtmnt_data[1])
                print("Apartment Square Footage :", aprtmnt_data[2])
                print("Rent Amount              :", aprtmnt_data[3], "\n")
                auditsearchdata(datatype, apartment_no)
                flag = True
        if flag:
            option = options_val("Do you want to search for another apartment data(1), search for another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 3
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def findrecord(file_name):
    record = []
    with open(file_name, "r") as records:
        for line in records:
            item = line.strip().strip(",").split(",")
            record.append(item)
        return record

def auditsearchdata(datatype, name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been searched")
    with open("audit", "a") as record:
        record.write(data + "\n")

def view_tenant_data():
    while True:
        flag = False
        file_name = "tenant"
        datatype = file_name
        tenant_list = findrecord(file_name)
        tenant_id_number = nosymbols_val("Which Tenant's Data do you wish to view? (Enter Tenant ID No.)\n")
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
                print("Apartment No.        :", tenantdata[8])
                print("Date of Rent         :", tenantdata[9], "\n")
                auditsearchdata(datatype, tenant_id_number)
                flag = True

        if flag:
            option = options_val("Do you want to search for another Tenant Data(1), search for another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 3
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def view_payment_data():
    while True:
        flag = False
        file_name = "payment"
        datatype = file_name
        payment_list = findrecord(file_name)
        tenant_id_number = nosymbols_val("Which Payment Data do you wish to view? (Enter Tenant ID No.)\n")
        for paymentdata in payment_list:
            if paymentdata[1] == tenant_id_number:
                print("Payment ID No.   :", paymentdata[0])
                print("Tenant ID No.    :", paymentdata[1])
                print("Apartment No.    :", paymentdata[2])
                print("Amount Paid      :", paymentdata[3])
                print("Payment Month    :", paymentdata[4], "\n")
                auditsearchdata(datatype, tenant_id_number)
                flag = True
        if flag:
            option = options_val("Do you want to search for another Payment Data(1), search for another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 3
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def viewpaymentstatus():
    while True:
        flag = False
        file_name = "paymentstatus"
        datatype = file_name
        records = findrecord(file_name)
        tenant_id_number = nosymbols_val("Which Payment Data do you wish to view? (Enter Tenant ID No.)\n")
        for lines in records:
            if lines[1] == tenant_id_number:
                print("Payment Month    :", lines[0])
                print("Tenant ID No.    :", lines[1])
                print("Apartment No.    :", lines[2])
                print("Rental Fee       :", lines[3])
                print("Amount Paid      :", lines[4])
                print("Payment Status   :", lines[5], "\n")
                auditsearchdata(datatype, tenant_id_number)
                flag = True
        if flag:
            option = options_val("Do you want to search for another Payment Data(1), search for another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 3
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def modify_apartment_data():
    while True:
        file_name = "apartment"
        record = findrecord(file_name)
        column = noempty_val("Which Apartment Data do you wish to Modify? (Enter Apartment No.)\n")
        selection, replacement = showapdata(record, column)
        if selection is None and replacement is None:
            pass
        else:
            replacedata(column, record, selection, replacement, file_name)
            option = options_val("Do you want to continue modifying Apartment Data(1), modify another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 4
                return i
            elif option == 3:
                i = 1
                return i

def showapdata(record, column):
    selection = None
    replacement = None
    flag = False
    for data in record:
        while data[0] == column:
            print("The current data available for the Apartment No. you wish to modify is:\n")
            print("1. Apartment No.            : ", data[0])
            print("2. Date of acquisition      : ", data[1])
            print("3. Apartment Square Footage : ", data[2])
            print("4. Rent Amount              : ", data[3], "\n")
            time.sleep(0.5)
            selection = options_val("Which data do you wish to modify?\n", 4)
            selection -= 1
            flag = True
    if flag:
        if selection == 0:
            replacement = noempty_val("What do you want to replace the data with?\n")
            return selection, replacement
        elif selection == 1:
            replacement = date_val("What do you want to replace the data with? (DD/MM/YY) \n")
            return selection, replacement
        elif selection == (2 or 3):
            replacement = numbers_val("What do you want to replace the data with?\n")
            return selection, replacement
    else:
        print("No matching data found")
        time.sleep(0.5)
        return selection, replacement

def replacedata(column, record, selection, replacement, file_name):
    datatype = file_name
    for data in record:
        if column == data[0]:
            data[selection] = replacement
            auditmodifydata(datatype, data[0])

    replacedatatofile(file_name, record)

    print("Data Modified")
    time.sleep(0.5)

def modify_tenant_data():
    while True:
        file_name = "tenant"
        record = findrecord(file_name)
        column = nosymbols_val("Which Tenant's Data do you wish to Modify? (Enter Tenant ID No.)\n")
        selection, replacement = showtndata(record, column)
        if selection is None and replacement is None:
            pass
        else:
            replacedata(column, record, selection, replacement, file_name)
            option = options_val("Do you want to continue modifying Tenant Data(1), modify another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 4
                return i
            elif option == 3:
                i = 1
                return i

def auditmodifydata(datatype, name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been modify")
    with open("audit", "a") as record:
        record.write(data + "\n")

def showtndata(record, column):
    selection = None
    replacement = None
    flag = False
    for data in record:
        while data[0] == column:
            print("The current data available for the Tenant No. you wish to modify is:\n")
            print("1. Tenant ID No.         :", data[0])
            print("2. Full Tenant Name      :", data[1])
            print("3. Tenant Gender         :", data[2])
            print("4. Tenant Phone Number   :", data[3])
            print("5. Tenant Address        :", data[4])
            print("6. Tenant City           :", data[5])
            print("7. Tenant Job History    :", data[6])
            print("8. Tenant Current Job    :", data[7])
            print("9. Apartment No.         :", data[8])
            print("10. Date of Rent         :", data[9], "\n")
            time.sleep(0.5)
            selection = options_val("Which data do you wish to modify?\n", 10)
            selection -= 1
            flag = True
    if flag:
        if selection == 0:
            print("Tenant ID No. could not be changed, please try again")
            time.sleep(0.5)
            pass
        elif selection == (1 or 2 or 5 or 6 or 7):
            replacement = characters_val("What do you want to replace the data with?1\n")
            return selection, replacement
        elif selection == 3:
            replacement = numbers_val("What do you want to replace the data with?2\n")
            return selection, replacement
        elif selection == (4 or 8):
            replacement = noempty_val("What do you want to replace the data with?3\n")
            return selection, replacement
        elif selection == 9:
            replacement = date_val("What do you want to replace the data with? (DD/MM/YY) \n")
            return selection, replacement
    else:
        print("No matching data found")
        time.sleep(0.5)
        return selection, replacement

def modify_payment_data():
    while True:
        file_name = "payment"
        record = findrecord(file_name)
        column = nosymbols_val("Which Payment Data do you wish to Modify? (Enter Payment ID No.)\n")
        selection, replacement = showpmdata(record, column)
        if selection is None and replacement is None:
            pass
        else:
            replacedata(column, record, selection, replacement, file_name)
            option = options_val("Do you want to continue modifying Payment Data(1), modify another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 4
                return i
            elif option == 3:
                i = 1
                return i

def showpmdata(record, column):
    selection = None
    replacement = None
    flag = False
    for data in record:
        while data[0] == column:
            print("The current data available for the Payment No. you wish to modify is:\n")
            print("1. Payment ID No.   :", data[0])
            print("2. Tenant ID No.    :", data[1])
            print("3. Apartment No.    :", data[2])
            print("4. Amount Paid      :", data[3])
            print("5. Payment Month    :", data[4], "\n")
            time.sleep(0.5)
            selection = options_val("Which data do you wish to modify?\n", 5)
            selection -= 1
            flag = True
    if flag:
        if selection == 0:
            print("Payment ID No. could not be changed, please try again")
            time.sleep(0.5)
            pass
        elif selection == 1:
            replacement = nosymbols_val("What do you want to replace the data with?\n")
            return selection, replacement
        elif selection == 2:
            replacement = noempty_val("What do you want to replace the data with?\n")
            return selection, replacement
        elif selection == 3:
            replacement = numbers_val("What do you want to replace the data with?\n")
            return selection, replacement
        elif selection == 4:
            replacement = month_val("What do you want to replace the data with (MM/YY)?\n")
            return selection, replacement
    else:
        print("No matching data found")
        time.sleep(0.5)
        return selection, replacement

def remove_apartment_data():
    while True:
        flag = False
        file_name = "apartment"
        apartment_record = findrecord(file_name)
        apartment_no = noempty_val("Which Apartment Data do you wish to Delete? (Enter Apartment No.)\n")
        for apdata in apartment_record:
            if apdata[0] == apartment_no:
                print("The matching data for", apartment_no, " is found:\n")
                print("Apartment No.            :", apdata[0])
                print("Date of Acquisition.     :", apdata[1])
                print("Apartment Square Footage :", apdata[2])
                print("Rent Amount              :", apdata[3], "\n")
                confirmation = characters_val("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                if confirmation.lower() == "x":
                    apartment_record.remove(apdata)
                    deletedata(file_name, apartment_record, apdata[0])
                    flag = True
        if flag:
            option = options_val("Do you want to delete other Apartment Data(1), delete another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 5
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def deletedata(file_name, record, name):
    datatype = file_name
    with open(file_name, "w") as updateData:
        for data in record:
            for item in data:
                updateData.write(item + ",")
            updateData.write("\n")
    print("Data Deleted")
    time.sleep(0.5)
    auditdeletedata(datatype, name)

def auditdeletedata(datatype, name):
    dnt = currentdatetime()
    data = (dnt + datatype + " data of " + name + " has been deleted")
    with open("audit", "a") as record:
        record.write(data + "\n")

def remove_tenant_data():
    while True:
        flag = False
        file_name = "tenant"
        tenant_record = findrecord(file_name)
        tnid_no = nosymbols_val("Which Tenant's Data do you wish to Delete? (Enter Tenant ID No.)\n")
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
                print("9. Apartment No.        :", tndata[8])
                print("10. Date of Rent        :", tndata[9], "\n")
                confirmation = characters_val("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                if confirmation.lower() == "x":
                    tenant_record.remove(tndata)
                    deletedata(file_name, tenant_record, tndata[0])
                    flag = True
        if flag:
            option = options_val("Do you want to delete other Tenant Data(1), delete another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 5
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def remove_payment_data():
    while True:
        flag = False
        file_name = "payment"
        payment_record = findrecord(file_name)
        pmid_no = nosymbols_val("Which Tenant's Payment Data do you wish to Delete? (Enter Payment ID No.)\n")
        for pmdata in payment_record:
            if pmdata[0] == pmid_no:
                print("The matching data for", pmid_no, " is found:\n")
                print("1. Payment ID No.   :", pmdata[0])
                print("2. Tenant ID No.    :", pmdata[1])
                print("3. Apartment No.    :", pmdata[2])
                print("4. Amount Paid      :", pmdata[3])
                print("5. Payment Month    :", pmdata[4], "\n")
                confirmation = characters_val("Do you wish to remove the displayed data? If yes, enter 'X'\n")
                if confirmation.lower() == "x":
                    payment_record.remove(pmdata)
                    deletedata(file_name, payment_record, pmdata[0])
                    flag = True
        if flag:
            option = options_val("Do you want to delete other Payment Data(1), delete another type of data(2) or return to Main Menu(3)?\n", 3)
            if option == 1:
                continue
            elif option == 2:
                i = 5
                return i
            elif option == 3:
                i = 1
                return i
        else:
            print("No matching data found")
            time.sleep(0.5)

def userpasswordreset(status):
    while True:
        print("Change Username/Password")
        time.sleep(0.5)
        file_name = "userpw"
        result = None
        type = None
        userpw = findrecord(file_name)
        username = characters_val("Enter the username: ")
        passwrd = noempty_val("Enter the password: ")
        for data in userpw:
            while data[0] == username and data[1] == passwrd:
                result = statuscheck(data, status)
                if result == "no":
                    break
                else:
                    option = options_val("Do you want to change the Username(1) or Password(2)?\n", 2)
                    if option == 1:
                        type = "Username"
                    elif option == 2:
                        type = "Password"
                    option -= 1
                    replacement = changeuserpw(option)
                    selection = options_val("Do you want to save the new " + type + "(1) or change another new " + type + "(2) ?\n", 2)
                    if selection == 1:
                        data[option] = replacement
                        replacedatatofile(file_name,userpw)
                        print("The data have been changed!")
                        auditchguserpw(username, type)
                        time.sleep(0.5)
                        print("Redirecting you to Main Menu")
                        result = "back"
                        time.sleep(0.5)
                        break
                    elif selection == 2:
                        pass

        if result == "no":
            continue
        elif result == "back":
            i = 1
            return i
        else:
            print("No matching Username and Password found, please try again")
            time.sleep(0.5)

def statuscheck(data, status):
    datastatus = data[2]
    power = statustonumb(status)
    power2 = statustonumb(datastatus)
    if power >= power2:
        pass
    else:
        print("You do not have the authority to change this Username or Password")
        time.sleep(0.5)
        print("Redirecting you to Change Username/Password page")
        result = "no"
        time.sleep(0.5)
        return result

def statustonumb(status):
    if status == "superadmin":
        numb = 3
        return numb
    elif status == "admin":
        numb = 2
        return numb
    elif status == "tenant":
        numb = 1
        return numb

def changeuserpw(option):
    while True:
        validation = None
        if option == 0:
            validation = characters_val
        elif option == 1:
            validation = noempty_val
        replacement = validation("What do you want it to be changed to?\n")
        confirmation = validation("Please retype again for confirmation\n")
        if replacement == confirmation:
            if option == 0:
                print("Your username will be changed to", replacement)
                return replacement
            elif option == 1:
                passwordstrength(replacement)
                return replacement

        else:
            print("Wrong input please try again")
            pass

def passwordstrength(password):
    score, hint = securityscore(password)
    if 0 <= score <= 2:
        print("Your password's security is weak")
    elif 2 < score <= 4:
        print("Your password's security is average")
    elif 4 < score <= 6:
        print("Your password's security is strong")
    if score != 6:
        print("To increase your password's security, make another password with: \n", ",".join(hint))

def securityscore(password):
    score = 0
    hint = []
    if not password.islower():  #to check the presence of uppercase character
        score += 1
    else:
        hint.append("uppercase character")
    if not password.isupper():  #to check the presence of lowercase character
        score += 1
    else:
        hint.append("lowercase character")
    if not password.isnumeric():  #to check if all the characters are numeric
        score += 1
    else:
        hint.append("characters other than numbers")
    if not password.isalpha():  #to check if all the characters are alphabet
        score += 1
    else:
        hint.append("characters other than alphabets")
    if not password.isalnum():  #to check if the characters are alphanumeric
        score += 1
    else:
        hint.append("special characters")
    if len(password) > 7:  #to check if the password has 8 or more characters
        score += 1
    else:
        hint.append("longer password")
    return score, hint

def replacedatatofile(file_name, newdata):
    with open(file_name, "w") as records:
        for record in newdata:
            for item in record:
                records.write(item + ",")
            records.write("\n")

def auditchguserpw(username, type):
    dnt = currentdatetime()
    data = (dnt + username + " has change his/her " + type)
    with open("audit", "a") as record:
        record.write(data + "\n")

def auditlogout(username):
    dnt = currentdatetime()
    data = (dnt + username + " has log out ")
    with open("audit", "a") as record:
        record.write(data + "\n")

def options_val(text, selection):
    while True:
        try:
            data = input(text)
            if len(data) > 0:
                if int(selection) + 1 > int(data) > 0:
                    return int(data)
                else:
                    print("Invalid Option! Please choose between [1]-[{}]".format(selection))
                    time.sleep(0.5)
            else:
                print("This column requires an input!")
                time.sleep(0.5)
        except:
            print("Only Numbers Allowed")
            time.sleep(0.5)

def characters_val(text):
    while True:
        i = 0
        data = input(text)
        if len(data) > 0:
            for alphabet in data:
                if alphabet.isalpha() or alphabet.isspace():
                    i += 1
            if i == len(data):
                return data
            else:
                print("No Numbers and Symbols Allowed! Please try again!")
        else:
            print("This column requires an input!")

def numbers_val(text):
    while True:
        i = 0
        data = input(text)
        if len(data) > 0:
            for number in data:
                if number.isnumeric():
                    i += 1
            if i == len(data):
                return data
            else:
                print("Only numbers are allowed! Please try again!")
        else:
            print("This column requires an input!")

def nosymbols_val(text):
    symbols_list = "~`!@#$%^&*()-_=\"+[]{}|\:;'?/<>,."
    flag = True
    while True:
        data = input(text)
        if len(data) > 0:
            for i in symbols_list:
                for x in data:
                    if i == x:
                        flag = False
                        continue
            if flag == False:
                print("No symbols allowed")
            else:
                return data
        else:
            print("This column requires an input!")

def noempty_val(text):
    while True:
        data = input(text)
        if len(data) > 0:
            return data
        else:
            print("This column requires an input!")

def date_val(text):
    while True:
        data = input(text)
        if len(data) > 0:
            try:
                day, month, year = data.split("/")
                datetime(int(year), int(month), int(day))
                return data

            except ValueError:
                print("Invalid input! Please enter according to the format!")
        else:
            print("This column requires an input!")

def month_val(text):
    while True:
        data = input(text)
        if len(data) > 0:
            try:
                month, year = data.split("/")
                day = 1
                datetime(int(year), int(month), int(day))
                return data

            except ValueError:
                print("Invalid input! Please enter according to the format!")
        else:
            print("This column requires an input!")

from datetime import datetime
import time
login()
