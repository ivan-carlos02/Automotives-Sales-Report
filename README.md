# Automotives Sales EDA Report

## Repository Outline
- P2M3_ivan_carlos_tambunan_DDL.txt - File .txt berisi SQL query memasukkan data .csv kedalam database PostgreSQL
- P2M3_ivan_carlos_tambunan_DAG.py -  File python script berisi proses DAG Airflow dari fetching data dari SQL, data cleaning dan data loading ke ElasticSearch
- P2M3_ivan_carlos_tambunan_GX.ipynb - File notebook berisi Great Expectation dengan 7 expectation terhadap dataset yang sudah clean
- P2M3_ivan_carlos_tambunan_conceptual.txt - File berisi pertanyaan sekitar NoSQL beserta jawaban
- Folder images - Berisi gambar-gambar hasil visualisasi

## Problem Background
Perlunya dilakukan Exploratory Data Analysis terhadap dataset, kususnya automotives sale dataset ini, untuk melihat pola seasonal dan juga pola performa dari tiap-tiap produk sehingga dari hasil pola ini bisa menjadi gambaran untuk mengambil keputusan bisnis domain berdasarkan pola dan trend tersebut.

## Project Output
Berupa images visualisasi hasil exploratory data analysis di dalam folder images

## Data
- Sumber Dataset - [Automotives sales dataset](https://www.kaggle.com/datasets/ddosad/auto-sales-data/data)

## Method
- Penggunaan Apache Airflow untuk penjadwalan Fetching Dataset dari PostgreSQL, data cleaning dan data loading ke ElasticSearch
- Visualisasi - Horizontal dan Vertical Bar Chart, Pie Chart, Line Chart, Data Table Chart using Kibana.
- Great Expectations 

## Stacks
- Pandas
- Elasticsearch
- Great Expectation
- Airflow Operator
- Datetime 

## Reference
- [Great Expectation Available Rules](https://greatexpectations.io/expectations/)
- [Kibana Custom Visualization](https://logz.io/blog/kibana-visualizations/)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)