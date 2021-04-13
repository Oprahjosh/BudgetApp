class Budget:

    def __init__(self,food,clothing,entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def deposit(self):
        depositAmount = int(input("Input the amount to deposit \n"))
        depositTo = int(input("Select where to add your deposit to \n 1. Food \n 2. Clothing \n 3. Entertainment \n"))
        if depositTo == 1:
            foodBudget = depositAmount + self.food
            print("Your new budget allocation for food is " + str(foodBudget) )
        elif depositTo == 2:
            clothingBudget = depositAmount + self.clothing
            print("Your new budget allocation for clothing is " + str(clothingBudget) )
        elif depositTo == 3:
            entertainmentBudget = depositAmount + self.entertainment
            print("Your new budget allocation for clothing is " + str(entertainmentBudget) )
        else:
            print("select a valid option")
            deposit()
            
    def withdraw(self):
        withdrawFrom = int(input("Select budget account from which you want to withdraw \n 1. Food \n 2. Clothing \n 3. Entertainment \n " ))
        withdrawAmount = int(input("How much would you like to withdraw ? \n"))

        if withdrawFrom == 1:
            if withdrawAmount <= self.food:
                foodBudget = self.food - withdrawAmount
                print("You have successfully withdrawn " + str(withdrawAmount) + " from the food budget.")
                print("Your food budget balance is " + str(foodBudget))
            else:
                print("The amount selected is above your food budget balance of " + str(self.food) )

        elif withdrawFrom == 2:
            if withdrawAmount <= self.clothing:
                clothingBudget = self.clothing - withdrawAmount
                print("You have successfully withdrawn " + str(withdrawAmount) + " from the food budget.")
                print("Your food budget balance is " + str(clothingBudget))
            else:
                print("The amount selected is above your food budget balance of " + str(self.clothing) )

        elif withdrawFrom == 3:
            if withdrawAmount <= self.entertainment:
                entertainmentBudget = self.entertainment - withdrawAmount
                print("You have successfully withdrawn " + str(withdrawAmount) + " from the food budget.")
                print("Your food budget balance is " + str(entertainmentBudget))
            else:
                print("The amount selected is above your food budget balance of " + str(self.entertainment) )



    def transfer(self):
        sourceAccount = int(input("Select the source account for transfer \n 1. Food Budget \n 2. Clothing Budget \n 3. Entertainment Budget \n" ))
        transferAmount = int(input("How much do you want to transfer ? \n"))
        #I don't know why this dictionary is not working to pass transferTo into the dictionary
        '''budgetOption = {1:"Food Budget" , 2:"Clothing Budget" , 3:"Entertainment Budget"}
    
            for transferTo,budgetItem in budgetOption.items():
    
                if transferTo == 1:
                    transferTo = budgetOption.get(1)
                elif transferTo == 2:
                    transferTo = budgetOption.get(2)
                elif transferTo == 3:
                    transferTo = budgetOption.get(3)
    '''
        transferTo = int(input("Select receiving account. \n 1. Food Budget \n 2. Clothing Budget \n 3. Entertainment Budget\n"))
        if transferTo == 1 and sourceAccount == 1:
            print (" You cannot transfer to the same account\n Transfer Not Allowed.")
        elif transferTo == 2 and sourceAccount == 1:
            print("You have sucessfully transferred "+ str(transferAmount) + " to " + str(transferTo))
            print("Your new "+ str(transferTo) + " balance is " + str( transferAmount+self.clothing))
        elif transferTo == 3 and sourceAccount == 1:
            print("You have sucessfully transferred "+ str(transferAmount) + " to " + str(transferTo))
            print("Your new "+ str(transferTo) + " balance is " + str( transferAmount+self.clothing))




        #pass the transferTo input to the object property
        #if 1 == self.food and 2 == self.clothing and 3 == self.entertainment :


    def  transferTransaction(transferTo,transferAmount) :
        newBalance = transferTo+transferAmount
        print(newBalance)




Budget_2020 = Budget(20000,12000,30000)
Budget_2021 = Budget(30000,22000,40000)
#Budget_2020.deposit()
#Budget_2020.withdraw()
Budget_2020.transfer()