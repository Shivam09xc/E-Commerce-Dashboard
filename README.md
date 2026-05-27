# 🛒 E-Commerce Sales Analytics Portal

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=30&pause=1000&color=00F7FF&center=true&vCenter=true&width=900&lines=Modern+E-Commerce+Analytics+Dashboard;Interactive+Business+Intelligence+Portal;Streamlit+%2B+Chart.js+%2B+PowerBI+Inspired+UI;Built+By+Shivam+Soni+🚀" />
</p>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDl2dTQ4dDFlN2k0OWE1cXZsOWF4OHM2bG55ZnM5N3N5eWVzN2s4aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3vRfNA1p0rvhMSvS/giphy.gif" width="100%" />
</p>

<div align="center">

[![Streamlit App](https://img.shields.io/badge/Streamlit_Cloud-Live_App-FF4B4B?style=for-the-badge\&logo=Streamlit\&logoColor=white)](https://e-commerce-dashboardgit-qd3gjlse3fsulugafbvx5c.streamlit.app/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Static_Portal-121013?style=for-the-badge\&logo=GitHub\&logoColor=white)](https://shivam09xc.github.io/E-Commerce-Dashboard/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=Python\&logoColor=white)](https://www.python.org/)

<img src="https://komarev.com/ghpvc/?username=Shivam09xc&label=Repository+Views&color=00fff7&style=for-the-badge" />

📊 **Superstore Dataset · 3,500 Transactions · Interactive Analytics & Corporate Visualizations** 📈

[🌐 Live Streamlit App](https://e-commerce-dashboardgit-qd3gjlse3fsulugafbvx5c.streamlit.app/) | [🎨 Live Static Portal](https://shivam09xc.github.io/E-Commerce-Dashboard/)

---

<p align="center">
  <img src="https://raw.githubusercontent.com/andruim/andruim/master/images/forecasting.gif" width="40" />
</p>

### ✨ A unified business analytics hub presenting two distinct frontend visual layouts of E-Commerce transaction data.

### 🚀 Explore sales trends, KPIs, profit margins, and moving average forecasts with elegant animations and premium UI effects.

</div>

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# 🌟 Project Overview

This project is a complete **E-Commerce Analytics Dashboard Ecosystem** designed to provide deep business insights using:

* 📈 Interactive data visualizations
* 🧠 Intelligent KPI analytics
* ⚡ Dynamic filtering systems
* 🎨 Modern glassmorphism UI
* 📊 Forecasting & sales tracking
* ☁️ Cloud deployment support

The platform combines:

* **Streamlit-powered Python analytics**
* **Interactive JavaScript dashboards**
* **Power BI inspired corporate reports**
* **Real-time filtering experiences**

making it a professional-grade business intelligence portal.

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# 🛠️ Built With & Tech Stack

<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-for-the-badge\&logo=Streamlit\&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=flat-for-the-badge\&logo=pandas\&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=flat-for-the-badge\&logo=javascript\&logoColor=black)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D?style=flat-for-the-badge\&logo=chart.js\&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat-for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat-for-the-badge\&logo=css3\&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=flat-for-the-badge\&logo=microsoft-excel\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-for-the-badge\&logo=github\&logoColor=white)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# 🚀 Key Features

## 📊 1. Interactive Chart.js Dashboard (Dark Theme)

✨ Beautiful modern dashboard with premium UI animations.

### Features:

* 🌌 Glassmorphism design system
* ⚡ Dynamic slicers & filters
* 📈 Real-time analytics updates
* 📉 Moving average forecasting
* 🎯 Revenue tracking visualizations
* 🧠 Smart KPI recalculations
* 🌙 Dark neon dashboard aesthetics

---

## 🎨 2. Power BI Styled Corporate Report

📋 Enterprise-level reporting portal inspired by Microsoft Power BI.

### Features:

* 🏢 Corporate UI layouts
* 📊 KPI delta cards
* 📌 Region-based drill-through
* 📉 Profitability analysis
* 📍 Interactive data segmentation
* ⚙️ Advanced dashboard structure

---

## 🔍 3. Streamlit Data Explorer

⚡ Powerful analytics engine built with Python & Pandas.

### Features:

* 🔎 Search engine filtering
* 📁 Dataset exploration
* 📥 CSV export functionality
* 📊 Real-time metric updates
* 🧮 Business calculations
* 📈 Interactive visual insights

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# ⚙️ How to Run Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shivam09xc/E-Commerce-Dashboard.git
cd E-Commerce-Dashboard
```

---

## 2️⃣ Install Dependencies

Ensure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start the Streamlit Application

```bash
python -m streamlit run app.py
```

✅ This automatically launches the dashboard at:

```bash
http://localhost:8501
```

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# 🔄 Data Rebuilding Pipeline

If you update transaction data in Excel sheets, rebuild the datasets using the automated processing pipeline.

```mermaid
graph LR
    Excel[ecommerce_analytics.xlsx] -->|Python pandas| Proc[process_data.py]
    Proc -->|Generates| JSON[transactions.json]
    JSON -->|Python compiler| Comp[build_dynamic_dashboards.py]
    Comp -->|Injects Data & Recompiles| HTML1[ecommerce_dashboard.html]
    Comp -->|Injects Data & Recompiles| HTML2[ecommerce_powerbi_dashboard.html]
```

## ▶️ Run Commands Sequentially

```bash
# Process Excel rows into JSON
python process_data.py

# Rebuild dashboards dynamically
python build_dynamic_dashboards.py
```

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# ☁️ Deployment Guide

## 🌐 GitHub Pages Deployment

1. Open repository settings
2. Navigate to **Pages**
3. Select:

   * Source → Deploy from branch
   * Branch → main
   * Folder → /(root)
4. Save changes

🚀 Your static analytics portal will go live instantly.

---

## ☁️ Streamlit Cloud Deployment

1. Visit Streamlit Cloud
2. Connect your GitHub account
3. Select repository:

```bash
Shivam09xc/E-Commerce-Dashboard
```

4. Set entry file:

```bash
app.py
```

5. Click Deploy 🚀

---

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>

# 📈 GitHub Analytics

<p align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=Shivam09xc&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117"/>

  <img height="180em" src="https://github-readme-streak-stats.herokuapp.com/?user=Shivam09xc&theme=tokyonight&hide_border=true&background=0D1117"/>
</p>

---

# 🏆 GitHub Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=Shivam09xc&theme=tokyonight&no-frame=true&row=1&column=6" />
</p>

---

# 🐍 Contribution Snake Animation

<p align="center">
  <img src="https://raw.githubusercontent.com/Shivam09xc/Shivam09xc/output/snake.svg" alt="Snake animation" />
</p>

---

# 🌟 Future Enhancements

* 🔐 Authentication System
* 🌙 Dark/Light Theme Switcher
* ☁️ Firebase Integration
* 📱 Fully Responsive Mobile Layouts
* 📊 AI-based Forecasting
* 🧠 Machine Learning Analytics
* 🔔 Smart Notifications
* 🛒 Product Inventory Management

---

<div align="center">

# 💙 Crafted with Passion by Shivam Soni

<img src="https://skillicons.dev/icons?i=python,js,html,css,github,vscode" />

### ⭐ If you like this project, give it a star and support the repository!

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:7F00FF&height=120&section=footer" />

</div>
