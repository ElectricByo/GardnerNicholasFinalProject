import tkinter as tk

# Program by Nicholas Gardner. This is the first and last version. Final revision on 5/10/24




root = tk.Tk()
root2 = tk.Tk()
myEntry = tk.Entry(root)
myEntry.pack()
#Entry field and two windows initialized


tax_levels = [
    (30000, 0.03),
    (50000, 0.05),
    (85000, 0.08),
    (115000, 0.11),
    (150000, 0.15),
    (200000, 0.18),
    (500000, 0.23)
                ]
# Taxes based on income made in a year

errors = tk.Label(root, text = "")
errors.pack()
gross_income = tk.Label(text = "")
gross_income.pack()
taxed_income = tk.Label(text = "")
taxed_income.pack()
Label = tk.Label(root2,  text = "")
Label.pack()
#String effects when buttons are clicked










def income():
  global monthly_pay #This represents the number that will entered in by the user. Its made global so it can be used by other functions
  monthly_pay = float(myEntry.get())
  global annual_pay #This represents the number entered by the user multiplied by 12 hence annual pay
  annual_pay = 12 * monthly_pay
  gross_income.configure(text = ("This is your income for the year: " , str(annual_pay)))
  
  
#User input being multiplied by 12 and being displayed  
  





def taxes():
 
  
  
  for incomeLevel , tax_rate in tax_levels: #This represnts the data set i declared earlier. This loop is going to go through that data set and check if the annual pay is below or equal to a threshhold i made. 
    if annual_pay <= incomeLevel:           #If the threshhold is higher than it will keep looping until it meets the condition set. If not then the else statement will be executed
      
      tax = tax_rate * annual_pay
      new_total = annual_pay - tax #If the threshold is not met then the tax will be calculated#
      taxed_income.configure(text = "This is your income after taxes!: " + str(new_total)) #New total is the the taxed income being displayed on thw window
      return deduce(tax) #I return tax because my deduce function needs not the variable tax itself but the value that is being held
  else:
      taxed_income.configure(text = "You have too much money to tax!: " ) 
#The tax money being calculated. Incime after tax and actual money taken out of original income.

#All the iterations of the money and tax percentage thresholds are being represented by the variables incomeLevel and tax_rate.
    
  


  
def deduce(tax):
  Label.configure(text = "These are your tax deuctions!: " + str(tax))    
#I display the value returned from the previous function
#separate function to display money taken out on separate window


def error():
 
  if monthly_pay == "":
    print("Please enter a number")
  elif monthly_pay <= 0:
    errors.configure( text = "Please enter a number above zero")
  elif isinstance(monthly_pay, str):
    print("Please enter a valid integer") 
 #Function specifically to catch user errors 
    


def error_income():
  income()
  error()
#Combining the income and error functions into one





def deleted():
  myEntry.delete(0 , tk.END)
  taxed_income.configure(text = "")
  gross_income.configure(text = "")
  Label.configure(text = "")
  errors.configure(text = "")
#Deletes data inputted by user and varies string effects resulted in 'Calculate gross pay' and 'Calculate taxed income' buttons being clicked






root.geometry("800x500")
root2.geometry("800x500")
root2.title("Tax deductions")
root.title("Taxes")
#Window size and titles being created

myLabel = tk.Label(root, text = "Please enter your monthly pay above")
myLabel.pack()
tax_deductions = tk.Label( root2 , text = "This is how much you lost in a year to taxes")
tax_deductions.pack()
taxy = tk.Label(root, text = "Please check the tax deductions window to see how much money was lost to taxes")
taxy.pack()
#All labels being created


delButton = tk.Button(root, text = "Erase", command = deleted)
delButton.pack()
myButton = tk.Button(root, text = "Calculate gross pay", command = error_income)
myButton.pack()
taxed = tk.Button( root , text = "Calculate taxed income" , command = taxes)
taxed.pack()
#All buttons being made


root2.mainloop()
root.mainloop()
