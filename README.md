# 🚀 Adruva Creation - Digital Marketing Agency Website

A modern, responsive Django-based website for **Adruva Creation**, a digital marketing agency specializing in performance marketing, social media management, and creative campaigns.

## 🎯 Features

### 🏠 Homepage
- Hero section with compelling call-to-action
- Featured services showcase (top 3)
- Portfolio highlights (top 3 projects)
- Client testimonials (top 4 approved feedback)
- Why choose us section with 4 key benefits
- Ready-to-scale CTA section

### 📋 Services
- Full services listing page
- Individual service detail pages
- Service icons and descriptions
- Service images for visual appeal

### 🎨 Portfolio
- Complete portfolio showcase
- Project case studies with results metrics
- Client information and project details
- Portfolio detail page for each project
- Visual portfolio management

### 💬 Testimonials
- Display approved client testimonials
- Star rating system (1-5 stars)
- Client name and company info
- Add feedback form for visitors
- Admin moderation before publishing

### 📧 Contact & Forms
- Contact form (name, email, phone, message)
- Feedback/testimonial submission form
- Form submissions stored in database
- Admin panel for managing submissions

### 🎨 Design
- **Tailwind CSS** - Modern, responsive design
- **Dark Theme** - Professional slate/purple color scheme
- **Mobile Responsive** - Works on all devices
- **Smooth Animations** - Hover effects and transitions
- **Inter Font** - Clean typography

## 📁 Project Structure

```
Adruva_creation/
├── agency/                 # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI app
│   └── asgi.py            # ASGI app
├── core/                   # Main app
│   ├── models.py          # Database models (Service, Portfolio, Testimonial, Contact)
│   ├── views.py           # View handlers
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin configuration
│   ├── migrations/        # Database migrations
│   └── templates/         # HTML templates
│       ├── base.html      # Base template (navbar, footer)
│       ├── home.html      # Homepage
│       ├── services.html  # Services list
│       ├── portfolio.html # Portfolio list
│       ├── contact.html   # Contact page
│       ├── add_feedback.html
│       └── ...
├── static/                # Static files (CSS, JS, images)
├── media/                 # Uploaded images
├── manage.py              # Django CLI
├── requirements.txt       # Python dependencies
└── db.sqlite3            # SQLite database
```

## 🛠️ Tech Stack

- **Backend:** Django 5.1.5
- **Database:** SQLite (development) / PostgreSQL (production-ready)
- **Frontend:** Tailwind CSS 3
- **Image Processing:** Pillow 10.1.0
- **Python:** 3.11+

## 📋 Requirements

- Python 3.11 or higher
- pip (Python package manager)
- Git

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/adruva-creation.git
cd adruva-creation
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
# Follow prompts to set username, email, password
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The website will be available at: **http://127.0.0.1:8000**

Admin panel at: **http://127.0.0.1:8000/admin**

## 📦 Dependencies

```
Django==5.1.5           # Web framework
Pillow==10.1.0         # Image processing
asgiref==3.8.1         # ASGI server
sqlparse==0.5.5        # SQL parser
tzdata==2025.3         # Timezone database
```

## 🗂️ Database Models

### Service
- `title` - Service name
- `short_description` - Quick summary
- `description` - Full description
- `icon` - Icon class (Font Awesome, etc.)
- `image` - Service image
- `created_at` - Creation timestamp

### Portfolio
- `title` - Project name
- `client_name` - Client company
- `short_description` - Project summary
- `description` - Full project details
- `image` - Portfolio image
- `results` - Results metrics (e.g., "3x ROAS, 200 Leads")
- `created_at` - Creation timestamp

### Testimonial
- `name` - Client name
- `company` - Client company
- `message` - Testimonial text
- `rating` - Star rating (1-5)
- `image` - Client photo
- `is_approved` - Admin approval flag
- `created_at` - Creation timestamp

### Contact
- `name` - Visitor name
- `email` - Email address
- `phone` - Phone number
- `message` - Contact message
- `created_at` - Creation timestamp

## 🔗 URL Routes

| Route | Purpose |
|-------|---------|
| `/` | Homepage |
| `/services/` | All services |
| `/services/<id>/` | Service detail |
| `/portfolio/` | All portfolio items |
| `/portfolio/<id>/` | Portfolio detail |
| `/testimonials/` | All testimonials |
| `/add-feedback/` | Add testimonial form |
| `/contact/` | Contact form |
| `/admin/` | Admin panel |

## 🎯 Usage

### Add a Service
1. Go to `/admin/`
2. Click "Services" 
3. Click "Add Service"
4. Fill in details and save

### Add Portfolio Item
1. Go to `/admin/`
2. Click "Portfolios"
3. Click "Add Portfolio"
4. Include results metrics for case study

### Manage Testimonials
1. Go to `/admin/`
2. Click "Testimonials"
3. Check `is_approved` to publish a testimonial
4. Visitors can submit via `/add-feedback/`

### View Contact Messages
1. Go to `/admin/`
2. Click "Contacts" to see all submissions

## 🚢 Deployment Guide

### Heroku Deployment
```bash
# Install Heroku CLI first

# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secure-key

# Deploy
git push heroku main
```

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Update `ALLOWED_HOSTS` with domain
- [ ] Use environment variables for secrets
- [ ] Switch to PostgreSQL database
- [ ] Configure static files collection
- [ ] Set up email backend for forms
- [ ] Enable HTTPS
- [ ] Configure CSRF_TRUSTED_ORIGINS

## 🔐 Security Notes

⚠️ **Development Only:** Current settings are for development. Before deploying:

1. Generate new `SECRET_KEY`
2. Set `DEBUG = False`
3. Configure proper `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Set up environment variables (`.env` file)
6. Enable HTTPS

## 👥 Contributing

1. Clone the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make changes and commit (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature/your-feature`)
5. Create a Pull Request

## 📧 Contact & Support

- **Website:** adruva-creation.com
- **Email:** info@adruva.com
- **Phone:** +91 98765 43210
- **Location:** New Delhi, India

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Built with Django and Tailwind CSS
- Icons from Font Awesome
- Fonts from Google Fonts

---

**Last Updated:** February 19, 2026  
**Version:** 1.0.0  
**Status:** ✅ Production Ready
