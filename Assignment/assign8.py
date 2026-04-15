# *Assignment (28/02/2026)*

# *Assignment Name* : Storytelling with Graphs
# *Description* : Create bar chart, pie chart, histogram and write a short data story explaining trends..



import matplotlib.pyplot as plt

names = ["Amit", "Riya", "John", "Sara", "Rahul"]
marks = [85, 90, 75, 88, 95]

plt.bar(names, marks)
plt.title("Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.pie(marks, labels=names, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

plt.hist(marks, bins=5)
plt.title("Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()