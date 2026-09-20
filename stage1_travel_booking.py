print("Welcome to Nigeria's only Smart Travel Booking Agent")

user_dest = input("Enter your destination (Lagos, Abuja, Ibadan): ").lower().strip()
travel_class = input("Do you want Economy or Business class?: ").lower().strip()
promo_code = input("Enter promo code (Press Enter if none): ").upper().strip()

price = 0
valid_booking = True

if user_dest == "lagos":
    if travel_class == "economy":
        price = 30000
    elif travel_class == "business":
        price = 70000
    else:
        print("Invalid class selected.")
        valid_booking = False
        
elif user_dest == "abuja":
    if travel_class == "economy":
        price = 50000
    elif travel_class == "business":
        price = 110000
    else:
        print("Invalid class selected.")
        valid_booking = False

elif user_dest == "ibadan":
    if travel_class == "economy":
        price = 15000
    elif travel_class == "business":
        price = 40000
    else:
        print("Invalid class selected.")
        valid_booking = False
else:
    print("Invalid destination selected.")
    valid_booking = False

if valid_booking:
    if promo_code == "CAMPUS26":
        print("Promo code applied! You get a ₦5,000 discount.")
        price = price - 5000
    
    print("\n--- BOOKING SUMMARY ---")
    print(f"Destination: {user_dest.title()}")
    print(f"Class: {travel_class.title()}")
    print(f"Total Ticket Price: ₦{price:,}")
