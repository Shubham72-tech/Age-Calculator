from tkinter import *
import datetime
from calendar import leapdays
from calendar import isleap

class Age_Calculator(Tk):
    def __init__(self):
        super(Age_Calculator, self).__init__()

        self.title('Age Calculator')
        self.geometry("190x420")
        self['bg'] = 'black'

        self.label = Label(text='Age Calculator', bg="black", fg="orange").grid(row=0, column=0, columnspan=3)

        self.label_date = Label(text='Date', bg="black", fg="red").grid(row=1, column=0)
        self.label_month = Label(text='Month', bg="black", fg="green").grid(row=1, column=1)
        self.label_year = Label(text='Year', bg="black", fg="blue").grid(row=1, column=2)
        self.label_hour = Label(text='Hour', bg="black", fg="pink").grid(row=3, column=0)
        self.label_minute = Label(text='Minute', bg="black", fg="purple").grid(row=3, column=1)

        self.var_date = IntVar()
        self.var_month = IntVar()
        self.var_year = IntVar()
        self.var_hour = IntVar()
        self.var_minute = IntVar()

        self.entry_year = Entry(textvariable=self.var_year, width=10).grid(row=2, column=2)

        self.current_date_for_entry = datetime.datetime.now()

        self.var_date.set(self.current_date_for_entry.day)
        self.var_month.set(self.current_date_for_entry.month)
        self.var_year.set(self.current_date_for_entry.year)
        self.var_hour.set(self.current_date_for_entry.hour)
        self.var_minute.set(self.current_date_for_entry.minute)

        self.button = Button(text='Calculate', command=self.Age, bg="yellow").grid(row=5, column=0, columnspan=3)

        self.options_for_days = OptionMenu(self, self.var_date, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        28, 29, 30, 31).grid(row=2, column=0)

        self.options_for_months = OptionMenu(self, self.var_month, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.options_for_months.grid(row=2,column=1)

        self.entry_minute = Entry(textvariable=self.var_minute, width=10).grid(row=4, column=1)

        self.options_for_hours = OptionMenu(self, self.var_hour, 0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                            16, 17, 18, 19, 20, 21, 22, 23)
        self.options_for_hours.grid(row=4, column=0)

    def Age(self):
        self.date = self.var_date.get()
        self.month = self.var_month.get()
        self.year = self.var_year.get()
        self.hour = self.var_hour.get()
        self.minute = self.var_minute.get()

        self.current_date = datetime.datetime.today()

        self.calculated_date = (31 + self.current_date.day) - self.date
        self.calculated_month = ((12 + self.current_date.month) - self.month) - 1
        self.calculated_year = (self.current_date.year - self.year) - 1
        self.calculated_hour = (self.current_date.hour - self.hour)
        self.calculated_minute = (self.current_date.minute - self.minute)

        if self.current_date.hour < self.hour:
            self.calculated_hour = (self.current_date.hour - (self.hour - 24))

        if self.minute > self.current_date.minute:
            self.calculated_hour -= 1
            self.calculated_minute = self.minute + self.current_date.minute

        if self.current_date.hour < self.hour:
            self.calculated_date -= 1

        if self.current_date.minute < self.minute:
            self.calculated_minute = (60 - self.minute) + self.current_date.minute

        if self.hour == self.current_date.hour and self.minute > self.current_date.minute:
            self.calculated_hour = 23
            self.calculated_date -= 1

        self.all_months = self.calculated_month + (self.calculated_year * 12)

        if self.current_date.day >= self.date:
            self.all_months += 1

        self.all_days_addon = leapdays(self.year, self.current_date.year)

        self.all_days = (self.calculated_year * 365) + (self.calculated_month * (365/12)) + self.calculated_date + \
                       self.all_days_addon

        if self.calculated_date > 30:
            self.calculated_date = self.current_date.day - self.date

        if self.calculated_month > 11:
            self.calculated_year = self.current_date.year - self.year
            self.calculated_month = self.current_date.month - self.month

        if self.current_date.month > self.month and self.current_date.day < self.date:
            self.calculated_month -= 1

        if self.current_date.month < self.month and self.current_date.day > self.date:
            self.calculated_month += 1

        if self.current_date.month == self.month and self.current_date.day >= self.date:
            self.calculated_month = 0
            self.calculated_year += 1

        self.leapyearid = isleap(self.year)

        if self.leapyearid == True and self.month > self.current_date.month:
            self.all_days += 1

        if self.leapyearid == False and self.month > self.current_date.month:
            self.all_days += 2

        if self.month > 7:
            self.all_days -= 1

        self.all_hours = (int(self.all_days) * 24) + self.calculated_hour

        self.all_minutes = (self.all_hours * 60) + self.calculated_minute

        self.all_seconds = (self.all_minutes * 60) + self.current_date.second

        if self.date <= 31 and self.month <= 12:
            self.Myage = Label(text=('Age: \n'
                                     + str(self.calculated_year) + '  Years, ' + str(self.calculated_month) +
                                     '  Months, ' + str(self.calculated_date) + '  Days\n' + str(self.calculated_hour) +
                                     '  Hours, ' + str(self.calculated_minute) + '  Minutes\n'
                                     + 'Or\n'
                                     + str(self.all_months) + '  Months, ' + str(self.calculated_date) + '  Days\n' +
                                     str(self.calculated_hour) + '  Hours, ' + str(self.calculated_minute) + '  Minutes\n'
                                     + 'Or\n'
                                     + '{:,}  Days, '.format(int(self.all_days)) +
                                     str(self.calculated_hour) + '  Hours, \n' + str(self.calculated_minute) + '  Minutes\n'
                                     + 'Or\n'
                                     + '{:,}  Hours, '.format(self.all_hours) +
                                     str(self.calculated_minute) + '  Minutes\n'
                                     + 'Or\n'
                                     + '{:,}  Minutes\n'.format(self.all_minutes)
                                     + 'Or\n'
                                     + '{:,}  Seconds\n'.format(self.all_seconds)
                                     + 'Old\n'),
                               bg="black", fg="white")
            self.Myage.grid(row=6, column=0, columnspan=3)

        if self.date == 31 and (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11):
            self.warning_label_1 = Label(text='There are only\n30 days in\n' + str(self.month) + 'th Month of year',
                                         bg="red")
            self.warning_label_1.grid(row=6, column=0, columnspan=3)

        if self.date > 28 and self.month == 2 and self.leapyearid == False:
            self.warning_label_2 = Label(text='There are only\n28 days in\nFeburary Month', bg="red")
            self.warning_label_2.grid(row=6, column=0, columnspan=3)

        if self.date > 29 and self.month == 2 and self.leapyearid == True:
            self.warning_label_3 = Label(text='There are only\n29 days in\nFeburary Month of\nLeapyear', bg="red")
            self.warning_label_3.grid(row=6, column=0, columnspan=3)

        if self.date == self.current_date.day and self.month == self.current_date.month:
            self.birthday = Label(text=('Happy Birthday\nto you on\nyour ' + str(self.calculated_year) + ' Birthday'),
                                  bg="yellow")
            self.birthday.grid(row=6, column=0, columnspan=3)

Age_Calculator().mainloop()
