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
mkdir data_given
git init
dvc init
dvc add data_given/winequality.csv
git add .
git config --global user.email 'parvyadav2011@gmail.com'
git config --global user.name "Parv Yadav"
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ParvYadav/Mlops.git
git push -u origin main
git add . && git commit -m 'update Readme.md'
hsitory