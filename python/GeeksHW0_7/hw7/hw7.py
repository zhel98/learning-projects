import sqlite3

# connect = connect to database
# cursor = edit
# commit = типа чета git push без него данные не будут обновляться

#A4
connect = sqlite3.connect("store.db")
#рука с ручкой 
cursor = connect.cursor()

cursor.execute('''
           CREATE TABLE IF NOT EXISTS products(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(50) NOT NULL,
           price INTEGER NOT NULL,
           quantity INTEGER NOT NULL
        )       
''')
connect.commit()


#CRUD

def create_product(name,price,quantity): #---Create---#
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES(?,?,?)',
        (name,price,quantity)
        )
    print("Новый товар успешно добавлен!")
    connect.commit()


def read_products(): #---Read---#
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    print(f'{data}')


def update_product(id,price):
    cursor.execute(
        'UPDATE products SET price =? WHERE id = ?',
        (price, id)
        )
    connect.commit()
    print("Price updated")


def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id=?',
        (id,)
    )
    connect.commit()
    print("Product deleted")
  
    
# delete_product(2)
# update_product(2,25)   
# create_product("bread", 20, 1)
# read_products()   