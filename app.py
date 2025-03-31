from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def is_admin():
    return session.get('role') == 'admin'

# MongoDB connection
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['supermarket']
users = db['users']
products_collection = db['products']
orders_collection = db['orders']  # Assuming you have an 'orders' collection

@app.route("/")
def home():
    return render_template("Login.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    selected_role = request.form.get("role")  # Get the selected role from the form

    user = users.find_one({"username": username})

    if user and user["password"] == password:
        actual_role = user.get("role", "user")  # Default role is 'user'
        
        if selected_role == "admin" and actual_role != "admin":
            return render_template("Login.html", status="You are not an admin!.")
        
        session['username'] = username
        session['role'] = actual_role  
        
        if actual_role == "admin":
            return redirect(url_for('adminindex'))
        else:
            return redirect(url_for('index'))
    
    return render_template("Login.html", status="Invalid Credentials")




@app.route("/Signup")
def signup():
    return render_template("Signup.html")

@app.route("/Signup", methods=['POST'])
def Signup():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role", "user")  # Default role is 'user'

    # Ensure only an admin can create another admin
    if role == "admin":
        if "username" not in session or not is_admin():
            return render_template("Signup.html", status="Only admins can create admin accounts.")

    user = users.find_one({"username": username})
    if user:
        return render_template("Signup.html", status="Username Already Exists")

    # Insert the new user with a role
    users.insert_one({"username": username, "email": email, "password": password, "role": role})
    return render_template("Signup.html", status="Registration Successful")


# Product List Route
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/product')
def product_list():
    products = list(products_collection.find())  # Convert cursor to list
    return render_template('product.html', products=products)

# Add to Cart Route
@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    product = products_collection.find_one({'_id': ObjectId(product_id)})  # Ensure _id is of the right type
    if 'cart' not in session:
        session['cart'] = []
   
    if product:
        # Add product details to the cart
        session['cart'].append({
            'id': str(product['_id']),
            'name': product['name'],
            'price': product['price'],
            'original_price': product['original_price'],
            'image': product['image']
        })
        session.modified = True  # Mark session as modified to ensure it is saved

    return redirect(url_for('cart'))  # Redirect to the cart page

# Route to display the Add Product page
@app.route('/add_products', methods=['GET'])
def add_product_page():
    return render_template('add_products.html')

# Route to handle the form submission for adding products
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    original_price = float(request.form['original_price'])
    image = request.form['image']
    description = request.form['description']

    # Insert the new product into the database
    products_collection.insert_one({
        'name': name,
        'price': price,
        'original_price': original_price,
        'image': image,
        'description': description
    })

    return redirect(url_for('adminproduct'))  # Redirect to the admin product page


# Cart Route
@app.route('/cart')
def cart():
    return render_template('cart.html', cart=session.get('cart', []))

# Route to handle ordering an item
@app.route('/order_item/<item_id>')
def order_item(item_id):
    item_to_order = None
    
    # Find the item in the cart to order it
    for item in session.get('cart', []):
        if item['id'] == item_id:
            item_to_order = item
            break
    
    if item_to_order:
        # Save the ordered item to the orders collection
        orders_collection.insert_one(item_to_order)  # Save the ordered item
        
        # Optional: Remove the item from the cart after ordering
        session['cart'] = [item for item in session.get('cart', []) if item['id'] != item_id]
        session.modified = True  # Mark session as modified to save changes

    return redirect(url_for('orders'))  # Redirect to orders page

# Route to handle canceling an item
@app.route('/cancel_item/<item_id>')
def cancel_item(item_id):
    # Remove the item from the cart
    session['cart'] = [item for item in session.get('cart', []) if item['id'] != item_id]
    session.modified = True  # Mark session as modified to save changes
    return redirect(url_for('cart'))  # Redirect back to the cart page

# Orders Route
@app.route("/orders")
def orders():
    orders = list(orders_collection.find())  # Get all orders
    return render_template("orders.html", orders=orders)

@app.route("/aboutus")
def about():
    return render_template("aboutus.html")

@app.route('/profile')
def profile():
    if 'username' in session:
        user = users.find_one({'username': session['username']}, {'_id': 0, 'username': 1, 'email': 1})  # Only fetch username and email
        if user:
            return render_template('profile.html', user=user)
    return redirect(url_for('login'))


@app.route("/adminindex")
def adminindex():
    if not is_admin():
        return redirect(url_for('home'))  # Redirect non-admins to login
    return render_template("Adminindex.html")

@app.route("/adminproduct")
def adminproduct():
    if not is_admin():
        return redirect(url_for('home'))
    products = list(products_collection.find())
    return render_template("adminproduct.html", products=products)

@app.route('/delete_product/<product_id>', methods=['POST'])
def delete_product(product_id):
    products_collection.delete_one({'_id': ObjectId(product_id)})  # Delete the product from the database
    return redirect(url_for('delete_product'))  # Redirect back to the delete products page

@app.route("/delete_product")
def delete_products():
    products = list(products_collection.find())  # Fetch all products
    return render_template("delete_product.html", products=products)

if not users.find_one({"username": "admin"}):
    users.insert_one({"username": "admin", "email": "admin@example.com", "password": "chanti", "role": "admin"})
    print("Default admin created: Username - admin, Password - chanti")


# Run the application
if __name__ == "__main__":
    app.run(port=5900, debug=True)