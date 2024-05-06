import tkinter as tk
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Actual']



def update_document():
 job_id = int(job_id_entry.get())
 document = collection.find_one({"Job ID": job_id})

 if document:
    old_beg_inv_idm = document.get("Begining inventory IDM", 0)
    old_purchase_price_idm = document.get("Purchase price IDM", 0)
    old_end_inv_idm = document.get("Ending inventory IDM", 0)
    old_custom_duities_idm=document.get("Custom duities IDM", 0)
    old_vat_idm=document.get("VAT IDM", 0)
    old_transpartion_idm=document.get("Transpartion IDM", 0)
    old_Purchase_return_and_allowance_idm=document.get("Purchase return and allowance IDM",0)
    old_purchase_discount_idm=document.get("Purchase discount IDM",0)      
    # Ask for new values from the user
    new_beg_inv_idm = float(new_beg_inv_idm_entry.get())
    new_purchase_price_idm = float(new_purchase_price_idm_entry.get())
    new_end_inv_idm = float(new_end_inv_idm_entry.get())
    new_custom_duities_idm=float(new_custom_duities_idm_entry.get())
    new_vat_idm=float(new_vat_idm_entry.get())
    new_transpartion_idm=float(new_transpartion_idm_entry.get())
    new_Purchase_return_and_allowance_idm=float(new_Purchase_return_and_allowance_idm_entry.get())
    new_purchase_discount_idm=float(new_purchase_discount_idm_entry.get())


    # Calculate the updated values by adding the old and new values
    beg_inv_idm = old_beg_inv_idm + new_beg_inv_idm
    purchase_price_idm = old_purchase_price_idm + new_purchase_price_idm
    end_inv_idm = old_end_inv_idm + new_end_inv_idm
    custom_duities_idm=old_custom_duities_idm+new_custom_duities_idm
    vat_idm = old_vat_idm+new_vat_idm
    transpartion_idm = old_transpartion_idm+new_transpartion_idm
    Purchase_return_and_allowance_idm = old_Purchase_return_and_allowance_idm+new_Purchase_return_and_allowance_idm
    purchase_discount_idm = old_purchase_discount_idm+new_purchase_discount_idm
    


    Indirect_material_cost = beg_inv_idm + purchase_price_idm + custom_duities_idm + vat_idm + transpartion_idm -Purchase_return_and_allowance_idm - purchase_discount_idm - end_inv_idm
    idel_hours= document.get("Idel hours", 0)
    base_wage_idl=document.get("Base wage for IDL", 0)
    total_idel_workers=document.get("Number of idel workers", 0)
    idel_time=document.get("Idel time", 0)
    over_hours=document.get("Over hours", 0)
    over_time_wage=document.get("Over time wage", 0)
    tot_over_workers=document.get("Numbers of over time workers", 0)
    over_time=document.get("Over time", 0)
    other_idl=document.get("Other IDL", 0)
    idl_cost=document.get("Indirect labour cost", 0)
    print("IDL_COST:",idl_cost)



    purchase_price_dep = document.get("Purchase price equipment")
    salvage_value_dep=document.get("Salvage value", 0)
    useful_years=document.get("Useful years", 0)
    deprecition_method_stright_line=(purchase_price_dep-salvage_value_dep)/useful_years
    print("DP:",deprecition_method_stright_line)
    Insurance_factory=document.get("Insurance factory", 0)
    utility_bills=document.get("Utility bills", 0)
    lease=document.get("Lease", 0)
    other_MOH=document.get("Other MOH", 0)
    actual_manufactoring_overhead=Indirect_material_cost+idl_cost+deprecition_method_stright_line+Insurance_factory+utility_bills+lease+other_MOH

    result_label_1.config(text="Fields updated and recalculated successfully!")
    result_label_2.config(text=f"Added indirect material cost: {idl_cost}")
    result_label_3.config(text=f"Deprecition straight line method: {deprecition_method_stright_line}")
    result_label_4.config(text=f"Actual manufactoring overhead: {actual_manufactoring_overhead}")



    updates = { 
        "Begining inventory IDM": beg_inv_idm,
        "Purchase price IDM":purchase_price_idm,
        "Custom duities IDM":custom_duities_idm,
        "VAT IDM":vat_idm,
        "Transpartion IDM":transpartion_idm,
        "Purchase return and allowance IDM":Purchase_return_and_allowance_idm,
        "Purchase discount IDM":purchase_discount_idm,
        "Ending inventory IDM": end_inv_idm,
        "Indirect material cost":Indirect_material_cost,
        "Actual manufactoring overhead":actual_manufactoring_overhead
        
       
    }
    collection.update_one({"Job ID": job_id}, {"$set": updates})
    print("Fields updated and recalculated successfully!")
 else:
        print("Document not found for the provided Job ID")


root = tk.Tk()
root.title("Update Direct Material Document")
label_texts = [
    "Job number:",
    "New begining inventory of indirect material:",
    "New purchase price IDM:",
    "New ending inventory of indirect material:",
    "New custom duities IDM:",
    "New VAT IDM:",
    "New transporation IDM:",
    "New purchase return and allowance IDM:",
    "New purchase discount IDM:"
]

for i, label_text in enumerate(label_texts):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

new_entries = []
for i in range(len(label_texts)):
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    new_entries.append(entry)

job_id_entry = new_entries[0]
new_beg_inv_idm_entry = new_entries[1]
new_purchase_price_idm_entry = new_entries[2]
new_end_inv_idm_entry = new_entries[3]
new_custom_duities_idm_entry = new_entries[4]
new_vat_idm_entry = new_entries[5]
new_transpartion_idm_entry = new_entries[6]
new_Purchase_return_and_allowance_idm_entry = new_entries[7]
new_purchase_discount_idm_entry = new_entries[8]

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(label_texts) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(label_texts) + 3, columnspan=2, padx=5, pady=5)

result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(label_texts) + 4, columnspan=2, padx=5, pady=5)

result_label_4 = tk.Label(root, text="")
result_label_4.grid(row=len(label_texts) + 5, columnspan=2, padx=5, pady=5)

update_button = tk.Button(root, text="Update Document", command=update_document)
update_button.grid(row=len(label_texts) + 1, columnspan=2, padx=5, pady=10)


root.mainloop()
