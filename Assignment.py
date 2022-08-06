def newdata():
    dfile = []
    with open ("tenent.txt", "a") as file:
        tname = input("Enter Tenent's Name")
        tid = input("Enter Tenent's ID Number")
        tbirthplace = input("Enter Tenent's Place of Birth")
        tbirthcity = input("Enter Tenent's City of Birth")
        tworkhis = input("Enter Tenent's Work History")
        tworkemp = input("Enter Tenet's Work Employee")
        details = [tname, tid, tbirthplace, tbirthcity, tworkhis, tworkemp]
        dfile.append(details)
        for record in dfile:
            for item in record:
                file.write(item + ",")
            file.write("\n")
  
def mainmenu():
  data = []
  while flag == true:
    option = (" Please select an option\n1. Add New Data\n2. Edit Existing Data\n3. Search Data\n4. View All Data\n5.Exit")
    if option == 1
    newdata()
    
