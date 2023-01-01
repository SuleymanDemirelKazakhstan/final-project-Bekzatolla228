import glob
import pandas as pd
import re
from bs4 import BeautifulSoup
my_array = [[]]
i = 0
for file in glob.glob("messages_part2/messages/inbox/**/*.html"):
    t = open(file, 'r')
    soup = BeautifulSoup(t, features="html.parser")
    for script in soup(["script", "style", "head", "table"]):
        script.extract()
    for scores in soup.find_all(text=re.compile('Suleyman Demirel University 🇰🇿')):
        div = scores.parent.parent
        div.extract()
    for div in soup.find_all("div", {'class':'_3-94'}):
        div.decompose()
    for div in soup.find_all("div", {'class':'_2pim'}):
        div.decompose()
    for div in soup.find_all("div", {'class':'_3-8y'}):
        div.decompose()
    text = soup.get_text(separator=u' ')
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = re.sub(r"https?://[^,\s]+,?", " ", text)
    text = re.sub(r'[^\w\s]',' ', text)
    if(text != ""):
        my_array.append([text, "Type"])

my_df = pd.DataFrame(my_array)
my_df.to_csv('C_01.csv', header=["Date", "Type"], index = False)