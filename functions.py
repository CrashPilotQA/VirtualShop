import sqlite3

class Functions:
    def bill(self, item, app_instance):
        lv_single_item_price = 0.00
        # Connect to the SQLite database (creates a new database if not exists)
        conn = sqlite3.connect('virtual_shop.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM items WHERE name = ?", (item,))
        result = cursor.fetchone()

        if result:
            # Extract values from the result tuple
            lv_item_id, lv_item_name, lv_item_price, lv_stock_quantity = result
            if lv_stock_quantity == 0:
                app_instance.update_oostock_message(f'We are out of {lv_item_name}s I am afraid')
            else:
                app_instance.update_oostock_message('')
                lv_stock_quantity -= 1
                # After decrementing lv_stock_quantity
                cursor.execute("UPDATE items SET stock_quantity = ? WHERE id = ?", (lv_stock_quantity, lv_item_id))
                conn.commit()
                print(lv_stock_quantity)

                # Update lv_total in the App instance
                app_instance.lv_total += lv_item_price
                # Update total display in the App instance
                app_instance.update_total_display()

        # Close the cursor and connection
        cursor.close()
        conn.close()
