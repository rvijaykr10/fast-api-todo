## windows

# bash

python -m venv env
./env/Scripts/activate
deactivate

pip install -r requirements.txt
pip list

uvicorn main:app --reload
uvicorn main:app --reload --port 5000
