default:
    just --choose

install:
    cd client && npm install
    cd server && pip install -r requirements.txt

dev:
    cd client && npm run build
    cd server && python -m app.main

run:
    cd client && npm run build
    cd server && python -m app.main --prod
