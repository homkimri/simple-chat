from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key, model):
    # 如果使用的不是 openai 的api，需要添加openai_api_base="你的 api 地址"
    model = ChatOpenAI(model=model, openai_api_key=openai_api_key,
                       openai_api_base="https://api.deepseek.com/v1")
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]
