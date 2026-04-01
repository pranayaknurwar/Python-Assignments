"""
Import sales data of a Cosmetic Company. Analyze it through following ways with visualization using Matplotlib:

a) Read the total profit of all the months and visualize it using a Line Plot.
b) Read all product sales data and show it using a Multiline Plot.
c) Read face cream and face wash product sales data and show it using a Bar chart.
d) Calculate total sale data for last year for each product and show it using a Pie chart.
"""

import matplotlib.pyplot as plt

months = [1,2,3,4,5,6,7,8,9,10,11,12]
total_profit = [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]

facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]

plt.plot(months, total_profit)
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()


plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.legend()
plt.title("Product Sales")
plt.show()


plt.bar(months, facecream)
plt.title("Face Cream Sales")
plt.show()

products = ['Face Cream', 'Face Wash']
sales = [sum(facecream), sum(facewash)]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Yearly Sales")
plt.show()