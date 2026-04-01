"""
Import a dataset of new recruitments in companies such as Microsoft, Google, Amazon, IBM, Deloitte, Capgemini, ATOS Origin, Amdocs etc.

Generate & visualize reports of new recruitments using:

a) Bar Chart
b) Pie Chart
c) Customize Pie Chart
d) Doughnut Chart

Compare the new recruitments in IBM & Amdocs using visualization.
"""

import matplotlib.pyplot as plt

companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','Amdocs']
recruitments = [120,150,180,90,110,130,80]

plt.bar(companies, recruitments)
plt.title("Company Recruitments")
plt.xticks(rotation=30)
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%', startangle=90)
plt.title("Customized Pie Chart")
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.5,color='white')
plt.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

compare = ['IBM','Amdocs']
values = [90,80]

plt.bar(compare, values)
plt.title("IBM vs Amdocs Recruitment")
plt.show()