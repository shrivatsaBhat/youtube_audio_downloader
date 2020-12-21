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
        # print(f'{msg}')
        pass

def OnComplete_hook(status):
    if status['status'] == 'downloading':
        print(f"{status['status']}>>> {status['_percent_str']} of file-size: {status['_total_bytes_str']}")

    if status['status'] == 'finished':
        isFinished = True
        print(f"{status['status']} downloading -> {status['filename']} \nNow converting ...")

def run(video_url='https://youtu.be/BLeOcCeqsfI'):
    ydl_opts = {
        'ignoreerrors':True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': DisplayLog(),
        'progress_hooks': [OnComplete_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except:
            pass

def fetchFromSongList(songList):
    for song in songList:
        songInfo=song['Title']
        try:
            songInfo= songInfo.split('](')
        except:
            pass
        title= songInfo[0]
        title = title[1:]

        videoUrl = songInfo[1]
        videoUrl = videoUrl[:-1]
        video_url = videoUrl.split('?list')
        video_url = video_url[0]

        artistName = song['Artiste']

        return {'title':title, 'videoUrl':videoUrl, 'artist':artistName}


def main():
    # Feth each csv file 
    songListCSVFiles = os.listdir('./songList')
    fileLocation = os.getcwd()
    downloadFileFolder = 'download'
    customPath = os.path.join(fileLocation,downloadFileFolder)

    for csvFile in songListCSVFiles:
        os.chdir(fileLocation)
        songList = getCsvData('./songList/'+csvFile)
        try:
            video_info = fetchFromSongList(songList)

            path = os.path.join(customPath, video_info['artist'].replace(" ", "_"),'etc')

            try:
                dn = os.path.dirname(path)
                try:
                    os.chdir(dn)
                except:
                    pass
                if dn and not os.path.exists(dn):
                    os.makedirs(dn)
                    os.chdir(dn)
            except (OSError, IOError) as err:
                self.report_error('unable to create directory ' + error_to_compat_str(err))

            run(video_info['videoUrl'])
            try:
                # print('changed directory')
                os.chdir(customPath)
            except:
                pass
            # print(os.getcwd()) # get current directory information

        except:
            print('failed to load ',str(songList))

if __name__ == '__main__':
    main()