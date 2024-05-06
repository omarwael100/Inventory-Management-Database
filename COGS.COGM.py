import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Inventory']
collection = db['COGS']
collection1 = db['Direct_material']
collection2 = db['Direct_labour']
collection3 = db['Allocated']


def calculate_cogs():

 job_id = int(job_id_entry.get())

# Find the document with the actual manufacturing overhead for the specific job
 dm_document1 = collection1.find_one({"Job ID": job_id})
 dl_document2 = collection2.find_one({"Job ID": job_id})
 allo_document3 = collection3.find_one({"Job ID": job_id})

  


# Check if the document is found
 if dm_document1 is not None:
    # Access the actual manufacturing overhead value
     Direct_material_cost= dm_document1["Direct material cost"]
     
     
     
 else:
    # Handle the case where the document is not found
    result_label_1.config(text="No actual data for this job")
    Direct_material_cost = 0


 if dl_document2 is not None:
        Direct_labour_cost=dl_document2["Direct labour cost"]
 else:
    # Handle the case where the document is not found
    print("No actual data found for job ID", job_id)
    Direct_labour_cost= 0
 if allo_document3 is not None:
         allocated_moh_for_job=allo_document3["Allocated MOH for the job"]
         total_over_under_allocated_MOH=allo_document3["Total of over or under allocated MOH"]
         
 else:
   
    print("No actual data found for job ID", job_id)
    allocated_moh_for_job= 0
    total_over_under_allocated_MOH=0
    
                

 total_man_cost_for_specific_job=Direct_material_cost+Direct_labour_cost+allocated_moh_for_job
 result_label_1.config(text=f"Total manfucatred cost for a specific job:{total_man_cost_for_specific_job}")
 beg_WIP=float(beg_WIP_entry.get())
 end_WIP=float(end_WIP_entry.get())
 cost_of_good_manfucatred_for_specific_job=(total_man_cost_for_specific_job+beg_WIP)-end_WIP
 result_label_2.config(text=f"Cost of good manfucatred for a specific job: {cost_of_good_manfucatred_for_specific_job}")


 beg_inv_of_finished_good_used_for_specific_job=float(beg_inv_of_finished_good_used_for_specific_job_entry.get())
 end_inv_of_finished_good_used_for_specific_job=float(end_inv_of_finished_good_used_for_specific_job_entry.get())

 cost_of_good_sold=(beg_inv_of_finished_good_used_for_specific_job+cost_of_good_manfucatred_for_specific_job)-end_inv_of_finished_good_used_for_specific_job
 prorated_cogs=cost_of_good_sold+total_over_under_allocated_MOH
 result_label_3.config(text=f"Cost of goods sold: {cost_of_good_sold}")
 result_label_4.config(text=f"Prorated cost of goods sold:{prorated_cogs}")



 document = {
    "Job ID":job_id,    
    "Total manfucatred cost for a specific job":total_man_cost_for_specific_job,
    "Begining work in process used for a specific job":beg_WIP,
    "Ending work in process used for a specific job":end_WIP,
    "Cost of good manfucatred for specific job":cost_of_good_manfucatred_for_specific_job,
    "Beginig inventory of finished good used for a specific job":beg_inv_of_finished_good_used_for_specific_job,
    "Ending inventory of finished good used for a specific job":end_inv_of_finished_good_used_for_specific_job,
    "Cost of good sold for a specific job":cost_of_good_sold,
    "Prorated cost of good sold for a specific job":prorated_cogs  
}
 collection.insert_one(document)
 

root = tk.Tk()
root.title("Direct Material Cost Calculator")

labels = [
    "Job number:",
    "Begining work in process used for a specific job:",
    "Ending work in process used for a specific job:",
    "Beginig inventory of finished good used for a specific job:",
    "Ending inventory of finished good used for a specific job:",

]

entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

job_id_entry = entries[0]
beg_WIP_entry = entries[1]
end_WIP_entry = entries[2]
beg_inv_of_finished_good_used_for_specific_job_entry = entries[3]
end_inv_of_finished_good_used_for_specific_job_entry = entries[4]

result_label_1 = tk.Label(root, text="")
result_label_1.grid(row=len(labels) + 2, columnspan=2, padx=5, pady=5)

result_label_2 = tk.Label(root, text="")
result_label_2.grid(row=len(labels) + 3, columnspan=2, padx=5, pady=5)


result_label_3 = tk.Label(root, text="")
result_label_3.grid(row=len(labels) + 4, columnspan=2, padx=5, pady=5)

result_label_4 = tk.Label(root, text="")
result_label_4.grid(row=len(labels) + 5, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_cogs)
calculate_button.grid(row=len(labels) + 1, columnspan=2, padx=5, pady=10)

root.mainloop()
