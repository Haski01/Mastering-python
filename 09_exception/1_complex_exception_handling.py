def withdraw_money(balance, amount):
    try:
        print(f"Trying to withdraw ₹{amount}...")

        # Raise error if insufficient balance
        if amount > balance:
            raise ValueError("Insufficient funds!")

    except ValueError as e:
        # Handle specific error
        print("❌ Transaction failed:", e)

    else:
        # Runs only if no exception
        balance -= amount
        print(f"✅ Transaction successful. Remaining balance: ₹{balance}")

    finally:
        # Always runs (cleanup or closing connections in real-world)
        print("🏦 Thank you for banking with us!\n")

    return balance


# ------------------ USAGE ------------------

balance = 1000

# Successful withdrawal
balance = withdraw_money(balance, 500)

# Failed withdrawal (exception triggered)
balance = withdraw_money(balance, 2000)


# Explanation
"""
try → Attempts to withdraw money.

raise ValueError → If balance is insufficient.

except → Handles the error gracefully.

else → Runs only if no error (deducts amount).

finally → Always executes (good for cleanup/logs).
"""