# Shozaty E-commerce Application

Shozaty is an e-commerce web application that allows users to browse and purchase shoes online. The application includes user authentication, profile management, and a dynamic product ordering system with real-time stock management. The project integrates a user-friendly interface and an admin dashboard for efficient management of orders and customer interactions.

## Features

### For Users:
- **User Registration & Login:** Users can register, log in, and manage their profiles. They can edit their personal information, such as their address and phone number, directly from their profile page.
- **Product Browsing:** Browse a wide variety of shoes categorized by types.
- **Product Details:** Detailed product pages showing the price, available stock, and other shoe details.
- **Order Placement:** Users can place an order by filling out an auto-populated order form with their information. Stock is automatically reduced upon successful order placement.
- **Order Management:** Users can view their past orders and track their order status from their profile page.
  
### For Admin:
- **Admin Panel:** The Django admin panel allows the admin to manage users, products, categories, and orders.
- **Order Status Management:** Admins can view and update the status of customer orders (delivered, in delivery, received) directly from the admin panel.
- **Order Tracking:** Admins can view the order details for each user, including product, total price, and customer contact details.
  
### Key Functionalities:
- **Dynamic Forms:** User profiles and order forms are dynamically populated based on logged-in user data.
- **Stock Management:** Real-time stock updates on product purchase.
- **Customizable Order Flow:** Orders automatically transition through status changes (from "Pending" to "In Delivery" and "Delivered").

## Project Structure

```bash
Shozaty/
├── categories/      # App handling shoe categories
├── products/        # App managing products (shoes) and order handling
├── profiles/        # App handling user authentication, profiles, and user info management
├── store/           # App for the landing page and homepage functionality
├── templates/       # HTML templates for rendering UI
├── static/          # CSS, JS, images, and other static files
├── shozaty/         # Main project directory
└── manage.py        # Django management file
```

## Tech Stack

- **Frontend:**
  - HTML/CSS (for designing user-friendly pages)
  - JavaScript (for basic interactivity)
- **Backend:**
  - Python 3.x
  - Django (Web framework for rapid development)
- **Database:**
  - SQLite (default Django database, easy to set up and manage for development)
- **Version Control:**
  - Git & GitHub for source code management

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shozaty.git
   cd shozaty
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Apply migrations and create superuser for admin access:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the app at `http://127.0.0.1:8000/` and the admin panel at `/admin/`.

## How to Use

- **For Users:**
  1. Register or log in to access all functionalities.
  2. Browse the catalog of shoes and click on any product to see details.
  3. Click "Order Now" to place an order and fill out the order form.
  4. View past orders and their status from your profile page.

- **For Admin:**
  1. Log in to the admin panel (`/admin/`) using your superuser account.
  2. Manage products, categories, and orders from the Django admin interface.
  3. Update order statuses to keep users informed about their purchases.

## Future Improvements

- **Payment Integration:** Implementing payment gateway integration for a more complete e-commerce experience.
- **Search and Filtering:** Adding advanced search and filtering capabilities for product discovery.
- **Order Tracking:** Adding real-time order tracking with notifications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
