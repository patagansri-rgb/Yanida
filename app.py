import streamlit as st
from logic import validate_and_classify
from data_store import save_record, load_records

st.title("📚 Study Time Tracker")
st.write("ระบบบันทึกเวลาเรียนรู้")

# ฟอร์มรับข้อมูล
with st.form("study_form"):
    subject = st.text_input("ชื่อวิชา (Subject)")
    duration = st.text_input("เวลาเรียนเป็นนาที (Duration)")
    submit_button = st.form_submit_button("บันทึกข้อมูล")

    if submit_button:
        is_valid, message, category = validate_and_classify(subject, duration)
        if is_valid:
            save_record(subject.strip(), int(duration), category)
            st.success(f"{message} (ประเภท: {category})")
        else:
            st.error(message)

# แสดงประวัติการเรียน
st.subheader("📋 ประวัติการเรียนทั้งหมด")
records = load_records()

if records:
    st.info(f"จำนวนรายการที่บันทึกทั้งหมด: {len(records)} รายการ")
    for idx, rec in enumerate(records, 1):
        st.write(f"{idx}. วิชา: **{rec['subject']}** | เวลา: {rec['duration']} นาที | หมวดหมู่: {rec['category']}")
else:
    st.write("ยังไม่มีประวัติการบันทึก")