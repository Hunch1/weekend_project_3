# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create 
# a program that will calculate the Return on Investment(ROI) for a rental property.
#XPENSES:
    #Bottom Left Box
    #Tax - 150
    #Insurance - 100
    #Utilities - 0
        #electric 
        #water
        #sewer
        #garbage
        #gas
    #HOA FEES - 0
    #Lawn/snow care - 0
    #Vacancy  - 5% / (100)
    #repairs - 100
    #CapEx (new roof/heater/etc...) 100 
    #Prop MGMT - 10% / 200/month
    #Mortgage: 860
                          #TOTAL MONTHLY XPENSES = $1610

#Cash Flow
    #Top Right Box
    #Income - Xpenses
        #2000-1610
        # MONTHLY CASH FLOW: 390 * 12 = YEARLY CASH FLOW 4680

#Cash On Cash ROI
    #is your money earning a good percent?
    #Downpayment - 40,000
    #closing costs - 3000
    #rehab budget - 7000
    #misc other - 0
        #total investment:  - 50k
        #yearly cashflow = 4680
        #Yearly cashflow divided by total investment:
                             # 4690/50000  ROI = 9.36%

class rental_property:
    def __init__(self):
        self.monthly_income = 0 
        self.monthly_expense = {}
        self.total_invesment= {}

    def user_input(self):
        self.monthly_income = float(input("Enter the monthly income(Rental Income, Laundry, Storage, misc): "))
        numExpenses = int(input("Please enter the number of expenses you have (Tax, Insurance, Utilities, repairs, etc):  "))
        for x in range(numExpenses):
            expense_name = input(f"Enter the name of your expense {x + 1}:  ")
            expense_cost = float(input(f"Now enter the cost of the expense {x + 1}:  "))
            self.monthly_expense[expense_name] = expense_cost
        numInvesments = int(input("Please enter the number of invesments you have (Down payment,closing costs,Rehab budget, misc other, etc):   ")) 
        for y in range(numInvesments):
            Invesments_name = input(f"Enter the name of your Invesment {y + 1}:  ")
            Invesment_cost = float(input(f"Now enter the cost of the Invesment {y + 1}:  "))
            self.total_invesment[Invesments_name] = Invesment_cost


    def annual_income(self):
        return self.monthly_income * 12
    
    def annual_expenses(self):
        total_expenses = sum(self.monthly_expense.values()) * 12
        return total_expenses

    def total_investments(self):
        total_investments = sum(self.total_invesment.values())
        return total_investments

    def total_cashflow(self):
        cashflow = self.annual_income() - self.annual_expenses() 
        return cashflow
    

    def calculate_roi(self):
        investments = self.total_investments()
        cashflow = self.total_cashflow()

        roi = (cashflow / investments) * 100
        return roi
    
rentalproperty = rental_property()
rentalproperty.user_input()
theRoi = rentalproperty.calculate_roi()
print(f"The cash on cash Return on Investment (ROI) for this rental property is: {theRoi}%")
