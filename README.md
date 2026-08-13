# <img width="74" height="64" alt="Logo" src="https://github.com/user-attachments/assets/505e5aa4-fdec-49f2-a13e-49c550203796" />  Emergency Rescue Dashboard

- This project contains searchable data of dog breeds for quick humanitarian rescue missions. 
---

## 📌 Overview
- The problem of missing persons is very prominent globally. This application is a means to help solve the problem
of missing persons specifically within the United States.

- The core idea is to use a small dataset of dogs that can be used to track humans based on a dog's strength,
primary specialty, group, trainability, energy level, and temperament with humans.

- The main features include a database, a viewable map (geolocation) with animal shelter longitude and latitude,
a front‑end data view, and a search feature for the dashboard to swiftly search for mission needs.

- The intended audience for this application is families and small businesses.

---

## 🧠 Project Explanation
- **System organization**  
  The system comprises three elements. The client side (`app.py`) is where the layout code is housed.
  It features the dashboard table data itself. At the bottom of the file is where the callbacks for search
  functionality via the data table are placed. To the right of the data table lies the map container.
  `animal_shelter.py` contains the mock database code, giving the app the capability to connect to a MongoDB database.
  `geolocation.py` contains the map display logic.

- `animal_shelter.py` is the key module.  
- The data is pulled from the CSV file and placed within a DataFrame for front‑end rendering in `app.py`.
- **Tech stack used:** VSCode, Python3, pip3, pandas, Plotly Dash, base64, embedded HTML (Dash imports),
  MongoDB, CLI, and Git.

---

## ⚙️ Installation
Steps to set up the project locally.  
Include prerequisites (software versions, environment variables, etc.).

1. Download, install, and verify Python and pip.  
   `python --version` | `python -m pip --version`
2. Create a project folder anywhere of your choice.
3. If using the command line, `cd` into the project folder and create the virtual environment:  
   `python -m venv venv`
4. Create the `app.py` file within the folder itself or in your IDE.

---

## 🚀 Usage
- Run `python app.py` to interact. Click the link and you're good to go.

---

## 📁 Project Structure
<img width="344" height="412" alt="Screenshot 2026-08-13 182830" src="https://github.com/user-attachments/assets/d59c277a-91c7-4911-8484-57b04b443752" />


## Demonstration
<img width="1904" height="855" alt="brave_screenshot" src="https://github.com/user-attachments/assets/ec7c5b6b-38a9-480e-bedd-acb6980f57ad" />
<img width="1920" height="804" alt="Search" src="https://github.com/user-attachments/assets/563cd6f4-13c6-45b3-8be2-948f2547a44a" />
<img width="1920" height="911" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/32544443-ca67-432a-ba1b-14ecb840af9b" />

## Optimal screen size breaks
- iPad Air
- Surface Pro 7
- Asus Zen book Fold
- Computer Monitor
- Laptop

---

## 🔗 Sources / References
- https://www.python.org/doc/
- https://pip.pypa.io/en/stable/
- https://docs.python.org/3/library/
- https://pandas.pydata.org/docs/
- https://plotly.com/python/
- https://dash.plotly.com/
- https://flask.palletsprojects.com/
- https://geopy.readthedocs.io/en/stable/
- https://stackoverflow.com/
- https://pypi.org/
- https://copilot.microsoft.com

## 🙌 Acknowledgments
- Southern New Hampshire University college project (2023) enhanced (2026).


