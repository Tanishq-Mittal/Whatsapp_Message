from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = '................................'
auth_token = '................................'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:.............',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

name = input('Enter the recipient name : ')
recipient_number = input('Enter the recipient whatsapp number with country code (e.g. +12345): ')
message_body = input(f'Enter the message you want to send to {name} : ')

date_str = input('Enter the date to send the message (YYYY-MM-DD) : ')
time_str = input('Enter the time to send the message (HH:MM in 24 hour format) : ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M") #strptime is string pass time
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
   print('The specified time is in the past. Please enter a future date and time : ')
else:
   print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

   time.sleep(delay_seconds) #1000
   send_whatsapp_message(recipient_number, message_body)