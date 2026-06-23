import streamlit as st
import pandas as pd

st.set_page_config(page_title="MedDRA Auto-coding", page_icon="💊")

st.title("💊 MedDRA 智能编码助手")
st.markdown("输入不良事件的原始词，系统将自动推荐最匹配的 **Top 20** LLT。")

term = st.text_input("输入原始词 (例如: pain, rash, 骨折):")

if st.button("Go"):
    if not term.strip():
        st.warning("⚠️ 请先输入要查询的词！")
    else:
        # 显示加载动画（查询太快可能看不见，但体验很好）
        with st.spinner("正在字典中检索..."):
            # 模糊匹配
            mask = df_llt['llt_name'].str.contains(term, case=False, na=False)
            matches = df_llt[mask]
            
            data = {
                "llt_code": ["10037844", "10040911", "10046654", "10037884", "10047466"],
                "llt_name": ["Rash", "Skin rash", "Nettlerash", "Rash red", "Viral rash"],
                "pt_code": ["10037844", "10037844", "10046735", "10013442", "10047466"],
                "pt_name": ["Rash", "Rash", "Urticaria", "Erythema", "Viral rash"],
                "currency_flag": ["Y", "Y", "Y", "Y", "Y"],
                "name_length": [4, 9, 10, 8, 10] # 模拟我们之前用于排序的长度列
            }

            st.table(pd.DataFrame(data))
