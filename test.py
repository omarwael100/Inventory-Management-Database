'''
DM_cost=float(purchase_price + custom_duities+vat+transpartion-Purchase_returen_and_allowance-purchase_discount)
DL_cost=int(production+assembly+finishing)

production=total_hours*base_wadge+fringe_benefit_of_production
assembly=total_hours*base_wadge+fringe_benefit_of_assembly
finishing=total_hours*base_wadge+fringe_benefit_of_finishing

'''




beg_inv_dm=float(input("Begining inventory of direct material:"))

purchase_price_dm=float(input("Purchase price DM:"))
custom_duities_dm=float(input("Custom duities:"))
vat_dm=float(input("VAT:"))
transpartion_dm=float(input("Transpartion:"))
Purchase_return_and_allowance_dm=float(input("Purchase return and allowance:"))
purchase_discount_dm=float(input("Purchase discount:"))
end_inv_dm=float(input("Ending inventory of direct material:"))

Direct_material_avaliable_for_use=purchase_price_dm+custom_duities_dm+vat_dm+transpartion_dm-Purchase_return_and_allowance_dm-purchase_discount_dm
Direct_material_cost=(beg_inv_dm+Direct_material_avaliable_for_use)-end_inv_dm
print("Direct material cost used for specific job:",f"{Direct_material_cost:.2f}")




print("*********************************************************************")
#fringe benefits (production,assembly,finished) is the sum total for all workers in their respected line of work
total_working_hours_p=int(input("Total working hours production:"))
base_wage_p=int(input("Base wage for production:"))
fringe_benefit_of_production_tot=int(input("Fringe benefit of production :"))
total_p_workers=int(input("Total workers for production:"))

production=(total_working_hours_p*base_wage_p)*total_p_workers+fringe_benefit_of_production_tot

total_working_hours_a=int(input("Total working hours of assembling:"))
base_wage_a=int(input("Base wage for assembling:"))
fringe_benefit_of_assembly_tot=int(input("Fringe benefit of assembling:"))
total_a_workers=int(input("Total workers for assembling:"))


assembly=(total_working_hours_a*base_wage_a)*total_a_workers+fringe_benefit_of_assembly_tot

total_working_hours_f=int(input("Total working hours of finishing:"))
base_wage_f=int(input("Base wage for finishing:"))
fringe_benefit_of_finishing_tot=int(input("Fringe benefit of finishing:"))
total_finishing_workers=int(input("Total workers for finishing:"))


finishing=(total_working_hours_f*base_wage_f)*total_finishing_workers+fringe_benefit_of_finishing_tot

Direct_labour_cost=production+assembly+finishing

print(Direct_labour_cost)
print("*********************************************************************")


'''
IDM_cost=float(purchase_price_I + custom_duities_I+vat_I+transpartion_I-Purchase_returen_and_allowance_I-purchase_discount_I)
IDL_cost=int(ideal_time+over_time+other_IDL)
ideal_time=ideal_hours*base_rate
over_time=over_hours*over_time_wage
deprecition_method_stright_line=(purchase_price-salvage_value)/useful_life
Insurance_factory=int()
utility_bills=int()
lease=int()
other_MOH=int()
actual_manufactoring_overhead=IDM_cost+IDL_cost+ideal_time+over_time+deprecition_method_stright_line+Insurance_factory+lease+other_MOH
'''
print("******************************************************************")
beg_inv_idm=float(input("Begining inventory for IDM:"))
purchase_price_idm=float(input("Purchase price for IDM:"))
custom_duities_idm=float(input("Custom duities for IDM:"))
vat_idm=float(input("VAT for IDM:"))
transpartion_idm=float(input("Transpartion for IDM:"))
Purchase_return_and_allowance_idm=float(input("Purchase return and allowance for IDM:"))
purchase_discount_idm=float(input("Purchase discount for IDM:"))
end_inv_idm=float(input("Ending inventory for IDM:"))

idm_cost=beg_inv_idm+purchase_price_idm+custom_duities_idm+vat_idm+transpartion_idm-Purchase_return_and_allowance_idm-purchase_discount_idm-end_inv_idm
print("IDM_COST:",idm_cost)
idel_hours=int(input("Idel hours:"))
base_wage_idl=int(input("Base wage for IDL:"))
total_idel_workers=int(input("Number of idel workers:"))
idel_time=(idel_hours*base_wage_idl)*total_idel_workers
over_hours=int(input("Over hours:"))
over_time_wage=int(input("Over time wage:"))
tot_over_workers=int(input("Numbers of over time workers:"))
over_time=(over_hours*over_time_wage)*tot_over_workers
other_idl=int(input("Other IDL:"))
idl_cost=int(idel_time+over_time+other_idl)
print("IDL_COST:",idl_cost)



purchase_price_dep=float(input("Purchase price EQ :"))
salvage_value_dep=float(input("salvage value:"))
useful_life=float(input("useful life years:"))
deprecition_method_stright_line=(purchase_price_dep-salvage_value_dep)/useful_life
print("DP:",deprecition_method_stright_line)
Insurance_factory=int(input("Insurance factory:"))
utility_bills=int(input("utility bills:"))
lease=int(input("lease:"))
other_MOH=int(input("Other MOH:"))
total_IULO=Insurance_factory+utility_bills+lease+other_MOH
print("TOTAL IULO:",total_IULO)
actual_manufactoring_overhead=idm_cost+idl_cost+deprecition_method_stright_line+total_IULO

print(actual_manufactoring_overhead)

print("***********************************************************************")

total_budget_moh_year=int(input("Enter estimated MOH for the year:"))
total_budgeted_moh_hour_year=int(input("Enter estimated MOH hours for the year:"))
actual_base=int(input("Enter estimated hours for the job:"))
allocated_moh_for_job=(total_budget_moh_year/total_budgeted_moh_hour_year)*actual_base

print("Allocated MOH for specific job:",allocated_moh_for_job)


total_over_under_allocated_MOH=allocated_moh_for_job-actual_manufactoring_overhead

if total_over_under_allocated_MOH<0:
    print("Under allocated:",total_over_under_allocated_MOH)
elif total_over_under_allocated_MOH>0:
    print("Over allocated:",total_over_under_allocated_MOH) 
else:
    print("Correct estamtion:",total_over_under_allocated_MOH)  

total_man_cost_for_specific_job=Direct_material_cost+Direct_labour_cost+allocated_moh_for_job
print("Total manfucatred cost for specific job:",total_man_cost_for_specific_job)
beg_WIP=float(input("Begining work in process used for job:"))
end_WIP=float(input("Ending work in process used for job:"))
cost_of_good_manfucatred_for_specific_job=(total_man_cost_for_specific_job+beg_WIP)-end_WIP

print("Cost of good manfucatred:",cost_of_good_manfucatred_for_specific_job)

beg_inv_of_finished_good_used_for_specific_job=float(input("Begining inventory of finished goods for specific job:"))
end_inv_of_finished_good_used_for_specific_job=float(input("Ending inventory of finished goods for specific job:"))

cost_of_good_sold=(beg_inv_of_finished_good_used_for_specific_job+cost_of_good_manfucatred_for_specific_job)-end_inv_of_finished_good_used_for_specific_job



print("Cost of good sold:",cost_of_good_sold)