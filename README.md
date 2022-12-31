create virtual env
'''bash
conda create -n wineq python=3.10 -y

activate env 
'''bash
conda activate wineq

created requirement.txt file

install the requirements
'''bash
pip install -r requiements.txt

create directiorary for simple templates project structure 

download the dataset of wineuality 

git init

dvc init

dvc add data_given/winequality.csv

git add .
git commit -m "First commit "
