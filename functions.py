import sqlite3

class Functions:
    @staticmethod
    def bill(item, app_instance):
        lv_single_item_price = 0.00
        # Connect to the SQLite database (creates a new database if not exists)
        conn = sqlite3.connect('virtual_shop.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        cursor.execute("SELECT price FROM items WHERE name = ?", (item,))
        lv_single_item_price, = cursor.fetchone()

        # Update lv_total in the App instance
        app_instance.lv_total += lv_single_item_price
        # Update total display in the App instance
        app_instance.update_total_display()

        # Close the cursor and connection
        cursor.close()
        conn.close()
