# <img width="74" height="64" alt="Logo" src="https://github.com/user-attachments/assets/505e5aa4-fdec-49f2-a13e-49c550203796" />  Emergency Rescue Dashboard

- This project contains searchable data of dog breeds for quick humanitarian rescue missions. 
---

## 📌 Overview
- The problem of missing persons is very prominent globally. This application is a means to solve the problem
of missing persons specifically within the United States. 

- The core idea is to use a small dataset of dogs that can be used to track humans based from a dog's strength, 
primary specialty, group, trainability, energy level and temperament with humans.

- The main features include a database, viewable map (geolocation) with animal shelter longitude and latitude,
front end data view and a search feature for the dashboard to swiftly search for mission needed.  

- The intended audience for this application are families and small businesses.  

---

## 🧠 Project Explanation
- System organization  
The system comprises three elements. The client side (app.py) is where the layout code is housed. 
it features the dashboard table data itself. At the bottom of the file is where I placed my callbacks for search 
functionality via data table. To the right of the datatable, lies the map container. animal_shelter.py contains 
the mock database lines of code giving the app the capability to connect to a MongoDB database. 
geolocation.py is the code of the map display data. 

- animal_shelter.py is the key module.   
- The data is pulled from the CSV file then place within a data frame for front end rendering within app.py.
- Tech stack used: VSCode, Python3, pip3, pandas, plotly Dash, base64, embedded HTML (dash import),
MongoDB, CLI and Git. 

---

## ⚙️ Installation
Steps to set up the project locally.  
Include prerequisites (software versions, environment variables, etc.).

1. Download, install, and verify python and pip. 'python --version' | 'python -m pip --version'
2. Create project folder anywhere of your choice.
3. If using the command line 'cd' into the project folder and create the virtual environment 'pyhon -m venv venv'
4. Create app.py file within the folder itself or in the IDE.

---

## 🚀 Usage

- Run - 'python app.py' to interact. Click the link and your good to go.

---

## 📂 Project Structure
     📂Dash 
       📂assets/logo.png
       🗄️.venv
       📂data/data.csv
       📂geolocation/geolocation.py
       📂modules/animal_shelter.py
       📂test/test_cases.py
     app.py

---

## 🧪 Testing
- app.run_server(debug=True) at the bottom of the main file for testing.
- Test cases. Filter uses assertion testing, styles uses exception check, and DB uses mock testing. 
---

## 📄 Commands Reference
- python --version
- pip --version
- python -m ensurepip --default-pip
- python -m venv venv
- venv\Scripts\activate
- pip install --upgrade pip
- pip install pandas
- pip install numpy
- pip install plotly
- pip install dash
- pip install flask
- pip install geopy
- pip install base64
- python app.py

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

---

## 🙌 Acknowledgments
- Southern New Hampshire University college project (2023) enhanced (2026).

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