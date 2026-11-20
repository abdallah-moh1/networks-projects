default:
    just --choose

install:
    cd client && npm install
    cd server && pip install -r requirements.txt

dev:
    cd client && npm run build
    cd server && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run:
    cd client && npm run build
    cd server && uvicorn app.main:app --host 0.0.0.0 --port 8000
