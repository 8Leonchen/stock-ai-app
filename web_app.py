import streamlit as st
import google.generativeai as genai


st.title("📈 巴菲特毒舌股票点评器")
st.write("输入股票代码，看看股神怎么吐槽。")


if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    api_key = st.sidebar.text_input("请输入 Google API Key", type="password")



user_input = st.text_input("想查哪只股票？(例如: TSLA, 茅台)")


if st.button("开始点评"):
    if not api_key:
        st.error("大哥，先在左边填一下 API Key！")
    elif not user_input:
        st.warning("你得告诉我查啥呀！")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-3-flash-preview') 
        
        st.info("巴菲特正在看财报...")
        
        try:
            prompt = f"""
            你现在是沃伦·巴菲特，风格犀利、幽默。
            请点评：{user_input}。
            要求：100字以内，包含一个具体的比喻。
            """
            
            response = model.generate_content(prompt)
            
            st.success("点评完成：")
            st.markdown(f"### {response.text}")
            
        except Exception as e:
            st.error(f"出错了: {e}")
