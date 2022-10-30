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
              i+=1
        return order
    def __str__(self):
        if self.isValidDate():
           return str(self.day) + " / " + str(self.month) + " / " + str(self.year)
        else:
           return ("Input date is Invalid")
    def __add__(self,other):
        if self.isValidDate():
             N=self.MonthD[self.month -1]-self.day
             if N >= other:
                 self.day+=other
             elif N< other:
                 if self.month < 12:
                     self.month+=1
                 elif self.month == 12:
                    self.year+=1
                    self.month=1
                 self.day=other -N
             #print(self)
             #return  (self.day,self.month,self.year)
             return(self)
    def __sub__(self,other):
        if self.isValidDate() and other.isValidDate():
            n1=self.year*365 + self.day
            for k in range(0,self.month-1):
                n1+=self.MonthD[k]
            n2 = other.year * 365 + other.day
            for k in range(0, other.month - 1):
                n2 += other.MonthD[k]
            n=abs(n1-n2)
            return n

    def __lt__(self, other):
        return self.order() < other.order()
    def __gt__(self, other):
        return self.order() > other.order()
    def __le__(self, other):
        return self.order() <= other.order()
    def __ge__(self, other):
        return self.order() >= other.order()
    def __eq__(self, other):
        return self.order() == other.order()
    def __ne__(self, other):
        return self.order() != other.order()