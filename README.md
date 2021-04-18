# beeradvocate


**How to set up project locally:**

1) make sure you have python 3.9 and conda installed (depends on your OS)

2) clone repo:
git clone https://github.com/adam21241/beeradvocate.git

3) download dataset (into root of the project) from:
https://data.world/socialmediadata/beeradvocate/

4) create conda virtualenv:
conda create -n beeradvocate python=3.9

5) activate conda virtualenv:
conda activate beeradvocate

6) install packages from requirements:
conda install --file requirements.txt
</br>

**Other helpful commands:**

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
</br>

**In this project I wanted to provide an answer for the following questions:**

1. Which brewery produces the strongest beers by abv ? (answer in data_exploration.ipynb)

2. If you had to pick 3 beers to recommend to someone, how would you approach the problem ? (answer in beer_recommendation.ipynb)

3. What are the factors that impacts the quality of beer the most ? (answer in data_exploration.ipynb)

4. I enjoy a beer which aroma and appearance matches the beer style. What beer should I buy ? (proposal of answer in issue #5)
