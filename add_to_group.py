import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
import time

# Telegram API credentials
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE'  # Your Telegram account's phone number

# Group ID (find it programmatically or via Telegram clients)
group_entity = 'GROUP_ID_OR_USERNAME'

# Load phone numbers from CSV
df = pd.read_csv('numbers.csv')
phone_numbers = df['Phone Number Column Name'].tolist()

# Initialize Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    client.start(phone)

    # Fetch the target group
    group = client.get_entity(group_entity)

    for number in phone_numbers:
        try:
            # Create a contact and add to group
            contact = InputPhoneContact(client_id=0, phone=number, first_name="", last_name="")
            client(AddChatUserRequest(group.id, contact, fwd_limit=0))
            print(f"Added {number}")
            time.sleep(5)  # Avoid rate limits (5-10 seconds between adds)
        except Exception as e:
            print(f"Failed to add {number}: {str(e)}")
