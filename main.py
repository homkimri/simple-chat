import streamlit as st
from langchain.memory import ConversationBufferMemory
from untils import get_chat_response

st.title("💬简易聊天助手")
options = ['deepseek-chat', 'deepseek-reasoner']
# 初始化会话状态
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是一个聊天助手，有什么可以帮你的吗？"}]
# 侧边栏设置
with st.sidebar:
    model = st.selectbox("选择使用的模型", options)
    openai_api_key = st.text_input("deepseek API密钥", type="password")
    st.markdown("[获取deepseek API密钥](https://platform.deepseek.com/)")
    if st.button("创建新对话"):
        st.session_state["memory"] = ConversationBufferMemory(return_messages=True)  # 重置记忆
        st.session_state["messages"] = [
            {"role": "ai", "content": "你好，我是一个聊天助手，有什么可以帮你的吗？"}]  # 重置聊天记录
        st.rerun()  # 重新运行应用以更新界面

# 显示聊天记录
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入处理
prompt = st.chat_input("请输入问题")
if prompt:
    if not openai_api_key:
        st.info("请输入您的通义千问API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key, model)
        msg = {"role": "ai","content": response}
        st.session_state["messages"].append(msg)
        st.chat_message("ai").write(response)