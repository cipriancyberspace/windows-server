# ⚙️ PowerShell – Basic Navigation Commands

This cheat sheet includes the most useful commands for navigating and managing files and folders using PowerShell.

---

## 📁 Directory Navigation

| Command                          | Description                                 |
|----------------------------------|---------------------------------------------|
| `pwd`                            | Show current directory (Print Working Directory) |
| `cd <path>`                      | Change directory to specified path          |
| `cd ..`                          | Go up one level                             |
| `cd \`                           | Go to root of current drive                 |
| `cd ~`                           | Go to user profile directory (e.g. `C:\Users\YourName`) |
| `ls` or `Get-ChildItem`          | List files and folders in current directory |
| `ls -Recurse`                    | List all files and folders recursively      |
| `ls -Force`                      | Show hidden and system files                |
| `dir`                            | Alias for `Get-ChildItem`                   |

---

## 📂 File & Folder Management

| Command                                      | Description                                 |
|----------------------------------------------|---------------------------------------------|
| `mkdir <foldername>`                         | Create new folder                           |
| `New-Item -Path . -Name "file.txt" -ItemType File` | Create a new empty file                     |
| `Remove-Item <filename>`                     | Delete a file or folder                     |
| `Copy-Item <source> <destination>`           | Copy file or folder                         |
| `Move-Item <source> <destination>`           | Move/rename file or folder                  |
| `Rename-Item <oldname> <newname>`            | Rename file or folder                       |

---

## 🧭 Path Helpers

| Expression             | Result                                 |
|------------------------|-----------------------------------------|
| `.`                    | Current directory                       |
| `..`                   | Parent directory                        |
| `$HOME`                | User profile directory                  |
| `$env:USERPROFILE`     | Same as `$HOME`                         |
| `$PWD`                 | Full path to current directory          |

---

## 🔍 File Search & Filtering

| Command                                         | Description                              |
|-------------------------------------------------|------------------------------------------|
| `Get-ChildItem -Recurse -Filter *.txt`          | Find all `.txt` files in current dir & subdirs |
| `Get-ChildItem -Recurse | Where-Object { $_.Length -gt 1MB }` | Find files larger than 1MB |

---

## 📄 Read & View Content

| Command                      | Description                              |
|------------------------------|------------------------------------------|
| `Get-Content file.txt`       | View content of a text file              |
| `gc file.txt`                | Alias for `Get-Content`                  |
| `cat file.txt`               | Another alias for `Get-Content`          |
| `type file.txt`              | Classic CMD-style display                |

---

## 🆘 Help & Aliases

| Command                      | Description                              |
|------------------------------|------------------------------------------|
| `Get-Command <keyword>`      | Show all commands matching a keyword     |
| `Get-Alias`                  | Show all available aliases                |
| `Get-Help <command>`         | Show help for a specific command          |
| `help <command> -Examples`   | Show example usage                        |

---

## 🧪 Examples

```powershell
cd "C:\Users\Administrator\Desktop"
mkdir logs
cd logs
New-Item -Name notes.txt -ItemType File
Get-Content notes.txt
```

---

✅ This file is useful for beginners, sysadmins, penetration testers, and anyone working regularly with Windows PowerShell.

