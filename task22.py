#Напишите функцию который будет конвертировать 
# # Фаренгейт в Цельсии и наоборот.
def temp(c):
    cell = c * 2.8
    return cell
def temp2(f):
    far =  f / 2.8
    return far
c = float(input('Celsius :'))
f = float(input('Farengate :'))
print("Celsius-conversion-Farengate -",temp(c))
print("Farengate-conversion-Celsius -",temp2(f))


