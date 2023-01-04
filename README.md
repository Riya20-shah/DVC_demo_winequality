create virtual env
```bash
conda create -n wineq python=3.10 -y
```
activate env 
```bash
conda activate wineq
```
created requirement.txt file

install the requirements
```bash
pip install -r requiements.txt
```
create directiorary for simple templates project structure 

download the dataset of wineuality 
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
git commit -m "First commit "
```

```bash
git remote add origin https://github.com/Riya20-shah/DVC_demo_winequality.git
```

```bash
git push -u origin master
```

when we run this command dvc will check the dvc.yaml file when we apply one by one stages
its start tracking of our data 
```bash
dvc repro      ## 
```
this command is use to check parameters of model ,  it featch the details from dvc.yml file metrics 
```bash
dvc metrics show      # 
```

this command show the difference in params ,  it featch the details from dvc.yml file metrics
```bash
dvc metrics diff      #  
```

tox commands -  
```bash
tox
```

for rebulding -
```bash
tox -r
```

pytest command 
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package commands -
python3 setup.py 
