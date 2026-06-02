# Student Task Tracker

A simple Python command-line app for tracking school tasks.

This is Version 0 of the project.  
It uses Python lists and dictionaries, and saves tasks to a JSON file.

## Goal

The goal of this project is to practice:

- Python functions
- Lists and dictionaries
- User input
- Basic command-line menus
- Saving and loading data with JSON

## Features

The program can:

- Add a task
- List all tasks
- Mark a task as done
- Delete a task
- Save tasks to `tasks.json`
- Load tasks from `tasks.json`

## Task Structure

Each task has these fields:

```python
{
    "title": "Finish math homework",
    "subject": "Math",
    "due_date": "2026-05-12",
    "status": "todo"
}