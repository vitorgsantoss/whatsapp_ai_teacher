from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from tools.config import SYSTEM_PROMPT, OPENAI_API_KEY, OPENAI_MODEL_NAME


def format_prompt(messages: list) -> list:
    msgs = [SystemMessage(content=SYSTEM_PROMPT)]
    for item in messages:
        role, text = item.split('_role_', 1)
        if role == 'user':
            msgs.append(HumanMessage(content=text.strip()))
        else:
            msgs.append(AIMessage(content=text.strip()))
    return msgs


async def translate_with_ai(messages_list: list) -> str:
    model = ChatOpenAI(
        model=OPENAI_MODEL_NAME,
        api_key=OPENAI_API_KEY
    )
    response = await model.ainvoke(messages_list)
    return response.content
