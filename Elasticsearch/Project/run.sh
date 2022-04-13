pkill -f "5050"
nohup python3 app.py -a 5050 &
python3 testCase.py
