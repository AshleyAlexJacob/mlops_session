1. python -m venv .venv/
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. Download Dataset
https://shorturl.at/9vhVM
mlflow server --backend-store-uri ./mlruns

docker build -t predict:latest .
docker run -p 8000:8000 prediction:latest

#### Jenkins Pipeline
1. Pipeline configured
