# -*- coding: utf-8 -*-
X=int(input())
Y=float(input())
def car_average_consumption(X,Y):
    return(X/Y)
average=car_average_consumption(X,Y)
print(f"{average:.3f} km/l")