from config import api_id, api_hash, number
from telegram.client import Telegram


class Check:

    def __init__(self):
        
        self.tg = Telegram(
            api_id=api_id,
            api_hash=api_hash,
            phone=number,
            database_encryption_key='changeme1234',
        )
        self.tg.login()

    def pick(self, num):
        
        r = self.tg.call_method('importContacts', {'contacts':[{'phone_number': num}]})
        r.wait()
        user_id = r.update['user_ids']

        if user_id[0] == 0:
            print('This contact is NOT using Telegram.')
        else:
            print(f'¡This contact({user_id[0]}) uses Telegram!')

s = Check()
s.pick('+380632245000')