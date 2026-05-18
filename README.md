# AH CompSci SDD Python

A Python learning repository for Advanced Higher Computer Science: Software Design & Development.

This repository contains structured programming lessons, code examples, and tasks across four booklets:
- **Booklet 1:** Object-oriented programming concepts
- **Booklet 2:** Data types and structures
- **Booklet 3:** Standard algorithms
- **Booklet 4:** Database connections

## AI Use in This Course

This course is about learning to code yourself, not relying on AI to generate answers.

Switch off AI coding tools while working on tasks.

### How to switch off AI in Codespaces/VS Code

1. Open **Extensions**.
2. Find **GitHub Copilot** and choose **Disable**.
3. Find **GitHub Copilot Chat** and choose **Disable**.
4. Open **Settings** and turn off **Editor: Inline Suggest: Enabled**.

You can still use the repository guides and examples to support your own coding practice.

## Getting Started

### 1. Fork the repository

1. Open this repository on GitHub.
2. Click **Fork** to create your own copy.
3. Open your forked repository.

### 2. Create a Codespace

1. Click **Code**.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait for the codespace to start in the browser.

### 3. Install VS Code extensions

Install these required extensions:

1. Open the **Extensions** view in VS Code.
2. Search for **PDF Viewer**.
3. Install **PDF Viewer**.
4. Search for **Live Server**.
5. Install **Live Server**.

Use **PDF Viewer** for booklet files and **Live Server** for the generated website pages.

### 4. Set up your environment

First, open a terminal in Codespaces:

1. Click **Terminal** on the top menu.
2. Click **New Terminal**.
3. Keyboard shortcuts:
	- Toggle terminal: **Ctrl+`** (Windows/Linux) or **Cmd+`** (Mac)
	- New terminal: **Ctrl+Shift+`** (Windows/Linux) or **Cmd+Shift+`** (Mac)

Then run the setup commands below.

In the terminal, from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 5. Configure Git

Set your Git name and email (required for commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 6. Create `.env` file

Create a file named `.env` in the project root and add your database details:

```env
DB_HOST=your-host-name
DB_USER=your-username
DB_PASS=your-password
DB_NAME=your-database-name
```

Ask your teacher for the correct values if using a shared/school database.

### 7. Verify setup

Run the first program to test your setup:

```bash
python "Booklet 1 - OOP/Program 1 - defining a class.py"
```

You should see a successful program output.

### 8. Open the website

The HTML pages are stored in the `website` folder.

1. Open `website/index.html` in VS Code.
2. Right-click the file and choose **Open with Live Server**.
3. Your browser should open the website entry page and link to every booklet page.

If Live Server opens the wrong folder, stop it and start it again from `website/index.html`.

## Daily Workflow

See [STARTING_YOUR_DAY.md](STARTING_YOUR_DAY.md) for how to begin a coding session each day.

## Saving Your Work

See [COMMIT_AND_PUSH.md](COMMIT_AND_PUSH.md) for how to save and push your changes to GitHub at the end of each session.