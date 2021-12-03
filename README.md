```bash
conda create -n wineq python=3.8 -y
```
```bash
conda activate wineq
```
```bash
touch requirement.txt
```
```bash
pip install -r requirement.txt
```
```bash
touch README.md
```
```bash
python template.py
```
```bash
mkdir data_given
```
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git config --global user.email 'parvyadav2011@gmail.com'
```
```bash
git config --global user.name "Parv Yadav"
```
```bash
git commit -m "first commit"
```
```bash
git branch -M main
```
```bash
git add set-url origin https://github.com/ParvYadav/Mlops.git
git remote set-url origin https://github.com/ParvYadav/Mlops.git
git config credential.helper store
git push https://github.com/ParvYadav/Mlops.git
```
```bash
git push -u origin main
```
```bash
git add . && git commit -m 'update Readme.md'
```
```bash
history
```
```bash
touch src/get_data.py
```
```bash
touch src/load_data.py
```
``` bash
dvc repro
```
To see the metrics of the model
dvc metrics show

to compare metrics old and the new one

dvc metrics diff

after creating setup.py

pip install -e .

to create our own pip wheel
python setup.py sdist bdist_wheel

cp saved_models/model.joblib prediction_service/model

python app.py
