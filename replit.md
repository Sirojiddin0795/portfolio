# Django Portfolio Website

## Overview

This is a professional portfolio website built with Django 5.x that showcases personal information, projects, skills, video lessons, blog posts, and provides a contact form. The application is designed to be managed through Django's admin panel, allowing non-technical users to update content without code changes.

The portfolio includes six main sections:
- **Home**: Personal information with profile image, bio, and social media links
- **Projects**: Showcase of work with images, descriptions, and links to GitHub/live demos
- **Skills**: Visual representation of technical skills with progress bars
- **Lessons**: Video tutorials with YouTube embeds or direct video files
- **Blog**: Rich text blog posts with CKEditor support
- **Contact**: Contact form that saves submissions and sends email notifications

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture

**Framework**: Django 5.2.7 with traditional MVT (Model-View-Template) pattern
- **Models**: Database models for Project, Skill, Lesson, Post, Contact, and HomePageContent
- **Views**: Function-based views handling all page rendering and form processing
- **Templates**: Django template inheritance with a base template for consistent layout
- **Admin Interface**: Customized Django admin with list displays, filters, search fields, and date hierarchies

**Key Design Decisions**:
- Uses function-based views for simplicity and straightforward request handling
- Content management entirely through Django admin panel for easy updates
- Context processor for HomePageContent to make it globally available across templates
- Slug-based URLs for blog posts for SEO-friendly links

### Frontend Architecture

**Styling Framework**: TailwindCSS (loaded via CDN)
- Responsive design supporting mobile, tablet, and desktop viewports
- Custom gradient backgrounds and hover animations
- FontAwesome icons for visual enhancement

**Design Patterns**:
- Template inheritance from `base.html` for consistent navigation and styling
- Mobile-first responsive design with breakpoints
- Card-based layouts for projects, skills, lessons, and blog posts
- Gradient color scheme (purple/pink) as primary branding

### Data Storage

**Database**: PostgreSQL (configured via dj-database-url)
- Production database configuration through environment variables
- Django ORM for all database interactions
- Auto-generated timestamps (created_at, updated_at) on all content models

**File Storage**:
- Media files (images, uploads) stored in Django's MEDIA_ROOT
- Separate upload directories: projects/, lessons/, profile/, banners/, blog/
- CKEditor file uploads supported through ckeditor_uploader

**Key Models**:
- **Project**: Portfolio projects with images, descriptions, GitHub and demo links
- **Skill**: Technical skills with percentage levels and Font Awesome icons
- **Lesson**: Video lessons with YouTube URL support or direct video files
- **Post**: Blog posts with rich text content (CKEditor), images, and slugs
- **Contact**: Contact form submissions with name, email, and message
- **HomePageContent**: Singleton model for homepage personalization and social links

### Rich Text Editing

**CKEditor Integration**:
- django-ckeditor and django-ckeditor-uploader packages
- RichTextUploadingField for blog post content with image upload capability
- Separate URL route for CKEditor file uploads (/ckeditor/)

## External Dependencies

### Third-Party Packages

**Django Extensions**:
- `django-ckeditor`: Rich text editor for blog content
- `django-ckeditor-uploader`: File upload support for CKEditor
- `Pillow`: Image processing for uploaded files
- `python-decouple`: Environment variable management
- `dj-database-url`: PostgreSQL database URL parsing

### Frontend Libraries (CDN)

- **TailwindCSS**: Utility-first CSS framework (cdn.tailwindcss.com)
- **Font Awesome 6.5.1**: Icon library (cdnjs.cloudflare.com)

### Email Services

**Contact Form Email**:
- Uses Django's built-in `send_mail` function
- Configured through Django settings (EMAIL_BACKEND, EMAIL_HOST, etc.)
- Sends admin notifications when contact form is submitted

### Database

**PostgreSQL**:
- Primary database system
- Connection configured via DATABASE_URL environment variable
- Supports all Django ORM features and migrations

### Environment Configuration

**Required Environment Variables**:
- `SECRET_KEY`: Django secret key (has default for development)
- `DEBUG`: Debug mode toggle (defaults to True)
- `DATABASE_URL`: PostgreSQL connection string (via dj-database-url)
- Email configuration variables (if email functionality enabled)

### Static and Media Files

**Static Files**: Served in development mode via Django
**Media Files**: User-uploaded content (images, videos) served from MEDIA_ROOT
**Production Considerations**: Static/media files should be served via CDN or web server (nginx/Apache) in production