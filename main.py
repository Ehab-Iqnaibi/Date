
class Date:
    def __init__(day, month, year):
        isValidDate = True
        try :
            datetime.datetime(int(year), int(month), int(day))
            datetime.datetime(int(day), int(month), int(year))
            datetime.datetime(int(year), int(month),int(day))
        except ValueError :
            isValidDate = False

        if(isValidDate) :
            print ("Input date is Valid!")
        else :
            print ("Input date is Invalid")

    def get_date(self):
        inputDate = input("Enter the date in format 'dd/mm/yy' : ")
        day,month,year = inputDate.split('/')
        date1= Date(int(day), int(month),  int(year))


    def put_date(self):
        print ("Input date: " +inputDate)


date1= Date()
date1.get_date()
date1.put_date()
