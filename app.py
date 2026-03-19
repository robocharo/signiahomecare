"""
Signia Home Care - Minnesota Home Care Company Website
Flask application with Jinja templates.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "signia-home-care-secret-key-change-in-production"

# Email configuration - set these environment variables for production
FORM_EMAIL_TO = "hi@signiasolutions.com"
MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"


def send_form_email(subject: str, body: str) -> bool:
    """Send form submission to hi@signiasolutions.com. Returns True if sent successfully."""
    if not MAIL_USERNAME or not MAIL_PASSWORD:
        app.logger.warning("Email not configured: set MAIL_USERNAME and MAIL_PASSWORD environment variables")
        return False
    try:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = MAIL_USERNAME
        msg["To"] = FORM_EMAIL_TO
        msg.attach(MIMEText(body, "plain"))
        with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
            if MAIL_USE_TLS:
                server.starttls()
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.sendmail(MAIL_USERNAME, FORM_EMAIL_TO, msg.as_string())
        return True
    except Exception as e:
        app.logger.error(f"Failed to send email: {e}")
        return False


@app.context_processor
def inject_global():
    """Inject global template variables."""
    from datetime import datetime
    return {
        "current_year": datetime.now().year,
        "business": BUSINESS,
    }

# Business info
BUSINESS = {
    "name": "Signia Home Care",
    "address": "3030 Holmes Ave S",
    "city": "Minneapolis",
    "state": "MN",
    "zip": "55408",
    "phone": "(763) 308-3282",
    "fax": "(612) 395-5381",
    "email": "hi@signiasolutions.com",
    "hours": "Monday–Friday, 8:00 AM – 4:30 PM",
}


# =============================================================================
# Service definitions for Comprehensive Home Care and Basic 245D
# Based on Minnesota MDH and DHS official sources
# =============================================================================

# Service group keys for visual grouping and icons
SERVICE_GROUPS = {
    "nursing": {"label": "Skilled Nursing", "icon": "stethoscope"},
    "therapy": {"label": "Therapy & Rehabilitation", "icon": "heart-pulse"},
    "clinical": {"label": "Clinical & Specialty", "icon": "clipboard-user"},
    "personal": {"label": "Personal Care", "icon": "user-nurse"},
    "household": {"label": "Household & Daily Living", "icon": "house"},
}

COMPREHENSIVE_SERVICES = [
    {
        "slug": "advanced-practice-nurse-services",
        "title": "Advanced Practice Nurse Services",
        "short_desc": "Specialized nursing care from advanced practice registered nurses.",
        "group": "nursing",
    },
    {
        "slug": "registered-nurse-services",
        "title": "Registered Nurse Services",
        "short_desc": "Skilled nursing care in the comfort of home.",
        "group": "nursing",
    },
    {
        "slug": "licensed-practical-nurse-services",
        "title": "Licensed Practical Nurse Services",
        "short_desc": "Practical nursing support for daily health needs.",
        "group": "nursing",
    },
    {
        "slug": "physical-therapy-services",
        "title": "Physical Therapy Services",
        "short_desc": "Mobility and strength support at home.",
        "group": "therapy",
    },
    {
        "slug": "occupational-therapy-services",
        "title": "Occupational Therapy Services",
        "short_desc": "Help with daily activities and independence.",
        "group": "therapy",
    },
    {
        "slug": "speech-language-pathologist-services",
        "title": "Speech-Language Pathologist Services",
        "short_desc": "Communication and swallowing support.",
        "group": "therapy",
    },
    {
        "slug": "respiratory-therapy-services",
        "title": "Respiratory Therapy Services",
        "short_desc": "Breathing and respiratory care at home.",
        "group": "therapy",
    },
    {
        "slug": "social-worker-services",
        "title": "Social Worker Services",
        "short_desc": "Emotional support and care coordination.",
        "group": "clinical",
    },
    {
        "slug": "dietician-nutritionist-services",
        "title": "Dietician or Nutritionist Services",
        "short_desc": "Nutrition planning and dietary support.",
        "group": "clinical",
    },
    {
        "slug": "medication-management",
        "title": "Medication Management Services",
        "short_desc": "Safe medication oversight and reminders.",
        "group": "clinical",
    },
    {
        "slug": "delegated-tasks",
        "title": "Delegated Tasks to Unlicensed Personnel",
        "short_desc": "Trained caregivers performing delegated health tasks.",
        "group": "clinical",
    },
    {
        "slug": "treatment-therapies",
        "title": "Treatment and Therapies",
        "short_desc": "Ongoing treatment support in the home.",
        "group": "therapy",
    },
    {
        "slug": "eating-assistance",
        "title": "Eating Assistance",
        "short_desc": "Support for clients with complicating eating needs.",
        "group": "personal",
    },
    {
        "slug": "complex-specialty-healthcare",
        "title": "Complex or Specialty Healthcare Services",
        "short_desc": "Specialized medical care at home.",
        "group": "clinical",
    },
    {
        "slug": "personal-care-adls",
        "title": "Personal Care and Activities of Daily Living",
        "short_desc": "Dressing, grooming, bathing, and toileting support.",
        "group": "personal",
    },
    {
        "slug": "standby-assistance",
        "title": "Standby Assistance",
        "short_desc": "Safety support within arm's reach during activities.",
        "group": "personal",
    },
    {
        "slug": "medication-reminders",
        "title": "Medication Reminders",
        "short_desc": "Verbal or visual reminders for scheduled medications.",
        "group": "clinical",
    },
    {
        "slug": "treatment-exercise-reminders",
        "title": "Treatment and Exercise Reminders",
        "short_desc": "Reminders for treatments and exercises.",
        "group": "clinical",
    },
    {
        "slug": "modified-diets",
        "title": "Preparing Modified Diets",
        "short_desc": "Meals prepared per licensed professional orders.",
        "group": "household",
    },
    {
        "slug": "laundry",
        "title": "Laundry",
        "short_desc": "Laundry and linen care.",
        "group": "household",
    },
    {
        "slug": "housekeeping",
        "title": "Housekeeping and Household Chores",
        "short_desc": "Light housekeeping and home maintenance.",
        "group": "household",
    },
    {
        "slug": "meal-preparation",
        "title": "Meal Preparation",
        "short_desc": "Nutritious meal preparation at home.",
        "group": "household",
    },
    {
        "slug": "shopping",
        "title": "Shopping",
        "short_desc": "Grocery and errand assistance.",
        "group": "household",
    },
]

BASIC_245D_SERVICES = [
    {
        "slug": "individual-community-living-supports",
        "title": "Individual Community Living Supports",
        "short_desc": "Support for living independently in the community.",
        "group": "personal",
    },
    {
        "slug": "24-hour-emergency-assistance",
        "title": "24-Hour Emergency Assistance",
        "short_desc": "Around-the-clock emergency support.",
        "group": "clinical",
    },
    {
        "slug": "companion-services",
        "title": "Companion Services",
        "short_desc": "Friendly companionship and socialization.",
        "group": "personal",
    },
    {
        "slug": "homemaker-services",
        "title": "Homemaker Services",
        "short_desc": "Household management and daily living support.",
        "group": "household",
    },
    {
        "slug": "individualized-home-supports",
        "title": "Individualized Home Supports Without Training",
        "short_desc": "Personalized in-home support.",
        "group": "personal",
    },
    {
        "slug": "night-supervision",
        "title": "Night Supervision",
        "short_desc": "Overnight support and monitoring.",
        "group": "clinical",
    },
    {
        "slug": "respite-care-services",
        "title": "Respite Care Services",
        "short_desc": "Short-term relief for primary caregivers.",
        "group": "personal",
    },
]


def get_all_services():
    """Return all services grouped by license type."""
    return {
        "comprehensive": COMPREHENSIVE_SERVICES,
        "basic_245d": BASIC_245D_SERVICES,
    }


def group_services_by_category(services_list):
    """Group services by their category for display."""
    grouped = {}
    for s in services_list:
        g = s.get("group", "clinical")
        if g not in grouped:
            grouped[g] = []
        grouped[g].append(s)
    return grouped


def get_service_by_slug(slug: str):
    """Find a service by slug from either category."""
    for s in COMPREHENSIVE_SERVICES + BASIC_245D_SERVICES:
        if s["slug"] == slug:
            return s
    return None


def get_service_category(slug: str) -> str | None:
    """Return 'comprehensive' or 'basic_245d' for a service slug."""
    for s in COMPREHENSIVE_SERVICES:
        if s["slug"] == slug:
            return "comprehensive"
    for s in BASIC_245D_SERVICES:
        if s["slug"] == slug:
            return "basic_245d"
    return None


def get_service_content(slug: str) -> dict | None:
    """Get page content for a service from service_content module."""
    from service_content import SERVICE_CONTENT
    return SERVICE_CONTENT.get(slug)


# =============================================================================
# Routes
# =============================================================================


def _render_with_business(template, **kwargs):
    """Ensure business is passed to all templates."""
    kwargs.setdefault("business", BUSINESS)
    return render_template(template, **kwargs)


@app.route("/")
def home():
    """Homepage - default route."""
    return _render_with_business(
        "pages/home.html",
        page_title="Signia Home Care | Compassionate Home Care in Minneapolis & Twin Cities",
        meta_description="Signia Home Care provides dignified, personalized home care services in Minneapolis, Minnesota and the Twin Cities. Trusted caregivers. Independence at home.",
    )


@app.route("/about/")
def about():
    """About page."""
    return _render_with_business(
        "pages/about.html",
        page_title="About Signia Home Care | Our Mission & Values",
        meta_description="Learn about Signia Home Care's mission, values, and commitment to compassionate care in Minneapolis and the Twin Cities.",
    )


@app.route("/services/")
def services():
    """Main services landing page."""
    services = get_all_services()
    return _render_with_business(
        "pages/services.html",
        page_title="Our Services | Signia Home Care",
        meta_description="Signia Home Care offers comprehensive home care and 245D basic support services in Minneapolis, Minnesota. Skilled nursing, personal care, and more.",
        services=services,
        service_groups=SERVICE_GROUPS,
        comprehensive_grouped=group_services_by_category(services["comprehensive"]),
        basic245d_grouped=group_services_by_category(services["basic_245d"]),
    )


@app.route("/services/comprehensive-home-care/")
def services_comprehensive():
    """Comprehensive Home Care overview - redirects to main services with anchor."""
    return redirect(url_for("services") + "#comprehensive")


@app.route("/services/basic-245d/")
def services_basic_245d():
    """Basic 245D overview - redirects to main services with anchor."""
    return redirect(url_for("services") + "#basic-245d")


@app.route("/services/<slug>/")
def service_detail(slug: str):
    """Individual service landing page."""
    service = get_service_by_slug(slug)
    if not service:
        return "Service not found", 404
    content = get_service_content(slug)
    if not content:
        return "Service content not found", 404
    category = get_service_category(slug)
    # Related services: same category, exclude current
    all_services = get_all_services()
    list_key = "comprehensive" if category == "comprehensive" else "basic_245d"
    related = [s for s in all_services[list_key] if s["slug"] != slug][:4]
    return _render_with_business(
        "services/detail.html",
        page_title=f"{service['title']} | Signia Home Care",
        meta_description=f"{service['short_desc']} in Minneapolis, Minnesota. Signia Home Care - compassionate, trusted home care.",
        service=service,
        content=content,
        category=category,
        related_services=related,
    )


@app.route("/referral/", methods=["GET", "POST"])
def referral():
    """Referral page with form."""
    if request.method == "POST":
        # Form handling - in production, send email or save to database
        referrer_name = request.form.get("referrer_name", "").strip()
        referrer_type = request.form.get("referrer_type", "").strip()
        organization = request.form.get("organization", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        preferred_contact = request.form.get("preferred_contact", "").strip()
        client_name = request.form.get("client_name", "").strip()
        client_phone = request.form.get("client_phone", "").strip()
        client_email = request.form.get("client_email", "").strip()
        client_address = request.form.get("client_address", "").strip()
        service_interest = request.form.get("service_interest", "").strip()
        urgency = request.form.get("urgency", "").strip()
        insurance = request.form.get("insurance", "").strip()
        notes = request.form.get("notes", "").strip()

        # Basic validation
        if not referrer_name or not email:
            flash("Please provide your name and email.", "error")
            return redirect(url_for("referral"))

        body = f"""New Referral Submission - Signia Home Care

