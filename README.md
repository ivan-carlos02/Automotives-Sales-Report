# Automotives Sales EDA Report

## Repository Outline
- DAG.py -  File python script berisi proses DAG Airflow dari fetching data dari SQL, data cleaning dan data loading ke ElasticSearch
- GX.ipynb - File notebook berisi Great Expectation dengan 7 expectation terhadap dataset yang sudah clean
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