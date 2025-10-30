# 🧾 Employee Material Management System

**Developed for:** Ethiopian Statistics Service (ESS)  
**Prepared by:** Demirewu Manidefro  
**Program:** Data Science Internship  
**Duration:** 2 Months  
**Institution:** Ethiopian Statistics Service (ESS)  
**Supervisor:** Mr. Stotaw (ESS Manager)  
**Date:** October 2025  

---

## 📘 Abstract

The **Employee Material Management System (EMMS)** was developed during a two-month Data Science Internship at the **Ethiopian Statistics Service (ESS)**.  
The system replaces manual, paper-based tracking of office materials with a **digital, web-based solution** that simplifies the management of borrowed, returned, and pending items.

Built using **Flask (Python)** for the backend, **PostgreSQL** for the database, and **HTML/CSS (Bootstrap)** for the frontend, the system provides:
- Real-time tracking of materials  
- Role-based login (Admin, Supervisor, Viewer)  
- Data export to Excel  
- Cloud deployment on **Render**

The project demonstrates practical skills in full-stack web development, database design, and system deployment.

---

## 🎯 Introduction

The Ethiopian Statistics Service (ESS) manages many employees and materials across departments.  
Previously, these were tracked manually — a process that was **slow, prone to errors, and difficult to monitor**.  
This project was developed to address these limitations by creating a **centralized, automated, and transparent system**.

---

## 🧩 Problem Statement

Manual tracking of office materials at ESS caused:
- Loss or duplication of records  
- Difficulty identifying available and borrowed materials  
- No quick view of employees who left with unreturned items  

The solution: a **web-based management system** to ensure accountability and efficiency.

---

## 🎯 Objectives

### General Objective
To develop a digital system that automates and simplifies material and employee record management at ESS.

### Specific Objectives
- Store and manage employee and material data using a relational database  
- Track borrowing and returning of materials in real time  
- Implement secure role-based access control  
- Generate Excel reports for administrative use  
- Deploy the system online using **Render**

---

## 🧱 System Overview

### 🧭 Architecture
The system follows a **three-tier architecture**:

1. **Frontend (Presentation Layer)**  
   Built with **HTML, CSS, and Bootstrap**, providing a clean and responsive interface.

2. **Backend (Application Layer)**  
   Developed using **Flask**, handling routing, authentication, and business logic.

3. **Database (Data Layer)**  
   Managed with **PostgreSQL** via **SQLAlchemy ORM**, ensuring data integrity.

### ⚙️ Entity Relationships


---

## ⚒️ Implementation Summary

1. **Database Setup**  
   Defined models for `Employee`, `Material`, `BorrowedMaterial`, and `LeaveOutMember` using SQLAlchemy.

2. **Backend Logic**  
   Created Flask routes for adding employees/materials, borrowing, returning, and exporting data.  
   Added validation, flash messages, and session management.

3. **Frontend Development**  
   Built dynamic templates for all features.  
   Used Bootstrap for layout, color scheme, and responsiveness.

4. **Authentication & Roles**  
   Implemented secure login with password hashing and role-based permissions (Admin, Supervisor, Viewer).

5. **Deployment**  
   Deployed on **Render** using an online PostgreSQL database.  
   Configured environment variables for production.

---

## 🌟 Key Features

- Add and manage **employees** and **materials**  
- Borrow and return materials (individual or all)  
- Track materials by **name and serial number**  
- View **available**, **borrowed**, and **returned** materials  
- Manage a **“Waiting for Return”** list for employees with pending items  
- Export data to **Excel**  
- **Role-based login** for Admin, Supervisor, and Viewer  
- Password change and session security  
- Fully **responsive interface**

---

## 🧰 Tools & Technologies

| Category | Tool / Technology |
|-----------|-------------------|
| Programming Language | Python |
| Framework | Flask |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, Bootstrap |
| Deployment | Render |
| Development Environment | VS Code |
| Version Control | Git & GitHub |

---

## ⚠️ Challenges & Solutions

| Challenge | Description | Solution |
|------------|--------------|-----------|
| Online Database Connection | Render PostgreSQL connection issue | Reconfigured Render environment variables and secured DB URI |
| Data Consistency | Duplicate or missing records | Added validation and waiting-list logic |
| UI Responsiveness | Layout issues on mobile screens | Applied Bootstrap grid and container system |
| Role Restrictions | Feature access control | Implemented role-based routing with session checks |

---

## 🚀 Deployment Details

- **Hosting:** Render  
- **Database:** Render PostgreSQL (Cloud)  
- **Environment Variables:**
  - `DATABASE_URL`
  - `SECRET_KEY`

Minor connection issues encountered during testing were resolved by updating Render network settings and verifying persistent connections.

---

## ✅ Results & Impact

The system:
- Eliminated paper-based record issues  
- Improved accountability for material tracking  
- Reduced time spent on manual supervision  
- Made reports instantly available in Excel format  

---

## 🔮 Future Improvements

- Integrate **machine learning** to predict material usage  
- Generate **PDF reports** automatically  
- Add **mobile-friendly dashboard** and push notifications  
- Implement **email reminders** for overdue material returns  

---

## 🙏 Acknowledgment

Special thanks to **Mr. Stotaw**, ESS Manager and Internship Supervisor, for his guidance and support.  
Gratitude to the **Ethiopian Statistics Service (ESS)** for providing the platform, resources, and mentorship to complete this project successfully.

---

## 📚 References

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)  
- [Render Deployment Guide](https://render.com/docs)

---

## 👨‍💻 Author

**Demirewu Manidefro**  
_Data Science Intern – Ethiopian Statistics Service (ESS)_  
📅 October 2025  
