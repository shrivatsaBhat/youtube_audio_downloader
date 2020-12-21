import YT_DL 

if __name__ == "__main__":
    # download any one audio with link
    video_url = 'https://youtu.be/7WOY6gFUk5s?list=PLIO7o3VwD0X_hglBI3zHjZQW6GOJT30Vy'
    video_url = video_url('?list')
    # print(video_url)
    video_url = video_url[0]
    YT_DL.run(video_url='https://youtu.be/BLeOcCeqsfI', titile='other', artist='other')

