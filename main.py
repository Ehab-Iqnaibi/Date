from date import Date


while user != 'esc':
        day,month,year = input("Enter the date in format 'dd,mm,yyyy' : ").split(' , ')
        d1= Date(int(day), int(month),  int(year))
        print(d1)
        d2=input("Enter the 2nd date in format 'dd,mm,yyyy' : ").split(' , ')
        d1 = Date(int(day), int(month), int(year))
        print(d2)

        enter=1
        while enter:
            user1= int(input('''what test you want to perform ??
                1. add a number to date ?
                2. Order of date?
                3. subtract the first and the second dates ? 
                4. First Date order > second date order?
                5. First Date order < second date order?
                6. First Date order >= second date order?
                7. First Date order <= second date order?
                8. First Date order = second date order?
                9. First Date order != second date order? '''))
            if user1 == 1:
                user2 = int(input('1. d1 OR 2. d2: ' )
                if user2 == 1:
                  print(d1 + int(input('Enter a number to add to first Date= ')))
                if user2 == 2:
                  print(d2 + int(input('Enter a number to add to first Date= ')))
            elif user1 == 2:
                 user2 = int(input('1. d1 OR 2. d2: ')
                 if user2 == 1:
                   print(d1.order())
                 if user2 == 2:
                   print(d2.order())
            elif user1 == 3:
                 print(d1 - d2)
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




d1 = Date(23, 12, 2020)
print(d1)
my_order=d1.order()
print(my_order)

d2 = Date(23, 13, 2020)
print(d2)
print(d2.order())

d3 = Date(13, 7, 2019)
print(d3)
print(d3.order())

d4=d1-d3
print('number of days between two dates: ',str(d4))

update=d1+22
dd, mm,yyyy =update
print(update,type(update))
update = Date(int(dd), int(mm), int(yyyy))
my_order=update.order()
print(my_order)


