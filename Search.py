import tkinter as tk
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection1 = db['Direct_material']
collection2 = db['Actual']
collection3 = db['COGS']
collection4 = db['Allocated']

# Function to search for Job ID and display beginning and ending inventory
def search_job():
    job_id = int(job_id_entry.get())  # Get the Job ID from the entry widget

    # Query the MongoDB collections
    job_data_dm = collection1.find_one({"Job ID": job_id})
    job_data_actual = collection2.find_one({"Job ID": job_id})
    job_data_cogs = collection3.find_one({"Job ID": job_id})
    job_data_allocated = collection4.find_one({"Job ID": job_id})

    if job_data_dm and job_data_actual and job_data_cogs and job_data_allocated:
        beginning_inventory_dm = job_data_dm.get("Begining inventory DM")
        ending_inventory_dm = job_data_dm.get("Ending inventory DM")
        beginning_inventory_idm = job_data_actual.get("Begining inventory IDM")
        ending_inventory_idm = job_data_actual.get("Ending inventory IDM")
        beg_wip = job_data_cogs.get("Begining work in process used for a specific job")
        end_wip = job_data_cogs.get("Ending work in process used for a specific job")
        beg_f_wip = job_data_cogs.get("Beginig inventory of finished good used for a specific job")
        end_f_wip = job_data_cogs.get("Ending inventory of finished good used for a specific job")
        cost_of_man_good_sold = job_data_cogs.get("Cost of good manfucatred for specific job")
        cost_of_good_sold = job_data_cogs.get("Cost of good sold for a specific job")
        tot_over_under_allocated = job_data_allocated.get("Total of over or under allocated MOH")
        prorated = job_data_cogs.get("Prorated cost of good sold for a specific job")

        # Update labels with retrieved data
        result_label0.config(text=f"Results for Job ID {job_id}")
        result_label1.config(text=f"Beginning inventory for DM: {beginning_inventory_dm}")
        result_label2.config(text=f"Ending inventory for DM: {ending_inventory_dm}")
        result_label3.config(text=f"Beginning inventory for IDM: {beginning_inventory_idm}")
        result_label4.config(text=f"Ending inventory for IDM: {ending_inventory_idm}")
        result_label5.config(text=f"Begining work in process used for a specific job: {beg_wip}")
        result_label6.config(text=f"Ending work in process used for a specific job: {end_wip}")
        result_label7.config(text=f"Beginig inventory of finished good used for a specific job: {beg_f_wip}")
        result_label8.config(text=f"Ending inventory of finished good used for a specific job: {end_f_wip}")
        result_label9.config(text=f"Cost of good manfucatred for specific job: {cost_of_man_good_sold}")
        result_label10.config(text=f"Cost of good sold for a specific job: {cost_of_good_sold}")
        result_label11.config(text=f"Total of over or under allocated MOH: {tot_over_under_allocated}")
        result_label12.config(text=f"Prorated cost of good sold for a specific job: {prorated}")
    else:
        result_label0.config(text=f"No data found for Job ID {job_id}")

# Create the tkinter window
root = tk.Tk()
root.title("Job ID Search")

# Create a frame for the input fields and results
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Job ID input widgets
job_id_label = tk.Label(input_frame, text="Job ID:")
job_id_label.grid(row=0, column=0)
job_id_entry = tk.Entry(input_frame)
job_id_entry.grid(row=0, column=1)

search_button = tk.Button(input_frame, text="Search", command=search_job)
search_button.grid(row=0, column=2)

# Results frame to display output
results_frame = tk.Frame(root)
results_frame.pack(padx=10, pady=10)

# Result labels
result_label0 = tk.Label(results_frame, text="")
result_label0.pack()

result_label1 = tk.Label(results_frame, text="")
result_label1.pack()

result_label2 = tk.Label(results_frame, text="")
result_label2.pack()

result_label3 = tk.Label(results_frame, text="")
result_label3.pack()

result_label4 = tk.Label(results_frame, text="")
result_label4.pack()

result_label5 = tk.Label(results_frame, text="")
result_label5.pack()

result_label6 = tk.Label(results_frame, text="")
result_label6.pack()

result_label7 = tk.Label(results_frame, text="")
result_label7.pack()

result_label8 = tk.Label(results_frame, text="")
result_label8.pack()

result_label9 = tk.Label(results_frame, text="")
result_label9.pack()

result_label10 = tk.Label(results_frame, text="")
result_label10.pack()

result_label11 = tk.Label(results_frame, text="")
result_label11.pack()

result_label12 = tk.Label(results_frame, text="")
result_label12.pack()

# Run the tkinter main loop
root.mainloop()
