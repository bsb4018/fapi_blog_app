Create Environment
```
conda create -p venv python=3.8 -y
```

Activate Environment
```
conda activate venv/
```

Install the requirements
```
pip install -r requirements.txt
```

Start the application
```
uvicorn main:app --reload
```

Swagger UI
```
http://localhost:8000/docs
```

Redoc
```
http://localhost:8000/redoc
```

Start the blog application
```
uvicorn blog.main:app --reload
```

