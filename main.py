from bs4 import BeautifulSoup
import requests
fullAllAnime = []
fullAnime =[]
url = 'https://animego.org/anime'
page = requests.get(url)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")
    AllAnime = soup.findAll('div', class_='h5 font-weight-normal mb-1')
    Anime = soup.findAll('div', class_='description d-none d-sm-block')
    if AllAnime:
        for i in AllAnime:
            name = i.get_text(strip=True)
            fullAllAnime.append(name)
        if Anime:
            for i in Anime:
                opis = i.get_text(strip=True)
                fullAnime.append(opis)
for i in range(len(fullAllAnime)):
    print(str(i+1)+"."+"Название:\n"+fullAllAnime[i])
    print("\n")
    print("Описание:\n"+fullAnime[i])
    print("\n")


with open("anime.csv", mode="w", encoding='utf-8') as csvfile:
    csvfile.write('Название, Описание\n')

    for item in range(len(fullAllAnime)):
        line = f"{fullAllAnime[item]},{fullAnime[item]}\n"
        csvfile.write(line)
print()


        

