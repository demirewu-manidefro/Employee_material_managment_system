# Employee Material Management System

**Developed for:** Ethiopian Statistics Service (ESS)  
**Prepared by:** Demirewu Manidefro  
**Program:** Data Science Internship  
**Duration:** 2 Months  
**Institution:** Ethiopian Statistics Service (ESS)  
**Supervisor:** Mr. Stotaw (ESS Manager)  
**Date:** October 2025  

---

## Abstract

The Employee Material Management System (EMMS) was developed during a two-month Data Science Internship at the Ethiopian Statistics Service (ESS).  
The system replaces manual, paper-based tracking of office materials with a digital web-based solution that simplifies the management of borrowed, returned, and pending items.

It is built using Flask (Python) for the backend, PostgreSQL for the database, and HTML/CSS (Bootstrap) for the frontend.  
The system provides real-time tracking, role-based login (Admin, Supervisor, Viewer), data export to Excel, and deployment on Render.  
The project demonstrates full-stack web development, database design, and cloud deployment skills.

---

## Introduction

The Ethiopian Statistics Service (ESS) manages a large number of employees and materials across departments.  
Previously, these were tracked manually, which was slow, error-prone, and difficult to monitor.  
This project was developed to provide a centralized, automated, and transparent system for tracking materials and employee activities.

---

## Problem Statement

Manual tracking of office materials caused several challenges:

- Loss or duplication of records  
- Difficulty identifying available and borrowed materials  
- Lack of accountability for unreturned items  

To solve these issues, a web-based management system was developed to ensure accuracy, accountability, and efficiency.

---

## Objectives

### General Objective
To develop a digital system that automates and simplifies material and employee record management at ESS.

### Specific Objectives
- Store and manage employee and material data using a relational database  
- Track borrowing and returning of materials in real time  
- Implement secure role-based access control  
- Generate Excel reports for administrative use  
- Deploy the system online using Render  

---

## System Overview

### Architecture
The system follows a three-tier architecture:

1. **Frontend (Presentation Layer)**  
   Built with HTML, CSS, and Bootstrap to provide a clean, responsive interface.

2. **Backend (Application Layer)**  
   Developed using Flask to handle routing, authentication, and business logic.

3. **Database (Data Layer)**  
   Managed with PostgreSQL using SQLAlchemy ORM for efficient data management.

### Entity Relationships

---

## Implementation Summary

1. **Database Setup**  
   Defined models for Employee, Material, BorrowedMaterial, and LeaveOutMember using SQLAlchemy.

2. **Backend Logic**  
   Created Flask routes for adding, borrowing, returning, and exporting data.  
   Added input validation, flash messages, and session management.

3. **Frontend Development**  
   Built HTML templates for all major features and styled with Bootstrap.

4. **Authentication and Roles**  
   Implemented login and password hashing with role-based access (Admin, Supervisor, Viewer).

5. **Deployment**  
   Deployed on Render with a connected PostgreSQL database.  
   Configured environment variables for production.

---

## Key Features

- Add and manage employees and materials  
- Borrow and return materials (individual or all)  
- Track materials by name and serial number  
- View available, borrowed, and returned materials  
- Manage “Waiting for Return” list for pending items  
- Export data to Excel  
- Role-based login (Admin, Supervisor, Viewer)  
- Password change and session security  
- Responsive user interface  

---

## Tools and Technologies

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

## Challenges and Solutions

| Challenge | Description | Solution |
|------------|--------------|-----------|
| Online Database Connection | Render PostgreSQL connection issue | Reconfigured environment variables and secured database URI |
| Data Consistency | Duplicate or missing records | Implemented validation and waiting list tracking |
| UI Responsiveness | Layout issues on small screens | Applied Bootstrap grid system |
| Role Restrictions | Access control for different users | Added role-based routing and session checks |

---

## Deployment Details

- **Hosting:** Render  
- **Database:** Render PostgreSQL (Cloud)  
- **Environment Variables:**  
  - DATABASE_URL  
  - SECRET_KEY  

Minor connection issues were resolved by updating Render network settings and ensuring persistent connections.

---

## Results and Impact

The system:
- Eliminated paper-based management  
- Improved accountability and transparency  
- Reduced administrative workload  
- Enabled instant Excel reporting for managers  

---

## Future Improvements

- Integration of machine learning for usage prediction  
- Automated PDF report generation  
- Mobile-friendly dashboard  
- Email notifications for overdue returns  

---

## Acknowledgment

I would like to thank Mr. Stotaw, ESS Manager and Internship Supervisor, for his continuous support and guidance.  
I am also grateful to the Ethiopian Statistics Service for providing the opportunity and resources to complete this project.

---

## References

- [Flask Official Documentation](https://flask.palletsprojects.com/)  
- [SQLAlchemy ORM Documentation](https://www.sqlalchemy.org/)  
- [Render Deployment Guide](https://render.com/docs)

---

## Author

**Demirewu Manidefro**  
Data Science Intern – Ethiopian Statistics Service (ESS)  
October 2025
