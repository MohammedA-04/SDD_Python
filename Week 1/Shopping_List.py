#Shoping Cart Exercise

Flowerpot_QTY = int(input('QtyFlowerpots?'))
Seeds_QTY = int(input('QtySeeds?'))
Soil_QTY = int(input('QtySoil?'))
Flowerpot_Price = 4.00
Seeds_Price = 1.00
Soil_Price = 5.00
Tax_Rate = 0.06

Cost_of_items = (Flowerpot_QTY * Flowerpot_Price) + (Seeds_QTY * Seeds_Price) + (Soil_QTY * Soil_Price)

# Total_Cost = (Cost_of_items + Tax_Rate)
Total_Cost = (Cost_of_items * Tax_Rate) + Cost_of_items

print(f'The Cost of the items are : £{Cost_of_items}')
print(f'Total Cost incl VAT TAX : £{Total_Cost}')