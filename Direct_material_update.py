import tkinter as tk
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['Direct_material']

def update_document():
    job_id = int(job_id_entry.get())

    document = collection.find_one({"Job ID": job_id})

    if document:
        old_beg_inv_dm = document.get("Begining inventory DM", 0)
        old_purchase_price_dm = document.get("Purchase price DM", 0)
        old_end_inv_dm = document.get("Ending inventory DM", 0)
        old_custom_duities_dm = document.get("Custom duities DM", 0)
        old_vat_dm = document.get("VAT DM", 0)
        old_transpartion_dm = document.get("Transpartion DM", 0)
        old_Purchase_return_and_allowance_dm = document.get("Purchase return and allowance DM", 0)
        old_purchase_discount_dm = document.get("Purchase discount DM", 0)

        new_beg_inv_dm = float(new_beg_inv_dm_entry.get())
        new_purchase_price_dm = float(new_purchase_price_dm_entry.get())
        new_end_inv_dm = float(new_end_inv_dm_entry.get())
        new_custom_duities_dm = float(new_custom_duities_dm_entry.get())
        new_vat_dm = float(new_vat_dm_entry.get())
        new_transpartion_dm = float(new_transpartion_dm_entry.get())
        new_Purchase_return_and_allowance_dm = float(new_Purchase_return_and_allowance_dm_entry.get())
        new_purchase_discount_dm = float(new_purchase_discount_dm_entry.get())

        beg_inv_dm = old_beg_inv_dm + new_beg_inv_dm
        purchase_price_dm = old_purchase_price_dm + new_purchase_price_dm
        end_inv_dm = old_end_inv_dm + new_end_inv_dm
        custom_duities_dm = old_custom_duities_dm + new_custom_duities_dm
        vat_dm = old_vat_dm + new_vat_dm
        transpartion_dm = old_transpartion_dm + new_transpartion_dm
        Purchase_return_and_allowance_dm = old_Purchase_return_and_allowance_dm + new_Purchase_return_and_allowance_dm
        purchase_discount_dm = old_purchase_discount_dm + new_purchase_discount_dm
        Direct_material_avaliable_for_use = (
            beg_inv_dm + purchase_price_dm + custom_duities_dm + vat_dm + transpartion_dm -
            Purchase_return_and_allowance_dm - purchase_discount_dm
        )

        Direct_material_cost = Direct_material_avaliable_for_use - end_inv_dm
        
        # Update the result labels to display the calculated values and success message
        result_label_1.config(text="Fields updated and recalculated successfully!")
        result_label_2.config(text=f"New direct material available for use: {Direct_material_avaliable_for_use}")
        result_label_3.config(text=f"New direct material cost used for specific job: {Direct_material_cost:.2f}")

        updates = {
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

        collection.update_one({"Job ID": job_id}, {"$set": updates})
    else:
        result_label_3.config(text="Document not found for the provided Job ID")

root = tk.Tk()
root.title("Update Direct Material Document")

# Create labels and entry fields
label_texts = [
    "Job number:",
    "New begining inventory of direct material:",
    "New purchase price DM:",
    "New ending inventory of direct material:",
    "New custom duities DM:",
    "New VAT:",
    "New transpartion:",
    "New purchase return and allowance:",
    "New purchase discount:"
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
new_beg_inv_dm_entry = new_entries[1]
new_purchase_price_dm_entry = new_entries[2]
new_end_inv_dm_entry = new_entries[3]
new_custom_duities_dm_entry = new_entries[4]
new_vat_dm_entry = new_entries[5]
new_transpartion_dm_entry = new_entries[6]
new_Purchase_return_and_allowance_dm_entry = new_entries[7]
new_purchase_discount_dm_entry = new_entries[8]

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(label_texts) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(label_texts) + 3, columnspan=2, padx=5, pady=5)

result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(label_texts) + 4, columnspan=2, padx=5, pady=5)

update_button = tk.Button(root, text="Update Document", command=update_document)
update_button.grid(row=len(label_texts) + 1, columnspan=2, padx=5, pady=10)


root.mainloop()
