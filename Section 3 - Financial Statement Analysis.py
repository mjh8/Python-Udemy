# Section 3 - Financial Statement Analysis

# Monthly Revenue and Monthly Expenses



# Dataset ->

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]



# Profit (Revenue - Expenses) ->

profit = list([])

for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
profit



# Taxes (Profit x 30%)->

tax = [round(i * 0.3, 2) for i in profit]
tax



# Profit remaining after Tax ->

profit_after_tax = list([])

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i]) #Brackets are Indexing each by i
profit_after_tax    
    


# Profit Margin After Tax ->

profit_margin = list([])

for i in range(0, len(profit)):
    profit_margin.append(profit_after_tax[i] / revenue[i])

profit_margin = [round((i*100), 2) for i in profit_margin]
profit_margin
    


# Profit After Tax

mean_pat = sum(profit_after_tax) / len(profit_after_tax)
mean_pat



# Good Months ->

good_months = list([])

for i in range(0, len(profit)):
    good_months.append(profit_after_tax[i] > mean_pat)
good_months    



# Bad Months ->

bad_months = list([])

for i in range(0, len(profit)):
    bad_months.append(profit_after_tax[i] < mean_pat)
bad_months    



# Best Month ->

best_month = list([])

for i in range(0, len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax)) # Max
best_month
    



# Worst Month ->

worst_month = list([])

for i in range(0, len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax)) # Min
worst_month



# Convert All Calculations To Units of One Thousand Dollars

revenue_1000 = [round(i/1000, 2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 2) for i in profit_after_tax]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]



# Print Results ->

print("Revenue :")
print(revenue_1000)

print("Expenses :")
print(expenses_1000)

print("Profit :")
print(profit_1000)

print("Profit After Tax :")
print(profit_after_tax_1000)

print("Profit Margin :")
print(profit_margin)

print("Good Months :")
print(good_months)

print("Bad Months :")
print(bad_months)

print("Best Month :")
print(best_month)

print("Worst Month :")
print(worst_month)