REFERRER INFORMATION:
Name: {referrer_name}
Type: {referrer_type or '(not specified)'}
Organization: {organization or '(not specified)'}
Phone: {phone or '(not specified)'}
Email: {email}
Preferred Contact: {preferred_contact or '(not specified)'}

CLIENT INFORMATION:
Name: {client_name or '(not specified)'}
Phone: {client_phone or '(not specified)'}
Email: {client_email or '(not specified)'}
Address: {client_address or '(not specified)'}
Service of Interest: {service_interest or '(not specified)'}
Urgency: {urgency or '(not specified)'}
Insurance/Funding: {insurance or '(not specified)'}

Notes:
{notes or '(none)'}
"""
        send_form_email("New Referral - Signia Home Care", body)
        flash("Thank you for your referral. We will contact you shortly.", "success")
        return redirect(url_for("referral"))

    return _render_with_business(
        "pages/referral.html",
        page_title="Make a Referral | Signia Home Care",
        meta_description="Refer a client to Signia Home Care. Hospitals, social workers, case managers, and families can refer. Easy referral process.",
        services=get_all_services(),
    )


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    """Contact page with form."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please provide your name, email, and message.", "error")
            return redirect(url_for("contact"))

        body = f"""New Contact Form Submission - Signia Home Care

Name: {name}
Email: {email}
Phone: {phone or '(not specified)'}
Subject: {subject or '(not specified)'}

Message:
{message}
"""
        send_form_email("Contact Form - Signia Home Care", body)
        flash("Thank you for reaching out. We will respond within 1–2 business days.", "success")
        return redirect(url_for("contact"))

    return _render_with_business(
        "pages/contact.html",
        page_title="Contact Signia Home Care | Minneapolis, Minnesota",
        meta_description="Contact Signia Home Care in Minneapolis, MN. Questions about care, referrals, or getting started? We're here to help.",
    )


