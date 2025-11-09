import asyncio
from collections import defaultdict
import redis.asyncio as redis

from tools.config import BUFFER_KEY_SUFFIX, REDIS_URL, BUFFER_TTL
from tools.ai_tools import format_prompt, translate_with_ai
from tools.evolution_api import send_whatsapp_message


redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
debounce_tasks = defaultdict(asyncio.Task)


def log(*args):
    print('[BUFFER]', *args)


async def buffer_message(chat_id: str, message: str):
    buffer_key = f'{chat_id}{BUFFER_KEY_SUFFIX}'
    await redis_client.rpush(buffer_key, f'user_role_{message}')
    await redis_client.expire(buffer_key, BUFFER_TTL)
    messages = await redis_client.lrange(buffer_key, 0, -1)
    prompt = format_prompt(messages)
    if prompt:
        ai_response = await translate_with_ai(prompt)
        await redis_client.rpush(buffer_key, f'ai_role_{ai_response}')
        send_whatsapp_message(chat_id, ai_response)
    log(f' Mensagens de {chat_id}: {prompt}')
