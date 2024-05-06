import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Direct_material']

def calculate_direct_material_cost():
    job_id = int(job_id_entry.get())
    existing_document = collection.find_one({"Job ID": job_id})
    if existing_document:
        # Display a message if the job_id already exists
        result_label_1.config(text="Job ID already exists!")
        return
    beg_inv_dm = float(beg_inv_dm_entry.get())
    purchase_price_dm = float(purchase_price_dm_entry.get())
    custom_duities_dm = float(custom_duities_dm_entry.get())
    vat_dm = float(vat_dm_entry.get())
    transpartion_dm = float(transpartion_dm_entry.get())
    Purchase_return_and_allowance_dm = float(Purchase_return_and_allowance_dm_entry.get())
    purchase_discount_dm = float(purchase_discount_dm_entry.get())
    end_inv_dm = float(end_inv_dm_entry.get())

    Direct_material_avaliable_for_use = beg_inv_dm + purchase_price_dm + custom_duities_dm + vat_dm + transpartion_dm - Purchase_return_and_allowance_dm - purchase_discount_dm
    Direct_material_cost = Direct_material_avaliable_for_use - end_inv_dm
    
    # Reconfigure the result_label text to display the calculated values
    result_label_1.config(text=f"Direct material avaliable for use: {Direct_material_avaliable_for_use}")
    result_label_2.config(text=f"Direct material cost used for specific job: {Direct_material_cost:.2f}")

    document = {
        "Job ID": job_id,
        "Begining inventory DM": beg_inv_dm,
        "Purchase price DM": purchase_price_dm,
        "Custom duities DM": custom_duities_dm,
        "VAT DM": vat_dm,
        "Transpartion DM": transpartion_dm,
        "Purchase return and allowance DM": Purchase_return_and_allowance_dm,
        "Purchase discount DM": purchase_discount_dm,
        "Ending inventory DM": end_inv_dm,
        "Direct material avaliable for use": Direct_material_avaliable_for_use,
        "Direct material cost": Direct_material_cost
    }
    collection.insert_one(document)

root = tk.Tk()
root.title("Direct Material Cost Calculator")

# Create labels and entry fields
labels = [
    "Job number:",
    "Begining inventory of direct material:",
    "Purchase price DM:",
    "Custom duities:",
    "VAT:",
    "Transpartion:",
    "Purchase return and allowance:",
    "Purchase discount:",
    "Ending inventory of direct material:"
]

entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

job_id_entry = entries[0]
beg_inv_dm_entry = entries[1]
purchase_price_dm_entry = entries[2]
custom_duities_dm_entry = entries[3]
vat_dm_entry = entries[4]
transpartion_dm_entry = entries[5]
Purchase_return_and_allowance_dm_entry = entries[6]
purchase_discount_dm_entry = entries[7]
end_inv_dm_entry = entries[8]

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(labels) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(labels) + 3, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_direct_material_cost)
calculate_button.grid(row=len(labels) + 1, columnspan=2, padx=5, pady=10)

root.mainloop()
