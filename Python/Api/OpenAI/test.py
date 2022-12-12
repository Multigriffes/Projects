from bs4 import BeautifulSoup
import requests

def get_lyrics(song_title):
  # Replace spaces in the song title with "+" for the query string
  query_string = song_title.replace(" ", "+")

  # Use requests to search for the song on a lyrics website
  response = requests.get(f"https://genius.com/{query_string}")
  html = response.text

  # Use BeautifulSoup to extract the lyrics from the page
  soup = BeautifulSoup(html, "html.parser")
  lyrics = soup.find('pre', {'id': 'lyric-body-text'}).text
  return lyrics

if __name__ == '__main__':
  song_title = input('Enter a song title: ')
  lyrics = get_lyrics(song_title)
  print(lyrics)
