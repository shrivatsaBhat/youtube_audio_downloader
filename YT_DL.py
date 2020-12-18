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

def run(video_url='https://youtu.be/BLeOcCeqsfI', titile='other', artist='other'):

    filename = f"./download/{artist}/{titile}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            # ydl.download([video_info['webpage_url']])
            ydl.download([video_url])
            time.sleep(5) # Sleep for 5 seconds
            return 'success'
        except:
            print('Oops!! Something went wrong!!')
            return 'failed'

def fetchFromSongList(songList):
    for song in songList:
        songInfo=song['Title']
        songInfo= songInfo.split('](')
        title= songInfo[0]
        title = title[1:]
        videoUrl = songInfo[1]
        videoUrl = videoUrl[:-1]
        artistName = song['Artiste']
        status = run(str(videoUrl), str(title), str(artistName))
        if(status=='success'):
            pass
        elif(status == 'fail'):
            print('!!--- Sorry song '+str(title)+' from artist: '+str(artistName)+' from link: '+str(videoUrl)+' failed ---!!')
        else:
            print('Someting went wrong!!')

def main():
    # Feth each csv file 
    songListCSVFiles = os.listdir('./songList')

    for csvFile in songListCSVFiles:
        songList = getCsvData('./songList/'+csvFile)
        try:
            fetchFromSongList(songList)
        except:
            print('--- failed to load ',str(songList))

if __name__ == '__main__':
    main()