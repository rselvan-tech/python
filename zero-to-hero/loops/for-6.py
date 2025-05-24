names=['ram','aadhavan','manu','balarama','seetha','krish','vel','yaksha']

import random

for i in range(3):
    print(f'Winnner of the round {i} ...')
    winner=random.choice(names)
    print(winner)
    print('##############')
    names.remove(winner)
print('END') 