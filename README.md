# Django Portfolio Website

Bu loyiha Django 5.x, PostgreSQL, va TailwindCSS yordamida yaratilgan professional portfolio veb-saytidir.

## Xususiyatlar

### Asosiy Bo'limlar:

1. **Home (Asosiy sahifa)**
   - Shaxsiy ma'lumotlar (ism, kasb, bio)
   - Professional banner va gradient fon
   - "Hire Me" tugmasi
   - Profil rasmi

2. **Projects (Loyihalar)**
   - Loyihalarni card-style layoutda ko'rsatish
   - Rasm, tavsif, GitHub va Live Demo havolalari
   - Admin paneldan boshqarish

3. **Skills (Ko'nikmalar)**
   - Ko'nikmalarni progress bar yoki chip-style ko'rinishida ko'rsatish
   - Foiz ko'rsatkichi (0-100%)
   - Icon qo'llab-quvvatlash

4. **Lessons (Darslar)**
   - Video darslar (YouTube yoki to'g'ridan-to'g'ri video fayl)
   - Video preview ko'rinishi
   - Tavsif va sanalar

5. **Blog**
   - Blog postlarini ro'yxat va batafsil sahifalarda ko'rsatish
   - Rich text editor (CKEditor) qo'llab-quvvatlash
   - Rasm yuklash imkoniyati

6. **Contact (Bog'lanish)**
   - Kontakt forma (ism, email, xabar)
   - Email orqali admin ga xabar yuborish
   - Ijtimoiy tarmoq havolalari

### Texnologiyalar:

- **Backend**: Django 5.2.7
- **Ma'lumotlar bazasi**: PostgreSQL
- **Frontend**: TailwindCSS (CDN orqali)
- **Rich Text Editor**: django-ckeditor
- **Rasm boshqaruvi**: Pillow
- **Responsive dizayn**: Mobile, Tablet, Desktop

## O'rnatish va Ishga Tushirish

### 1. Kerakli kutubxonalar o'rnatilgan

Loyiha allaqachon quyidagi kutubxonalar bilan o'rnatilgan:
- Django 5.2.7
- psycopg2-binary
- django-ckeditor
- Pillow
- python-decouple
- dj-database-url

### 2. Ma'lumotlar bazasi migratsiyalari

Ma'lumotlar bazasi migratsiyalari allaqachon bajarilgan. Agar yangi o'zgarishlar qilsangiz:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Superuser (Admin) yaratish

Superuser allaqachon yaratilgan:
- **Username**: admin
- **Password**: admin123

Yangi superuser yaratish uchun:

```bash
python manage.py createsuperuser
```

Yoki avtomatik superuser yaratish uchun:

```bash
python create_superuser.py
```

### 4. Serverni ishga tushirish

Server allaqachon ishga tushirilgan va 5000 portda ishlayapti:

```bash
python manage.py runserver 0.0.0.0:5000
```

## Admin Panelga Kirish

1. Brauzerda `/admin/` sahifasiga o'ting
2. Username: `admin`, Password: `admin123` bilan kiring
3. Quyidagi modellarni boshqaring:
   - **Home Page Content** - Asosiy sahifa ma'lumotlari va ijtimoiy tarmoq havolalari
   - **Projects** - Loyihalar
   - **Skills** - Ko'nikmalar
   - **Lessons** - Video darslar
   - **Posts** - Blog postlar
   - **Contact** - Kontakt xabarlari

## Loyiha Tuzilishi

```
portfolio_project/
├── portfolio_project/        # Asosiy loyiha papkasi
│   ├── settings.py          # Sozlamalar
│   ├── urls.py              # Asosiy URL konfiguratsiyasi
│   └── portfolio/           # Portfolio ilova
│       ├── models.py        # Ma'lumotlar modellari
│       ├── views.py         # View funksiyalari
│       ├── admin.py         # Admin panel konfiguratsiyasi
│       ├── urls.py          # URL marshrutlari
│       └── context_processors.py  # Context processor
├── templates/               # HTML shablonlar
│   └── portfolio/
│       ├── base.html       # Asosiy shablon (Navbar, Footer)
│       ├── home.html       # Asosiy sahifa
│       ├── projects.html   # Loyihalar sahifasi
│       ├── skills.html     # Ko'nikmalar sahifasi
│       ├── lessons.html    # Darslar sahifasi
│       ├── blog_list.html  # Blog ro'yxati
│       ├── blog_detail.html # Blog batafsil
│       └── contact.html    # Kontakt forma
├── static/                 # Statik fayllar
├── media/                  # Media fayllar (yuklangan rasmlar)
└── manage.py              # Django boshqaruv fayli
```

## Modellar

### HomePageContent
- name, profession, bio
- profile_image, banner_image
- hire_me_link
- Ijtimoiy tarmoq havolalari (Facebook, Twitter, LinkedIn, GitHub, Instagram)

### Project
- title, description, image
- github_link, live_demo_link
- created_at

### Skill
- title, level (%), icon
- created_at

### Lesson
- title, description
- video_url, thumbnail
- created_at

### Post
- title, content (Rich Text)
- image, slug
- created_at, updated_at

### Contact
- name, email, message
- created_at

## Muhim Eslatmalar

1. **Media fayllar**: Yuklangan rasmlar va videolar `media/` papkasida saqlanadi
2. **Static fayllar**: CSS, JavaScript va boshqa statik fayllar `static/` papkasida
3. **TailwindCSS**: CDN orqali ulangan, internet talab qiladi
4. **Font Awesome**: Ikonlar uchun CDN orqali ulangan
5. **Email**: Console backend ishlatilmoqda (xabarlar terminalda ko'rinadi)

## Responsive Dizayn

Sayt quyidagi qurilmalar uchun moslashtirilgan:
- Mobile (telefon)
- Tablet
- Desktop (kompyuter)

## Animatsiyalar

- Hover effektlari
- Fade-in animatsiyalar
- Scale transformatsiyalar
- Progress bar animatsiyalari

## Email Sozlamalari

**Hozirgi holat**: Console backend ishlatilmoqda (kontakt xabarlari terminalda ko'rinadi).

**Production uchun**: Email xabarlarni haqiqiy jo'natish uchun `portfolio_project/settings.py` faylida EMAIL sozlamalarini o'zgartiring:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='your-email@gmail.com')
```

**Gmail uchun**: App Password yaratishingiz kerak (https://myaccount.google.com/apppasswords)

## Qo'shimcha Ma'lumotlar

- Django versiyasi: 5.2.7
- Python versiyasi: 3.11
- PostgreSQL ma'lumotlar bazasi ulanishi environment variables orqali

## Muammolarni Hal Qilish

Agar loyiha ishlamasa:

1. Ma'lumotlar bazasi ulanishini tekshiring
2. Migratsiyalar bajarilganligini tekshiring
3. Static fayllar to'g'ri yuklangan bo'lishini tekshiring
4. Server 0.0.0.0:5000 da ishga tushganligini tekshiring

## Ijtimoiy Tarmoq Havolalarini Qo'shish

1. Admin panelga kiring
2. "Home Page Content" bo'limiga o'ting
3. "Social Media Links" qismida havolalarni kiriting
4. Saqlang

Havolalar Navbar va Footer qismlarida avtomatik ko'rinadi.
