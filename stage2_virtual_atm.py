balance = 20000
while True:
  user_option = input("Choose an option (balance, withdraw, exit): ").lower().strip()
  if user_option == "balance":
    print(f"Your current balance is: #{balance}")
  elif user_option == "exit":
    print("Goodbye Thanks for using our ATM, have a wonderful day")
    break
  elif user_option == "withdraw":
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount <= balance:
      balance = balance - amount
      print(f"Withdrawal successful! you withdrew: #{amount}")
    else:
      print("Insufficient funds!")
else:
  print("Invalid option! please choose balance, withdraw, or exit.")
