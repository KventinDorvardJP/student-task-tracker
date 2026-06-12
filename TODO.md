# Student Task Tracker Roadmap

## Working Rules

* Work on only one milestone at a time.
* Do not add features from later milestones early.
* Manually test each milestone before marking it complete.
* Commit a stable checkpoint after completing each milestone.
* Keep the old CLI files until the Django version reaches feature parity.

---

## Version 0 — Python CLI with JSON

* [x] Create a looping command-line menu
* [x] Add tasks
* [x] List tasks
* [x] Mark tasks as done
* [x] Delete tasks
* [x] Save tasks to `tasks.json`
* [x] Load tasks automatically
* [x] Test the complete CLI flow

---

## Version 1 — Python CLI with SQLite

* [x] Create the SQLite database
* [x] Create the `tasks` table
* [x] Replace JSON loading with database queries
* [x] Insert new tasks into the database
* [x] List tasks from the database
* [x] Update task status in the database
* [x] Delete tasks from the database
* [x] Test the complete SQLite flow

---

## Version 1.1 — Validation and Status Changes

* [x] Reject an empty title
* [x] Reject an empty subject
* [x] Reject an empty due date
* [x] Validate the due-date format
* [x] Support `todo`, `doing`, and `done`
* [x] Test validation and status changes
* [x] Commit a stable CLI checkpoint

---

# Version 2 — Django Web Application

## Version 2.0 — Django Foundation

* [x] Create the Django project
* [x] Create the `tasks` application
* [x] Add `tasks` to `INSTALLED_APPS`
* [x] Create the Django `Task` model
* [x] Add status choices to the model
* [x] Create the initial migration
* [x] Apply the migration
* [x] Register `Task` in Django Admin
* [x] Create a task through Django Admin
* [x] Change a task through Django Admin
* [x] Delete a task through Django Admin
* [x] Protect local secrets with `.env`
* [x] Ignore local databases and cache files in Git

---

## CURRENT: Version 2.1 — Task List Page

### Goal

Display tasks from the Django database on a normal webpage without using Django Admin.

### Implementation Checklist

* [ ] Create `tasks/urls.py`
* [ ] Add a URL for the task-list page
* [ ] Include the tasks URLs in `student_tracker/urls.py`
* [ ] Create a `task_list` view
* [ ] Query tasks using `Task.objects`
* [ ] Create `tasks/templates/tasks/task_list.html`
* [ ] Pass the tasks from the view to the template
* [ ] Display each task’s title
* [ ] Display each task’s subject
* [ ] Display each task’s due date
* [ ] Display each task’s status
* [ ] Show a useful message when there are no tasks

### Acceptance Test

* [ ] Add two or more tasks through Django Admin
* [ ] Open the normal task-list page
* [ ] Confirm that every task appears
* [ ] Confirm that every task field appears correctly
* [ ] Confirm that an empty database does not cause an error
* [ ] Run `python manage.py check`
* [ ] Commit the completed milestone

### Not Part of This Milestone

* Do not create an add-task form.
* Do not add status buttons.
* Do not add deletion.
* Do not add CSS frameworks.
* Do not add authentication.

---

## Version 2.2 — Add Task Page

* [ ] Learn the purpose of a Django form
* [ ] Create a `TaskForm`
* [ ] Create an add-task view
* [ ] Create an add-task URL
* [ ] Create an add-task template
* [ ] Display all required fields
* [ ] Submit the form using `POST`
* [ ] Include CSRF protection
* [ ] Save valid tasks
* [ ] Display validation errors
* [ ] Redirect to the task list after success
* [ ] Test invalid and valid submissions
* [ ] Commit the completed milestone

---

## Version 2.3 — Change Task Status

* [ ] Create a status-change URL
* [ ] Create a status-change view
* [ ] Accept only valid status values
* [ ] Update the selected task
* [ ] Use `POST` for status changes
* [ ] Add status controls to the task list
* [ ] Redirect back to the task list
* [ ] Test `todo`, `doing`, and `done`
* [ ] Test an invalid task ID
* [ ] Commit the completed milestone

---

## Version 2.4 — Delete Tasks

* [ ] Create a delete-task URL
* [ ] Create a delete-task view
* [ ] Create a confirmation page
* [ ] Require `POST` for the actual deletion
* [ ] Redirect to the task list after deletion
* [ ] Test cancelling deletion
* [ ] Test confirming deletion
* [ ] Test an invalid task ID
* [ ] Commit the completed milestone

---

## Version 2.5 — Basic Interface Structure

* [ ] Create a shared base template
* [ ] Add navigation between task pages
* [ ] Add success and error messages
* [ ] Clearly distinguish task statuses
* [ ] Order tasks by due date
* [ ] Make overdue tasks recognizable
* [ ] Add simple project-owned CSS
* [ ] Test all navigation
* [ ] Commit the completed milestone

---

## Version 2.6 — Automated Tests

* [ ] Add model tests
* [ ] Test the task-list page
* [ ] Test the empty task list
* [ ] Test valid task creation
* [ ] Test invalid task creation
* [ ] Test status changes
* [ ] Test task deletion
* [ ] Run the complete test suite successfully
* [ ] Commit the completed milestone

---

## Version 2.7 — Documentation and Cleanup

* [ ] Update `README.md` for the Django version
* [ ] Document installation steps
* [ ] Document environment-variable setup
* [ ] Document migrations
* [ ] Update `CHANGELOG.md`
* [ ] Decide whether to archive or remove the old CLI files
* [ ] Confirm no secrets or databases are tracked
* [ ] Perform a complete manual test
* [ ] Commit the stable Django version

---

## Later Backlog — Do Not Start Yet

* [ ] User accounts
* [ ] Tasks belonging to individual users
* [ ] Filtering and searching
* [ ] Deployment
* [ ] REST API
* [ ] JavaScript enhancements
