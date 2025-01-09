import os
from yt_dlp import YoutubeDL

def download_audio_yt_dlp(video_url, output_folder):
    """
    Downloads the audio of a YouTube video using yt-dlp.
    
    Args:
        video_url (str): The URL of the YouTube video.
        output_folder (str): The directory where the audio file will be saved.
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best quality audio available
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Convert to mp3
                'preferredquality': '192',  # Set audio quality
            }],
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save with video title as file name
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Downloaded: {video_url}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

def download_playlist_audio(playlist_url, output_folder):
    """
    Downloads the audio of all videos in a YouTube playlist.
    
    Args:
        playlist_url (str): The URL of the YouTube playlist.
        output_folder (str): The directory where the audio files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        from pytube import Playlist
        playlist = Playlist(playlist_url)
        print(f"Found {len(playlist.video_urls)} videos in the playlist.")
        for video_url in playlist.video_urls:
            download_audio_yt_dlp(video_url, output_folder)
        print("All audio files downloaded!")
    except Exception as e:
        print(f"Error processing playlist: {e}")

if __name__ == "__main__":
    playlist_link = input("Enter the YouTube playlist link: ")
    output_directory = input("Enter the output folder (default is './downloads'): ") or "./downloads"
    download_playlist_audio(playlist_link, output_directory)
