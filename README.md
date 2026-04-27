# E-Commerce Analytics Dashboard 📊

A comprehensive interactive dashboard for analyzing e-commerce order data, built with Streamlit. This project visualizes customer behavior, delivery performance, and product trends from a Brazilian e-commerce dataset.

## 🔗 Live Dashboard

**[Access the Dashboard Here](https://dicoding-dashboard-e-commerce-daffa.streamlit.app/)**

## 📋 Project Overview

This dashboard provides insights into:
- **Order Metrics**: Total orders, revenue, and average customer ratings
- **Delivery Performance**: On-time delivery rates, delay analysis, and status distribution
- **Product Analysis**: Orders by category and price distribution
- **Customer Insights**: Orders by state and geographic distribution
- **Trends**: Historical order patterns over time
- **Customer Satisfaction**: Rating distribution and review scores

## 📂 Project Structure

```
submission/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── notebook.ipynb              # Data analysis notebook
├── dashboard/
│   ├── dashboard.py            # Main Streamlit application
│   └── main_data.csv           # Processed dataset for dashboard
└── data/
    ├── customers_dataset.csv
    ├── order_items_dataset.csv
    ├── order_payments_dataset.csv
    ├── order_reviews_dataset.csv
    ├── orders_dataset.csv
    ├── product_category_name_translation.csv
    ├── products_dataset.csv
    └── sellers_dataset.csv
```

## 🎯 Key Features

### 📈 Dashboard Sections

1. **Key Metrics Cards**
   - Total Orders count
   - Total Revenue (in R$)
   - Average Customer Rating
   - Average Delivery Delay
   - On-Time Delivery Percentage

2. **Interactive Visualizations**
   - Top 10 Product Categories by Orders
   - Top 10 States by Orders
   - Price Distribution Histogram
   - Customer Rating Distribution
   - Order Status Pie Chart
   - Monthly Orders Trend
   - On-Time vs Late Delivery
   - Delivery Delay Distribution

3. **Filters**
   - Filter by Customer State(s)
   - Filter by Product Category(ies)
   - Filter by Order Status
   - Real-time dashboard updates

4. **Data Table**
   - View detailed raw data
   - First 100 records displayed
   - Toggle visibility

## 📊 Dataset Description

The `main_data.csv` file contains aggregated data with the following columns:

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `customer_id` | Customer identifier |
| `product_id` | Product identifier |
| `product_category_name_english` | Product category in English |
| `price` | Product price in R$ |
| `freight_value` | Shipping cost in R$ |
| `order_status` | Current order status |
| `order_purchase_timestamp` | Order purchase date/time |
| `order_delivered_customer_date` | Actual delivery date/time |
| `order_estimated_delivery_date` | Estimated delivery date |
| `year` | Year of purchase |
| `month` | Month of purchase |
| `year_month` | Year-Month format |
| `delay_days` | Number of days delayed (negative = early) |
| `is_late` | Whether delivery was late |
| `customer_state` | Customer's state abbreviation |
| `customer_city` | Customer's city |
| `avg_review_score` | Average review rating (1-5) |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Clone or download the repository**

2. **Navigate to the project directory**
   ```bash
   cd submission
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. **Navigate to the dashboard directory**
   ```bash
   cd dashboard
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run dashboard.py
   ```

3. **Open your browser**
   The dashboard will automatically open at `http://localhost:8501`

## 📦 Dependencies

- **streamlit** - Web app framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization

See `requirements.txt` for specific versions.

## 💡 Usage Guide

### Using the Filters

1. Open the dashboard
2. Use the **Filters** panel on the left sidebar
3. Select:
   - One or more customer states
   - One or more product categories
   - One or more order statuses
4. The dashboard updates in real-time

### Viewing Details

- Check the **"Show raw data"** checkbox at the bottom to view detailed transaction data
- Hover over charts for more information
- Use the download button in chart menus to export visualizations

## 📈 Insights You Can Gain

- **Revenue Analysis**: Identify high-value products and categories
- **Delivery Performance**: Monitor on-time delivery metrics
- **Customer Satisfaction**: Analyze rating patterns and correlations
- **Geographic Trends**: Understand order distribution across states
- **Temporal Patterns**: Identify seasonal trends and growth periods

## 🔧 Customization

You can customize the dashboard by:

1. **Modifying colors and styles** in the CSS section at the top of `dashboard.py`
2. **Changing the number of top categories** displayed (modify the `.head(n)` values)
3. **Adding new visualizations** by following the existing pattern
4. **Adjusting filters** to include/exclude specific data dimensions

## 📝 Data Processing Notes

The `main_data.csv` is a pre-processed dataset that combines information from 8 different source CSV files in the `data/` folder. The processing includes:

- Merging order, customer, product, and review data
- Calculating delivery delays and late delivery flags
- Translating product categories to English
- Aggregating review scores by order

## 🎓 Learning Outcomes

This project demonstrates:
- Data analysis and visualization techniques
- Streamlit dashboard development
- Interactive filtering and real-time data updates
- Pandas data manipulation
- Python data science workflow

## 📄 License

This project is part of the Dicoding - Data Analysis Fundamental Course submission.

## 👤 Author

**Daffa**

## 📧 Contact

For questions or feedback about this project, please reach out through Dicoding.

---

**Last Updated**: April 2026

**Dashboard Status**: Live ✅

