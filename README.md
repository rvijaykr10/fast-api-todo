## windows

python -m venv env
./env/Scripts/activate
deactivate

## mac

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
pip list

uvicorn main:app --reload
uvicorn main:app --reload --port 5000
