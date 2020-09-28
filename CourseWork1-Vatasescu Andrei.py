#coursework1 open it in fullscreen mode because of indentation
##The big while loop will assure that the user will not enter 0 because
#we can`t divide by 0 so i tried an "except error" instruction
while True:
    try:
        #here I made an except error so the user can not enter a string or float
        while True:
            ownYears=raw_input("How many years do you want to own this car?")
            try:
                ownYears=int(ownYears)
                break
            except ValueError:
                 print("That is not an integer!Please enter an integer!")
        while True:
            averageMileage=raw_input("How many miles do you drive per year?")
            try:
                averageMileage=int(averageMileage)
                break
            except ValueError:
                  print("That is not an integer!Please enter an integer!")
        #here are the constants
        SKODA_PRICE=10000
        ROLLS_ROYCE_PRICE=50000
        FERRARI_PRICE=65000
        RENAULT_PRICE=25000
        SMART_PRICE=35000
        PETROL_PRICE=5.00
        #here I conditioned the fuel economy for each car depending on owning years
        if ownYears <= 5:
            skodaFuelEconomy = 65
            rollsroyceFuelEconomy =35
            ferrariFuelEconomy =42
            renaultFuelEconomy =45
            smartFuelEconomy =50
        elif ownYears > 5 and ownYears <= 10:
            skodaFuelEconomy =60
            rollsroyceFuelEconomy =30
            ferrariFuelEconomy =37
            renaultFuelEconomy =40
            smartFuelEconomy =45
        if ownYears > 10 and ownYears<=15:
            skodaFuelEconomy =55
            rollsroyceFuelEconomy =25
            ferrariFuelEconomy =32
            renaultFuelEconomy =35
            smartFuelEconomy =40
        ##here are the calculations
        #skoda
        milesDriven=float(averageMileage*ownYears)
        fuelCostSkoda=float((milesDriven/skodaFuelEconomy)*PETROL_PRICE)
        skodaFinalPrice=float(SKODA_PRICE+fuelCostSkoda)
        skodaAnnualCost=float(skodaFinalPrice/ownYears)
        a=int(skodaAnnualCost)
        #rollsroyce
        milesDriven=float(averageMileage*ownYears)
        fuelCostRollsRoyce=float((milesDriven/rollsroyceFuelEconomy)*PETROL_PRICE)
        rollsroyceFinalPrice=float((ROLLS_ROYCE_PRICE+fuelCostRollsRoyce))
        rollsroyceAnnualCost=float(rollsroyceFinalPrice/ownYears)
        b=int(rollsroyceAnnualCost)
        #ferrari
        milesDriven=float(averageMileage*ownYears)
        fuelCostFerrari=float((milesDriven/ferrariFuelEconomy)*PETROL_PRICE)
        ferrariFinalPrice=float(FERRARI_PRICE+fuelCostFerrari)
        ferrariAnnualCost=float(ferrariFinalPrice/ownYears)
        c=int(ferrariAnnualCost)
        #renault
        milesDriven=float(averageMileage*ownYears)
        fuelCostRenault=float((milesDriven/renaultFuelEconomy)*PETROL_PRICE)
        renaultFinalPrice=float(RENAULT_PRICE+fuelCostRenault)
        renaultAnnualCost=float(renaultFinalPrice/ownYears)
        d=int(renaultAnnualCost)
        #smart
        milesDriven=float(averageMileage*ownYears)
        fuelCostSmart=float((milesDriven/smartFuelEconomy)*PETROL_PRICE)
        smartFinalPrice=float(SMART_PRICE+fuelCostSmart)
        smartAnnualCost=float(smartFinalPrice/ownYears)
        e=int(smartAnnualCost)
        ##the print functions and the results being rounded to 2 decimals using %.2f
        print " "
        print"Average cost of Skoda per year:" , "%.2f"%skodaAnnualCost  
        print " "
        print"Average cost of Rolls-Royce per year:" , "%.2f"%rollsroyceAnnualCost
        print " "
        print"Average cost of Ferrari per year:"  , "%.2f"%ferrariAnnualCost
        print " "
        print"Average cost of Renault per year:"  , "%.2f"%renaultAnnualCost
        print " "
        print"Average cost of Smart per year:"  , "%.2f"%smartAnnualCost
        print" "
#Here I made an extra work, hope you don't mind, I just tought that what if my program
#will show the cheapest car so the user won't have to compare the prices, maybe the user is lazy:)
#so I made a comparison between the annualCost of each car by using the min function        
    

        if min(a,b,c,d,e)==a:
            print("The cheapest car is Skoda!")
        elif min(a,b,c,d,e)==b:
            print("The cheapest car is Rolls Royce!")
        elif min(a,b,c,d,e)==c:
            print("The cheapest car is Ferrari")
        elif min(a,b,c,d,e)==d:
            print("The cheapest car is Renault")
        elif min(a,b,c,d,e)==e:
            print("The cheapest car is Smart")
           
        break
    except ZeroDivisionError:
        print("Haha, I can not divide by 0. Please enter an owning period bigger than 0!")
#end of program

