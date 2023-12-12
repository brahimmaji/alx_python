def fahrenheit(n):
    return ((float(9)/5)*n + 32)
def celsius(n):
    return (float(5)/9)*(n-32)

temperatures = (36.5, 37, 37.5, 38, 39)

map(fahrenheit,temperatures)
map(celsius,temperatures)

