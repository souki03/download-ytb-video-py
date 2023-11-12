from pytube import YouTube

def download_youtube_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Téléchargement terminé avec succès !")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

if __name__ == "__main__":
    video_url = input("Entrez le lien de la vidéo YouTube que vous souhaitez télécharger : ")
    output_path = input("Entrez le chemin où vous souhaitez enregistrer la vidéo (par exemple, 'C:/Videos/') : ")
    download_youtube_video(video_url, output_path)
