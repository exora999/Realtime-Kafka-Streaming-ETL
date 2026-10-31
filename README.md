ache Kafka**, **Python**, **Pandas**, and **SQLite**. This repository demonstrates event-driven architecture, streaming ETL, and columnar data storage using Apache Parquet.

---

## 🏗️ Architecture & Data Flow

[ Producer / Interactive Console ]
│
▼ (JSON Events)
[ Apache Kafka Broker ]
│
▼ (Topic: ecommerce-sales)
[ Stream Consumer ] ──► [ live_sales.csv ]
│
┌──────────────────┴──────────────────┐
▼                                     ▼
[ Streaming ETL Cleaner ]            [ Streaming Analytics ]
│                                     │
▼                                     ▼
[ clean_sales.parquet ]                [ analytic_summary.csv ]


---

## 🛠️ Key Components & Scripts

1. **Event Producers (`producer.py` & `interactive_producer.py`):**
   * Generates continuous real-time e-commerce transactions and pushes JSON payload events to the `ecommerce-sales` Kafka topic.
   * Includes interactive CLI ingestion for manually broadcasting customer orders.

2. **Stream Consumer (`consumer.py`):**
   * Listens continuously to Kafka topic streams and persists incoming event streams to disk.

3. **Streaming ETL & Storage (`etl_cleaner.py`):**
   * Performs ongoing validation filters (validates product catalog, ensures positive prices/quantities).
   * Transforms and exports valid transactional records into optimized **Apache Parquet** columnar files.

4. **Stream Analytics Engine (`analytics_pipeline.py`):**
   * Continuously aggregates running gross revenue metrics per payload cycle.

5. **Batch Ingestion Simulation (`simulator.py` & `connected.py`):**
   * Simulates relational database operations using SQLite, multi-table `INNER JOIN` queries, and batch aggregations.

---

## 💻 Tech Stack
* **Streaming Platform:** Apache Kafka, Zookeeper
* **Languages & Libraries:** Python 3.x, `kafka-python`, Pandas, PyArrow/FastParquet
* **Storage Formats:** Parquet, SQLite, CSV
* **Environment:** Linux (WSL / Ubuntu)
