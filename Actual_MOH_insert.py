import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Actual']

def calculate_and_insert():
    job_id = int(job_number_entry.get())
    existing_document = collection.find_one({"Job ID": job_id})
    if existing_document:
        # Display a message if the job_id already exists
        result_label_1.config(text="Job ID already exists!")
        return
    beg_inv_idm = float(beg_inv_idm_entry.get())
    purchase_price_idm = float(purchase_price_idm_entry.get())
    custom_duties_idm = float(custom_duities_idm_entry.get())
    vat_idm = float(vat_idm_entry.get())
    transportation_idm = float(transpartion_idm_entry.get())
    purchase_return_allowance_idm = float(purchase_return_and_allowance_idm_entry.get())
    purchase_discount_idm = float(purchase_discount_idm_entry.get())
    end_inv_idm = float(end_inv_idm_entry.get())

    idm_cost = beg_inv_idm + purchase_price_idm + custom_duties_idm + vat_idm + transportation_idm - purchase_return_allowance_idm - purchase_discount_idm - end_inv_idm
    result_label_1.config(text=f"Indirect material avaliable for use: {idm_cost}")

    idle_hours = int(idel_hours_entry.get())
    base_wage_idl = int(base_wage_idl_entry.get())
    total_idle_workers = int(total_idel_workers_entry.get())
    idel_time = (idle_hours * base_wage_idl) * total_idle_workers
    result_label_2.config(text=f"Direct material avaliable for use: {idel_time}")

    over_hours = int(over_hours_entry.get())
    over_time_wage = int(over_time_wage_entry.get())
    total_over_workers = int(tot_over_workers_entry.get())
    
    over_time = (over_hours * over_time_wage) * total_over_workers
    result_label_3.config(text=f"Over time: {over_time}")

    other_idl = int(other_idl_entry.get())
    idl_cost = idel_time + over_time + other_idl
    result_label_4.config(text=f"Indirect labour cost: {idl_cost}")

    purchase_price_dep = int(purchase_price_dep_entry.get())
    salvage_value_dep = float(salvage_value_dep_entry.get())
    useful_years = float(useful_years_entry.get())
    depreciation_method_straight_line = (purchase_price_dep - salvage_value_dep) / useful_years
    result_label_5.config(text=f"Depreciation straight line method: {depreciation_method_straight_line}")

    insurance_factory = int(insurance_factory_entry.get())
    utility_bills = int(utility_bills_entry.get())
    lease = int(lease_entry.get())
    other_moh = int(other_MOH_entry.get())
    
    actual_manufacturing_overhead = idm_cost + idl_cost + depreciation_method_straight_line + insurance_factory + utility_bills + lease + other_moh
    result_label_6.config(text=f"Actual manufactoring overhead: {actual_manufacturing_overhead}")

    
    
    # Create the document
    document = {
        "Job ID": job_id,
        "Begining inventory IDM": beg_inv_idm,
        "Purchase price IDM": purchase_price_idm,
        "Custom duties IDM": custom_duties_idm,
        "VAT IDM": vat_idm,
        "Transpartion IDM": transportation_idm,
        "Purchase return and allowance IDM": purchase_return_allowance_idm,
        "Purchase discount IDM": purchase_discount_idm,
        "Ending inventory IDM": end_inv_idm,
        "Indirect material cost": idm_cost,
        
        "Idel hours": idle_hours,
        "Base wage for IDL": base_wage_idl,
        "Number of idel workers": total_idle_workers,
        "Idel time": idel_time,
        "Over hours": over_hours,
        "Over time wage": over_time_wage,
        
        "Numbers of over time workers": total_over_workers,
        "Over time": over_time,
        "Other IDL": other_idl,
        "Indirect labour cost": idl_cost,
        "Purchase price equipment": purchase_price_dep,
        "Salvage value": salvage_value_dep,
        "Useful years": useful_years,
        
        "Deprecition  stright line method": depreciation_method_straight_line,
        "Insurance factory": insurance_factory,
        "Utility bills": utility_bills,
        "Lease": lease,
        "Other MOH": other_moh,
        
        "Actual manufactoring overhead": actual_manufacturing_overhead 
    }
    
    # Insert document into MongoDB collection
    collection.insert_one(document)

def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Manufacturing Overhead Calculator")
root.geometry("800x600")

labels_left = [
    "Job ID",
    "Begining inventory IDM",
    "Purchase price IDM",
    "Custom duties IDM",
     "VAT IDM",
        "Transpartion IDM",
        "Purchase return and allowance IDM",
        "Purchase discount IDM",
        "Ending inventory IDM",
        "Idel hours",
        "Base wage for IDL",
        "Number of idel workers",
        "Over hours:" ,
]

labels_right = [
    "Over time wage:",
    "Numbers of over time workers:",
    "Other IDL:",
    "Purchase price equipment:",
        "Salvage value:",
        "Useful years:",
        
        "Insurance factory:",
        "Utility bills:",
        "Lease:",
        "Other MOH:",
]

entries = []
for i, label_text in enumerate(labels_left):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

for i, label_text in enumerate(labels_right):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=5, pady=5)
    entries.append(entry)

job_number_entry = entries[0]
beg_inv_idm_entry = entries[1]
purchase_price_idm_entry = entries[2]
custom_duities_idm_entry = entries[3]
vat_idm_entry = entries[4]
transpartion_idm_entry = entries[5]
purchase_return_and_allowance_idm_entry = entries[6]
purchase_discount_idm_entry = entries[7]
end_inv_idm_entry = entries[8]
idel_hours_entry = entries[9]
base_wage_idl_entry = entries[10]
total_idel_workers_entry = entries[11]
over_hours_entry = entries[12]
over_time_wage_entry = entries[13]
tot_over_workers_entry = entries[14]
other_idl_entry = entries[15]
purchase_price_dep_entry = entries[16]
salvage_value_dep_entry = entries[17]
useful_years_entry = entries[18]  
insurance_factory_entry = entries[19]
utility_bills_entry = entries[20]
lease_entry = entries[21]
other_MOH_entry = entries[22]
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_insert)
calculate_button.grid(row=len(labels_left), column=0, columnspan=2, padx=5, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=len(labels_left), column=2, columnspan=2, padx=5, pady=10)

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(labels_left) + 1, column=0, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(labels_left) + 2, column=0, columnspan=2, padx=5, pady=5)

result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(labels_left) + 3, column=0, columnspan=2, padx=5, pady=5)

result_label_4 = tk.Label(root, text="")
result_label_4.grid(row=len(labels_left) + 4, column=0, columnspan=2, padx=5, pady=5)

result_label_5 = tk.Label(root, text="")
result_label_5.grid(row=len(labels_left) + 5, column=0, columnspan=2, padx=5, pady=5)

result_label_6 = tk.Label(root, text="")
result_label_6.grid(row=len(labels_left) + 6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
