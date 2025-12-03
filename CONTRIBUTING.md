# Contributing Guidelines

Thanks for your interest in contributing to `irctc-backend`! This guide explains how to set up your environment, make changes, and submit them effectively.

## Prerequisites
- Python 3.10+
- MySQL server running locally or accessible remotely
- `git` installed and configured

## Setup
- Fork the repository and clone your fork.
- Create and activate a virtual environment.
- Install dependencies.
- Configure your `.env` for MySQL.

```bash
git clone <your-fork-url>
cd irctc-backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Create .env in the project root
cat > .env << 'EOF'
MYSQL_DATABASE="<your mysql db>"
MYSQL_USER="<your mysql user>"
MYSQL_ROOT_PASSWORD="<your mysql password>"
EOF
```

If you need to initialize the database, see `README.md` for the order of running SQL files (`railway_system`, `views`, `triggers`, `data`).

## Branching Strategy
- Base all work off `master` unless otherwise directed.
- Use short-lived feature branches: `feature/<short-description>`.
- For fixes: `fix/<short-description>`.
- For docs: `docs/<short-description>`.

## Commit Messages
- Use clear, imperative messages (e.g., "Add trips CRUD endpoint").
- Prefix scope when helpful: `routes:`, `models:`, `utils:`, `schemas:`.
- Reference issues/PRs where applicable: `Fixes #123`.

## Code Style
- Follow PEP 8 and keep code simple and readable.
- Use descriptive variable and function names.
- Avoid inline comments unless clarifying non-obvious logic.
- Keep changes minimal and focused; do not refactor unrelated code.

## Testing & Running Locally
- Start the server during development:
```bash
uvicorn main:app --reload
```
- Check interactive docs at `http://localhost:8000/docs` and `http://localhost:8000/redoc`.

## Database & Migrations
- Coordinate schema changes via PRs; include SQL files if needed.
- Document any migration steps in the PR description.
- Ensure local setup instructions remain valid after changes.

## Security
- Do not commit secrets or credentials.
- Store configuration in `.env` and keep it out of version control.
- Report security issues privately to the maintainers; do not open a public issue.

## Pull Requests
- Ensure your branch is rebased on `master` before opening a PR.
- Include a concise description, motivation, and screenshots for API docs changes where helpful.
- Add tests or manual verification steps (e.g., curl examples) when changing endpoints.
- Keep PRs small and focused; large PRs are harder to review.

## Issue Reporting
- Use clear titles and detailed descriptions.
- Include reproduction steps, expected vs actual behavior, and environment details.
- Label appropriately (bug, feature, docs).

## Checklist Before Requesting Review
- Code compiles and the app runs locally.
- No unrelated changes included.
- README or docs updated when behavior or setup changes.
- Commits are clean and logically grouped.

## Conduct
- Be respectful and collaborative.
- Provide constructive feedback in reviews.
- Assume best intent and focus on improving the project.

For general project usage and setup, see `README.md`. Happy contributing!

