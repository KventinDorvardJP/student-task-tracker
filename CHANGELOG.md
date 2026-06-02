## 2026-06-02

#### Added
 - SQLite database inplimented instead of using .json

## 2026-05-24

#### Added
- Added task creation
- Added task listing
- Added marking tasks as done
- Added deleting tasks
- Added saving tasks to `tasks.json`
- Added automatic loading from `tasks.json` on startup

#### Changed
- Removed manual "Load tasks" menu option
- Changed menu Exit option to 6

#### Fixed
- Added pause after invalid menu input
- Made saved JSON easier to read with `indent=4`

#### Problems
- No known major problems for Version 0

#### Next Step
- Final test of Version 0

## 2026-05-19

#### Added
- Added task creation
- Added task listing
- Added mark task as done logic
- Added delete task feature

#### Fixed
- Improved task listing pause behavior

#### Problems
- Tasks are not saved to `tasks.json` yet

#### Next Step
- Build Step 6: Save/Load tasks to/from .json file

## 2026-05-08

#### Added
- Created `README.md`
- Created `CHANGELOG.md`
- Defined Version 0 checklist
- Added looping menu in `main.py`

#### Problems
- `main.py` has not been implemented yet
- `tasks.json` has not been implemented yet

#### Next Step
- Build Step 1: menu loop