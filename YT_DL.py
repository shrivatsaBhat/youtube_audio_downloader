
# import os
# try:
#     import youtube_dl
# except:
#     os.system('pip install youtube_dl')
#     import youtube_dl
        
# import csv
# import json
# with open("C:\\Users\\shriv\Desktop\\tableconvert_csv_0ht0ew.csv", 'r') as file:
#     # reader = csv.reader(file)
#     # print(reader)
#     # for row in reader:

#     #     # row = row.split('(')
#     #     print(row)
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         j = dict(row)
#         print(j['Title'])
        


# def run(link):
#     # Ask the user for the video they want to download
#     # video_url = 'https://youtu.be/uKHlnmepnNA'
#     video_url=link
#     # Download and convert to mp3 and store in downloads folder
#     video_info = youtube_dl.YoutubeDL().extract_info(
#         url=video_url, download=False
#     )
#     filename = f"{video_info['title']}.mp3"
#     options = {
#         'format': 'bestaudio/best',
#         'keepvideo': False,
#         'outtmpl': filename,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }]
#     }
#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])


# if __name__ == '__main__':
# 	links=['https://youtu.be/uKHlnmepnNA','https://youtu.be/lG1y7x_W-kQ']
# 	for i in range(len(links)):
# 		print(links[i])
# 	for i in range(len(links)):
# 		run(links[i])

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

    # Download and convert to mp3 and store in downloads folder
    # try:
    #     video_info = youtube_dl.YoutubeDL().extract_info(
    #     url=video_url, download=False)
    # except:
    #     return 'failed'

    # filename = f"./DOWNLOADED/{artist}/{video_info['title']}.mp3"
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
            time.sleep(3) # Sleep for 3 seconds
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
            print('--failed to load '+songList)

if __name__ == '__main__':
    main()