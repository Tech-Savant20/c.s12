# Class 12 Computer Science Project: Tkinter Apps

My Class 12 Computer Science project work (CBSE): small desktop applications built with Python's Tkinter GUI library, plus a MySQL-backed record manager.

## Programs

| File | What it is |
|------|------------|
| `Calculator.py` | A GUI calculator with number and operator buttons (`calculator.png` is a screenshot) |
| `untitled4.py` | A register/login screen. Each user's credentials are saved to a text file named after the username, and logging in checks against it |
| `CLASS12CS - Copy.txt` | A Tkinter front end for a MySQL database (via `mysql-connector-python`), with sign-up, sign-in, and add, delete, list and search screens |
| `CALCULATOR.txt`, `calculator - Copy.txt` | Other versions of the calculator code |
| `bankingnote.txt` | Earlier text-based banking program (see the [Class 11 project](https://github.com/Tech-Savant20/c.s-project-class-11)) |
| `computer project 12.docx` | The written project report |
| `article.txt` | A short written piece, not code |

## Running

Tkinter ships with most Python installations.

```bash
python Calculator.py
python untitled4.py
```

The MySQL program needs a running MySQL server and `pip install mysql-connector-python`. Copy `CLASS12CS - Copy.txt` to a `.py` file and set your connection details before running it.

## Notes

This is school work, kept as a record of where I started. The login demo stores passwords in plain text files, which is fine for a classroom exercise but not something to reuse.
