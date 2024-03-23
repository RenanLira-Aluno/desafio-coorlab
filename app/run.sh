#!/bin/bash
cd backend
pip3 install -r requirements.txt
nohup python3 -m flask --app app.py run --port 3000 --debug > log.txt 2>&1 &
echo $! > ../save_pid.txt

cd ../frontend
npm install
nohup npm run dev > log.txt 2>&1 &
echo $! >> ../save_pid.txt

echo "frontend e backend rodando em segundo plano."
echo "http://localhost:8080/"
echo "http://localhost:3000/"
echo "logs em backend/log.txt e frontend/log.txt."

echo "Para parar os processos, execute:"
echo "kill -9 cat save_pid.txt"