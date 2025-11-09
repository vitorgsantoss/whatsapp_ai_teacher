from fastapi import Request, FastAPI
from tools.message_buffer import buffer_message
from tools.config import PHONE_NUMBER


app = FastAPI()


@app.post('/webhook')
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get('sender')
    message = data.get('data').get('message').get('conversation')
    if message and PHONE_NUMBER in chat_id:
        await buffer_message(chat_id, message)
    return {'status': 'ok'}
