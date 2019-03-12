cd /var/task

pip install --upgrade pip
pip install numpy --target .

pip freeze > requirements.txt
