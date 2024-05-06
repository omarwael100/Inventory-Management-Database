import tkinter as tk
from pymongo import MongoClient

# MongoDB initialization
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Direct_labour']

def update_collection():
    # Function to update MongoDB collection based on user input
    job_id = int(entry_job_number.get())
    updates = {}

    document = collection.find_one({"Job ID": job_id})

    if document:
        # Fetching data from the document for Production section
        old_total_working_hours_p = document.get("Total working hours of production", 0)
        old_fringe_benefit_of_production_tot = document.get("Fringe benefit of production total", 0)
        old_total_p_workers = document.get("Total number of production workers", 0)

        # Getting input values from the user for Production section
        new_total_working_hours_p = int(entry_add_working_hours_p.get())
        new_fringe_benefit_of_production_tot = int(entry_add_fringe_benefit_p.get())
        new_total_p_workers = int(entry_add_workers_p.get())

        # Calculating new values for Production section
        total_working_hours_p = old_total_working_hours_p + new_total_working_hours_p
        base_wage_p = document.get("Base wage of production", 0)
        fringe_benefit_of_production_tot = old_fringe_benefit_of_production_tot + new_fringe_benefit_of_production_tot
        total_p_workers = old_total_p_workers + new_total_p_workers

        production = (total_working_hours_p * base_wage_p) * total_p_workers + fringe_benefit_of_production_tot
        result_label_1.config(text=f"Production labour cost is:{production}")

        # Fetching data from the document for Assembly section
        old_total_working_hours_a = document.get("Total working hours of assembling", 0)
        old_fringe_benefit_of_assembly_tot = document.get("Fringe benefit of assembling total", 0)
        old_total_a_workers = document.get("Total number of assembling workers", 0)

        # Getting input values from the user for Assembly section
        new_total_working_hours_a = int(entry_add_working_hours_a.get())
        new_fringe_benefit_of_assembly_tot = int(entry_add_fringe_benefit_a.get())
        new_total_a_workers = int(entry_add_workers_a.get())

        # Calculating new values for Assembly section
        total_working_hours_a = old_total_working_hours_a + new_total_working_hours_a
        base_wage_a = document.get("Base wage of assembling", 0)
        fringe_benefit_of_assembly_tot = old_fringe_benefit_of_assembly_tot + new_fringe_benefit_of_assembly_tot
        total_a_workers = old_total_a_workers + new_total_a_workers

        assembly = (total_working_hours_a * base_wage_a) * total_a_workers + fringe_benefit_of_assembly_tot
        result_label_2.config(text=f"Assembling labour cost is:{assembly}")

        # Fetching data from the document for Finishing section
        old_total_working_hours_f = document.get("Total working hours of finishing", 0)
        old_fringe_benefit_of_finishing_tot = document.get("Fringe benefit of finishing total", 0)
        old_total_finishing_workers = document.get("Total number of finishing workers", 0)

        # Getting input values from the user for Finishing section
        new_total_working_hours_f = int(entry_add_working_hours_f.get())
        new_fringe_benefit_of_finishing_tot = int(entry_add_fringe_benefit_f.get())
        new_total_finishing_workers = int(entry_add_workers_f.get())

        # Calculating new values for Finishing section
        total_working_hours_f = old_total_working_hours_f + new_total_working_hours_f
        base_wage_f = document.get("Base wage of finishing", 0)
        fringe_benefit_of_finishing_tot = old_fringe_benefit_of_finishing_tot + new_fringe_benefit_of_finishing_tot
        total_finishing_workers = old_total_finishing_workers + new_total_finishing_workers

        finishing = (total_working_hours_f * base_wage_f) * total_finishing_workers + fringe_benefit_of_finishing_tot
        result_label_3.config(text=f"Finishing labour cost is:{finishing}")

        # Calculating Direct Labour Cost
        Direct_labour_cost = production + assembly + finishing
        result_label_4.config(text=f"Direct labour cost is:{Direct_labour_cost}")

        # Updating the updates dictionary with new values
        updates = {
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

        # Update MongoDB collection
        collection.update_one({"Job ID": job_id}, {"$set": updates})
        result_label_5.config(text="Fields updated and recalculated successfully!")
    else:
        result_label_1.config(text="Document not found for the provided Job ID")

# Creating the Tkinter window
root = tk.Tk()
root.title("Direct Labour Update")

label_texts = [
    "Job number:",
    "Added total working hours production:",
    "Added fringe benefit of production:",
    "Added total workers for production:",
    "Added total working hours of assembling:",
    "Added fringe benefit of assembling:",
    "Added total workers for assembling:",
    "Added total working hours of finishing:",
    "Added fringe benefit of finishing:",
    "Added total workers for finishing:",
    
]
for i, label_text in enumerate(label_texts):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

new_entries = []
for i in range(len(label_texts)):
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    new_entries.append(entry)
    
entry_job_number = new_entries[0]
entry_add_working_hours_p= new_entries[1]
entry_add_fringe_benefit_p= new_entries[2]
entry_add_workers_p = new_entries[3]
entry_add_working_hours_a = new_entries[4]
entry_add_fringe_benefit_a = new_entries[5]
entry_add_workers_a = new_entries[6]
entry_add_working_hours_f = new_entries[7]
entry_add_fringe_benefit_f = new_entries[8]
entry_add_workers_f=new_entries[9]
    
result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(label_texts) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(label_texts) + 3, columnspan=2, padx=5, pady=5)

result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(label_texts) + 4, columnspan=2, padx=5, pady=5)  

result_label_4 = tk.Label(root, text="")
result_label_4.grid(row=len(label_texts) + 5, columnspan=2, padx=5, pady=5)    

result_label_5 = tk.Label(root, text="")
result_label_5.grid(row=len(label_texts) + 6, columnspan=2, padx=5, pady=5)          

update_button= tk.Button(root, text="Update", command=update_collection)
update_button.grid(row=len(label_texts) + 1, columnspan=2, padx=5, pady=10)


root.mainloop()
