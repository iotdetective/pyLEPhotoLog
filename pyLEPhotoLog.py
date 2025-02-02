import os
import subprocess
import hashlib
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate MD5 sum of a file
def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to run exiftool and extract metadata
def get_exif_data(file_path):
    cmd = [
        "exiftool", "-DateTimeOriginal", "-Make", "-CameraModelName", "-ExposureTime", "-FNumber",
        "-ISO", "-Flash", "-LensType", "-LensID", "-FileSize", file_path
    ]
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exif_data = result.stdout.decode('utf-8').splitlines()

    exif_info = {
        'FileName': os.path.basename(file_path),
        'DateTimeOriginal': "N/A",
        'Make': "N/A",
        'CameraModelName': "N/A",
        'ExposureTime': "N/A",
        'FNumber': "N/A",
        'ISO': "N/A",
        'FlashType': "N/A",
        'LensType': "N/A",
        'LensID': "N/A",
        'FileSize': "N/A"
    }
    
    try:
        for line in exif_data:
            key_value = line.split(": ", 1)
            if len(key_value) < 2:
                continue
            key, value = key_value
            key = key.strip()
            value = value.strip()
            
            if key == "Date/Time Original":
                exif_info['DateTimeOriginal'] = value
            elif key == "Make":
                exif_info['Make'] = value
            elif key == "Camera Model Name":
                exif_info['CameraModelName'] = value
            elif key == "Exposure Time":
                exif_info['ExposureTime'] = value
            elif key == "F Number":
                exif_info['FNumber'] = value
            elif key == "ISO":
                exif_info['ISO'] = value
            elif key == "Flash":
                exif_info['FlashType'] = value
            elif key == "Lens Type":
                exif_info['LensType'] = value
            elif key == "Lens ID":
                exif_info['LensID'] = value
            elif key == "File Size":
                exif_info['FileSize'] = value
    except Exception:
        pass  # Keep default "N/A" values if parsing fails

    return exif_info

# Function to parse all photos in a directory
def parse_photos(directory_path):
    photo_data = []
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'tiff')):
                file_path = os.path.join(root, file)
                exif_info = get_exif_data(file_path)
                exif_info['FilePath'] = file_path
                exif_info['MD5'] = generate_md5(file_path)
                exif_info['Photo Description'] = ""  # Empty field for the detective to fill in later
                photo_data.append(exif_info)

    return photo_data

# Function to create an Excel file
def create_excel(photo_data, photographer_name, case_number, location, police_dept, output_filename="crime_scene_log.xlsx"):
    # Convert list of photo data to a DataFrame
    df = pd.DataFrame(photo_data)
    
    # Ensure DateTimeOriginal is parsed correctly
    df['DateTimeOriginal'] = pd.to_datetime(df['DateTimeOriginal'], format="%Y:%m:%d %H:%M:%S", errors='coerce')

    # Sort by DateTimeOriginal, keeping "N/A" values at the bottom
    df = df.sort_values('DateTimeOriginal', ascending=True, na_position='last')

    # Reorder columns to match the desired log structure
    df = df[['FileName', 'DateTimeOriginal', 'Make', 'CameraModelName', 'ExposureTime', 'FNumber', 
             'ISO', 'FlashType', 'LensType', 'LensID', 'FileSize', 'Photo Description', 'MD5']]

    # Create a new Excel writer object
    with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
        # Write additional case info at the top
        info_df = pd.DataFrame({
            'Photographer Name': [photographer_name],
            'Case Number': [case_number],
            'Location': [location],
            'Police Department': [police_dept]
        })
        
        # Write the case details to the first sheet
        info_df.to_excel(writer, index=False, header=True, startrow=0)
        
        # Write the photo data below the additional info
        df.to_excel(writer, index=False, header=True, startrow=len(info_df) + 2)

    return output_filename

# Function to open the file dialog for selecting a folder
def select_directory():
    folder_selected = filedialog.askdirectory()
    return folder_selected

# Function to run the entire process (called when the button is clicked)
def generate_log():
    photographer_name = photographer_name_entry.get()
    case_number = case_number_entry.get()
    location = location_entry.get()
    police_dept = police_dept_entry.get()

    if not photographer_name or not case_number or not location or not police_dept:
        messagebox.showwarning("Missing Information", "Please fill in all the fields.")
        return
    
    directory_path = select_directory()
    
    if not directory_path:
        messagebox.showwarning("No Directory", "Please select a directory containing images.")
        return
    
    try:
        photo_data = parse_photos(directory_path)
        
        if not photo_data:
            messagebox.showwarning("No Photos", "No photos found in the selected directory.")
            return
        
        output_filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not output_filename:
            messagebox.showwarning("No File", "Please specify a location to save the log file.")
            return
        
        log_file = create_excel(photo_data, photographer_name, case_number, location, police_dept, output_filename)
        messagebox.showinfo("Success", f"Log successfully generated: {log_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
def create_gui():
    global photographer_name_entry, case_number_entry, location_entry, police_dept_entry

    root = tk.Tk()
    root.title("Crime Scene Photo Log Generator")
    root.geometry("500x400")
    
    tk.Label(root, text="Photographer Name:", font=("Arial", 12)).pack(pady=5)
    photographer_name_entry = tk.Entry(root, font=("Arial", 12), width=40)
    photographer_name_entry.pack(pady=5)
    
    tk.Label(root, text="Case Number:", font=("Arial", 12)).pack(pady=5)
    case_number_entry = tk.Entry(root, font=("Arial", 12), width=40)
    case_number_entry.pack(pady=5)
    
    tk.Label(root, text="Location:", font=("Arial", 12)).pack(pady=5)
    location_entry = tk.Entry(root, font=("Arial", 12), width=40)
    location_entry.pack(pady=5)
    
    tk.Label(root, text="Police Department:", font=("Arial", 12)).pack(pady=5)
    police_dept_entry = tk.Entry(root, font=("Arial", 12), width=40)
    police_dept_entry.pack(pady=5)
    
    tk.Button(root, text="Generate Log", command=generate_log, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
