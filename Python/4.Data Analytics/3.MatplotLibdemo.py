import numpy as n
import matplotlib.pyplot as p

x1=n.array([2013,2014,2015,2016])
y1=n.array([25,50,5,75])
p.plot(x1,y1,marker='*',markersize=10,markerfacecolor='red',)
p.title("Sales Data")
p.xlabel("year")
p.ylabel("sales")
# p.xticks(x1)
# p.yticks(y1)
# p.show()

x2=n.array([2013,2014,2015,2016])
y2=n.array([5,50,62,75])
p.plot(x2,y2,marker='*',markersize=10,markerfacecolor='red',)
p.title("Sales Data")
p.xlabel("year")
p.ylabel("sales")
p.xticks(x2)
p.yticks(y2)
p.show()


#GridLines

p.grid()
p.show()


