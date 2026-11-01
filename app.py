import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(page_title="موقعي مع Gemini", page_icon="🤖")
st.title("🤖 تطبيق الذكاء الاصطناعي الخاص بي")
st.write("موقع بسيط، مجاني، ويعمل مباشرة بدون تعقيد!")

# إدخال مفتاح الـ API بأمان
api_key = st.text_input("أدخل مفتاح Google Gemini API الخاص بك:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # استخدام نموذج جيميناي
    model = genai.GenerativeModel("gemini-1.5-flash")

    # خانة إدخال الرسالة للمستخدم
    user_prompt = st.text_area("اكتب سؤالك أو طلبك هنا:")
    
    if st.button("إرسال"):
        if user_prompt:
            with st.spinner("جاري التفكير..."):
                try:
                    response = model.generate_content(user_prompt)
                    st.subheader("النتيجة:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
        else:
            st.warning("الرجاء كتابة نص أولاً.")
else:
    st.info("الرجاء إدخال مفتاح الـ API للبدء (يمكنك الحصول عليه مجاناً من Google AI Studio).")