@app.route("/careers/", methods=["GET", "POST"])
def careers():
    """Careers page with application form."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        zip_code = request.form.get("zip", "").strip()
        position = request.form.get("position", "").strip()
        employment_type = request.form.get("employment_type", "").strip()
        start_date = request.form.get("start_date", "").strip()
        experience_years = request.form.get("experience_years", "").strip()
        certifications = request.form.get("certifications", "").strip()
        experience = request.form.get("experience", "").strip()
        how_heard = request.form.get("how_heard", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email:
            flash("Please provide your name and email.", "error")
            return redirect(url_for("careers"))

        body = f"""New Job Application - Signia Home Care

CONTACT INFORMATION:
Name: {name}
Email: {email}
Phone: {phone or '(not specified)'}
Address: {address or '(not specified)'}
City: {city or '(not specified)'} State: {state or ''} ZIP: {zip_code or ''}

POSITION & AVAILABILITY:
Position: {position or '(not specified)'}
Employment Type: {employment_type or '(not specified)'}
Earliest Start Date: {start_date or '(not specified)'}
Years of Experience: {experience_years or '(not specified)'}

BACKGROUND:
Certifications/Licenses: {certifications or '(not specified)'}
Experience Summary: {experience or '(not specified)'}
How Did You Hear About Us: {how_heard or '(not specified)'}

Additional Information:
{message or '(none)'}
"""
        send_form_email("Job Application - Signia Home Care", body)
        flash("Thank you for your application. We will review it and be in touch.", "success")
        return redirect(url_for("careers"))

    return _render_with_business(
        "pages/careers.html",
        page_title="Careers | Signia Home Care",
        meta_description="Join the Signia Home Care team. We're hiring compassionate caregivers in Minneapolis and the Twin Cities.",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
