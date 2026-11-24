# VS Code Extensions Documentation

## 1. Overview

Visual Studio Code was used as the main development environment for RollCall.

The selected extensions supported:

- Python development
- Code completion
- Code formatting
- Git and GitHub workflow
- SQLite database inspection

The extensions were selected because they were directly related to the technologies used in the project.

## 2. Selected Extensions

| Extension                  | Publisher        | Purpose                                               |
| -------------------------- | ---------------- | ----------------------------------------------------- |
| Python                     | Microsoft        | Runs and debugs Python applications                   |
| Pylance                    | Microsoft        | Provides Python code completion and error detection   |
| Prettier - Code formatter  | Prettier         | Formats HTML, CSS, and other supported files          |
| GitLens — Git supercharged | GitKraken        | Displays Git history, commits, and branch information |
| SQLite Viewer              | Florian Klampfer | Displays SQLite database tables inside VS Code        |

## 3. Python Extension

### Purpose

The Python extension provides Python language support in Visual Studio Code.

### How It Was Used

The extension was used to:

- Run app.py
- Select the Python interpreter
- Start the Flask application
- Support Python development

### Evidence

Screenshot:

    screenshots/1-python-running-app.png

The screenshot shows the RollCall Flask application being run from VS Code.

## 4. Pylance Extension

### Purpose

Pylance provides Python language features such as autocomplete, code navigation, type information, and error detection.

### How It Was Used

Pylance was used while editing:

- app.py
- database.py
- holiday_service.py
- tests/test_app.py

It helped identify Python syntax and coding issues during development.

### Evidence

Screenshot:

    screenshots/2-pylance-code-assistance.png

The screenshot shows Pylance code suggestions or code assistance inside VS Code.

## 5. Prettier - Code Formatter

### Purpose

Prettier automatically formats supported files using a consistent style.

### How It Was Used

Prettier was used to format:

- HTML templates
- CSS files
- Project documentation files where applicable

It improved indentation, spacing, and code readability.

### Evidence

Screenshot:

    screenshots/3-prettier-formatting.png

The screenshot shows a formatted HTML or CSS file in VS Code.

## 6. GitLens — Git supercharged

### Purpose

GitLens provides additional Git and GitHub information inside Visual Studio Code.

### How It Was Used

GitLens was used to:

- View commit history
- Review file changes
- Identify commits connected to files
- Observe branch development
- Review the project’s Git workflow

The project used several feature branches, including:

- feature/interface-improvements
- feature/testing-and-validation
- feature/documentation-and-release

### Evidence

Screenshot:

    screenshots/4-gitlens-commit-history.png

The screenshot shows the RollCall commit history or Git branch information.

## 7. SQLite Viewer

### Purpose

SQLite Viewer allows database tables to be opened and inspected directly inside VS Code.

### How It Was Used

SQLite Viewer was used to inspect:

- students
- classes
- enrollments
- attendance

It helped verify that records were being stored correctly in the RollCall database.

### Extension Information

Name:

    SQLite Viewer

Publisher:

    Florian Klampfer

Extension ID:

    qwtel.sqlite-viewer

### Evidence

Screenshot:

    screenshots/5-sqlite-database-viewer.png

The screenshot shows the RollCall SQLite database and its tables.

## 8. Benefits to the Project

The extensions improved the development process by:

- Making Python development easier
- Providing code completion and error detection
- Improving code formatting
- Making Git history easier to review
- Allowing the SQLite database to be inspected visually

## 9. Limitations

The extensions depend on the selected VS Code environment.

Some limitations include:

- Extensions may have different features across versions.
- SQLite Viewer is primarily used for viewing database content.
- Pylance suggestions depend on the selected Python interpreter.
- Prettier may format files differently from the developer’s preferred style.
- GitLens features may vary depending on GitHub connection settings.

## 10. Conclusion

The selected VS Code extensions supported the development, testing, database inspection, formatting, and version-control requirements of RollCall.

Five relevant extensions were used and documented based on their contribution to the software development process.
