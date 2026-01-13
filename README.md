
---

````markdown
# 🚀 FastAPI MongoDB API

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen.svg)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple.svg)
![AsyncIO](https://img.shields.io/badge/AsyncIO-supported-blue.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-BaseModel-yellow.svg)
![dotenv](https://img.shields.io/badge/python--dotenv-green.svg)

This project is a **FastAPI-based REST API** that interacts with **MongoDB Atlas** using the **Motor async driver**.  
It provides a simple and efficient way to **insert, fetch, update, and delete data** asynchronously.

The API leverages **FastAPI**, **asyncio**, and **Motor** for **non-blocking, high-performance operations**, perfect for real-time applications.

---

## 🌟 Key Features

- 🔄 **Async Database Access** with Motor for non-blocking I/O  
- ⚡ **FastAPI Framework** for high-performance REST APIs  
- 🔐 **MongoDB Atlas** for secure, scalable cloud database  
- 📄 **Swagger UI** for interactive API docs (`/docs`)  
- ☁️ **Deployment-ready** for **Render**  
- 🗂️ Supports **CRUD operations**: create, read, full/partial update, delete  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/emkays-codelabs/FastAPI-Guide.git
cd FastAPI-Guide
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file:
```env
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/eurondb?retryWrites=true&w=majority
DB_NAME=eurondb
```
> 🚫 **Do not commit `.env` to GitHub.**

---

## 🖥️ Run the API Locally
```bash
uvicorn main:app --reload
```

* Open **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
* Check API status: `GET /`

---

## 🌐 API Endpoints

| #  | Method | Endpoint                  | Description                |
| -- | ------ | ------------------------- | -------------------------- |
| 7a | GET    | `/`                       | Health check               |
| 7b | GET    | `/get_eurondata`          | Fetch all records          |
| 7c | POST   | `/euron/insert_data`      | Insert new record          |
| 7d | PUT    | `/euron/update_data/{id}` | Full update of a record    |
| 7e | PATCH  | `/euron/patch_data/{id}`  | Partial update of a record |
| 7f | DELETE | `/euron/delete_data/{id}` | Delete a record            |

---

### Example: Insert Data
```json
POST /euron/insert_data
{
  "name": "John",
  "phone": 9876543210,
  "city": "Delhi",
  "course": "FastAPI"
}
```

**Response**
```json
{
  "status": "success",
  "message": "Record inserted successfully",
  "id": "642f1e3b8e1f1234abcd5678"
}
```

---

## 🗃️ MongoDB Collection Structure

| Field  | Type     | Description       |
| ------ | -------- | ----------------- |
| `_id`  | ObjectId | MongoDB unique ID |
| name   | string   | Name of the user  |
| phone  | int      | Phone number      |
| city   | string   | City              |
| course | string   | Course enrolled   |

> `_id` is converted to `id` in API responses for JSON compatibility.

**Visual MongoDB Structure (ASCII Placeholder)**
```
MongoDB Collection: euron_coll
┌──────────────┬──────────┬----------------------┐
│ Field        │ Type     │ Description          │
├──────────────┼──────────┼----------------------┤
│ _id          │ ObjectId │ MongoDB unique ID    │
│ name         │ String   │ Name of the user     │
│ phone        │ Int      │ Phone number         │
│ city         │ String   │ City                 │
│ course       │ String   │ Course enrolled      │
└──────────────┴──────────┴----------------------┘
API Response Example: { "id": "...", "name": "John", "phone": 9876543210, ... }
```

---

## 🔄 CRUD Workflow (ASCII Placeholder)

```
         Client 💻
           |
    ----------------
    | GET / POST   |
    ----------------
           |
         FastAPI ⚡
           |
  --------------------
  | Endpoint Logic   |
  | (Insert / Find)  |
  --------------------
           |
       MongoDB 🗄️
     (euron_coll)
           |
     ----------------
     | Response JSON 📄 |
     ----------------
```

---

## ☁️ Deployment on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

**Steps:**
1. Push code to GitHub  
2. Create a **Web Service** on Render ☁️  
3. Connect repository  
4. Set **Build Command**:  
```bash
pip install -r requirements.txt
```  
5. Set **Start Command**:  
```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```  
6. Add Environment Variables on Render:  
```text
MONGODB_URI=<your-mongodb-uri>
DB_NAME=eurondb
```

---

## 💡 Tips & Best Practices

- Use `.env` for credentials 🌱  
- Test locally before deploying 🔄  
- Always check **Swagger UI** for endpoint testing 🔍  
- Follow CRUD order: GET → POST → PUT → PATCH → DELETE  

---

## 👨‍💻 Author

**Emkays Codelabs**  
🔗 [GitHub](https://github.com/emkays-codelabs)
````

---


