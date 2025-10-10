
Developed for: Ethiopian Statistics Service (ESS)
Prepared by: Demirewu Manidefro
Program: Data Science Internship
Duration: 2 Months
Institution: Ethiopian Statistics Service (ESS)
Supervisor: Stotaw (ESS Manager)
Date: October 2025

1. Abstract
This project, titled Employee Material Management System, was developed during a two-month Data Science Internship at the Ethiopian Statistics Service (ESS).
The main goal of the project is to digitize and simplify the management of office materials, including tracking of borrowed items, returned materials, and employees who have left or are waiting to return materials.
The system is implemented using Flask (Python Framework) for the backend, PostgreSQL for the database, and HTML/CSS (Bootstrap) for the frontend. The application provides secure role-based access (Admin, Supervisor, and Viewer), data export functionality, and a clean, responsive user interface. The project was also deployed on Render, demonstrating the intern’s ability to work with online servers and cloud databases.

2. Introduction
The Ethiopian Statistics Service manages a wide range of resources and employees across departments. Traditional paper-based systems for recording the borrowing and returning of materials are time-consuming, error-prone, and difficult to monitor.
To address these issues, the Employee Material Management System was developed as part of this internship to provide a digital, centralized, and automated system for material tracking and employee record management.


3. Problem Statement
The manual method of tracking materials in ESS led to several challenges:
 	Difficulty in monitoring borrowed and returned items
 	Loss or duplication of material records
 	Inability to view available or borrowed materials instantly
 	Lack of accountability for employees who leave with unreturned items
Hence, there was a clear need for a web-based management system to ensure transparency, accountability, and efficiency.

4. Objectives
General Objective
To develop a digital system that automates and simplifies the management of materials and employee records at ESS.
Specific Objectives
 	To store and manage employee and material data efficiently using a relational database.
 	To enable borrowing and returning of materials with real-time updates.
 	To implement role-based access control for different system users.
 	To generate Excel reports and maintain a record of leave-out employees.
 	To deploy the system on a cloud platform (Render) for online access.

5. Scope of the Project
The system is designed for internal use within the Ethiopian Statistics Service. It covers:
 	Adding and updating employee and material records
 	Borrowing and returning materials
 	Viewing available, borrowed, and returned materials
 	Tracking employees who have left or are waiting to return items
 	Role-based login and account management
 	Exporting data to Excel for reporting
This project focuses on backend development, database design, and frontend integration. Mobile app support and complex analytics are considered outside the current scope.

6. System Design & Architecture
The system follows the three-tier architecture:
1.	Presentation Layer (Frontend):
Built using HTML, CSS, and Bootstrap, providing a clean, user-friendly dashboard for all users.
2.	Application Layer (Backend):
Developed using Flask, a lightweight Python framework, managing business logic, authentication, and routing.
3.	Database Layer:
Uses PostgreSQL, managed through SQLAlchemy ORM, to handle relationships between Employees, Materials, Borrowed Items, and Leave-Out Members.
Entity Relationship Overview
 	Employee ↔ BorrowedMaterial (One-to-Many)
 	Material ↔ BorrowedMaterial (One-to-Many)
 	Employee ↔ LeaveOutMember (One-to-One)

7. Implementation Details
The system was implemented in the following steps:
1.	Database Setup:
Configured PostgreSQL database using SQLAlchemy ORM, defining models for Employee, Material, BorrowedMaterial, and LeaveOutMember.
2.	Backend Development:
 	Implemented Flask routes for adding employees, materials, borrowing, returning, and exporting data.
 	Added session management and flash messages for better user interaction.
3.	Frontend Design:
 	Created HTML templates for all operations (add, borrow, return, upload, etc.).
 	Integrated Bootstrap for responsiveness and consistent styling.
4.	Security & Authentication:
 	Added a login and registration system with password hashing.
 	Role-based access (Admin, Supervisor, Viewer) controls access to specific features.
5.	Deployment:
o	Deployed on Render, connecting to an online PostgreSQL database.
o	Encountered and planned to resolve online database connection issues (under review).

8. Key Features
 	Add and manage employee and material records.
 	Borrow and return materials (individual or all).
 	Track materials by name and serial number.
 	View available and borrowed materials.
 	“Waiting for Return” list for employees with unreturned items.
 	Export data to Excel for administrative use.
 	Role-based login (Admin, Supervisor, Viewer).
 	Password change and account management.
 	Responsive and easy-to-use interface.

9. Tools and Technologies Used
Category	Tool / Technology
Programming Language	Python
Framework	Flask
Database	PostgreSQL
ORM	SQLAlchemy
Frontend	HTML, CSS, Bootstrap
Deployment	Render
Development Environment	VS Code
Version Control	Git & GitHub

10. Challenges Faced & Solutions
Challenge	Description	Solution
Online Database Connection	Render PostgreSQL connection issue	Plan to reconfigure Render environment variables and secure DB URI
Data Consistency	Duplicate or missing borrow records	Implemented validation and “waiting for return” tracking
UI Responsiveness	Layout issues on smaller screens	Used Bootstrap grid system
Role Management	Restricted access based on user type	Added role-based route control and Flask session tracking

11. Deployment Details
The application was deployed on Render, using a connected PostgreSQL cloud database.
Environment variables were configured for:
 	DATABASE_URL
 	SECRET_KEY
During deployment, minor issues occurred with the online database connection. These will be fixed by updating Render’s network settings and ensuring persistent connections for production mode.

12. Conclusion and Future Work
The Employee Material Management System successfully digitalized the manual process of managing materials within ESS. It demonstrated the practical application of data science and web development skills in solving real-world administrative problems.
Future Enhancements
•	Integration of machine learning analytics for usage prediction.
•	Generating automated PDF reports.
•	Adding mobile accessibility for employees.
•	Implementing email notifications for overdue returns.

13. Acknowledgment
I would like to express my sincere gratitude to Stotaw, my supervisor at ESS, for his continuous support and guidance during my internship.
I also thank the Ethiopian Statistics Service for providing the opportunity and resources to carry out this project.

14. References
•	Flask Official Documentation – https://flask.palletsprojects.com/
•	SQLAlchemy ORM Documentation – https://www.sqlalchemy.org/
•	Render Deployment Guide – https://render.com/docs

