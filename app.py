from fastapi import Request, FastAPI
from tools.message_buffer import buffer_message
from tools.config import PHONE_NUMBER, REMOTE_JID


app = FastAPI()


@app.post('/webhook')
async def webhook(request: Request):
    data = await request.json()
    remote_jid = data.get('data').get('key').get('remoteJid')
    message = data.get('data').get('message').get('conversation')

    if message and remote_jid == REMOTE_JID or PHONE_NUMBER in remote_jid:
        await buffer_message(PHONE_NUMBER, message)
    return {'status': 'ok'}
