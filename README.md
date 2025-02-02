# 📸 pyLEPhotoLog (Crime Scene Photo Log Generator)
Crime Scene Photo Log Generator – A Python 3 GUI application that extracts EXIF metadata from images, generates an MD5 hash, and exports a sortable Excel report for investigative use.

## 🚀 Features
- Extracts metadata from images using `exiftool`
- Generates an MD5 hash for file integrity verification
- Outputs a structured **Excel (.xlsx) log** in a naming convention you select
- Provides a **fillable "Photo Description" column** for law enforecement to describe the contents of the photo is necessary
- Built in user-friendly **GUI for easy operation**

---

## 🛠️ Prerequisites

Before running this script, ensure you have the following installed:

### **1️⃣ Python 3.x**
📥 For Windows, download and install Python from [python.org](https://www.python.org/downloads/).

#### **Linux (Debian/Ubuntu)**
```sh
sudo apt install python3
```

### **2️⃣ Required Python Packages**
Install the pandas and openpyxl dependencies using **pip**:
```sh
pip install pandas openpyxl
```
Alternatively, on some newer Ubuntu systems you may have to install these packages in the following manner:
```sh
sudo apt install python3-pandas python3-openpyxl
```

### **3️⃣ ExifTool**
`exiftool` is required to extract image metadata.

#### **Windows**
1. Download ExifTool from: [https://exiftool.org/](https://exiftool.org/)
2. Extract `exiftool(-k).exe`
3. Rename it to `exiftool.exe`
4. Place it in `C:\Windows\` or add its location to the system **PATH**

#### **Mac (via Homebrew)**
```sh
brew install exiftool
```

#### **Linux (Debian/Ubuntu)**
```sh
sudo apt install exiftool
```

---

## 🎮 How to Run

1️⃣ **Clone this repository**  
```sh
git clone https://github.com/iotdetective/pyLEPhotoLog.git
cd pyLEPhotoLog
```

2️⃣ **Run the script**
```sh
python3 pyLEPhotoLog.py
```

3️⃣ **Follow the GUI prompts to:**
   - Enter the photographers name and case details
   - Select the local folder containing the crime scene images
   - Generate and save the Excel report in the location and with the name of your choice

---

## 📊 Output Example
The generated **Excel file** contains:

| File Name  | Date/Time Original | Make | Camera Model Name | Exposure Time | F Number | ISO | Flash Type | Lens Type | Lens ID | File Size | Photo Description | MD5 |
|------------|-------------------|------|------------------|--------------|---------|-----|------------|----------|--------|----------|----------------|------|
| image1.jpg | 2024:01:15 14:30:00 | Canon | EOS 5D Mark IV | 1/250s | f/2.8 | 100 | No Flash | EF 24-70mm | 123456 | 4.5 MB | [Detective Fills] | 8f7a89... |

---

## 🔏 License
This project is licensed under the **GNU General Public License v3.0**. See the [`LICENSE`](LICENSE) file for details.

---

## 🤝 Contributing
Feel free to submit **issues** or **pull requests** to improve this tool!

---

## 📝 Credits
Developed by **Rich Theberge**, [IOTDetective].

📧 Contact: rich@nhletoolkit.com
