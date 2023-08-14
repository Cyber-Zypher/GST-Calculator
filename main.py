import pymysql

# MySQL database configuration
DB_HOST = "localhost"
DB_USER = "UNAME"
DB_PASSWORD = "PASSWD"
DB_NAME = "DB_NAME"

# Connect to the MySQL database
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
cursor = db.cursor()

# Create a transactions table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    vendor_address VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    gst_rate DECIMAL(4, 2) NOT NULL,
    gst_amount DECIMAL(10, 2) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()

def calculate_gst(amount, gst_rate):
    gst_amount = (amount * gst_rate) / 100
    return gst_amount

def record_transaction(vendor_name, vendor_address, amount, gst_rate, gst_amount):
    insert_query = "INSERT INTO transactions (vendor_name, vendor_address, amount, gst_rate, gst_amount) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (vendor_name, vendor_address, amount, gst_rate, gst_amount))
    db.commit()
    print("Transaction recorded successfully!")

def show_transactions():
    select_query = "SELECT id, vendor_name, vendor_address, amount, gst_rate, gst_amount FROM transactions"
    cursor.execute(select_query)
    transactions = cursor.fetchall()
    
    print("\nTransaction History:")
    print("{:<5} {:<20} {:<30} {:<10} {:<10} {:<10}".format("ID", "Vendor Name", "Vendor Address", "Amount", "GST Rate", "GST Amount"))
    print("=" * 85)
    for transaction in transactions:
        print("{:<5} {:<20} {:<30} {:<10} {:<10} {:<10}".format(transaction[0], transaction[1], transaction[2], transaction[3], transaction[4], transaction[5]))

def delete_transaction(transaction_id):
    delete_query = "DELETE FROM transactions WHERE id = %s"
    cursor.execute(delete_query, (transaction_id,))
    db.commit()
    print(f"Transaction with ID {transaction_id} deleted successfully!")

def main():
    while True:
        print("GST Calculator")
        print("1. Calculate GST")
        print("2. Show Transactions")
        print("3. Delete Transaction")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            vendor_name = input("Enter vendor name: ")
            vendor_address = input("Enter vendor address: ")
            amount = float(input("Enter the amount: "))
            gst_rate = float(input("Enter the GST rate (%): "))
            
            gst_amount = calculate_gst(amount, gst_rate)
            print(f"GST Amount: {gst_amount:.2f}")
            
            record_transaction(vendor_name, vendor_address, amount, gst_rate, gst_amount)
        
        elif choice == "2":
            show_transactions()
            
        elif choice == "3":
            transaction_id = int(input("Enter the transaction ID to delete: "))
            delete_transaction(transaction_id)

        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

    db.close()

if __name__ == "__main__":
    main()
