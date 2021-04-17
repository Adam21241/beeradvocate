# beeradvocate


How to set up project locally:

1) make sure you have python 3.9 and conda installed (depends on your OS)

2) clone repo:
git clone https://github.com/adam21241/beeradvocate.git

3) create conda virtualenv:
conda create -n beeradvocate python=3.9

4) install packages from requirements:
conda install --file requirements.txt

5) activate conda virtualenv:
conda activate beeradvocate


Other helpful commands:

1) install some package:
conda install pandas

2) update some package:
conda update pandas

3) create requirements file:
conda list --export > requirements.txt

4) show all conda virtualenvs:
conda env list

5) deactivate conda virtualenv:
conda deactivate
