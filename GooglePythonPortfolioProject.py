#Google Course 7 Portfolio Activity
#Maintain whitelist for confidential access


#Open the file that contains the whitelist
basedir = "C:\\BASE_DIR\\OF\\WHITELIST\\"  #!!!SPECIFY FILE LOCATION!!!
import_file = (basedir + "allow_list.txt")


#Create Remove List (Static - This should be dynamic for actual usage by retrieving the ip addresses from a file via code in the same manner as allow_list.txt)
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]


# Read import_file with the open() command and convert to a list format using the split() command stored in ip_addresses variable
with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()


#Loop through ip_addresses using a for loop that processes each ip_address as a variable named element
for element in ip_addresses:
  #Remove ip from allow list if found on remove list using the remove() command until each element (which contains a single ip address) has been removed from the allow list
    if element in remove_list:
        ip_addresses.remove(element)


# Display `ip_addresses` using the print() command
print(ip_addresses) #Debug Code / Remove before production
#Convert list back to string using the join() command with a space a the separator.  "\n" could be used in place of " " to make the .txt output file more human readable by adding line breaks if so desired.
lsString = " " . join(ip_addresses)


print(ip_addresses) #Debug Code / Remove before production


#Write the parsed string back to the whitelist using the open() command in write mode and the write() command.
with open(import_file, "w") as file:
   file.write(lsString)


"""
This script is far from useful for a complete implementation on keeping a whitelist update.
The minimal code is include as instructed by Google Cybersecurity Professional certification
  to demonstrate basic working knowledge of core Python code.


A complete implimitations would use this code to dynamically import the remove list (not just the allow list) as well as creating a self contained def that takes the whitelist and remove list in as arguments defined by two parameters.
"""


