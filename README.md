# Team Management System

## Overview
A comprehensive Python-based project management system designed for college students to efficiently track team projects, manage student assignments, monitor milestones, and generate insightful reports.

## System Architecture
The system follows a **modular procedural architecture** with clear separation of concerns:

```
Team Management System
├── main.py                 # Entry point and main menu
├── data_storage.py         # Data persistence and validation
├── project_manager.py      # Project CRUD operations
├── student_manager.py      # Student and team management
├── milestone_tracker.py    # Milestone tracking and progress
├── reports.py             # Analytics and reporting
├── error_handler.py       # Error handling and logging
└── requirements.txt       # System dependencies
```

## Functional Requirements

### 1. Project Management Module
- **Create Projects**: Add new projects with validation
- **Read Projects**: View individual and all projects
- **Update Projects**: Modify project status and details
- **Delete Projects**: Remove projects with cleanup

### 2. Student/Team Management Module
- **Student Registration**: Add students with unique roll numbers
- **Team Assignment**: Assign/remove students from projects
- **Student Tracking**: Monitor student workload and assignments
- **Student Management**: Complete CRUD operations for students

### 3. Milestone Tracking Module
- **Milestone Creation**: Add milestones with due dates
- **Progress Tracking**: Update milestone status and monitor progress
- **Automatic Updates**: Auto-update project status based on milestone completion
- **Milestone Analytics**: Generate progress statistics

## Non-Functional Requirements

### 1. Usability
- **Intuitive Interface**: Simple, menu-driven console interface
- **Clear Navigation**: Organized menu structure with logical grouping
- **User Feedback**: Immediate confirmation of all operations
- **Help System**: Clear error messages and guidance

### 2. Reliability
- **Data Persistence**: Automatic saving to JSON files
- **Data Integrity**: Validation of all inputs and relationships
- **Backup System**: Manual save functionality
- **Crash Recovery**: Graceful handling of unexpected errors

### 3. Error Handling Strategy
- **Input Validation**: Comprehensive validation for all user inputs
- **Exception Management**: Centralized error handling system
- **Logging System**: Detailed error logging to files
- **User-Friendly Messages**: Clear error communication to users

### 4. Maintainability
- **Modular Design**: Clear separation of functionality into modules
- **Clean Code**: Well-documented functions with single responsibilities
- **Extensible Architecture**: Easy to add new features
- **Code Reusability**: Common functions centralized in utilities

## Technical Implementation

### Core Technologies
- **Language**: Python 3.6+
- **Data Storage**: JSON files for persistence
- **Architecture**: Modular procedural design
- **Error Handling**: Centralized logging system

### Key Features
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Data Validation**: Input validation and error checking
- **Progress Tracking**: Automatic progress calculation
- **Report Generation**: Multiple analytical reports
- **Data Export**: Summary export functionality

## Installation and Setup

1. **Clone/Download** the project files to your local directory
2. **Ensure Python 3.6+** is installed on your system
3. **Navigate** to the project directory
4. **Run** the application:
   ```bash
   python main.py
   ```

## Usage Guide

### Getting Started
1. Run `python main.py` to start the application
2. Use the numbered menu to navigate features
3. Follow on-screen prompts for data entry
4. Data is automatically saved after each operation

### Basic Workflow
1. **Add Projects** (Option 1) - Create your projects first
2. **Add Students** (Option 6) - Register team members
3. **Assign Students** (Option 8) - Build your project teams
4. **Add Milestones** (Option 11) - Set project milestones
5. **Track Progress** (Option 12) - Update milestone status
6. **Generate Reports** (Options 15-19) - Analyze progress

## File Structure
```
Vityarthi_project/
├── main.py                    # Main application entry point
├── data_storage.py           # Data persistence and validation
├── project_manager.py        # Project management functions
├── student_manager.py        # Student and team management
├── milestone_tracker.py      # Milestone tracking system
├── reports.py               # Report generation module
├── error_handler.py         # Error handling and logging
├── requirements.txt         # System requirements
├── README.md               # This documentation
├── team_data.json          # Data storage file (created automatically)
├── team_management.log     # Error log file (created automatically)
└── team_management_summary.txt # Export file (created on demand)
```

## Features

### Project Management
- Add, view, update, and delete projects
- Project status tracking
- Team assignment management
- Progress monitoring

### Student Management
- Student registration with unique roll numbers
- Project assignment tracking
- Workload analysis
- Team composition management

### Milestone Tracking
- Milestone creation with due dates
- Status updates (Pending, In Progress, Completed, Delayed)
- Automatic project progress calculation
- Deadline monitoring

### Reports and Analytics
- Project summary reports
- Student workload analysis
- Milestone status reports
- Deadline alert system
- Data export functionality

## Data Persistence
- All data is stored in JSON format for easy portability
- Automatic saving after each operation
- Manual save option available
- Data validation ensures integrity

## Error Handling
- Comprehensive input validation
- Centralized error logging
- User-friendly error messages
- Graceful failure recovery

## Future Enhancements
- Database integration (SQLite)
- Web-based interface
- Data visualization charts
- Email notifications for deadlines
- Multi-user support with authentication

## Python Concepts Demonstrated
- **Modular Programming**: Separation of concerns into modules
- **File I/O**: JSON data persistence
- **Error Handling**: Try-catch blocks and logging
- **Data Structures**: Dictionaries, lists for data management
- **Functions**: Modular function design
- **Input Validation**: Comprehensive data validation
- **Date/Time Handling**: Date validation and calculations
- **String Manipulation**: Data formatting and processing

## Academic Requirements Fulfilled

### Functional Requirements
- Three major modules: Project Management, Student Management, Milestone Tracking
- Clear input/output handling
- Logical workflow implementation
- Complete CRUD operations

### Non-Functional Requirements
- Usability: Menu-driven interface
- Reliability: Data persistence and validation
- Error Handling: Comprehensive error management
- Maintainability: Modular, clean code structure

### Technical Requirements
- Modular architectural design
- Application of core Python concepts
- Clean, maintainable implementation
- 8 meaningful modules/files
- Comprehensive documentation
