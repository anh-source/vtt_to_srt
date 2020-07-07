import webvtt
import os
from webvtt import MalformedFileError

def filter_srt(file):
    if file[len(file) - 3:] == 'vtt':
        return file

def convert_vtt_to_srt(folder_path):
    file_list = os.listdir(folder_path)
    for i in file_list:
        if filter_srt(i) != None:
            vtt = webvtt.read(folder_path + '/{}'.format(filter_srt(i)))
            vtt.save_as_srt()
    pass
def main(path):
    folder_list = os.listdir(path)
    for i in folder_list:
        folder_path = path + '/{}'.format(i)
        try:
            convert_vtt_to_srt(folder_path)
        except MalformedFileError:
            print('invalid format')
        except NotADirectoryError:
            print("No results directory for baseline.")
    pass


if __name__ == '__main__':
    path = '/Users/apple/Desktop/.../'#path to your folder
    main(path)