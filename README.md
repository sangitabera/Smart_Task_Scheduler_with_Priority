# 🚀 Smart Task Scheduler with Priority Queue
A professional web-based task management system built using Streamlit + Python Heap (Priority Queue) that intelligently prioritizes tasks based on urgency and deadlines.

# This project demonstrates strong understanding of:

Object-Oriented Programming (OOP)

Priority Queue (Heap)

JSON Persistence

Clean Project Architecture

Streamlit Web UI

Deadline-based dynamic prioritization

# 📌 Features

✅ Add tasks with title, description, priority, and deadline

✅ Automatic sorting using Heap-based Priority Queue

✅ Smart urgency calculation

✅ Mark tasks as completed

✅ Delete tasks

✅ Filter tasks (High Priority, Today, Completed, Overdue)

✅ Persistent storage using JSON

✅ Color-coded deadline highlighting

✅ Modular and clean folder structure

✅ Deployable on Streamlit Cloud

# 🧠 How It Works (Technical Overview)

# 1️⃣ Task Modeling

Each task is represented as a Task object with:
title

description

priority (1 = High, 2 = Medium, 3 = Low)

deadline (datetime)

created_at

status

Custom comparison logic ensures intelligent sorting.

# 2️⃣ Priority Queue (Heap)

**Tasks are stored using Python’s heapq:**

(priority, deadline, counter, task)

**This guarantees:**

Highest priority tasks appear first

Earlier deadlines override same-priority tasks

Stable ordering using unique counter

**Time Complexity:**

Insert → O(log n)

Retrieve → O(n log n) for sorted display

# 3️⃣ Smart Urgency Logic

**The system dynamically increases urgency if:**

Deadline is within 24 hours

This makes the scheduler adaptive and intelligent.

# 4️⃣ Persistent Storage

**Tasks are stored in:**

data.json

**Features:**

Safe JSON serialization

Datetime → ISO format conversion

Error handling for corrupted or empty files

# 📁 Project Structure

smart_task_scheduler/
│
├── app.py
│
├── models/
│   └── task.py
│
├── services/
│   ├── scheduler.py
│   ├── storage.py
│   └── urgency.py
│
├── data/
│   └── data.json
│
└── requirements.txt

# ⚙️ Installation

# 1️⃣ Clone Repository

git clone https://github.com/your-username/smart-task-scheduler.git

cd smart-task-scheduler

# 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv

venv\Scripts\activate   # Windows

source venv/bin/activate   # Mac/Linux

# 3️⃣ Install Dependencies

pip install -r requirements.txt

# 4️⃣ Run Application

streamlit run app.py

**Open in browser:**

http://localhost:8501

# 🌍 Deployment (Streamlit Cloud)

Push project to GitHub

Go to https://streamlit.io/cloud⁠�

Connect GitHub repository

Select app.py

Deploy

Free tier is sufficient for portfolio usage.

# 🛠 Technologies Used

Python 3.x

Streamlit

Heapq (Priority Queue)

JSON

Datetime module

# 🎯 Key Learning Outcomes

**This project demonstrates:**

Data structure implementation in real-world systems

Clean modular backend architecture

Separation of concerns

State management in web apps

Production-ready folder structure

Debugging and serialization handling

Practical algorithm application

# 🚀 Future Improvements

User authentication system

SQLite / PostgreSQL integration

Real-time notifications

Multi-user support

Docker containerization

REST API integration (FastAPI backend)

Role-based access control

Email reminders

# 👩‍💻 Author
Sangita Bera

Python Developer | Backend Enthusiast | Building Real-World Systems
📜 License
This project is open-source and available under the MIT License.
⭐ If you like this project, give it a star on GitHub!
