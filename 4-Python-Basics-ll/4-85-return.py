def sum_bad(num1, num2): #om funktionen utför någonting, så returneras det automatiskt. Finns inget "return" på logik som inte utför något så returneras inget 
    print('hiii')
    num1 + num2
# En funktion bör göra en sak väldigt bra
# En funktion bör returnera något
# Detta är ett exempel på bad practice. Funktionen gör saker som namnet inte anger.
    
def sum(num1, num2):
    return num1 + num2 

total = (sum(10,5))
print(sum(10,total))