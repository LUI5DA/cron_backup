# 🗄️ Backup Tool with Cron

A simple and efficient Python tool that automates the backup of specified directories or files using cron jobs.  
Backups are automatically stored in **Azure Blob Storage** for secure and scalable cloud storage.

---

## ✨ Features

- 🔹 Uploads backup data directly to **Azure Blob Storage**.  
- 🔹 Automates the backup process through **cron jobs**.  
- 🔹 Lightweight and easy to configure.  

---

## ⚙️ Setup Steps

### 0. Clone repo
```bash
git clone https://github.com/LUI5DA/cron_backup.git cron_backup
```


### 1. Set up an Azure Storage Account  
Create an Azure Storage account to store your backup files.

---

### 2. Create a Python Virtual Environment

```bash
cd cron_backup/src
```

```bash
python -m venv env
```

---

### 3. Activate the Virtual Environment
```bash
source ./env/bin/activate
```

---

### 4. Install the Required Packages
```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables
Create a `.env` file in the project directory and add your Azure credentials:

```bash
BLOB_STORAGE_STRING="your_azure_blob_storage_connection_string"
CONTAINER_NAME="your_container_name"
BLOB_NAME="your_blob_name"
```

---

### 6. Set Up a Cron Job
Edit your crontab file to define how often the backup script should run:
```bash
crontab -e
```

Add the following line to run the backup script every minute (modify the schedule as needed):
```bash
* * * * * /bin/bash -c 'cd /home/ldg4mez/Documents/cron_practices/src && /home/ldg4mez/Documents/cron_practices/src/env/bin/python backup.py backup test zip >> backup.log 2>>&1'
```

---

✅ Once configured, the script will automatically create and upload backups to your Azure Blob Storage at the defined intervals.