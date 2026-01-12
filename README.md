Sure! Here's the updated version of your **README.md**, now including the correct **`requirements.txt`** section with the dependencies and versions you've mentioned:

---

```md
# FastAPI MongoDB API 🚀

A **FastAPI REST API** fully connected to **MongoDB Atlas** using the **async Motor driver**.  

This project allows you to **insert and fetch data** from MongoDB and is ready for **cloud deployment on Render**.

---

## 📦 Tech Stack & Libraries

- **Python** 3.11+ 🐍  
- **FastAPI** 🚀 – Web framework  
- **Motor** 🔄 – Async MongoDB driver (built on **pymongo**)  
- **Pymongo** 🔐 – Synchronous MongoDB support (used by Motor internally)  
- **Uvicorn** ⚡ – ASGI server  
- **python-dotenv** 🌱 – Load environment variables from `.env`  
- **MongoDB Atlas** 💾 – Cloud database  

---

## 📁 Project Structure

```

FastAPI-Guide/
│
├── main.py                # FastAPI app & routes
├── requirements.txt       # Python dependencies
├── .gitignore
├── .env.example           # Template for environment variables
├── README.md              # This file

````

---

## ⚙️ Environment Variables

Create a `.env` file in your project root:

```env
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/eurondb?retryWrites=true&w=majority
DB_NAME=eurondb
````

> 🚫 **Do not commit `.env` to GitHub.**

---

## 🚀 Local Setup (Beginner-Friendly)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/emkays-codelabs/FastAPI-Guide.git
cd FastAPI-Guide
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API

```bash
uvicorn main:app --reload
```

### 5️⃣ Access Swagger UI

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

## 💻 API Endpoints

### ➕ Insert Data

`POST /euron/insert_data`

**Request JSON**:

```json
{
  "name": "John",
  "phone": 9876543210,
  "city": "Delhi",
  "course": "FastAPI"
}
```

### 📄 Fetch All Data

`GET /get_eurondata`

**Response**:

```json
[
  {
    "id": "642f1e3b8e1f1234abcd5678",
    "name": "John",
    "phone": 9876543210,
    "city": "Delhi",
    "course": "FastAPI"
  }
]
```

---

## ☁️ Deployment on Render

1. Push code to GitHub
2. Create a **New Web Service** on Render ☁️
3. Connect your repository
4. Set **Build Command**:

```bash
pip install -r requirements.txt
```

5. Set **Start Command**:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

6. Add Environment Variables on Render:

* `MONGODB_URI`
* `DB_NAME`

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

---

## 🛠️ Troubleshooting

### ❌ SSL Handshake Failed (MongoDB Atlas)

* Ensure Atlas **IP Whitelist = 0.0.0.0/0**
* Use **Python 3.11** (Render default)
* Do **NOT** use `ssl_context`
* Connect like this:

```python
AsyncIOMotorClient(MONGO_URI, tls=True)
```

### ❌ Motor Version Error

Ensure you are using compatible versions:

### `requirements.txt` Example

For your `requirements.txt`, here is the correct version constraints:
```
fastapi>=0.110
uvicorn>=0.18
motor>=3.3
pymongo>=4.6
python-dotenv>=0.19
```

### 💡 Tips

* Always use `.env` for sensitive credentials 🌱
* Test locally before deploying to Render 🔄
* Use **Swagger UI** for testing your API endpoints 🔍

---

## 👨‍💻 Author

**Emkays Codelabs**
🔗 [GitHub](https://github.com/emkays-codelabs)



