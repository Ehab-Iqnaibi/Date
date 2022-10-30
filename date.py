class Date:

    def __init__(self, day, month, year):
        self.MonthD= [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
        self.MonthN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        if self.isValidDate():
            print("Input date is Valid!")

    def isValidDate(self):
        #print(self.MonthD[self.month - 1])
        if 1 <= self.month <= 12 and 1 <= self.day <= self.MonthD[self.month -1]:
            isValidDate = True
        else:
            isValidDate = False
        return isValidDate
    def order(self):
        order=0
        if self.isValidDate():
          i = 1
          while i <= self.month :
              if i < self.month:
                  order=order+self.MonthD[i-1]
              elif i == self.month:
                  order=order+self.day
        return order

    def __str__(self):
        if self.isValidDate():
           return str(self.day) + " / " + str(self.month) + " / " + str(self.year)
        else:
           return ("Input date is Invalid")