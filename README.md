🧾 Employee Material Management System

Developed for: Ethiopian Statistics Service (ESS)
Prepared by: Demirewu Manidefro
Program: Data Science Internship
Duration: 2 Months
Institution: Ethiopian Statistics Service (ESS)
Supervisor: Stotaw (ESS Manager)
Date: October 2025

📘 1. Abstract

The Employee Material Management System was developed during a two-month Data Science Internship at the Ethiopian Statistics Service (ESS).
The main goal of the project is to digitize and simplify the management of office materials, including the tracking of borrowed items, returned materials, and employees who have left or are waiting to return materials.

The system was developed under the guidance of the ESS manager, who provided the functional requirements and feedback during development.
It was implemented using Flask (Python Framework) for the backend, PostgreSQL for the database, and HTML/CSS (Bootstrap) for the frontend.

Flask was chosen for its flexibility and to allow future integration of Machine Learning models with the web system.

The system was deployed on Render, demonstrating both web development and cloud deployment skills.

🏢 2. Introduction

The Ethiopian Statistics Service (ESS) manages various materials and employees across departments.
Traditional paper-based systems were time-consuming, error-prone, and hard to track.

This system was built based on the manager’s request to create a centralized, digital solution for tracking materials and employee borrowing activities.
It provides automation, accountability, and transparency.

❗ 3. Problem Statement

The manual system caused several issues:

Difficulty in tracking borrowed and returned materials

Loss or duplication of records

Lack of real-time availability data

No accountability for unreturned items

👉 Therefore, a web-based system was needed for improved efficiency, accuracy, and visibility.

🎯 4. Objectives
General Objective

To develop a web-based system that automates and simplifies material and employee record management at ESS.

Specific Objectives

Manage employee and material data efficiently using a relational database.

Enable real-time borrowing and returning of materials.

Implement role-based access for Admin, Supervisor, and Viewer.

Generate and export Excel reports.

Track leave-out employees.

Deploy the system online (Render).

Prepare the system for Machine Learning integration in the future.

🧭 5. Scope of the Project

The system supports:

Adding and updating employee & material records

Borrowing and returning materials

Viewing available, borrowed, and returned materials

Tracking leave-out and “waiting for return” employees

Role-based login

Exporting data to Excel

Note: Mobile app and advanced ML analytics are planned for future versions.

⚙️ 6. System Design & Architecture

The system uses a Three-Tier Architecture:

Presentation Layer (Frontend):
Built using HTML, CSS, Bootstrap — provides a clean, responsive dashboard.

Application Layer (Backend):
Developed using Flask, managing business logic, authentication, and routes.

Database Layer:
Uses PostgreSQL with SQLAlchemy ORM for efficient data relationships.

Entity Relationships:

Employee ↔ BorrowedMaterial (One-to-Many)

Material ↔ BorrowedMaterial (One-to-Many)

Employee ↔ LeaveOutMember (One-to-One)

🧩 7. Implementation Details

Database Setup:
Defined models for Employee, Material, BorrowedMaterial, and LeaveOutMember.

Backend Development:
Created Flask routes for add, borrow, return, and export features.
Added flash messages and session management.

Frontend Design:
Developed reusable HTML templates and used Bootstrap for responsiveness.

Security & Authentication:
Role-based login (Admin, Supervisor, Viewer) with password hashing.

Deployment:
Deployed on Render using environment variables for security.
Encountered minor DB connection issues — planned reconfiguration.

🚀 8. Key Features

✅ Add & manage employees and materials
✅ Borrow & return materials (individual or all)
✅ Track materials by name and serial number
✅ “Waiting for Return” list for pending returns
✅ Export data to Excel
✅ Role-based login (Admin, Supervisor, Viewer)
✅ Password management
✅ Responsive UI with Bootstrap
✅ Future-ready for ML integration

🛠️ 9. Tools and Technologies Used
Category	Tool / Technology
Programming Language	Python
Framework	Flask
Database	PostgreSQL
ORM	SQLAlchemy
Frontend	HTML, CSS, Bootstrap
Deployment	Render
IDE	VS Code
Version Control	Git & GitHub
🧠 10. Challenges & Solutions
Challenge	Description	Solution
Online DB Connection	Render PostgreSQL connectivity	Reconfigure environment variables & DB URI
Data Consistency	Duplicate/missing borrow records	Added validation & tracking logic
UI Responsiveness	Layout issues on small screens	Used Bootstrap grid & components
Role Management	Access restriction by user	Implemented Flask session-based roles
🌐 11. Deployment Details

Platform: Render

Database: PostgreSQL (Cloud)

Environment Variables:

DATABASE_URL

SECRET_KEY

⚠️ Minor deployment issues (DB connection) will be resolved through Render’s network reconfiguration.

🏁 12. Conclusion & Future Work

The system successfully digitalized ESS’s material management process, replacing manual methods with an efficient and transparent web-based solution.

Future Enhancements

Add Machine Learning analytics for predicting material usage

Generate automated PDF reports

Enable mobile accessibility

Implement email alerts for overdue items

🙏 13. Acknowledgment

I would like to express my sincere gratitude to Mr. Stotaw (ESS Manager) for his continuous support, direction, and feedback during this project.
This system was developed based on his requirements and guidance.

Special thanks to the Ethiopian Statistics Service (ESS) for the opportunity and resources to complete this internship successfully.

📚 14. References

Flask Official Documentation

SQLAlchemy ORM Documentation

Render Deployment Guide

⭐ Note

This project was built by Demirewu Manidefro, Data Science Intern at ESS, using Flask with future plans to integrate Machine Learning models into the system for predictive analysis and smart resource management.
