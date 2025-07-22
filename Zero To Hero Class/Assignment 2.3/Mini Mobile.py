"""
Create a Python program that simulates a mini mobile app with the following superhero features:

        Recharge your phone number with any network (MTN, Glo, Airtel, 9mobile – yes, no discrimination here 😄).

        Share airtime with friends, family, or that one cousin who always asks at the worst time.

        Share mobile data too—because sharing is caring, right?

Bonus Points if:

    Your app has menus or prompts that feel like a real user interface.

    You handle “invalid input” like a pro (even if someone tries to recharge with ₦5 million 😅).

    You add a bit of fun to your messages/output (think: "You just recharged like a boss!" 💸)

"""

#Solution to the mini mobile app with superhero features
#Thought process:
#1. Create a simple menu-driven program that allows users to recharge, share airtime,
#   share data, and handle invalid inputs gracefully.

import time

# Superhero-themed mobile app
def superhero_mobile_app():
    balance = {"airtime": 0, "data": 0}  # Default balance
    networks = ["MTN", "Glo", "Airtel", "9mobile"]
    
    print("\n🦸 Welcome to **Superhero Mobile App**! 🦸")
    print("----------------------------------------")
    
    while True:
        print("\n🔹 Main Menu:")
        print("1. Recharge Airtime 💰")
        print("2. Share Airtime 🎁")
        print("3. Share Data 📶")
        print("4. Check Balance 📱")
        print("5. Exit 🚪")
        
        choice = input("\nChoose your superpower (1-5): ")
        
        # 1. Recharge Airtime
        if choice == "1":
            print("\n⚡ Recharge Airtime ⚡")
            print("Available Networks:", ", ".join(networks))
            
            network = input("Choose network: ").strip().title()
            if network not in networks:
                print("🚨 Invalid network! Try again.")
                continue
            
            #Handles the recharge amount and checks for valid input
            try:
                amount = float(input("Enter amount (₦): "))
                if amount <= 0:
                    print("🚨 Amount must be positive!")
                elif amount > 5_000_000:
                    print("😅 Whoa! Even superheroes have limits. Try a smaller amount.")
                else:
                    balance["airtime"] += amount
                    print(f"\n✅ Success! ₦{amount:,.2f} added to {network}.")
                    print("💸 You just recharged like a boss!")
            except ValueError:
                print("🚨 Invalid amount! Enter numbers only.")
        
        # 2. Share Airtime
        elif choice == "2":
            print("\n🎁 Share Airtime 🎁")
            if balance["airtime"] <= 0:
                print("😢 Oops! Your airtime balance is ₦0. Recharge first!")
                continue
            
            try:
                amount = float(input("Enter amount to share (₦): "))
                if amount <= 0:
                    print("🚨 Amount must be positive!")
                elif amount > balance["airtime"]:
                    print(f"🚨 Insufficient balance! (Current: ₦{balance['airtime']:,.2f})")
                else:
                    recipient = input("Enter recipient's number: ").strip()
                    if len(recipient) != 11 or not recipient.isdigit():
                        print("🚨 Invalid phone number! Use 11 digits (e.g., 08012345678).")
                    else:
                        balance["airtime"] -= amount
                        print(f"\n✅ Sent ₦{amount:,.2f} to {recipient}!")
                        print("🦸 Superhero move! You saved their day!")
            except ValueError:
                print("🚨 Invalid amount! Enter numbers only.")
        
        # 3. Share Data
        elif choice == "3":
            print("\n📶 Share Data 📶")
            if balance["data"] <= 0:
                print("😢 Oops! No data to share. Buy data first!")
                continue
            
            #Handles the data sharing amount and checks for valid input
            try:
                mb = float(input("Enter MB to share: "))
                if mb <= 0:
                    print("🚨 MB must be positive!")
                elif mb > balance["data"]:
                    print(f"🚨 Insufficient data! (Current: {balance['data']} MB)")
                else:
                    recipient = input("Enter recipient's number: ").strip()
                    if len(recipient) != 11 or not recipient.isdigit():
                        print("🚨 Invalid phone number! Use 11 digits.")
                    else:
                        balance["data"] -= mb
                        print(f"\n✅ Sent {mb} MB to {recipient}!")
                        print("🌐 Data shared like a true hero!")
            except ValueError:
                print("🚨 Invalid input! Enter numbers only.")
        
        # 4. Check Balance
        elif choice == "4":
            print("\n📱 Your Super Balance:")
            print(f"💰 Airtime: ₦{balance['airtime']:,.2f}")
            print(f"📶 Data: {balance['data']} MB")
            print("🦸 Keep being awesome!")
        
        # 5. Exit
        elif choice == "5":
            print("\n🚪 Exiting...")
            print("Thanks for using Superhero Mobile App! 🦸")
            break
        
        # Invalid choice
        else:
            print("\n🚨 Invalid choice! Pick 1-5.")
        
        time.sleep(1)  # Small delay for better UX

# Run the app!
if __name__ == "__main__":
    superhero_mobile_app()