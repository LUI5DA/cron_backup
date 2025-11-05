# 🗄️ Automated Backup System with Cron & Terraform

A complete and easy-to-deploy backup system written in Python, designed to automatically back up files or directories and store them securely in **Azure Blob Storage**.  
The infrastructure is provisioned using **Terraform**, and the backup process is automated via **cron jobs**.

---

## 📂 Project Structure

```
cron_backup/
│
├── azure_infra/
│   └── main.tf                # Terraform configuration for Azure resources
│
├── src/
│   ├── env/                   # Python virtual environment
│   ├── .env                   # Environment variables (Azure credentials)
│   ├── test/                  # Directory or files to be backed up
│   ├── abc.txt                # Example file for testing
│   ├── backup.py              # Backup script
│   └── requirements.txt       # Python dependencies
```

---

## ☁️ Infrastructure Setup with Terraform

The `azure_infra/` folder contains the Terraform configuration to provision:
- A **Resource Group**
- A **Randomized Azure Storage Account**
- Automatically generated **outputs** (name, access key, connection string)

---

## Prerequisites

Before you begin, please ensure you have the following tools installed and configured:

| Tool | Purpose | Installation Guide |
|------|---------|--------------------|
| **Terraform** | Used to provision the Azure infrastructure (Resource Group, Storage Account, Outputs). | [Install Terraform CLI](https://developer.hashicorp.com/terraform/install) :contentReference[oaicite:0]{index=0} |
| **Azure CLI (az)** | Used to interact with Azure (login, resource management) and required by the Terraform provider. | [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) :contentReference[oaicite:1]{index=1} |
| **Python 3** | Used to run the backup script (`backup.py`) and manage dependencies via `pip`. | [Install Python](https://realpython.com/installing-python/) :contentReference[oaicite:2]{index=2} |

### Additional Setup
- Ensure you have an Azure subscription with permissions to create Resource Groups and Storage Accounts.  
- Once Terraform has created the storage account, make sure to copy the **connection string output** into the `.env` file as **BLOB_STORAGE_STRING**.  
- If you run the Python script via cron (on Linux/macOS), be sure the virtual environment activated path and working directory are correct.



### 🧱 1. Initialize Terraform

Go to the Terraform directory:
```bash
cd azure_infra
```

Initialize the Terraform environment:
```bash
terraform init
```

---

### 🪄 2. Create and Apply the Infrastructure Plan

Generate a plan:
```bash
terraform plan -out create_plan
```

Apply the plan:
```bash
terraform apply "create_plan"
```

This will create:
- A resource group (`storage`)
- A randomized Azure Storage Account (e.g., `backups3fa7c9d1`)

---

### 📤 3. View and Use Terraform Outputs

Once applied, retrieve your outputs:
```bash
terraform output
```

You’ll see something like:
```
storage_account_name = "backups3fa7c9d1"
storage_account_primary_access_key = (sensitive value)
storage_account_connection_string = (sensitive value)
```

To print the actual values:
```bash
terraform output storage_account_connection_string
```

Copy the value of the output in your BLOB_STORAGE_STRING .env file variable

---

## 🐍 Python Backup Script Setup

Now that your Azure infrastructure is ready, move into the Python project directory:

```bash
cd ../src
```

---

### ⚙️ 1. Create a Virtual Environment

```bash
python -m venv env
```

Activate it:
```bash
source ./env/bin/activate
```

---

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔐 3. Configure Environment Variables

Create a `.env` file in the `src/` folder with the following content:

```bash
BLOB_STORAGE_STRING="your_azure_blob_storage_connection_string"
CONTAINER_NAME="your_container_name"
BLOB_NAME="your_blob_name"
```

*(You must use the connection string output from Terraform here.)*

the values of CONTAINER_NAME and BLOB_NAME can be any you want, they container and blob are created for the script if not exists
---

### 💾 4. Run the Backup Script Manually (Optional)

```bash
python backup.py backup test zip
```

This will:
- Compress the `test/` folder into `backup.zip`
- Upload it automatically to your configured Azure Blob Storage

---

## ⏰ Automating Backups with Cron

You can automate backups using **cron** on Linux.

Edit your crontab:
```bash
crontab -e
```

Add this line to run the backup every minute (adjust schedule as needed):
```bash
* * * * * /bin/bash -c 'cd /home/ldg4mez/Documents/cron_practices/src && /home/ldg4mez/Documents/cron_practices/src/env/bin/python backup.py backup test zip >> backup.log 2>&1'
```

This ensures:
- You execute from the correct directory (`src`)
- The virtual environment’s Python is used
- Output and errors are logged to `backup.log`

---

## 🧠 Troubleshooting

- **Empty log or no backup generated?**  
  Cron uses a minimal environment. Always use full paths and ensure your `.env` file is accessible from where the script runs.

- **Terraform output not found?**  
  Ensure you’re running `terraform output` **inside** the `azure_infra` directory.

- **Security tip:**  
  Do **not** commit `terraform.tfstate` or `.env` files to version control. These contain sensitive credentials.

---

## 🚀 Summary

| Component | Tool | Purpose |
|------------|------|----------|
| **Azure Infra** | Terraform | Creates the storage account and outputs credentials |
| **Backup Logic** | Python (`backup.py`) | Compresses and uploads files to Azure |
| **Automation** | Cron | Schedules automatic backups |
