import database as db

while True:
    print('''Welcom to PhoneBook:
    >>>PhoneBook Commands are:1,2,3,4,5<<<
    1. Show all Contact
    2. Search Contact By PhoneNumberID
    3. Insert Contact
    4. Update Contact
    5. Delete Contact
    0. Exit
    ''')

    choice = int(input('Enter Your Choice: '))
    if choice==0:
        print('Thanking for using  the MyPhoneBook')
        break
    elif choice==1:
        #it show all Contact
        data = db.ShowContact()
        for i in data:
            print(f'PhoneNumberID: {i[0]}\nFirstName: {i[1]}\nlastname: {i[2]}\nworkphone: {i[3]}\nhomephone:{i[4]}')
    elif choice==2:
        #search specific Contact
        PhoneNumberID= input('Enter the ID by PhoneNumberID: ')
        data = db.searchContact(PhoneNumberID)
        try:
            print(f'PhoneNumberID: {data[0]}\nFirstName: {data[1]}\nlastname: {data[2]}\nworkphone: {data[3]}\nhomephone: {data[4]}')
        except:
            print('Contact Record Does Not Exists')
    elif choice==3:
        #insert
        Firstname =input('Enter Your FirstName: ')
        lastname = input('Enter Your lastname: ')
        workphone= int(input('Enter Your wrokphone: '))
        homephone= int(input('Enter Your homephone: '))
        try:
            db.insertContact(Firstname,lastname,workphone,homephone)
            print('Contact Inserted Successfully')
        except:
            print('Insert Operation Failed')

    elif choice==4:
        #update
        PhoneNumberID= int(input('Enter the ID of the PhoneNumber whose Contact is to be updated: '))

        print('''What do you want to update?
            1. Firstname
            2. lastname
            3. workphone
            4. homephone
        ''')
        updatechoice = int(input('Enter Your Choice: '))

        column = '' 
        newvalue = ''
        if updatechoice == 1:
            newvalue = input('Enter New FirstName: ')
            column = 'Firstname'
        elif updatechoice == 2:
            newvalue = input('Enter New lastname: ')
            column = 'lastname'
        elif updatechoice == 3:
            newvalue = input('Enter New workphone: ')
            column = 'workphone'
        elif updatechoice == 4:
            newvalue = int(input('Enter New homePhone: '))
            column = 'homephone'

        try:
            db.updateContact(PhoneNumberID,column,newvalue)
            print("Contact Updated Successfully")
        except:
            print('Contact Records Does Not Exists')
    elif choice==5:
        #delete
        PhoneNumberID= int(input('Enter the ID of the PhoneNumber whose Contact is to be deleted: '))
        try:
            db.deleteContact(PhoneNumberID)
            print('Contact Deleted Successfully')
        except:
            print('Contact Records Does Not Exists')
    else:
        print('Invalid Choice')