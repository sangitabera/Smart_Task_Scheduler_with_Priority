import streamlit as st
from datetime import datetime
from models.task import Task
from services.scheduler import TaskScheduler
from services.storage import save_tasks, load_tasks
from services.urgency import calculate_urgency


st.set_page_config(page_title="Smart Task Scheduler", layout="wide")
st.title("Smart Task Scheduler with Priority Queue")
scheduler = TaskScheduler()


loaded_task = load_tasks()
for task in loaded_task:
    scheduler.add_task(task)

with st.form("add_task_form"):
    st.subheader("Add New Task")
    title = st.text_input("Task Title")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", [1,2,3])
    deadline = st.date_input("Deadline")
    submit = st.form_submit_button("Add Task")

    if submit:
        if title:
            task = Task(
                title,
                description,
                priority,
                datetime.combine(deadline, datetime.min.time())
            )
            scheduler.add_task(task)
            save_tasks(scheduler.get_sorted_tasks())

            st.success("Task Added Successfully!")
        else:
            st.error("Title cannot be empty")


st.subheader("Filters")
filter_option = st.selectbox(
    "Filter by",
    ["All", "High Priority", "Today", "Completed","Overdue"]
)
tasks = scheduler.get_sorted_tasks()
filtered_tasks = []

for task in tasks:
    if filter_option == "High Priority" and task.priority != 1:
        continue
    if filter_option == "Today" and task.deadline.date() != datetime.now().date() :
        continue
    if filter_option == "Completed" and task.status != "Completed" :
        continue
    if filter_option == "Overdue" and task.deadline < datetime.now():
        continue
    filtered_tasks.append(task)


st.subheader("Task List")

for index, task in enumerate(filtered_tasks):
    urgency = calculate_urgency(task)
    color = "white"

    if task.deadline < datetime.now():
        color = "red"
    elif task.deadline.date() == datetime.now().date():
        color = "orange"

    st.markdown(
        f"""
        <div 
        style="padding:10px;
        border_radius:10px;
        background-color:{color}">
        <b>{task.title}</b><br>
        Description: {task.description}<br>
        Priority: {task.priority}<br>
        Deadline: {task.deadline}<br>
        Status: {task.status}
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    if col1.button("Mark Completed", key=f"complete_{index}"):
        task.status = "Completed"
        save_tasks(tasks)
        st.rerun()

    if col2.button("Delete", key=f"delete_{index}"):
        tasks.remove(task)
        save_tasks(tasks)
        st.rerun()