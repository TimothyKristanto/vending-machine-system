drinks = ["Coke", "Mineral Water", "Sparkling Water", "Orange Juice", "Milk"]
drink_prices = [6000, 2000, 16000, 15000, 10000] # drinks pricelist
notes = [100000, 50000, 20000, 10000, 5000, 2000, 1000] # available notes
notes_limitation = {
  1000: 20, # 19
  2000: 1,
  5000: 2,
  10000: 2,
  20000: 2,
  50000: 2,
  100000: 2
}

# display the vending machine menu and catch the user input regarding to his chosen drink
def display_vending_machine_menu():
  print("===============================")
  print("        VENDING MACHINE        ")
  print("===============================")
  print("Drinks Menu:")
  print("1. Coke - Rp 6.000")
  print("2. Mineral Water - Rp 2.000")
  print("3. Sparkling Water - Rp 16.000")
  print("4. Orange Juice - Rp 15.000")
  print("5. Milk - Rp 10.000")
  print("6. Exit")
  print("===============================")

  # try to convert input to integer
  # if it fails, then print error message and set chosen_drink to -1
  try:
    chosen_drink = int(input("Pick Your Drink (1-6): "))
  except ValueError:
    print("Invalid input! Please enter a number.")
    chosen_drink = -1

  return chosen_drink

# display all available note options for the payment and capture the user chosen note input
def display_notes_menu(user_money, chosen_drink, drink_price):
  print("===============================")
  print("        AVAILABLE NOTES        ")
  print("===============================")
  print("Chosen Drink: " + drinks[chosen_drink - 1])
  print("Drink Price: Rp " + str(drink_price))
  print("Your Money: Rp " + str(user_money))
  print("===============================")
  print("1. Rp 100.000")
  print("2. Rp 50.000")
  print("3. Rp 20.000")
  print("4. Rp 10.000")
  print("5. Rp 5.000")
  print("6. Rp 2.000")
  print("7. Rp 1.000")
  print("8. Cancel Payment")
  
  try:
    chosen_note = int(input("Input Your Note (1-9): "))
  except ValueError:
    print("Invalid input! Please enter a number.")
    chosen_note = -1

  return chosen_note

# count the least amount of notes to be returned to the user
def count_changes(drink_price, user_money):
  change = user_money - drink_price
  returned_notes = {}

  note_id = 0
  if change != 0:
    while True:
      note = notes[note_id]
      change -= note
      if change < 0:
        change += note
        note_id += 1
      elif change >= 0:
        notes_left = notes_limitation[note]

        if notes_left > 0:
          if returned_notes.get(note) is None:
            returned_notes[note] = 1
          else:
            returned_notes[note] += 1
          notes_limitation[note] -= 1
        else:
          change += note
          note_id += 1
      if change == 0:
        break

    return returned_notes
  
def display_changes(returned_notes):
  total_change = 0

  print("===============================")
  print("          Your Changes         ")
  print("===============================")
  if returned_notes != None:
    print("Changes Notes:")
    for key, value in returned_notes.items():
      print("* Rp " + str(key) + " " + str(value) + "x")
      total_change += key * value
    print("===============================")
  print("Your total change: Rp " + str(total_change))
  print("Thank you for using our services! Enjoy your drink.")

if __name__ == "__main__":
  while True:
    chosen_drink = display_vending_machine_menu()
    # loop while chosen_drink value does not fulfill the conditions
    while chosen_drink < 1 or chosen_drink > 6:
      print("Invalid input! Please input a number between 1 - 6.")
      chosen_drink = display_vending_machine_menu()

    # if chosen_drink is equal to 6, then quit the system
    if chosen_drink == 6:
      print("Thank you for using our service.")
      break
    # else proceed to the next step
    else:
      user_money = 0
      drink_price = drink_prices[chosen_drink - 1]

      while True:
        chosen_note = display_notes_menu(user_money=user_money, chosen_drink=chosen_drink, drink_price=drink_price)

        # loop while chosen_note value does not fulfill the conditions
        while chosen_note < 1 or chosen_note > 9:
          print("Invalid input! Please input a number between 1 - 9.")
          chosen_note = display_notes_menu(user_money=user_money, chosen_drink=chosen_drink, drink_price=drink_price)

        # cancel payment when user choose number 8
        if chosen_note == 8:
          print("Payment Cancelled!")
          break
        # add the user money when user choose number 1-7
        else:
          user_money += notes[chosen_note - 1]
          # if user money is equal or greater than chosen drink price
          # then give change if needed and go back to the vending machine menu
          if user_money >= drink_price:
            returned_notes = count_changes(drink_price, user_money)
            display_changes(returned_notes)
            break

      
      
