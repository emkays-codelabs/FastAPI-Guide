# FastAPI MongoDB API 🚀

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen.svg)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple.svg)

This project is a **FastAPI-based REST API** that interacts with **MongoDB Atlas** using the **Motor** async driver. It is designed to provide a simple and efficient way to **insert and fetch data** from a MongoDB database, specifically for applications needing real-time, asynchronous interactions with their database.

The API is **built with high performance** in mind, making use of the **FastAPI framework** and **asynchronous programming** with **Motor** to allow non-blocking database operations, perfect for applications with high throughput requirements.

### Key Features:
- **Async Database Access**: Uses **Motor** (an async driver for MongoDB) for non-blocking I/O.
- **FastAPI Framework**: Ensures high performance and easy development of RESTful APIs.
- **MongoDB Atlas**: A cloud-based MongoDB solution for secure and scalable database management.
- **Swagger UI**: Automatically generated interactive documentation for your API, accessible through the `/docs` endpoint.
- **Deployment-Ready**: The app can be easily deployed on **Render** for cloud hosting.

### API Endpoints:
- **POST `/euron/insert_data`**: Insert data into the MongoDB collection.
- **GET `/get_eurondata`**: Retrieve all documents from the MongoDB collection.

### Technologies Used:
- **Python 3.11+** for fast and efficient execution.
- **FastAPI** for creating RESTful APIs with automatic validation and serialization.
- **Motor** for async interaction with MongoDB.
- **MongoDB Atlas** for cloud-based NoSQL database management.
- **Uvicorn** as the ASGI server for serving FastAPI applications.
- **python-dotenv** for managing environment variables.

This project serves as a template for building FastAPI applications connected to MongoDB, especially useful for applications requiring high-speed, non-blocking interactions with a cloud-based database. You can deploy this app to **Render** with a single click to get it running in the cloud.

---

### Project Purpose:

This project is designed to provide an easy-to-understand, practical example of a high-performance API using FastAPI and MongoDB Atlas. It is perfect for developers who are:
- Learning how to interact with MongoDB in an asynchronous environment.
- Looking to build fast, production-ready APIs with minimal overhead.
- Wanting a simple template to deploy applications to the cloud using **Render**.

### How It Works:
1. **Insert Data**: The `/euron/insert_data` endpoint allows you to insert documents into the MongoDB collection with the fields: `name`, `phone`, `city`, and `course`.
2. **Fetch Data**: The `/get_eurondata` endpoint retrieves all the documents stored in the collection.

This setup ensures that your API is **non-blocking** and **scalable**, with MongoDB Atlas handling your database at scale.

---

### Deployment:

This API is ready for deployment on **Render**, a cloud platform that automates deployment and scaling of apps. The **Render deployment button** is provided in the README for a one-click deploy experience.

---

Feel free to customize this project for your use case, integrate more endpoints, and scale it to meet your needs!

---

## 📦 Tech Stack & Dependencies

![Tech Stack](https://raw.githubusercontent.com/emkays-codelabs/FastAPI-Guide/main/assets/tech-stack.svg)

- **Python** 3.11+ 🐍  
- **FastAPI** >=0.110 ⚡  
- **Uvicorn** >=0.18 🌐  
- **Motor** >=3.3 🔄  
- **PyMongo** >=4.6 🗄️  
- **python-dotenv** >=0.19 🌱  
- **MongoDB Atlas** 🔐  
- **Render** ☁️  

---

## 📁 Project Structure

```

FastAPI-Guide/ 🚀
│
├── main.py             # 🔹 FastAPI app and API routes
├── requirements.txt    # 📦 Python dependencies
├── .gitignore          # 🚫 Files/folders to ignore in Git
├── .env.example        # 🔐 Example environment variables
├── README.md           # 📝 Project documentation
└── **pycache**/        # ⚡ Python cache files (auto-generated)

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

![Swagger UI](https://raw.githubusercontent.com/emkays-codelabs/FastAPI-Guide/main/assets/swagger-ui.png)

---

## 🌍 Deployment on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

**Steps:**

1. Push code to GitHub
2. Create a new **Web Service** on Render ☁️
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

```text
MONGODB_URI=<your-mongodb-uri>
DB_NAME=eurondb
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

## 🛠️ Troubleshooting

### ❌ SSL Handshake Fail (MongoDB Atlas)

✅ Fix:

* Ensure **Atlas IP Whitelist = 0.0.0.0/0**
* Use **Python 3.11** (recommended)
* Do **NOT** override `ssl_context`
* Connect using:

```python
AsyncIOMotorClient(MONGO_URI, tls=True)
```

### ❌ Library Version Issues

Ensure you are using compatible versions in `requirements.txt`:

```txt
fastapi>=0.110
uvicorn>=0.18
motor>=3.3
pymongo>=4.6
python-dotenv>=0.19
```

---

### 💡 Tips

* Always use `.env` for sensitive credentials 🌱
* Test locally before deploying to Render 🔄
* Use **Swagger UI** for testing your API endpoints 🔍

---

## 👨‍💻 Author
**Emkays Codelabs**
🔗 [GitHub](https://github.com/emkays-codelabs)

---
