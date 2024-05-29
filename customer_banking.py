# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from Account import Account
from savings_account import create_savings_account
from cd_account import create_cd_account  

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("\nEnter your savings balance ($): "))
    savings_interest = float(input("Enter interest rate (%): "))
    savings_maturity = int(input("Enter maturity (months): "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest Earned: $",format(interest_earned,",.3f"), "Updated Savings Balance: $", format(updated_savings_balance,",.3f"))
    print("...................\n")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE5000
    cd_balance = float(input("Enter cd Balance($): "))
    cd_interest = float(input("Enter cd interest(%): "))   
    cd_maturity = int(input("Enter cd maturity in Months: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
  #  print(f"CD Updated Balance: ${updated_cd_balance:,.3f}, CD Interest Earned: ${interest_earned:,.3f}" )
    print(f"CD Updated Balance: $",format(updated_cd_balance,",.3f"), "CD Interest Earned: $", format(interest_earned,",.3f"))

if __name__ == "__main__":
    # Call the main function.
    main()