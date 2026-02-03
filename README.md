
# BurgerVerse 🍔

A full-featured food ordering platform built with Django.

## 🚀 Live Demo
- **Backend Admin**: `http://your-domain.com/admin`
- **Frontend**: `http://your-domain.com`

## 📋 Features

### ✅ Completed
- **User Authentication** - Custom User model with email login
- **Menu Management** - Categories & products with availability toggles
- **Shopping Cart** - Add/remove items, real-time total calculation
- **Order Processing** - Checkout workflow with status tracking
- **Admin Panel** - Full CRUD operations for all models
- **Responsive Design** - Clean, mobile-friendly interface
- **Production Ready** - PostgreSQL, environment variables, security settings

### 🔄 Order Status Lifecycle
1. `PENDING` → Order placed, awaiting confirmation
2. `CONFIRMED` → Order accepted, in preparation
3. `OUT_FOR_DELIVERY` → On the way to customer
4. `DELIVERED` → Order completed
5. `CANCELLED` → Order cancelled (admin only)

## 🏗️ Architecture

### Project Structure
```
BurgerVerse/
├── burgerverse_backend/          # Django project
│   ├── accounts/                 # Authentication app
│   ├── menu/                     # Products & categories
│   ├── orders/                   # Cart & checkout system
│   ├── core/                     # Common pages
│   └── burgerverse_backend/      # Project settings
├── burgerverse_env/              # Virtual environment
├── static/                       # CSS, JS, images
├── templates/                    # HTML templates
├── .env                          # Environment variables
├── requirements.txt              # Python dependencies
├── manage.py                     # Django CLI
└── README.md                     # This file
```

### Database Schema
```
User → Order (One-to-Many)
Category → Product (One-to-Many)
Order → OrderItem (One-to-Many)
Product → OrderItem (One-to-Many)
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip

### Setup Steps

1. **Clone & Enter**
```bash
git clone <repository-url>
cd BurgerVerse
```

2. **Create Virtual Environment**
```bash
python -m venv burgerverse_env
source burgerverse_env/bin/activate  # On Windows: burgerverse_env\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Database Setup**
```bash
# Create PostgreSQL database
createdb burgerverse_db

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

6. **Load Sample Data (Optional)**
```bash
python manage.py runscript seed_data
```

7. **Run Development Server**
```bash
python manage.py runserver
```

## ⚙️ Configuration

### Environment Variables (.env)
```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=burgerverse_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

# Email (for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Production Settings
- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS`
- Set up HTTPS with SSL certificate
- Use production email backend
- Configure static files with CDN/Whitenoise

## 👥 User Roles

### Customer
- Browse menu
- Add items to cart
- Place orders
- View order history

### Admin
- Manage products & categories
- Process orders (update status)
- View sales reports
- Manage users

## 📊 Admin Features

### Product Management
- Add/edit/delete products
- Toggle availability
- Set prices
- Upload product images

### Order Management
- View all orders
- Update order status
- Filter by date/status
- View order details with totals

### User Management
- View registered users
- Reset passwords
- Deactivate accounts

## 🔧 API Endpoints

### Menu API
```
GET     /api/menu/                 # List all products
GET     /api/menu/categories/      # List categories
GET     /api/menu/<id>/           # Product detail
```

### Order API
```
GET     /api/orders/              # User's orders
POST    /api/orders/checkout/     # Create order
GET     /api/orders/<id>/        # Order detail
```

### Cart API
```
GET     /api/cart/                # View cart
POST    /api/cart/add/            # Add item
POST    /api/cart/remove/         # Remove item
```

## 🧪 Testing

### Run Tests
```bash
# All tests
python manage.py test

# Specific app
python manage.py test accounts
```

### Test Coverage
```bash
coverage run manage.py test
coverage report
coverage html  # Generates HTML report
```

## 🚢 Deployment

### Docker Deployment
```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
CMD gunicorn burgerverse_backend.wsgi:application --bind 0.0.0.0:8000
```

### Deployment Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL connection
- [ ] Configure static files (CDN/Whitenoise)
- [ ] Set up HTTPS
- [ ] Configure email backend
- [ ] Set up error logging
- [ ] Create backup strategy

## 📱 Frontend Features

### Responsive Design
- Mobile-first approach
- Bootstrap 5 components
- Custom CSS for branding

### User Experience
- Real-time cart updates
- Order status tracking
- Clean checkout flow
- Order history view

## 🔒 Security

### Implemented Measures
- CSRF protection
- XSS prevention
- SQL injection protection
- Password hashing
- Secure session management
- HTTPS enforcement (production)

### Security Checklist
- [ ] Regular dependency updates
- [ ] Security headers configured
- [ ] Rate limiting on auth endpoints
- [ ] Input validation
- [ ] Output escaping

## 📈 Performance

### Optimization Tips
1. **Database**
   - Add indexes on frequently queried fields
   - Use `select_related` and `prefetch_related`
   - Implement database connection pooling

2. **Caching**
   ```python
   # settings.py
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379',
       }
   }
   ```

3. **Static Files**
   - Use CDN in production
   - Enable compression
   - Set long cache headers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

### Code Style
- Follow PEP 8
- Use Django coding style
- Document complex logic
- Write tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check `.env` credentials
   - Ensure database exists

2. **Static Files Not Loading**
   - Run `collectstatic`
   - Check `STATIC_URL` in settings
   - Verify file permissions

3. **Migration Errors**
   - Delete migration files and database
   - Run `makemigrations` then `migrate`
   - Check model field changes

### Getting Help
- Check existing issues
- Review Django documentation
- Contact project maintainers

## 🎯 Roadmap

### Planned Features
- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Real-time order tracking
- [ ] Customer reviews & ratings
- [ ] Loyalty program
- [ ] Mobile app (React Native)
- [ ] Analytics dashboard
- [ ] Multi-vendor support
- [ ] SMS notifications

### Future Improvements
- GraphQL API
- Microservices architecture
- Machine learning recommendations
- IoT integration for kitchen

## 🙏 Acknowledgments

- Django team for the amazing framework
- Bootstrap for frontend components
- PostgreSQL community
- All contributors and testers

---

**BurgerVerse** - Order your favorite burgers with ease! 🍔🚀

*Last Updated: March 2024*
*Version: 1.0.0*