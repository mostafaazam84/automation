CM = 1
INSH = 2.54

From = input ("Exchinge (CM, INSH): ").upper()

height = int(input("How Long ? : "))

To = input("Exchange To (CM, INSH ) : ").upper()

NewLong = 0

if From == To :
   print(f" {height}  {From} = {NewLong} {To}" )

elif From == "CM" and To == "INSH":
     NewLong= height / INSH
     print(f" {height}  {From} ===>> {NewLong} {To}" )   

elif From == "INSH" and To == "CM":
     NewLong= height * INSH
     print(f" {height}  {From} ===>> {NewLong} {To}" ) 
else: 
 print("You wrote wrong currency")


