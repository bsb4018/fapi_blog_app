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


