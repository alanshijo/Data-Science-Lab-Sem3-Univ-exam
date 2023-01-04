import matplotlib.pyplot as plt

year = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
value = [24000, 22500, 19700, 17500, 15600, 12700, 10500]

plt.title("Dollar values in each year from 2001")
plt.xlabel("Year")
plt.ylabel("Dollar value")
plt.plot(year, value)
plt.show()