import tkinter as tk
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Allocated']
collection1 = db['Actual']
def calculate_allocated_moh():
    job_id = int(entry_job_number.get())

    actual_document = collection1.find_one({"Job ID": job_id})

    if actual_document is not None:
        actual_manufacturing_overhead = actual_document.get("Actual manufactoring overhead", 0)
    else:
        result_label_1.config(text=f"No actual data found for job ID:{job_id}")
        actual_manufacturing_overhead = 0

    total_budget_moh_year = int(entry_estimated_moh_year.get())
    total_budgeted_moh_hour_year = int(entry_estimated_moh_hours_year.get())
    actual_base = int(entry_estimated_hours_job.get())

    allocated_moh_for_job = (total_budget_moh_year / total_budgeted_moh_hour_year) * actual_base

    result_label_1.config(text=f"Allocated MOH for specific job: {allocated_moh_for_job}")

    total_over_under_allocated_MOH = allocated_moh_for_job - actual_manufacturing_overhead

    if total_over_under_allocated_MOH < 0:
        result_label_2.config(text=f"Under allocated:{total_over_under_allocated_MOH}")
    elif total_over_under_allocated_MOH > 0:
        result_label_2.config(text=f"Over allocated: {total_over_under_allocated_MOH}")
    else:
        result_label_2.config(text=f"Correct estimation: {total_over_under_allocated_MOH}")

    # Create and insert the document into MongoDB
    document = {
        "Job ID": job_id,
        "Estimated MOH for the year": total_budget_moh_year,
        "Estimated MOH hours for the year": total_budgeted_moh_hour_year,
        "Estimated hours for the job": actual_base,
        "Allocated MOH for the job": allocated_moh_for_job,
        "Total of over or under allocated MOH": total_over_under_allocated_MOH,
    }
    collection.insert_one(document)



# Create tkinter window
root = tk.Tk()
root.title("MOH Calculator")


labels = [
    "Job number:",
    "Estimated MOH for the year:",
    "Estimated MOH hours for the year:",
    "Estimated hours for the job:",
   
    
    
    
     
]

entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_job_number = entries[0]
entry_estimated_moh_year = entries[1]
entry_estimated_moh_hours_year = entries[2]
entry_estimated_hours_job = entries[3]


result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(labels) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(labels) + 3, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_allocated_moh)
calculate_button.grid(row=len(labels) + 1, columnspan=2, padx=5, pady=10)

root.mainloop()
