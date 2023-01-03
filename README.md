create virtual env
'''bash
conda create -n wineq python=3.10 -y
'''
activate env 
'''bash
conda activate wineq
'''
created requirement.txt file

install the requirements
'''bash
pip install -r requiements.txt
'''
create directiorary for simple templates project structure 

download the dataset of wineuality 
'''bash
git init
'''

'''bash
dvc init
'''

'''bash
dvc add data_given/winequality.csv
'''

'''bash
git add .
'''
'''bash
git commit -m "First commit "
'''

'''bash
git remote add origin https://github.com/Riya20-shah/DVC_demo_winequality.git
'''

'''bash
git push -u origin master
'''


'''bash
dvc repro      ##when we run this command dvc will check the dvc.yaml file when we apply one by one stages 
'''

'''bash
dvc metrics show      # this command is use to check parameters of model ,  it featch the details from dvc.yml file metrics 
'''


'''bash
dvc metrics diff      # this command show the difference in params ,  it featch the details from dvc.yml file metrics 
'''
