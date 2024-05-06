import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Direct_labour']

def calculate_direct_labour_cost():
    job_id = int(job_id_entry.get())
    existing_document = collection.find_one({"Job ID": job_id})
    if existing_document:
        # Display a message if the job_id already exists
        result_label_4.config(text="Job ID already exists!")
        return
    total_working_hours_p = int(total_working_hours_p_entry.get())
    base_wage_p = int(base_wage_p_entry.get())
    fringe_benefit_of_production_tot = int(fringe_benefit_of_production_tot_entry.get())
    total_p_workers = int(total_p_workers_entry.get())

    production = (total_working_hours_p * base_wage_p) * total_p_workers + fringe_benefit_of_production_tot
    result_label_1.config(text=f"Production labour cost is: {production}")

    total_working_hours_a = int(total_working_hours_a_entry.get())
    base_wage_a = int(base_wage_a_entry.get())
    fringe_benefit_of_assembly_tot = int(fringe_benefit_of_assembly_tot_entry.get())
    total_a_workers = int(total_a_workers_entry.get())

    assembly = (total_working_hours_a * base_wage_a) * total_a_workers + fringe_benefit_of_assembly_tot
    result_label_2.config(text=f"Assembly labour cost is: {assembly}")

    total_working_hours_f = int(total_working_hours_f_entry.get())
    base_wage_f = int(base_wage_f_entry.get())
    fringe_benefit_of_finishing_tot = int(fringe_benefit_of_finishing_tot_entry.get())
    total_finishing_workers = int(total_finishing_workers_entry.get())

    finishing = (total_working_hours_f * base_wage_f) * total_finishing_workers + fringe_benefit_of_finishing_tot
    result_label_3.config(text=f"Finishing labour cost is: {finishing}")

    Direct_labour_cost = production + assembly + finishing
    result_label_4.config(text=f"Direct labour cost is: {Direct_labour_cost}")

    document = {
        "Job ID": job_id,
        "Total working hours of production": total_working_hours_p,
        "Base wage of production": base_wage_p,
        "Fringe benefit of production total": fringe_benefit_of_production_tot,
        "Total number of production workers": total_p_workers,
        "Production": production,
        "Total working hours of assembling": total_working_hours_a,
        "Base wage of assembling": base_wage_a,
        "Fringe benefit of assembling total": fringe_benefit_of_assembly_tot,
        "Total number of assembling workers": total_a_workers,
        "Assembly": assembly,
        "Total working hours of finishing": total_working_hours_f,
        "Base wage of finishing": base_wage_f,
        "Fringe benefit of finishing total": fringe_benefit_of_finishing_tot,
        "Total number of finishing workers": total_finishing_workers,
        "Finishing": finishing,
        "Direct labour cost": Direct_labour_cost
    }

    collection.insert_one(document)
    print(Direct_labour_cost)

root = tk.Tk()
root.title("Direct Labour Cost Calculator")

labels = [
    "Job number:",
    "Total working hours of production:",
    "Base wage for production:",
    "Fringe benefit of production :",
    "Total workers for production:",
    "Total working hours of assembling:",
    "Base wage for assembling:",
    "Fringe benefit of assembling:",
    "Total workers for assembling:",
    "Total working hours of finishing:",
    "Base wage for finishing:",
    "Fringe benefit of finishing:",
    "Total workers for finishing:"
]

entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

job_id_entry = entries[0]
total_working_hours_p_entry = entries[1]
base_wage_p_entry = entries[2]
fringe_benefit_of_production_tot_entry = entries[3]
total_p_workers_entry = entries[4]
total_working_hours_a_entry = entries[5]
base_wage_a_entry = entries[6]
fringe_benefit_of_assembly_tot_entry = entries[7]
total_a_workers_entry = entries[8]
total_working_hours_f_entry = entries[9]
base_wage_f_entry = entries[10]
fringe_benefit_of_finishing_tot_entry = entries[11]
total_finishing_workers_entry = entries[12]

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(labels) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(labels) + 3, columnspan=2, padx=5, pady=5)

result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(labels) + 4, columnspan=2, padx=5, pady=5)

result_label_4 = tk.Label(root, text="")
result_label_4.grid(row=len(labels) + 5, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_direct_labour_cost)
calculate_button.grid(row=len(labels) + 1, columnspan=2, padx=5, pady=10)

root.mainloop()
