# Signia Home Care Website

A professional, warm, and trustworthy website for Signia Home Care—a Minnesota home care company based in Minneapolis, MN.

## Tech Stack

- **Backend:** Python, Flask
- **Templates:** Jinja2
- **Frontend:** HTML, CSS, optional JavaScript
- **Design:** Mobile-responsive, accessible, SEO-friendly

## Project Structure

```
calendar_web_app/
├── app.py                 # Flask application and routes
├── service_content.py     # Service page copy (Comprehensive Home Care + 245D)
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── static/
│   └── styles.css         # Main stylesheet
│   └── images/            # (Add logo and images here)
└── templates/
    ├── base.html          # Base template
    ├── components/
    │   ├── header.html    # Site header and navigation
    │   └── footer.html    # Site footer
    ├── pages/
    │   ├── home.html      # Homepage
    │   ├── about.html     # About page
    │   ├── services.html  # Main services landing page
    │   ├── referral.html  # Referral page with form
    │   └── contact.html   # Contact page with form
    └── services/
        └── detail.html    # Reusable service detail template
```

## Setup

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # or: source venv/bin/activate   # macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update business information in `app.py`:**
   - Replace placeholder phone: `(555) 123-4567`
   - Replace placeholder email: `hi@signiasolutions.com` (or update in app.py)
   - Update office hours if needed

4. **Add logo and images:**
   - Place logo in `static/images/logo.svg` (or .png)
   - Uncomment the logo `<img>` tag in `templates/components/header.html`

## Run the Site

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Page URLs

| Page | URL |
|------|-----|
| Home | `/` |
| About | `/about/` |
| Services | `/services/` |
| Referral | `/referral/` |
| Contact | `/contact/` |
| Careers | `/careers/` |
| Service detail | `/services/<slug>/` (e.g., `/services/medication-management/`) |

## Form Handling

All form submissions (Contact, Referral, Careers) are emailed to **hi@signiasolutions.com**.

To enable email sending, set these environment variables before running the app:

| Variable | Description | Example |
|----------|-------------|---------|
| `MAIL_USERNAME` | SMTP login email | `your-email@gmail.com` |
| `MAIL_PASSWORD` | SMTP password or app password | (Gmail: use [App Password](https://support.google.com/accounts/answer/185833)) |
| `MAIL_SERVER` | SMTP host (optional) | `smtp.gmail.com` (default) |
| `MAIL_PORT` | SMTP port (optional) | `587` (default) |
| `MAIL_USE_TLS` | Use TLS (optional) | `true` (default) |

Example (Windows PowerShell):
```powershell
$env:MAIL_USERNAME = "your-email@gmail.com"
$env:MAIL_PASSWORD = "your-app-password"
python app.py
```

If `MAIL_USERNAME` and `MAIL_PASSWORD` are not set, forms still submit successfully but no email is sent (a warning is logged).

## Licenses

Content is structured around:
- **Comprehensive Home Care** (Minnesota Department of Health)
- **Basic 245D** (Minnesota Department of Human Services)

Service descriptions use consumer-friendly language and include appropriate disclaimers (e.g., "Services may be available based on assessment, staff availability, and program fit").

## Production Checklist

- [ ] Set `app.secret_key` to a secure random value
- [ ] Set `debug=False` in `app.run()`
- [ ] Add real phone, email, and office hours
- [ ] Add logo and hero images
- [ ] Configure `MAIL_USERNAME` and `MAIL_PASSWORD` for form email delivery
- [ ] Add Google Maps embed on Contact page
- [ ] Consider adding SSL (HTTPS)
