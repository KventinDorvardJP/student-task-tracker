## Version 1.1 — Validation and Status Changes

- [x] Validate task title is not empty
- [x] Validate task subject is not empty
- [x] Validate due date is not empty
- [x] Validate due date format
- [x] Change task status: todo / doing / done
- [x] Test full validation and status flow
- [x] Push stable checkpoint to GitHub

## Version 1 — SQLite Storage

- [x] Create `tasks.db`
- [x] Create `tasks` table
- [x] Replace `load_tasks()` with database loading
- [x] Replace `save_tasks()` or remove manual saving
- [x] Change `add_task()` to insert into database
- [x] Change `list_tasks()` to read from database
- [x] Change `mark_task_done()` to update database
- [x] Change `delete_task()` to delete from database
- [x] Test full menu flow