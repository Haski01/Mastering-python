# boolean : True(1), False(0)

is_boiling = True

stri_count = 5
total_actions = stri_count + is_boiling # upcasting means 5 + True = 1 => 6 

print(f"Total actions: {total_actions}") # output 6

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}") # 0 = False

water_hot = True
tea_added = True
 
can_server = water_hot and tea_added # and operator (&&): both condition must be true
print(f"Can serve chai? {can_server}")

