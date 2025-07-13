# 🕷️ Web Scraper for Craigslist

A Django-based web scraping application that allows users to search Craigslist for listings based on custom keywords. Built with BeautifulSoup and Requests, the scraper retrieves relevant data—such as titles, prices, images, and links—and presents it through a secure, user-friendly web interface. This project is designed for educational use with a focus on ethical scraping practices.

---

## 📸 Live Demo

*Coming soon or hosted locally via `localhost:8000`.*

---

## 💡 Features

- 🔍 **Keyword-Based Scraping**  
  Search Craigslist listings by custom keywords and locations.

- 👤 **User Authentication**  
  Secure registration, login, and session handling.

- 🧾 **Clean Output**  
  Display title, price, image (if available), and direct listing links.

- 🔐 **Secure & Ethical**  
  Respects Craigslist's structure and terms of use. Built with scraping best practices in mind.

- ⚙️ **Scalable Backend**  
  Modular architecture ready for extension with APIs or multi-site support.

---

## ⚙️ Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Language       | Python 3.8+         |
| Framework      | Django              |
| Scraping       | BeautifulSoup, Requests |
| Frontend       | HTML, CSS (Django templates) |
| Database       | SQLite3             |
| Auth           | Django built-in auth system |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/subinsamu28/Webscrapper.git
cd Webscrapper
```

### 2. Set Up a Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

---

## 🧪 Testing

- ✅ Unit-tested views and models  
- ✅ Integration-tested keyword-based scraping logic  
- ✅ Manual QA of user auth and data output  

---

## 📁 Project Structure

```bash
Webscrapper/
├── listings/              # Core app: models, views, scraping logic
├── users/                 # Authentication: registration, login
├── templates/             # HTML templates
├── static/                # CSS, images
├── manage.py
├── db.sqlite3
├── requirements.txt
```

---

## 📜 License

© 2025 **Subin Samu**. All rights reserved.  
This project is licensed under the terms of the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).  
You may use, modify, and distribute the code under the same license with attribution.  
**Commercial use or redistribution without permission is not allowed.**

---

## 👨‍💻 Author

**Subin Samu**  
Cybersecurity enthusiast & MSc Applied Computer Science student  
📍 Deggendorf Institute of Technology  
📧 [subinsamu28@gmail.com](mailto:subinsamu28@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/subin-samu)  
🌐 [Portfolio](https://subinsamu.com)

---

> ⚠️ **Disclaimer**: This project is for educational purposes only. Web scraping should always respect the target site's terms of service, robots.txt, and local laws.
