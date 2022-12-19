
USD = 1
EUR = 0.99
SAR = 3.75
EG = 50


print("=================================================")

print("Welcome To $$ EXCHANGE STORE $$$")

print("===================================================")


From = input("Exchange FROM (USD, EUR ,SAR, EG) : ").upper()

Amount = float(input("How much ? "))

To = input("Exchange To (USD, EUR, SAR, EG) : ").upper()

NewAmount = 0

if From == To :
   print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )

elif From == "USD" and To == "EUR":
    NewAmount = Amount * EUR
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )   

elif From == "USD" and To == "SAR":
    NewAmount = Amount * SAR 
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )   

elif From == "EUR" and To == "USD":
    NewAmount = Amount / EUR  * SAR 
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )

elif From == "EUR" and To == "SAR":
    NewAmount = Amount / EUR   
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )

elif From == "SAR" and To == "USD":
    NewAmount = Amount / SAR  
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )  

elif From == "SAR" and To == "EUR":
    NewAmount = Amount * SAR * EUR
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )
    
elif From == "USD" and To == "EG":
    NewAmount = Amount * USD * EG
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )
    
elif From == "EG" and To == "USD":
    NewAmount = Amount * EG * USD
    print(f"You Will give {Amount}  {From}, and you will take {NewAmount} {To}" )
    
else: 
    print("You wrote wrong currency")
 
    
