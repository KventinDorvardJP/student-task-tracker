# Student Task Tracker

A simple Python command-line app for tracking school tasks.

This is Version 1 of the project.
It uses SQLite to save and load tasks.

## Goal

The goal of this project is to practice:

- Python functions
- Lists and dictionaries
- User input
- Basic command-line menus
- Saving and loading data with SQLite

## Features

The program can:

- Add a task
- List all tasks
- Change task status: todo / doing / done
- Delete a task
- Save tasks to a SQLite database
- Load tasks from a SQLite database

## Task Structure

Each task has these fields:

```python
{
    "title": "Finish math homework",
    "subject": "Math",
    "due_date": "2026-05-12",
    "status": "todo"
}