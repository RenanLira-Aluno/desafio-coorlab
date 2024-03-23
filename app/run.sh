#!/bin/bash
cd backend
pip3 install -r requirements.txt
nohup python3 -m flask --app app.py run --port 3000 --debug > log.txt 2>&1 &

cd ../frontend
npm install
nohup npm run dev > log.txt 2>&1 &