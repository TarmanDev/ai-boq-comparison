import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI BOQ Comparison",
    page_icon="📊",
    layout="wide"
)

st.title("🏗️ AI BOQ Comparison Tool")
st.markdown("เปรียบเทียบ BOQ แบบอัตโนมัติด้วย AI")

# Sidebar for file upload
with st.sidebar:
    st.header("📁 อัปโหลดไฟล์ BOQ")
    
    file1 = st.file_uploader(
        "เลือกไฟล์ BOQ ที่ 1",
        type=['xlsx', 'xls', 'csv'],
        key="file1"
    )
    
    file2 = st.file_uploader(
        "เลือกไฟล์ BOQ ที่ 2", 
        type=['xlsx', 'xls', 'csv'],
        key="file2"
    )
    
    if st.button("🚀 เริ่มเปรียบเทียบ"):
        if file1 and file2:
            st.success("กำลังประมวลผล...")
            
            # อ่านไฟล์ทดสอบ
            try:
                if file1.name.endswith('.csv'):
                    df1 = pd.read_csv(file1)
                else:
                    df1 = pd.read_excel(file1)
                
                if file2.name.endswith('.csv'):
                    df2 = pd.read_csv(file2)
                else:
                    df2 = pd.read_excel(file2)
                
                st.session_state['df1'] = df1
                st.session_state['df2'] = df2
                st.session_state['file1_name'] = file1.name
                st.session_state['file2_name'] = file2.name
                
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {str(e)}")
        else:
            st.error("กรุณาเลือกไฟล์ทั้ง 2 ไฟล์")

# Main content area
if 'df1' in st.session_state and 'df2' in st.session_state:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"📋 {st.session_state['file1_name']}")
        st.dataframe(st.session_state['df1'].head())
        st.write(f"จำนวนแถว: {len(st.session_state['df1'])}")
        
    with col2:
        st.subheader(f"📋 {st.session_state['file2_name']}")
        st.dataframe(st.session_state['df2'].head())
        st.write(f"จำนวนแถว: {len(st.session_state['df2'])}")
        
    st.subheader("📊 ผลการเปรียบเทียบ")
    st.info("🚧 ฟีเจอร์การเปรียบเทียบกำลังพัฒนา...")
    
    # แสดงชื่อคอลัมน์
    col1, col2 = st.columns(2)
    with col1:
        st.write("**คอลัมน์ในไฟล์ที่ 1:**")
        st.write(list(st.session_state['df1'].columns))
    
    with col2:
        st.write("**คอลัมน์ในไฟล์ที่ 2:**")
        st.write(list(st.session_state['df2'].columns))

else:
    st.info("👆 กรุณาอัปโหลดไฟล์ BOQ 2 ไฟล์จาก Sidebar เพื่อเริ่มการเปรียบเทียบ")
    
    # แสดงตัวอย่างรูปแบบไฟล์ที่รองรับ
    st.subheader("📄 รูปแบบไฟล์ที่รองรับ")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Excel (.xlsx, .xls)**")
        st.write("- Microsoft Excel")
        st.write("- Google Sheets (Export)")
        
    with col2:
        st.write("**CSV (.csv)**")
        st.write("- Comma Separated Values")
        st.write("- Plain text format")
        
    with col3:
        st.write("**ตัวอย่างโครงสร้าง**")
        sample_data = {
            'รายการ': ['งานขุดดิน', 'งานเทคอนกรีต', 'งานก่ออิฐ'],
            'หน่วย': ['ลบ.ม.', 'ลบ.ม.', 'ตร.ม.'],
            'ปริมาณ': [100, 50, 200],
            'ราคาต่อหน่วย': [150, 3500, 500],
            'รวม': [15000, 175000, 100000]
        }
        st.dataframe(pd.DataFrame(sample_data))