from __future__ import unicode_literals
import os
import time
try:
    import csv
except :
    print('!!---import csv failed---!!')
try:
    import json
except :
    print('!!---import json failed---!!')
try:
    import youtube_dl
except:
    print('!!---Install Youtube Dlownload Library---!!')
    print('--running pip install youtube_dl')
    os.system('pip install youtube_dl')
    print('--installed youtube downloader')
    import youtube_dl

def getCsvData(csvFile):
    # Fetch song information from csv file
    with open(csvFile, 'r') as file:
        csv_file = csv.DictReader(file)
        csvFileContent = []
        for row in csv_file:
            csvFileContent.append(dict(row))
        return csvFileContent

class DisplayLog(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(f'{msg}')

isFinished = False

def OnComplete_hook(status):
    if status['status'] == 'finished':
        isFinished = True
        print(f"{status['status']} downloading -> {status['filename']}\nNow converting ...")

def run(video_url='https://youtu.be/BLeOcCeqsfI', title='unknown', artist='other'):
    filename = f"./download/{artist}/{title}.mp3"
    ydl_opts = {
        'format': 'bestaudio/best',
        # 'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': DisplayLog(),
        'progress_hooks': [OnComplete_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def fetchFromSongList(songList):
    for song in songList:
        songInfo=song['Title']
        songInfo= songInfo.split('](')
        title= songInfo[0]
        title = title[1:]

        videoUrl = songInfo[1]
        videoUrl = videoUrl[:-1]

        artistName = song['Artiste']

        return {'title':title, 'videoUrl':videoUrl, 'artist':artistName}


def main():
    global isFinished
    # Feth each csv file 
    songListCSVFiles = os.listdir('./songList')

    for csvFile in songListCSVFiles:
        isFinished = False
        songList = getCsvData('./songList/'+csvFile)
        try:
            video_info = fetchFromSongList(songList)
            os.chdir(f"./download/{video_info['artist']}")
            run(video_info['videoUrl'], video_info['title'], video_info['artist'])
            os.chdir(f"./download")
            print('***')
        except:
            print('failed to load ',str(songList))

if __name__ == '__main__':
    main()