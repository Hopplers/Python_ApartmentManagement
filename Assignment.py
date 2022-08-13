def mainmenuselect():
    option = int(input(
        "Please select an option\n1. Apartment Details\n2. Tenant Details\n3. Payment Details\n4. Search Details\n5. Return to Log-in page\n"))
    if 5 > option > 0:
        i = option + 1
        flag = True
        return i, flag
    elif option == 5:
        i = None
        flag = False
        return i, flag

def new_apartment_data(): #Function for entering new apartment data
    i1 = 1
    while i1 == 1:
        apartment_data = []
        apartment_no = input("Enter Apartment No.:")
        apartment_square_footage = input("Enter Apartment Square Footage: ")
        rent_amount = input("Enter Rent Amount: ")
        details_apartment = [apartment_no, apartment_square_footage, rent_amount]
        apartment_data.append(details_apartment)
        with open("tenent", "a") as records:
            for record in apartment_data:
                for item in record:
                    records.write(item + ",")
                records.write("\n")
            print("Data saved.")
            option = input("Do you want to return to enter another new data(1), return to Apartment Details(2) or return to Main Menu(3)?\n")
            if option == "1":
                continue
            elif option == "2":
                i1 = 0
                i = 2
                return i
            elif option == "3":
                i1 = 0
                i = 1
                return i

def new_tenant_data(): #Function for entering new tenant data
    tenant_data = []
    i1 = 1
    while i1 == 1:
        tenant_data = []
        full_name = input("Enter Full Name: ")
        id_number = input("Enter ID Number: ")
        gender = input("Enter Gender: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter address: ")
        city = input("Enter City: ")
        job_history = input("Enter Job History: ")
        current_job = input("Enter Current Job: ")
        date_of_acquisition = input("Enter Date of Acquisition: ")
        apartment_no = input("Enter Apartment No.: ")
        details_tenant = [full_name, id_number, gender, phone_number, address, city, job_history, current_job,date_of_acquisition, apartment_no]
        tenant_data.append(details_tenant)
        with open("tenent", "a") as records:
            for record in tenant_data:
                for item in record:
                    records.write(item + ",")
                records.write("\n")
        print("Data saved.")
        option = input("Do you want to return to enter another new data(1), return to Tenent Details(2) or return to Main Menu(3)?\n")
        if option == "1":
            continue
        elif option == "2":
            i1 = 0
            i = 3
            return i
        elif option == "3":
            i1 = 0
            i = 1
            return i

def mainmenu():
    flag = True
    i = 1
    while flag:
        if i == 1:
            i, flag = mainmenuselect()
        if i == 2:
            option1 = int(input("\n1. New Apartment Data\n2. Edit Apartment Data\n3. Delete Apartment Data\n4. Return to Main Menu\n"))
            if option1 == 1:
                i = new_apartment_data()

        if i == 3:
            option1 = input("\n1. New Tenant Data\n2. Edit Tenant Data\n3. Delete Tenant Data\n4. Return to Main Menu\n")
            if option1 == "1":
                i = new_tenant_data()
