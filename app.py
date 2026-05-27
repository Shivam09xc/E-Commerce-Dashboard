import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="E-Commerce Sales Analytics Portal",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to style the Streamlit interface premium dark mode
st.markdown("""
    <style>
        .reportview-container {
            background: #090d16;
        }
        .main h3 {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🛒 Analytics Hub")
st.sidebar.markdown("Welcome to the central E-Commerce analytics portal. Choose a view below to explore transaction trends and KPIs.")

dashboard_choice = st.sidebar.radio(
    "Select Portal View:",
    ["Interactive Chart.js Dashboard", "Power BI Styled Report", "Raw Data Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 🛠️ Portal Specifications
* **Frontend:** Streamlit Components
* **Visuals:** Chart.js & CSS Grid
* **Analytics Engine:** Python Pandas
* **Data Sources:** Superstore Excel (3.5K Orders)
""")

# Option 1: Chart.js Dashboard
if dashboard_choice == "Interactive Chart.js Dashboard":
    st.markdown("### 📊 Interactive Sales & Revenue Dashboard (Chart.js Model)")
    html_path = "ecommerce_dashboard.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1050, scrolling=True)
    else:
        st.error("Dashboard file not found! Please make sure 'ecommerce_dashboard.html' exists in the workspace.")

# Option 2: Power BI Styled Dashboard
elif dashboard_choice == "Power BI Styled Report":
    st.markdown("### 🎨 Corporate Sales Analytics (Power BI Model)")
    html_path = "ecommerce_powerbi_dashboard.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=950, scrolling=True)
    else:
        st.error("Power BI Dashboard file not found! Please make sure 'ecommerce_powerbi_dashboard.html' exists in the workspace.")

# Option 3: Raw Data Explorer
elif dashboard_choice == "Raw Data Explorer":
    st.markdown("### 🔍 Raw Transactions Explorer")
    st.markdown("Search, filter, and export the active E-Commerce transaction dataset.")
    
    excel_path = "ecommerce_analytics (1).xlsx"
    if os.path.exists(excel_path):
        try:
            # Load and display statistics
            df = pd.read_excel(excel_path)
            
            # KPI Cards
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric("Total Transactions", f"{len(df):,}")
            kpi2.metric("Accumulated Sales", f"₹{df['Sales'].sum()/100000:.1f} Lakh")
            kpi3.metric("Net Profit", f"₹{df['Profit'].sum()/100000:.1f} Lakh")
            kpi4.metric("Avg Profit Margin", f"{(df['Profit'].sum()/df['Sales'].sum()*100):.1f}%")
            
            st.markdown("---")
            
            # Interactive Search
            search_query = st.text_input("🔍 Search Products, Customers, or Regions:")
            
            filtered_df = df
            if search_query:
                filtered_df = df[
                    df['Product Name'].astype(str).str.contains(search_query, case=False) |
                    df['Region'].astype(str).str.contains(search_query, case=False) |
                    df['Customer ID'].astype(str).str.contains(search_query, case=False) |
                    df['Category'].astype(str).str.contains(search_query, case=False)
                ]
                
            st.dataframe(filtered_df, use_container_width=True)
            
            # Export Option
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Filtered Data as CSV",
                data=csv,
                file_name="filtered_ecommerce_data.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Error loading Excel data: {e}")
    else:
        st.error("Excel data source 'ecommerce_analytics (1).xlsx' not found!")
