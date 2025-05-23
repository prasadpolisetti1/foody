<h1>🛒 Foody Flask App</h1>

<p >
  A modern, full-featured supermarket web application built with <strong>Flask</strong> and <strong>MongoDB</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask" alt="Flask Version">
  <img src="https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb" alt="MongoDB">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 🌟 Features

- 🔐 **User Authentication** — Sign up / login with role-based access (Admin / User)
- 🛍️ **Product Browsing** — Add items to cart and search for products
- 🛒 **Cart & Checkout** — Manage shopping cart and place orders
- 🚚 **Order Tracking** — View order status: Ordered → Shipped → Delivered
- 🧑‍💼 **Admin Panel** — Manage products and view all orders

---

## 🛠️ Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| 🧠 Backend     | Python (Flask)     |
| 🎨 Frontend    | HTML, CSS, JS      |
| 🗄️ Database    | MongoDB (Local)    |
| 📦 Deployment | *Run locally*      |

---

## 🧑‍💻 Getting Started

### 📁 Clone the Repository
bash
git clone https://github.com/prasadpolisetti1/foody.git
cd supermarket

---
### 🐍Create a Virtual Environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

### 📦 Install Dependencies
pip install -r requirements.txt

### 🗄️ Make Sure MongoDB is Running Locally
The app connects to the default MongoDB URI:
mongodb://localhost:27017/

### ▶️ Run the App
python app.py
Open http://localhost:5000 in your browser.

### 📂Project Structure 
supermarket/
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── app.py               # Flask application
├── requirements.txt     # Project dependencies
└── README.md            # Project overview

## 📸 Screenshots

### 🔐 Login Page
![Login Page](https://github.com/user-attachments/assets/77a14bc7-f48f-4a3f-9b51-6087cd3a0c61)

### 🏠 User Homepage
![User Homepage](https://github.com/user-attachments/assets/3d1d4f49-7d38-4484-b1e0-f4c58d8a966b)

### 🛍️ Products Page
![Products Page](https://github.com/user-attachments/assets/c9c1656f-9889-49ae-9fdc-5cd01420da6b)

### 🛒 Cart
![Cart](https://github.com/user-attachments/assets/bb2999dc-8346-4c08-a8cc-47ad12d476b3)

### 📦 Orders
![Orders](https://github.com/user-attachments/assets/b2b5de9f-184d-47ff-be37-c1a59bdf6623)

### 🧑‍💼 Admin Home
![Admin Home](https://github.com/user-attachments/assets/05dcfc79-b13a-484e-a265-cd943b2f84a1)

### ➕ Admin Add New Products
![Admin Add](https://github.com/user-attachments/assets/96bee237-ff13-4753-b266-b838089c4600)

### 👤 Profile
![Profile](https://github.com/user-attachments/assets/4106a4d0-2118-4683-92fa-10d4b9ba7263)

### 🤝 Contributing
Pull requests are welcome!
If you find a bug or have a feature request, open an issue first to discuss it.
