## Dataset — Brazilian E-Commerce Public Dataset by Olist

This directory is reserved for the Olist dataset CSV files.  
**Do NOT commit the dataset files to GitHub** (they are excluded by `.gitignore`).

---

### Dataset Name
Brazilian E-Commerce Public Dataset by Olist

### Source
Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

### Required CSV Files

| File | Description |
|------|-------------|
| `olist_orders_dataset.csv` | Order-level records (status, timestamps) |
| `olist_order_items_dataset.csv` | Line items per order (product, price, freight) |
| `olist_customers_dataset.csv` | Customer info (unique ID, city, state) |
| `olist_products_dataset.csv` | Product metadata (category, dimensions, weight) |
| `product_category_name_translation.csv` | Portuguese → English category translation |

> The following files are present in the dataset but are **not required** by this project's analysis:
> `olist_sellers_dataset.csv`, `olist_order_payments_dataset.csv`,
> `olist_order_reviews_dataset.csv`, `olist_geolocation_dataset.csv`

---

### How to Download

#### Option A — Kaggle Website
1. Go to https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
2. Click **Download** (you must be logged in to Kaggle)
3. Extract the ZIP archive

#### Option B — Kaggle CLI
```bash
pip install kaggle
kaggle datasets download -d olistbr/brazilian-ecommerce
unzip brazilian-ecommerce.zip -d olist_data/
```

---

### Where to Place Files

#### Google Colab (recommended)
Upload the CSV files to Google Drive, then set:
```python
DATA_PATH = "/content/drive/MyDrive/olist_data/"
```
Or upload directly to the Colab session:
```python
DATA_PATH = "/content/olist_data/"
```

#### Local Jupyter
Place CSV files in this `data/` directory and set:
```python
DATA_PATH = "data/"
```

---

### Expected DATA_PATH in Notebook

```python
DATA_PATH = "/content/olist_data/"   # Google Colab default
```

Change this to match your actual file location before running.

---

### Dataset License
CC BY-NC-SA 4.0 — See Kaggle dataset page for full license details.
