# Портал групи — Архітектура Django проєкту

## Опис проєкту

**Портал групи** — це веб-додаток, створений на фреймворку **Django**, який дозволяє студентам та викладачам взаємодіяти через єдину систему.

На порталі буде розміщено:

* інформацію про групу
* форум для спілкування
* електронний щоденник з оцінками
* календар подій
* систему опитувань
* систему голосувань
* оголошення
* навчальні матеріали
* портфоліо студентів
* галерею фото та відео

Проєкт реалізується у вигляді **Django-порталу, розділеного на окремі додатки (apps)**.
Кожен додаток відповідає за окрему функціональність системи.

Студенти можуть **обрати один із модулів та реалізувати його**.

---

# Архітектура проєкту

Проєкт буде складатися з **11 Django додатків (apps)**.

```
portal_project
│
├── core
├── users
├── forum
├── grades
├── events
├── calendar_app
├── polls
├── voting
├── announcements
├── materials
└── media_portal
```

---

# 1. Core — головна сторінка порталу

### Сторінка

Головна сторінка сайту з інформацією про групу та віджетами інших розділів.

### Функціонал

* відображення інформації про групу
* віджети інших модулів (новини, події, оголошення)
* навігація по сайту

### Моделі

**GroupInfo**

* title
* description
* created_at
* updated_at

**Widget**

* name
* type (events / announcements / forum / polls)
* is_active
* order

---

# 2. Users — користувачі та автентифікація

### Сторінки

* реєстрація
* авторизація
* профіль користувача
* редагування профілю

### Ролі користувачів

* User (звичайний користувач)
* Moderator (модератор)
* Admin (адміністратор)

### Моделі

**User**

* username
* email
* password
* first_name
* last_name
* role
* avatar
* created_at

**Profile**

* user (FK → User)
* phone
* birthday
* bio

---

# 3. Forum — форум

### Сторінки

* список категорій
* список тем
* сторінка теми
* створення повідомлення

### Функціонал

* користувачі можуть створювати повідомлення
* модератори та адміністратори можуть створювати та редагувати теми

### Моделі

**ForumCategory**

* name
* description

**ForumTopic**

* title
* author (FK → User)
* category (FK → ForumCategory)
* created_at

**ForumPost**

* topic (FK → ForumTopic)
* author (FK → User)
* content
* created_at

---

# 4. Grades — електронний щоденник

### Сторінки

* таблиця оцінок
* список предметів
* редагування оцінок (адмін)

### Моделі

**Subject**

* name
* description

**Grade**

* student (FK → User)
* subject (FK → Subject)
* grade
* date
* comment
* created_by (FK → User)

---

# 5. Events — події

### Сторінки

* список подій
* сторінка події
* створення / редагування події

### Моделі

**Event**

* title
* description
* location
* start_date
* end_date
* created_by (FK → User)
* created_at

---

# 6. Calendar — календар подій

### Сторінки

* календар
* перегляд подій за датою

### Моделі

**CalendarDay**

* date
* notes

**CalendarEvent**

* event (FK → Event)
* date

---

# 7. Polls — система опитувань

### Сторінки

* список опитувань
* проходження опитування
* результати опитування

### Функціонал

* багатосторінкові опитування
* користувач може пройти опитування один раз
* адміністратори можуть переглядати результати

### Моделі

**Poll**

* title
* description
* created_by
* created_at
* is_active

**Question**

* poll (FK → Poll)
* text
* order

**Choice**

* question (FK → Question)
* text

**PollResponse**

* poll (FK → Poll)
* user (FK → User)
* submitted_at

**Answer**

* response (FK → PollResponse)
* question (FK → Question)
* choice (FK → Choice)

---

# 8. Voting — система голосувань

### Сторінки

* список голосувань
* сторінка голосування
* результати голосування

### Моделі

**Vote**

* title
* description
* created_by
* end_date

**VoteOption**

* vote (FK → Vote)
* text

**UserVote**

* vote (FK → Vote)
* user (FK → User)
* option (FK → VoteOption)
* voted_at

---

# 9. Announcements — оголошення

### Сторінки

* список оголошень
* сторінка оголошення

### Моделі

**Announcement**

* title
* content
* author (FK → User)
* created_at
* updated_at
* is_active

---

# 10. Materials — навчальні матеріали

### Сторінки

* список матеріалів
* сторінка матеріалу
* завантаження матеріалу

### Функціонал

Підтримка:

* файлів
* зображень
* посилань
* відео з YouTube

### Моделі

**Material**

* title
* description
* file
* link
* youtube_url
* material_type (file / link / video)
* uploaded_by (FK → User)
* created_at

---

# 11. Media Portal — портфоліо та галерея

### Сторінки

* портфоліо студентів
* список проектів
* галерея фото та відео

### Моделі

**Portfolio**

* title
* description
* author (FK → User)
* link
* created_at

**PortfolioFile**

* portfolio (FK → Portfolio)
* file
* screenshot

**GalleryItem**

* title
* file
* type (image / video)
* uploaded_by (FK → User)
* is_approved
* created_at

---

# Навігація сайту

```
Головна
│
├── Форум
├── Електронний щоденник
├── Події
├── Календар
├── Опитування
├── Голосування
├── Оголошення
├── Матеріали
├── Портфоліо
├── Галерея
└── Профіль користувача
```

---

# Технології

Проєкт використовує:

* **Python**
* **Django**
* **HTML**
* **CSS**
* **Bootstrap**
* **Git**

---

# Робота в команді

Проєкт виконується командою студентів.

Кожен студент або група студентів:

* обирає **один модуль (app)**
* реалізує **моделі**
* створює **views**
* створює **HTML шаблони**
* підключає **URLs**

Весь код зберігається у **Git репозиторії**.

---

# Очікуваний результат

Після завершення проєкту повинен бути створений **повноцінний портал студентської групи**, де користувачі можуть:

* спілкуватися на форумі
* переглядати оцінки
* брати участь в опитуваннях
* голосувати
* переглядати матеріали
* публікувати свої проєкти
* переглядати фото та відео

---
