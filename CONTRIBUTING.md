# 📝 Contributing to pyLEPhotoLog

Thank you for considering contributing to **pyLEPhotoLog**, an open-source Python tool for generating crime scene photo logs with metadata extraction and evidence integrity checks.

We welcome contributions that improve the script, fix bugs, add new features, enhance security, or improve documentation. Please follow the guidelines below to make the contribution process smooth.

---

## 📢 How to Contribute

### **1️⃣ Reporting Issues & Feature Requests**
If you find a **bug**, have a **feature request**, or see something that needs improvement:
1. **Check existing issues** to see if it's already reported.
2. Open a **new issue** with:
   - A **clear title** and **description**.
   - Steps to **reproduce the bug** (if applicable).
   - Suggested improvements or **expected behavior**.

🔗 [Open a New Issue](https://github.com/iotdetective/pyLEPhotoLog/issues)

---

### **2️⃣ Submitting Code Contributions**
To contribute **code improvements**, follow these steps:

#### **✅ Prerequisites**
- Ensure you have **Python 3.x** installed.
- Install dependencies:
  ```sh
  pip install pandas openpyxl
  ```
- Install **ExifTool** for metadata extraction:
  - 📥 [Download ExifTool](https://exiftool.org/)

#### **🔄 Fork the Repository**
1. **Fork** the repository to your GitHub account.
2. **Clone** your fork:
   ```sh
   git clone https://github.com/your-username/pyLEPhotoLog.git
   ```
3. **Create a new branch** for your changes:
   ```sh
   git checkout -b feature-branch
   ```

#### **✍️ Code Style Guidelines**
- Use **PEP 8** for Python code formatting.
- Write **clear, concise comments** where necessary.
- Ensure **error handling** (e.g., handle missing metadata gracefully).

#### **📝 Commit & Push Your Changes**
1. **Add modified files**:
   ```sh
   git add .
   ```
2. **Write a meaningful commit message**:
   ```sh
   git commit -m "Added feature XYZ to improve metadata extraction"
   ```
3. **Push changes to your fork**:
   ```sh
   git push origin feature-branch
   ```

#### **📩 Submit a Pull Request**
- Go to **your fork** on GitHub and click **"New Pull Request"**.
- Ensure:
  - Your code is **tested and works**.
  - The description **explains the changes clearly**.
  - It follows **coding guidelines**.

🔗 [Create a Pull Request](https://github.com/iotdetective/pyLEPhotoLog/pulls)

---

## 📜 Contribution Rules
✔ Keep contributions **focused and relevant** to the project.  
✔ Write **meaningful commit messages**.  
✔ Do **not** submit files that are auto-generated (e.g., `.pyc`, `__pycache__/`).  
✔ Ensure new features do **not break existing functionality**.  
✔ If adding a new feature, update the **README.md** if necessary.  

---

## 🔒 Security & Responsible Disclosure
If you find a **security vulnerability**, please follow **responsible disclosure** and **do not post it publicly**.

📧 **Report vulnerabilities privately via email**:  
[rich@nhletoolkit.com]

For more details, see our [Security Policy](SECURITY.md).

---

## ❤️ Acknowledgments
Your contributions help **improve this project** and benefit the **law enforcement and forensic community**. Thank you for your support! 🚔📸

---
