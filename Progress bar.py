from tqdm import tqdm
from time import sleep
for char in tqdm(range(50), colour='green', ncols=100):
    sleep(0.25)
text= 'I love learning Python'
print(text)
