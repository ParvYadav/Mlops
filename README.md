conda create -n wineq python=3.8 -y
conda activate wineq
touch requirement.txt
pip install -r requirement.txt
touch README.md
python template.py
mkdir data_given