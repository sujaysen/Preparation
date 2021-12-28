# convert the format of a date
def convert_date(date):
  # Replace / by . 
  date = date.replace("/",".")
  # Return  
  return date

# Take date from user
date = input("Enter the date in format dd/mm/yyyy : ")
# Call the function to convert
res = convert_date(date)
# Display the converted date
print("Date with format dd.mm.yyyy : ",res)
