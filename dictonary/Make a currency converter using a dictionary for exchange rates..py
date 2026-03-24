from locale import currency


currency ={
  "usd":1.0,
  "india": 89.90,
  "euro": 0.86,
   "pound":0.76,
   "yen": 113.5,
}
amount_in_usd=int(input("enter the amount in usd : "))
converting_currency=input("enter te currenc you want to covert : ")
if converting_currency in currency:
    converted_amount=amount_in_usd*currency[converting_currency]
    print(f"{amount_in_usd} USD is equal to {converted_amount} {converting_currency}")
else:
  print("currency not found")
amount_to_reconvert = int(input("enter the amount you want to convert : "))
reconvert_the_currency=input("enter the currency you want to reconvert to usd :")
if reconvert_the_currency in currency:
    reconvert_the_currency=amount_to_reconvert/currency[reconvert_the_currency]
    print(f"{amount_to_reconvert} {reconvert_the_currency} is equal to {reconvert_the_currency} USD")