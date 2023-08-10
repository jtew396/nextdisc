This project is designed to take the data from innovadiscs.com and spit out the disc that is MOST DIFFERENT from the discs I currently have in my bag.
In 2D space this means finding the disc that falls (maybe on the fairway) furthest from the next closest disc in my bag.
In 4D space this means finding the disc that flies (flight path in the air) furthest from the next closest disc in my bag.
Results from each of the 2D and 4D scripts give the first and second most different disc(s) with their attributes.


The discs I currently have are hardcoded in each of the python files. They are the Aviar, Shark, Leopard, Mamba and Destoyer.


rawdiscdata.csv contains the raw data from innovadiscs.com/disc-golf-discs/disc-comparison/


findnextdisc2d.py takes the 4 attributes from the raw data and combines them into a 2D matrix.
The first 2 and last 2 attributes are combined to judge where a disc will fall in 2D space.
[Speed + Glide, Turn + Fade]
Each disc is given a 2D matrix that is then compared to the discs I currently own to see how far away it would fall from the next closest disc in my bag.


findnextdisc4d.py takes the 4 attributes from the raw data and directly compares these to the discs I have in my bag to find the disc that has a flight path most different from the next closest disc in my bag.
[Speed, Glide, Turn, Fade]


CURRENT RESULTS

2D

Your next disc(s) is/are ['MAX'] with a max difference of 6.0 points.
MAX: ['11', '3', '0', '5']

The next most different disc(s) is/are ['TEEREX', 'STARFIRE', 'INVICTUS', 'SIDEWINDER', 'ROADRUNNER', 'ARCHANGEL', 'RHYNOX'] with a max difference of 4.0 points.
TEEREX: ['11', '4', '0', '4']
STARFIRE: ['10', '4', '0', '3']
INVICTUS: ['10', '4', '0', '3']
SIDEWINDER: ['9', '5', '-3', '1']
ROADRUNNER: ['9', '5', '-4', '1']
ARCHANGEL: ['8', '6', '-4', '1']
RHYNOX: ['2', '1', '0', '4']


4D

Your next disc(s) is/are ['SONIC'] with a max difference of 4.0 points.
SONIC: ['1', '2', '-4', '0']

The next most different disc(s) is/are ['MONSTER', 'SIDEWINDER', 'ROADRUNNER', 'FIREBIRD', 'ARCHANGEL', 'WHIPPET', 'VIPER', 'GATOR', 'MIRAGE', 'BULLFROG', 'RHYNOX', 'BIRDIE'] with a max difference of 3.0 points.
MONSTER: ['10', '3', '0', '5']
SIDEWINDER: ['9', '5', '-3', '1']
ROADRUNNER: ['9', '5', '-4', '1']
FIREBIRD: ['9', '3', '0', '4']
ARCHANGEL: ['8', '6', '-4', '1']
WHIPPET: ['6', '3', '1', '5']
VIPER: ['6', '4', '1', '5']
GATOR: ['5', '2', '0', '4']
MIRAGE: ['3', '4', '-3', '0']
BULLFROG: ['3', '1', '0', '1']
RHYNOX: ['2', '1', '0', '4']
BIRDIE: ['1', '2', '0', '0']
