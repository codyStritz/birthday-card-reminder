"""This app will let me save the dates of all of my loved-ones' big 
days and remind me when any of them are within 2 weeks away so that I can send
them a card ahead of time."""

#Importing OS for deleting files
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client 

#Adds gaps in display for cleanliness
def gap(size):
	nl = "\n" * int(size)
	print(nl)

#Creates a new .txt file profile 
def create_profile(name):
	profiles_index = open("profiles.txt", "a")
	profiles_index.write(name + "\n")
	profiles_index.close()
	
	new_file_name = (name + ".txt")
	new_file = open(new_file_name, "w")
	new_file.close()
	
#Adds a new date to an existing profile's .txt file
def add_date(profile):
	profile_name = (profile + ".txt")
	if os.path.exists(profile_name):
		working_profile = open(profile_name, "a")
		new_occasion = input("What's the occasion?: ").lower()
		recurring = input("Is this an annual occasion?(y/n): ").lower()
		if recurring == "y":
			new_date = input("What's the date?(MM/DD): ")
			working_profile.write("annual " + new_occasion + " : " +
				new_date + "\n")
		elif recurring == "n":
			new_date = input("What's the date?(MM/DD/YYYY): ")
			working_profile.write(new_occasion + " : " + new_date +
			"\n")
		else:
			print("Invalid input.")
	else:
		print("Profile does not exist.")

#Displays a list of all profiles
def display_profiles():
	if os.path.exists("profiles.txt"):
		profiles_list = open("profiles.txt", "r")
		gap(1)
		for line in profiles_list:
			print(line)
	else:
		print("\nThere Are No Profiles To Display.")

#Displays all of a profiles' dates
def view_profile(profile):
	gap(1)
	print(profile.title() + "'s Significant Dates:")
	profile_name = (profile + ".txt")
	viewing_profile = open(profile_name, "r")
	for date in viewing_profile:
		print(date)

#Deleting a profile
def delete_profile(profile):
	profile_txt = (profile + ".txt")
	if os.path.exists(profile_txt): #checking profile exists
		os.remove(profile_txt)
		profile_index = open("profiles.txt", "r") #opens profile list
		profiles = profile_index.readlines() #reads all profiles
		profile_index.close()
		profile_index = open("profiles.txt", "w")
		for name in profiles: #rewrites all profiles except deleted
			
			if name != (profile + "\n"):
				profile_index.write(name)
		profile_index.close()
		print(profile.title() + "'s profile has been deleted.")
	else:
		print("Profile does not exist.")

#Deleting a date from a profile
def delete_date(profile, del_occasion):
	profile_txt = (profile + ".txt")
	if os.path.exists(profile_txt): #Ensures the profile exists already
		working_profile = open(profile_txt, "r")
		occasions = working_profile.readlines() #reads all occasions
		working_profile.close()
		working_profile = open(profile_txt, "w")
		for occasion in occasions: #write all dates back except deletion
			if not del_occasion in occasion:
				working_profile.write(occasion)
		working_profile.close()
		print(profile.title() + "'s " + del_occasion +
			" has been deleted.")
	else:
		print("Profile does not exist.")
		
def send_sms(profile, sms_occasion):
	# My Account SID from twilio.com/console
	# account_sid = ""
	# My Auth Token from twilio.com/console
	# auth_token  = ""
	client = Client(account_sid, auth_token)
	
	profile_txt = (profile + ".txt")
	if os.path.exists(profile_txt): #Ensures the profile exists already
		working_profile = open(profile_txt, "r")
		occasions = working_profile.readlines() #reads all occasions
		working_profile.close()
		for occasion in occasions:
			if sms_occasion in occasion:
				message = client.messages.create(
				# to="", 
				# from_="",
				body=profile.title() + "\n" + occasion.title())
				print(message.sid)
	else:
		print("Profile does not exist.")
	
		

#The main menu display and user input
def main_menu():
	print("Main Menu: ")
	print("1. Display List of Profiles" +
		"\n2. View a Profile" +
		"\n3. Create a Profile" +
		"\n4. Add a Date to a Profile" +
		"\n5. Delete a Profile" +
		"\n6. Delete a Date from Profile" +
		"\n7. Send Notification for Date" +
		"\n8. Exit")
	choice = input(": ")
	while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
		print("Invalid Input.")
		choice = input(": ")
	if choice == "1":
		display_profiles()
		gap(2)
		main_menu()
	elif choice == "2":
		profile_choice = input("Who's Profile?: ").lower()
		view_profile(profile_choice)
		gap(2)
		main_menu()
	elif choice == "3":
		new_profile = input("Name for New Profile: ").lower()
		create_profile(new_profile)
		gap(2)
		main_menu()
	elif choice == "4":
		new_date_profile = input("Profile to Add Date to: ").lower()
		add_date(new_date_profile)
		gap(2)
		main_menu()
	elif choice == "5":
		profile_to_delete = input("Enter Profile to Delete: ").lower()
		delete_profile(profile_to_delete)
		gap(2)
		main_menu()
	elif choice == "6":
		date_profile = input("Enter Profile Name: ").lower()
		date_to_del = input("Enter Name of Occasion to Delete: ").lower()
		delete_date(date_profile, date_to_del)
		gap(2)
		main_menu()
	elif choice == "7":
		sms_profile = input("Enter Profile Name: ").lower()
		sms_date = input("Enter Name of Occasion to Send: ").lower()
		send_sms(sms_profile, sms_date)
		gap(2)
		main_menu()
	else:
		print("Exiting")
		
		


main_menu()
		
		

	
	
