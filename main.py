from config import site
from parser_vse_pesni import open_input_file, get_soup, find_artist, find_song_text, find_song_name, record_to_csv, \
    get_netloc_from_url

'''
 Парсер исполнителю названия песни и текста песни
 с сайта https://vse-pesni.com/
'''

if __name__ == '__main__':
    urls = open_input_file()
    k = 0
    for url in urls:
        soup = get_soup(url)
        data = []
        artist_tag = site[get_netloc_from_url(url)]['artist_tag']
        category = find_artist(soup, artist_tag)
        data.append(category)
        song_name_tag = site[get_netloc_from_url(url)]['song_name_tag']
        title = find_song_name(soup, song_name_tag)
        data.append(title)
        text_song = find_song_text(soup)
        data.append(text_song)
        record_to_csv(data)
        k+= 1
    print(f'Всего обработано {k} ссылок')








'''myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]

'''