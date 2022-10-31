from date import Date

while True:
        day1,month1,year1 = input("Enter the date in format 'dd,mm,yyyy' : ").split(',')
        d1= Date(int(day1), int(month1),  int(year1))
        print(d1)
        day2,month2,year2=input("Enter the 2nd date in format 'dd,mm,yyyy' : ").split(',')
        d2 = Date(int(day2), int(month2), int(year2))
        print(d2)

        while True:
            user1= int(input('''
                1. Add a number to date :
                2. Order day in the year of date:
                3. subtract the first and the second dates : 
                4. First date order > Second date order?
                5. First date order < Second date order?
                6. First date order >= Second date order?
                7. First date order <= Second date order?
                8. First date order = Second date order?
                9. First date order != Second date order?
                10. Do you want to show the month in words?
                Choos the number of the operation to perform: '''))
            if user1 == 1:
                user2 = int(input('1. d1 OR 2. d2: ' ))
                if user2 == 1:
                   en=int(input('Enter a number to add to first Date= '))
                   print('Next date after '+str(en)+' days: '+str(d1 + en))
                elif user2 == 2:
                   en=int(input('Enter a number to add to second Date= '))
                   print('Next date after '+str(en)+' days: '+ str( d2 + en))
            elif user1 == 2:
                user2 = int(input('1. d1 OR 2. d2: '))
                if user2 == 1:
                   print('Order of the date is: '+str(d1.order()))
                elif user2 == 2:
                   print('Order of the date is: '+str(d2.order()))
            elif user1 == 3:
                 print('The difference (number of days) between two dates: '+str(d1 - d2))
            elif user1 == 4:
                 print(d1 > d2)
            elif user1 == 5:
                print(d1 < d2)
            elif user1 == 6:
                print(d1 >= d2)
            elif user1 == 7:
                print(d1 <= d2)
            elif user1 == 8:
                print(d1 == d2)
            elif user1 == 9:
                print(d1 != d2)
            elif user1 == 10:
                user2 = int(input('1.d1 OR 2.d2: '))
                if user2 == 1:
                    print(d1.MonthN[int(month1) -1])
                elif user2 == 2:
                    print(d2.MonthN[int(month2) -1])

            user_input = input('Do you want to choose another operation (yes/no): ')
            if user_input.lower() == 'yes':
                continue
            elif user_input.lower() == 'no':
                break
        user_input = input('Do you want to choose another dates (yes/no): ')
        if user_input.lower() == 'yes':
            continue
        elif user_input.lower() == 'no':
            break

print('Thank you :)')