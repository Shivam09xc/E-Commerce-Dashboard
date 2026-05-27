import json
import os

def build_dashboards():
    print("Loading transactions from JSON...")
    with open("transactions.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)
    
    # Serialize the transactions list to JSON
    transactions_js = json.dumps(transactions)

    # 1. PROCESS ECOMMERCE_DASHBOARD.HTML
    print("Processing ecommerce_dashboard.html...")
    with open("ecommerce_dashboard.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Define the Slicers CSS
    slicers_css = """
  /* ── Slicers Panel Styling ── */
  .slicers-panel {
    display: flex; gap: 24px; flex-wrap: wrap;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px; padding: 18px 24px;
    margin-bottom: 28px; align-items: center;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }
  .slicer { display: flex; align-items: center; gap: 12px; }
  .slicer-label { font-size: 11px; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; }
  .slicer-group { display: flex; gap: 6px; flex-wrap: wrap; }
  .slicer-btn {
    padding: 6px 12px; border-radius: 8px; font-size: 11px; font-weight: 600;
    cursor: pointer; border: 1px solid var(--border); background: var(--surface2);
    color: var(--text); transition: all 0.2s;
    font-family: 'Space Grotesk', sans-serif;
  }
  .slicer-btn:hover { border-color: var(--accent); color: var(--accent); }
  .slicer-btn.active { background: var(--accent); color: var(--bg); border-color: var(--accent); box-shadow: 0 0 15px rgba(0, 212, 255, 0.4); }
"""

    # Inject CSS before </style> if not already present
    if ".slicers-panel" not in html_content:
        style_idx = html_content.find("</style>")
        if style_idx != -1:
            html_content = html_content[:style_idx] + slicers_css + html_content[style_idx:]

    # Define the Slicers HTML
    slicers_panel_html = """
  <!-- SLICERS PANEL (GLASSMORPHISM STYLE) -->
  <div class="slicers-panel">
    <div class="slicer">
      <span class="slicer-label">Year</span>
      <div class="slicer-group" id="year-slicers">
        <button class="slicer-btn active" onclick="setFilter('year', 'all')">All</button>
        <button class="slicer-btn" onclick="setFilter('year', 2021)">2021</button>
        <button class="slicer-btn" onclick="setFilter('year', 2022)">2022</button>
        <button class="slicer-btn" onclick="setFilter('year', 2023)">2023</button>
        <button class="slicer-btn" onclick="setFilter('year', 2024)">2024</button>
      </div>
    </div>
    <div class="slicer">
      <span class="slicer-label">Region</span>
      <div class="slicer-group" id="region-slicers">
        <button class="slicer-btn active" onclick="setFilter('region', 'all')">All</button>
        <button class="slicer-btn" onclick="setFilter('region', 'Central')">Central</button>
        <button class="slicer-btn" onclick="setFilter('region', 'East')">East</button>
        <button class="slicer-btn" onclick="setFilter('region', 'North')">North</button>
        <button class="slicer-btn" onclick="setFilter('region', 'South')">South</button>
        <button class="slicer-btn" onclick="setFilter('region', 'West')">West</button>
      </div>
    </div>
    <div class="slicer">
      <span class="slicer-label">Category</span>
      <div class="slicer-group" id="category-slicers">
        <button class="slicer-btn active" onclick="setFilter('category', 'all')">All</button>
        <button class="slicer-btn" onclick="setFilter('category', 'Clothing')">Clothing</button>
        <button class="slicer-btn" onclick="setFilter('category', 'Food & Beverage')">F&B</button>
        <button class="slicer-btn" onclick="setFilter('category', 'Furniture')">Furniture</button>
        <button class="slicer-btn" onclick="setFilter('category', 'Office Supplies')">Office</button>
        <button class="slicer-btn" onclick="setFilter('category', 'Technology')">Tech</button>
      </div>
    </div>
  </div>
"""

    # Replace old year selector in header-right if present
    old_header_right = """    <div class="header-right">
      <span class="badge badge-live">● Live Data</span>
      <span class="badge badge-date">May 2026</span>
      <div class="period-selector">
        <button class="period-btn" onclick="filterYear(2021)">2021</button>
        <button class="period-btn" onclick="filterYear(2022)">2022</button>
        <button class="period-btn" onclick="filterYear(2023)">2023</button>
        <button class="period-btn" onclick="filterYear(2024)">2024</button>
        <button class="period-btn active" onclick="filterYear('all')">All</button>
      </div>
    </div>"""

    new_header_right = """    <div class="header-right">
      <span class="badge badge-live">● Live Data</span>
      <span class="badge badge-date">May 2026</span>
    </div>"""

    html_content = html_content.replace(old_header_right, new_header_right)

    # Inject Slicers Panel HTML below </header> if not already present
    if "slicers-panel" not in html_content:
        header_end_idx = html_content.find("</header>")
        if header_end_idx != -1:
            html_content = html_content[:header_end_idx + 9] + slicers_panel_html + html_content[header_end_idx + 9:]

    # Rewrite the Javascript code block
    script_start_idx = html_content.find("<script>")
    script_end_idx = html_content.find("</script>", script_start_idx)
    
    if script_start_idx != -1 and script_end_idx != -1:
        # We will build the new JS block using raw string replacement for safety
        js_code_template = """<script>
// ── REAL DATA INJECTED FROM EXCEL ──
const TRANSACTIONS = TRANSACTIONS_PLACEHOLDER;

// ── Chart defaults ──
Chart.defaults.color = '#64748b';
Chart.defaults.font.family = 'Space Grotesk';
Chart.defaults.plugins.legend.labels.boxWidth = 10;
Chart.defaults.plugins.legend.labels.padding = 16;

const COLORS = ['#00d4ff','#10b981','#ff4d6d','#7c3aed','#fbbf24','#06b6d4','#f97316'];
const REG_COLORS = { Central:'#7c3aed', East:'#00d4ff', North:'#10b981', South:'#ff4d6d', West:'#fbbf24' };
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

function fmt(n) {
  if (n >= 1e7) return '₹' + (n/1e7).toFixed(1) + 'Cr';
  if (n >= 1e5) return '₹' + (n/1e5).toFixed(1) + 'L';
  if (n >= 1e3) return '₹' + (n/1e3).toFixed(0) + 'K';
  return '₹' + n.toFixed(0);
}

// Moving average helper
function movingAvg(arr, window=3) {
  return arr.map((v,i) => {
    if (i < window-1) return null;
    const slice = arr.slice(i-window+1, i+1);
    return slice.reduce((a,b)=>a+b,0)/window;
  });
}

// Global Filter State
let selectedYear = 'all';
let selectedRegion = 'all';
let selectedCategory = 'all';

// Chart Instances
let trendChart, yearlyChart, regionChart, catChart, segChart, prodChart;

// Aggregate and Render Everything
function updateDashboard() {
  // 1. Filter Transactions
  let filtered = TRANSACTIONS;
  if (selectedYear !== 'all') filtered = filtered.filter(t => t[9] === parseInt(selectedYear, 10));
  if (selectedRegion !== 'all') filtered = filtered.filter(t => t[4] === selectedRegion);
  if (selectedCategory !== 'all') filtered = filtered.filter(t => t[5] === selectedCategory);

  // 2. Compute KPI Metrics
  let totalSales = 0;
  let totalProfit = 0;
  const uniqueOrders = new Set();
  const uniqueCustomers = new Set();
  const customerOrderCount = {};
  
  filtered.forEach(t => {
    totalSales += t[7];
    totalProfit += t[8];
    uniqueOrders.add(t[0]);
    uniqueCustomers.add(t[2]);
    customerOrderCount[t[2]] = (customerOrderCount[t[2]] || 0) + 1;
  });

  const ordersCount = uniqueOrders.size;
  const customersCount = uniqueCustomers.size;
  const margin = totalSales > 0 ? ((totalProfit / totalSales) * 100).toFixed(1) : "0.0";
  
  let repeatCust = 0;
  Object.values(customerOrderCount).forEach(cnt => {
    if (cnt > 1) repeatCust++;
  });
  const retention = customersCount > 0 ? ((repeatCust / customersCount) * 100).toFixed(1) : "0.0";

  // Update KPI UI Elements
  document.getElementById('k-sales').textContent = fmt(totalSales);
  document.getElementById('k-profit').textContent = fmt(totalProfit);
  document.getElementById('k-orders').textContent = ordersCount.toLocaleString();
  document.getElementById('k-cust').textContent = customersCount.toLocaleString();
  document.getElementById('k-margin').textContent = margin + '%';
  document.getElementById('k-ret').textContent = retention + '%';

  // 3. Aggregate Monthly Sales & Profit Trend
  let trendLabels = [];
  let trendSales = [];
  let trendProfit = [];
  
  const yearsToInclude = selectedYear === 'all' ? [2021, 2022, 2023, 2024] : [parseInt(selectedYear, 10)];
  yearsToInclude.forEach(y => {
    MONTHS.forEach(m => {
      trendLabels.push(m + ' ' + y);
      trendSales.push(0);
      trendProfit.push(0);
    });
  });

  filtered.forEach(t => {
    const yr = t[9];
    const dateStr = t[1];
    const moIdx = parseInt(dateStr.substring(5, 7), 10) - 1;
    const label = MONTHS[moIdx] + ' ' + yr;
    const idx = trendLabels.indexOf(label);
    if (idx !== -1) {
      trendSales[idx] += t[7];
      trendProfit[idx] += t[8];
    }
  });

  const maData = movingAvg(trendSales, 3);

  // Update/Create Trend Chart
  if (trendChart) {
    trendChart.data.labels = trendLabels;
    trendChart.data.datasets[0].data = trendSales;
    trendChart.data.datasets[1].data = trendProfit;
    trendChart.data.datasets[2].data = maData;
    trendChart.update();
  } else {
    const trendCtx = document.getElementById('trendChart').getContext('2d');
    trendChart = new Chart(trendCtx, {
      data: {
        labels: trendLabels,
        datasets: [
          {
            type: 'line', label: 'Sales',
            data: trendSales,
            borderColor: '#00d4ff', backgroundColor: 'rgba(0,212,255,0.08)',
            fill: true, tension: 0.4, pointRadius: 0, pointHoverRadius: 5,
            borderWidth: 2, order: 1
          },
          {
            type: 'line', label: 'Profit',
            data: trendProfit,
            borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.06)',
            fill: true, tension: 0.4, pointRadius: 0, pointHoverRadius: 5,
            borderWidth: 2, order: 2
          },
          {
            type: 'line', label: '3M Forecast',
            data: maData,
            borderColor: '#fbbf24', borderDash: [6,4],
            fill: false, tension: 0.4, pointRadius: 0,
            borderWidth: 1.5, order: 0
          }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: true,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: { position: 'top', align: 'end' },
          tooltip: {
            backgroundColor: '#111827',
            borderColor: '#1e2d45', borderWidth: 1,
            callbacks: { label: ctx => ' ' + ctx.dataset.label + ': ' + fmt(ctx.raw || 0) }
          }
        },
        scales: {
          x: { grid: { color: 'rgba(30,45,69,0.5)' }, ticks: { maxTicksLimit: selectedYear === 'all' ? 12 : 6, maxRotation: 30 } },
          y: { grid: { color: 'rgba(30,45,69,0.5)' }, ticks: { callback: v => fmt(v) } }
        }
      }
    });
  }

  // 4. Aggregate Yearly Growth Chart (respects Region & Category filters)
  let yearlyFiltered = TRANSACTIONS;
  if (selectedRegion !== 'all') yearlyFiltered = yearlyFiltered.filter(t => t[4] === selectedRegion);
  if (selectedCategory !== 'all') yearlyFiltered = yearlyFiltered.filter(t => t[5] === selectedCategory);

  const years = [2021, 2022, 2023, 2024];
  const yearlySales = [0, 0, 0, 0];
  const yearlyProfit = [0, 0, 0, 0];
  
  yearlyFiltered.forEach(t => {
    const yrIdx = years.indexOf(t[9]);
    if (yrIdx !== -1) {
      yearlySales[yrIdx] += t[7];
      yearlyProfit[yrIdx] += t[8];
    }
  });

  if (yearlyChart) {
    yearlyChart.data.datasets[0].data = yearlySales;
    yearlyChart.data.datasets[1].data = yearlyProfit;
    yearlyChart.update();
  } else {
    const yearlyCtx = document.getElementById('yearlyChart').getContext('2d');
    yearlyChart = new Chart(yearlyCtx, {
      type: 'bar',
      data: {
        labels: years.map(String),
        datasets: [
          { label: 'Sales', data: yearlySales, backgroundColor: 'rgba(0,212,255,0.7)', borderRadius: 6, borderSkipped: false },
          { label: 'Profit', data: yearlyProfit, backgroundColor: 'rgba(16,185,129,0.7)', borderRadius: 6, borderSkipped: false }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: true,
        plugins: {
          legend: { position: 'top' },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.dataset.label + ': ' + fmt(ctx.raw) } }
        },
        scales: {
          x: { grid: { display: false } },
          y: { grid: { color: 'rgba(30,45,69,0.5)' }, ticks: { callback: v => fmt(v) } }
        }
      }
    });
  }

  // 5. Aggregate Region Sales (Radar)
  const regionsList = ["Central", "East", "North", "South", "West"];
  const regionSales = [0, 0, 0, 0, 0];
  const regionProfit = [0, 0, 0, 0, 0];
  
  filtered.forEach(t => {
    const idx = regionsList.indexOf(t[4]);
    if (idx !== -1) {
      regionSales[idx] += t[7];
      regionProfit[idx] += t[8];
    }
  });

  if (regionChart) {
    regionChart.data.datasets[0].data = regionSales;
    regionChart.data.datasets[1].data = regionProfit;
    regionChart.update();
  } else {
    const regionCtx = document.getElementById('regionChart').getContext('2d');
    regionChart = new Chart(regionCtx, {
      type: 'radar',
      data: {
        labels: regionsList,
        datasets: [
          {
            label: 'Sales',
            data: regionSales,
            borderColor: '#00d4ff', backgroundColor: 'rgba(0,212,255,0.15)',
            pointBackgroundColor: '#00d4ff', pointRadius: 4
          },
          {
            label: 'Profit',
            data: regionProfit,
            borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.15)',
            pointBackgroundColor: '#10b981', pointRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { position: 'top' }, tooltip: { callbacks: { label: ctx => ' ' + ctx.dataset.label + ': ' + fmt(ctx.raw) } } },
        scales: { r: { grid: { color: 'rgba(30,45,69,0.8)' }, ticks: { display: false }, pointLabels: { color: '#94a3b8', font: { size: 11 } } } }
      }
    });
  }

  // 6. Aggregate Category Sales (Doughnut)
  const catList = ["Clothing", "Food & Beverage", "Furniture", "Office Supplies", "Technology"];
  const catSales = [0, 0, 0, 0, 0];
  
  filtered.forEach(t => {
    const idx = catList.indexOf(t[5]);
    if (idx !== -1) {
      catSales[idx] += t[7];
    }
  });

  if (catChart) {
    catChart.data.datasets[0].data = catSales;
    catChart.update();
  } else {
    const catCtx = document.getElementById('catChart').getContext('2d');
    catChart = new Chart(catCtx, {
      type: 'doughnut',
      data: {
        labels: catList,
        datasets: [{ data: catSales, backgroundColor: COLORS, borderWidth: 2, borderColor: '#111827', hoverOffset: 8 }]
      },
      options: {
        responsive: true, cutout: '62%',
        plugins: {
          legend: { position: 'bottom', labels: { font: { size: 10 } } },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.label + ': ' + fmt(ctx.raw) + ' (' + ((ctx.raw/catSales.reduce((a,b)=>a+b,0.001))*100).toFixed(1) + '%)' } }
        }
      }
    });
  }

  // 7. Aggregate Segment Sales (Doughnut)
  const segList = ["Consumer", "Corporate", "Home Office"];
  const segSales = [0, 0, 0];
  
  filtered.forEach(t => {
    const idx = segList.indexOf(t[3]);
    if (idx !== -1) {
      segSales[idx] += t[7];
    }
  });

  if (segChart) {
    segChart.data.datasets[0].data = segSales;
    segChart.update();
  } else {
    const segCtx = document.getElementById('segChart').getContext('2d');
    segChart = new Chart(segCtx, {
      type: 'doughnut',
      data: {
        labels: segList,
        datasets: [{ data: segSales, backgroundColor: ['#7c3aed','#00d4ff','#fbbf24'], borderWidth: 2, borderColor: '#111827', hoverOffset: 8 }]
      },
      options: {
        responsive: true, cutout: '62%',
        plugins: {
          legend: { position: 'bottom', labels: { font: { size: 10 } } },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.label + ': ' + fmt(ctx.raw) } }
        }
      }
    });
  }

  // 8. Top 10 Products by Revenue
  const prodSalesMap = {};
  const prodProfitMap = {};
  filtered.forEach(t => {
    const name = t[6];
    prodSalesMap[name] = (prodSalesMap[name] || 0) + t[7];
    prodProfitMap[name] = (prodProfitMap[name] || 0) + t[8];
  });

  const sortedProducts = Object.keys(prodSalesMap)
    .map(name => ({ name: name, sales: prodSalesMap[name], profit: prodProfitMap[name] }))
    .sort((a, b) => b.sales - a.sales)
    .slice(0, 10);

  const topProdLabels = sortedProducts.map(p => p.name.length > 20 ? p.name.substring(0, 18) + '...' : p.name);
  const topProdSales = sortedProducts.map(p => p.sales);
  const topProdProfit = sortedProducts.map(p => p.profit);

  if (prodChart) {
    prodChart.data.labels = topProdLabels;
    prodChart.data.datasets[0].data = topProdSales;
    prodChart.data.datasets[1].data = topProdProfit;
    prodChart.update();
  } else {
    const prodCtx = document.getElementById('prodChart').getContext('2d');
    prodChart = new Chart(prodCtx, {
      type: 'bar',
      data: {
        labels: topProdLabels,
        datasets: [
          { label: 'Sales', data: topProdSales, backgroundColor: 'rgba(0,212,255,0.75)', borderRadius: 4, borderSkipped: false },
          { label: 'Profit', data: topProdProfit, backgroundColor: 'rgba(16,185,129,0.75)', borderRadius: 4, borderSkipped: false }
        ]
      },
      options: {
        indexAxis: 'y', responsive: true,
        plugins: {
          legend: { position: 'top' },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.dataset.label + ': ' + fmt(ctx.raw) } }
        },
        scales: {
          x: { grid: { color: 'rgba(30,45,69,0.5)' }, ticks: { callback: v => fmt(v) } },
          y: { grid: { display: false }, ticks: { font: { size: 10 } } }
        }
      }
    });
  }

  // 9. Region Performance Table
  const tableSales = {};
  const tableProfit = {};
  const tableOrders = {};

  regionsList.forEach(r => {
    tableSales[r] = 0;
    tableProfit[r] = 0;
    tableOrders[r] = new Set();
  });

  filtered.forEach(t => {
    const r = t[4];
    if (tableSales.hasOwnProperty(r)) {
      tableSales[r] += t[7];
      tableProfit[r] += t[8];
      tableOrders[r].add(t[0]);
    }
  });

  const totalTableSales = Object.values(tableSales).reduce((a, b) => a + b, 0.001);
  const tbody = document.getElementById('regionBody');
  tbody.innerHTML = '';

  regionsList.forEach(r => {
    const s = tableSales[r];
    const p = tableProfit[r];
    const o = tableOrders[r].size;
    const m = s > 0 ? ((p / s) * 100).toFixed(1) : "0.0";
    const sh = ((s / totalTableSales) * 100).toFixed(1);

    tbody.innerHTML += '<tr>' +
      '<td><span class="tag" style="background:' + REG_COLORS[r] + '22;color:' + REG_COLORS[r] + '">' + r + '</span></td>' +
      '<td style="font-family:\\\'JetBrains Mono\\\',monospace;font-size:11px">' + fmt(s) + '</td>' +
      '<td style="font-family:\\\'JetBrains Mono\\\',monospace;font-size:11px;color:#10b981">' + fmt(p) + '</td>' +
      '<td>' + o.toLocaleString() + '</td>' +
      '<td>' +
        '<div style="font-size:11px;font-weight:600;color:' + (parseFloat(m)>40?'#10b981':'#fbbf24') + '">' + m + '%</div>' +
        '<div class="profit-bar"><div class="profit-fill" style="width:' + Math.min(parseFloat(m), 100) + '%"></div></div>' +
      '</td>' +
      '<td style="font-size:11px;color:#94a3b8">' + sh + '%</td>' +
      '</tr>';
  });
}

// ── FILTER ACTIONS ──
function setFilter(type, value) {
  if (type === 'year') {
    selectedYear = value;
    document.querySelectorAll('#year-slicers .slicer-btn').forEach(btn => {
      btn.classList.toggle('active', btn.textContent === (value === 'all' ? 'All' : String(value)));
    });
  } else if (type === 'region') {
    selectedRegion = value;
    document.querySelectorAll('#region-slicers .slicer-btn').forEach(btn => {
      btn.classList.toggle('active', btn.textContent === (value === 'all' ? 'All' : String(value)));
    });
  } else if (type === 'category') {
    selectedCategory = value;
    const catLabels = { 'all': 'All', 'Clothing': 'Clothing', 'Food & Beverage': 'F&B', 'Furniture': 'Furniture', 'Office Supplies': 'Office', 'Technology': 'Tech' };
    document.querySelectorAll('#category-slicers .slicer-btn').forEach(btn => {
      btn.classList.toggle('active', btn.textContent === catLabels[value]);
    });
  }

  updateDashboard();
}

// Initialize
updateDashboard();
</script>"""
        
        js_code_with_data = js_code_template.replace("TRANSACTIONS_PLACEHOLDER", transactions_js)
        html_content = html_content[:script_start_idx] + js_code_with_data + html_content[script_end_idx + 9:]

    with open("ecommerce_dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("ecommerce_dashboard.html processed and written successfully!")


    # 2. PROCESS ECOMMERCE_POWERBI_DASHBOARD.HTML
    print("Processing ecommerce_powerbi_dashboard.html...")
    with open("ecommerce_powerbi_dashboard.html", "r", encoding="utf-8") as f:
        pbi_content = f.read()

    pbi_script_start = pbi_content.find("<script>")
    pbi_script_end = pbi_content.find("</script>", pbi_script_start)

    if pbi_script_start != -1 and pbi_script_end != -1:
        pbi_js_template = """<script>
const RAW_TRANSACTIONS = TRANSACTIONS_PLACEHOLDER;

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const REG_COLS = {North:'#185FA5',East:'#1D9E75',Central:'#7F77DD',South:'#D85A30',West:'#BA7517'};
const PALETTE = ['#185FA5','#1D9E75','#D85A30','#7F77DD','#BA7517','#0F6E56'];

function fmt(n) {
  if (n >= 1e7) return '₹' + (n/1e7).toFixed(1) + 'Cr';
  if (n >= 1e5) return '₹' + (n/1e5).toFixed(1) + 'L';
  if (n >= 1e3) return '₹' + (n/1e3).toFixed(0) + 'K';
  return '₹' + Math.round(n);
}

function movAvg(arr, w=3) {
  return arr.map((v,i)=>i<w-1?null:arr.slice(i-w+1,i+1).reduce((a,b)=>a+b,0)/w);
}

// Global state
let selYr = 'all', selReg = 'all', selCat = 'all';
let trendCh, yearlyCh, catCh, prodCh;

Chart.defaults.font.family='var(--font-sans)';
Chart.defaults.color='#888780';
Chart.defaults.plugins.legend.display=false;

function makeChart(id,cfg) { return new Chart(document.getElementById(id),cfg); }

function getFilteredData() {
  let filtered = RAW_TRANSACTIONS;
  if (selYr !== 'all') filtered = filtered.filter(t => t[9] === parseInt(selYr, 10));
  if (selReg !== 'all') filtered = filtered.filter(t => t[4] === selReg);
  if (selCat !== 'all') filtered = filtered.filter(t => t[5] === selCat);
  return filtered;
}

function buildTrend() {
  let labels = [];
  let sales = [];
  let profit = [];
  
  const years = selYr === 'all' ? [2021, 2022, 2023, 2024] : [parseInt(selYr, 10)];
  years.forEach(y => {
    MONTHS.forEach(m => {
      labels.push(m + ' ' + y);
      sales.push(0);
      profit.push(0);
    });
  });

  const filtered = getFilteredData();
  filtered.forEach(t => {
    const yr = t[9];
    const dateStr = t[1];
    const moIdx = parseInt(dateStr.substring(5, 7), 10) - 1;
    const lbl = MONTHS[moIdx] + ' ' + yr;
    const idx = labels.indexOf(lbl);
    if (idx !== -1) {
      sales[idx] += t[7];
      profit[idx] += t[8];
    }
  });

  const ma = movAvg(sales);

  const cfg = {
    data: {
      labels: labels,
      datasets: [
        {type:'line',label:'Sales',data:sales,borderColor:'#185FA5',backgroundColor:'rgba(24,95,165,0.07)',fill:true,tension:.4,pointRadius:0,pointHoverRadius:4,borderWidth:2},
        {type:'line',label:'Profit',data:profit,borderColor:'#1D9E75',backgroundColor:'rgba(29,158,117,0.06)',fill:true,tension:.4,pointRadius:0,pointHoverRadius:4,borderWidth:2},
        {type:'line',label:'Forecast',data:ma,borderColor:'#BA7517',borderDash:[5,4],fill:false,tension:.4,pointRadius:0,borderWidth:1.5}
      ]
    },
    options: {
      responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},
      plugins:{tooltip:{callbacks:{label:c=>' ' + c.dataset.label + ': ' + fmt(c.raw||0)}}},
      scales:{
        x:{grid:{color:'rgba(136,135,128,0.1)'},ticks:{maxTicksLimit:selYr==='all'?12:6,maxRotation:30,font:{size:9}}},
        y:{grid:{color:'rgba(136,135,128,0.1)'},ticks:{callback:v=>fmt(v),font:{size:9}}}
      }
    }
  };

  if (trendCh) {
    trendCh.data = cfg.data;
    trendCh.options.scales.x.ticks.maxTicksLimit = selYr==='all'?12:6;
    trendCh.update();
  } else {
    trendCh = makeChart('trendC', cfg);
  }
}

function buildYearly() {
  let yearlyFiltered = RAW_TRANSACTIONS;
  if (selReg !== 'all') yearlyFiltered = yearlyFiltered.filter(t => t[4] === selReg);
  if (selCat !== 'all') yearlyFiltered = yearlyFiltered.filter(t => t[5] === selCat);

  const years = [2021, 2022, 2023, 2024];
  const yearlySales = [0,0,0,0];
  const yearlyProfit = [0,0,0,0];

  yearlyFiltered.forEach(t => {
    const idx = years.indexOf(t[9]);
    if (idx !== -1) {
      yearlySales[idx] += t[7];
      yearlyProfit[idx] += t[8];
    }
  });

  const cfg = {
    type:'bar',
    data:{
      labels: years.map(String),
      datasets: [
        {label:'Sales',data:yearlySales,backgroundColor:'rgba(24,95,165,0.8)',borderRadius:4,borderSkipped:false},
        {label:'Profit',data:yearlyProfit,backgroundColor:'rgba(29,158,117,0.8)',borderRadius:4,borderSkipped:false}
      ]
    },
    options:{
      responsive:true,maintainAspectRatio:false,
      plugins:{tooltip:{callbacks:{label:c=>' ' + c.dataset.label + ': ' + fmt(c.raw)}}},
      scales:{
        x:{grid:{display:false},ticks:{font:{size:10}}},
        y:{grid:{color:'rgba(136,135,128,0.1)'},ticks:{callback:v=>fmt(v),font:{size:9}}}
      }
    }
  };

  if (yearlyCh) {
    yearlyCh.data.datasets[0].data = yearlySales;
    yearlyCh.data.datasets[1].data = yearlyProfit;
    yearlyCh.update();
  } else {
    yearlyCh = makeChart('yearlyC', cfg);
  }
}

function buildRegBars() {
  const regions = ["North", "East", "Central", "South", "West"];
  const sales = [0,0,0,0,0];
  const profit = [0,0,0,0,0];

  const filtered = getFilteredData();
  filtered.forEach(t => {
    const idx = regions.indexOf(t[4]);
    if (idx !== -1) {
      sales[idx] += t[7];
      profit[idx] += t[8];
    }
  });

  const maxS = Math.max(...sales, 1);
  const el = document.getElementById('reg-bars');
  let rows = '';

  regions.forEach((r, i) => {
    if (selReg !== 'all' && r !== selReg) return;
    const pct = Math.round(sales[i] / maxS * 100);
    const m = sales[i] > 0 ? Math.round(profit[i] / sales[i] * 100) : 0;
    const col = REG_COLS[r] || '#185FA5';
    
    rows += '<div class="reg-row">' +
      '<span class="reg-name">' + r + '</span>' +
      '<div style="display:flex;flex-direction:column;gap:3px">' +
        '<div class="bar-wrap"><div class="bar-fill" style="width:' + pct + '%;background:' + col + '"></div></div>' +
        '<div style="font-size:10px;color:var(--color-text-tertiary)">' + fmt(profit[i]) + ' profit · ' + m + '% margin</div>' +
      '</div>' +
      '<span class="reg-val">' + fmt(sales[i]) + '</span>' +
    '</div>';
  });

  el.innerHTML = rows || '<span style="font-size:11px;color:var(--color-text-tertiary)">No data</span>';
}

function buildCat() {
  const categories = ["Technology", "Furniture", "Clothing", "Food & Beverage", "Office Supplies"];
  const sales = [0,0,0,0,0];

  const filtered = getFilteredData();
  filtered.forEach(t => {
    const idx = categories.indexOf(t[5]);
    if (idx !== -1) sales[idx] += t[7];
  });

  const cfg = {
    type:'doughnut',
    data:{
      labels: categories,
      datasets: [{data:sales,backgroundColor:PALETTE,borderWidth:1.5,borderColor:'#fff',hoverOffset:6}]
    },
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'60%',
      plugins:{
        legend:{display:true,position:'bottom',labels:{font:{size:9},padding:8,boxWidth:8}},
        tooltip:{callbacks:{label:c=>' ' + c.label + ': ' + fmt(c.raw) + ' (' + ((c.raw / (sales.reduce((a,b)=>a+b,0.01))) * 100).toFixed(1) + '%)'}}
      }
    }
  };

  if (catCh) {
    catCh.data = cfg.data;
    catCh.update();
  } else {
    catCh = makeChart('catC', cfg);
  }
}

function buildProd() {
  const filtered = getFilteredData();
  const prodMap = {};
  filtered.forEach(t => {
    prodMap[t[6]] = (prodMap[t[6]] || 0) + t[7];
  });

  const topProds = Object.keys(prodMap)
    .map(name => ({name: name, sales: prodMap[name]}))
    .sort((a,b)=>b.sales-a.sales)
    .slice(0, 7);

  const labels = topProds.map(p => p.name.length > 15 ? p.name.substring(0, 13) + '..' : p.name);
  const sales = topProds.map(p => p.sales);

  const cfg = {
    type:'bar',
    data:{
      labels: labels,
      datasets: [{
        label:'Sales',data:sales,
        backgroundColor:PALETTE.map(c=>c+'cc'),borderRadius:3,borderSkipped:false
      }]
    },
    options:{
      indexAxis:'y',responsive:true,maintainAspectRatio:false,
      plugins:{tooltip:{callbacks:{label:c=>' ' + fmt(c.raw)}}},
      scales:{
        x:{grid:{color:'rgba(136,135,128,0.1)'},ticks:{callback:v=>fmt(v),font:{size:9}}},
        y:{grid:{display:false},ticks:{font:{size:9}}}
      }
    }
  };

  if (prodCh) {
    prodCh.data.labels = labels;
    prodCh.data.datasets[0].data = sales;
    prodCh.update();
  } else {
    prodCh = makeChart('prodC', cfg);
  }
}

function updateKPIs() {
  const filtered = getFilteredData();
  let sales = 0, profit = 0;
  const uniqueOrders = new Set();
  const uniqueCusts = new Set();
  const custOrders = {};

  filtered.forEach(t => {
    sales += t[7];
    profit += t[8];
    uniqueOrders.add(t[0]);
    uniqueCusts.add(t[2]);
    custOrders[t[2]] = (custOrders[t[2]] || 0) + 1;
  });

  let repeats = 0;
  Object.values(custOrders).forEach(cnt => {
    if (cnt > 1) repeats++;
  });

  const margin = sales > 0 ? (profit/sales*100).toFixed(1)+'%' : '0.0%';
  const retention = uniqueCusts.size > 0 ? (repeats/uniqueCusts.size*100).toFixed(1)+'%' : '0.0%';

  document.getElementById('k0').textContent = fmt(sales);
  document.getElementById('k1').textContent = fmt(profit);
  document.getElementById('k2').textContent = uniqueOrders.size.toLocaleString();
  document.getElementById('k3').textContent = uniqueCusts.size.toLocaleString();
  document.getElementById('k4').textContent = margin;
  document.getElementById('k5').textContent = retention;

  const trendBadge = document.getElementById('trend-badge');
  const years = selYr === 'all' ? [2021, 2022, 2023, 2024] : [parseInt(selYr, 10)];
  trendBadge.textContent = (years.length * 12) + ' months';
}

function renderAll() {
  updateKPIs();
  buildTrend();
  buildYearly();
  buildRegBars();
  buildCat();
  buildProd();
}

document.getElementById('yr-chips').addEventListener('click', e => {
  const ch = e.target.closest('.chip'); if (!ch) return;
  document.querySelectorAll('#yr-chips .chip').forEach(c => c.classList.remove('active'));
  ch.classList.add('active');
  selYr = ch.dataset.yr;
  renderAll();
});

document.getElementById('reg-chips').addEventListener('click', e => {
  const ch = e.target.closest('.chip'); if (!ch) return;
  document.querySelectorAll('#reg-chips .chip').forEach(c => c.classList.remove('active'));
  ch.classList.add('active');
  selReg = ch.dataset.reg;
  renderAll();
});

document.getElementById('cat-chips').addEventListener('click', e => {
  const ch = e.target.closest('.chip'); if (!ch) return;
  document.querySelectorAll('#cat-chips .chip').forEach(c => c.classList.remove('active'));
  ch.classList.add('active');
  selCat = ch.dataset.cat;
  renderAll();
});

renderAll();
</script>"""
        
        pbi_js_with_data = pbi_js_template.replace("TRANSACTIONS_PLACEHOLDER", transactions_js)
        pbi_content = pbi_content[:pbi_script_start] + pbi_js_with_data + pbi_content[pbi_script_end + 9:]

    with open("ecommerce_powerbi_dashboard.html", "w", encoding="utf-8") as f:
        f.write(pbi_content)

    print("ecommerce_powerbi_dashboard.html processed and written successfully!")
    print("Dashboard compilation completed successfully!")


if __name__ == "__main__":
    build_dashboards()
