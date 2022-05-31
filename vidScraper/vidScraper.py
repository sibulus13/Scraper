# importing the module
import pytube
from pytube import YouTube
import pandas as pd
import os.path
from os import path

# Grab playlist excel sheets
# http://www.williamsportwebdeveloper.com/FavBackUp.aspx

#  return list of video links based off downloaded Excel sheet format.


def grab_playlist_links(fPath):
    print(fPath)
    data = pd.read_html(fPath)
    video_URLs = list(data[0][1].loc[2:])
    # print(video_URLs)
    return video_URLs


# download video from url to a specified local path.
def download_playlist(path_playlist_URLs, SAVE_PATH):
    video_URLs = grab_playlist_links(path_playlist_URLs)
    for url in video_URLs:
        try:
            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download(SAVE_PATH)
        except Exception as e:
            # in case of private videos & anything else
            print(e, url)
            continue


# ensures specified folder exists.
def verify_folder_loc(fPath):
    if not path.isdir(fPath):
        os.makedirs(fPath)
    return fPath


# TODO grab list of folders v list of xls files and compare to download any new playlists
if __name__ == "__main__":
    name = "Psych_Lec_Harvard_Steven_Pinker"
    ext = '.xls'
    download_dir_main_path = r"Z:\Videos\Pytube"
    path_data_dir = r"Z:\repo\Scraper\vidScraper\playlistLists"
    playlist_files = [f for f in os.listdir(path_data_dir) if f.endswith(ext)]
    playlist_names = [f.removesuffix(ext) for f in playlist_files]
    playlist_dirs = [f for f in os.listdir(download_dir_main_path)]

    not_downloaded_playlist_names = [f for f in playlist_names if f not in playlist_dirs]    
    # print(playlist_names, playlist_dirs, not_downloaded_playlist_names)
    for playlist_file in not_downloaded_playlist_names:
        print(playlist_file)
        name = playlist_file.removesuffix(ext)
        path_playlist_URLs = rf"Z:\repo\Scraper\vidScraper\playlistLists\{name}.xls"
        SAVE_PATH = verify_folder_loc(
            fPath=os.path.join(download_dir_main_path, name))
        download_playlist(path_playlist_URLs, SAVE_PATH)
