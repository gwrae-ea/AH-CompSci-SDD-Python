# AH CompSci SDD Python - Student Starter Guide (Codespaces)

Use this guide at the start of a learning topic to set up your own working copy in GitHub Codespaces.

## 1. Create your own copy on GitHub

1. Open this repository on GitHub.
2. Click **Fork** to create your own copy.
3. Open your forked repository.

## 2. Open your fork in Codespaces

1. In your fork, click **Code**.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main**.
4. When the codespace appears in the list, click the **...** menu next to it.
5. Choose **Open in** -> **Visual Studio Code**.
	This option launches the VS Code desktop app and attaches it to your codespace.

Wait for the desktop codespace window to finish loading before continuing.

## 3. Create and activate a virtual environment

In the Codespaces terminal, from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Create your `.env` file

The database code reads environment values from a `.env` file in the project root.

Create a file named `.env` and add:

```env
DB_HOST=your-host-name
DB_USER=your-username
DB_PASS=your-password
DB_NAME=your-database-name
```

Ask your teacher for the correct values if you are using a shared/school database.

## 5. Check your `.gitignore`

Your `.gitignore` should include at least:

```gitignore
.env
.venv
```

This prevents secrets and virtual environment files from being committed.

## 6. Test your setup

Run the first database connection program:

```bash
python "Booklet 4 - Database Connections/Program 19 - Initial Connection.py"
```

If setup is correct, you should see a successful connection message and the database server version.

## 7. Daily workflow in Codespaces

Each time you open a new terminal:

```bash
source .venv/bin/activate
```

Then run whichever program your class is currently learning.