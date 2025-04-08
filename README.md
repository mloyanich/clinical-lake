# clinical-lake

This is a project for building a Clinical Data Lakehouse using **PySpark** and **Apache Iceberg** for clinical trials data.

## Steps to Run

1. Clone the repository
2. Open the project in **GitHub Codespaces** or run the Docker container locally
3. Create a virtual
3. Install dependencies: `pip install -r requirements.txt`
4. Run the ETL script:

    ```bash
    python src/main.py
    ```

5. Query Iceberg tables using PySpark and Jupyter notebooks

## Project Structure

Project structure for Pharma Data Lakehouse with PySpark and Iceberg integration.

```bash
clinical-lake/
│pharma_data_lakehouse/
├── .devcontainer/                    # For GitHub Codespaces or local Docker dev environment
│   ├── Dockerfile                    # Defines the dev container with Spark + Iceberg setup
│   └── devcontainer.json             # VS Code settings for Codespaces
│
├── data/                             # Folder for input raw data (clinical trials)
│   └── clinical_trials.csv           # Sample data file (600MB, to be loaded into the system)
│
├── src/                              # Python source code
│   ├── etl/                          # ETL scripts for data transformation and loading into Iceberg
│   │   ├── __init__.py               # Marks as a package
│   │   └── transform.py              # Script for cleaning and transforming the raw data
│   └── main.py                       # Main entry point for executing the ETL pipeline
│
├── notebooks/                        # Jupyter notebooks for experimenting with data and queries
│   └── clinical_trials_etl.ipynb     # Jupyter notebook to test ETL logic and query Iceberg tables
│
├── warehouse/                        # Location for Iceberg table storage (can point to MinIO or S3)
│   └── local/                        # Local storage for Iceberg tables
│
├── .gitignore                        # Git ignore for unnecessary files (e.g., local warehouse)
├── pyproject.toml                    # Poetry project configuration file (dependencies, versioning)
├── requirements.txt                  # (Optional) If using both poetry and a fallback method
├── README.md                         # Project documentation
└── setup.py                          # Package setup for the project (optional, if creating a Python package)

```
