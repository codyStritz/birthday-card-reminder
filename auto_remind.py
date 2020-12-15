"""This program is to be automatically run by windows task manager
at a minimum of every day. The program will run through all users'
profiles and check for any dates that are within 2 weeks. For any
dates within 2 weeks, the program will send a text with a reminder
to send a card to the person for the specified occasion."""


#import date in order to compare dates with current date
from datetime import date, datetime, timedelta
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# My Account SID from twilio.com/console
# account_sid = 
# My Auth Token from twilio.com/console
# auth_token  = 
client = Client(account_sid, auth_token)

#The current date for reference
today = date.today()


profile_txt = open("profiles.txt", "r")
for profile in profile_txt:
	working_profile = (profile.rstrip() + ".txt")
	open_profile = open(working_profile, "r")
	profile_dates = open_profile.readlines()
	for profile_date in profile_dates:
		if "annual" in profile_date:
			month_day = profile_date[-6:].rstrip()
			full_date = month_day + "/" + str(today.year)
			working_date = (
				datetime.strptime(full_date, '%m/%d/%Y')).date()
			if working_date <= date.today():
				#timedelta add 1 year to annual dates that have passed
				working_date = working_date + timedelta(days = 365)
				delta = working_date - date.today()
				if delta.days <= 14:
					#The sms notification message
					notification = ("Make sure to send a card to " +
					profile.rstrip().title() + " for their" +
					profile_date[6:-8] + "on " + 
					str(working_date.strftime('%m/%d/%Y')) +
					"!")
					
					#Sending the sms
					message = client.messages.create(
					# to = "", 
					# from_ = "",
					body = notification)
					
			elif working_date > date.today():
				delta = working_date - date.today()
				if delta.days <= 14:
					#The sms notification message
					notification = ("Make sure to send a card to " +
					profile.rstrip().title() + " for their" +
					profile_date[6:-8].title() + "on " + 
					str(working_date.strftime('%m/%d/%Y')) + "!")
					
					#Sending the sms
					message = client.messages.create(
					# to = "", 
					# from_ = "",
					body = notification)
				
		else:
			full_date = profile_date[-11:].rstrip()
			working_date = (
				datetime.strptime(full_date, '%m/%d/%Y').date())
			delta = working_date - date.today()
			if delta.days <= 14:
				#the sms notification message
				notification = ("Make sure to send a card to " +
				profile.rstrip().title() + " for their " +
				profile_date[:-14].title() + " on " + 
				str(working_date.strftime('%m/%d/%Y')) + "!")
				
				#sending the sms
				message = client.messages.create(
				# to = "", 
				# from_ = "",
				body = notification)
				
