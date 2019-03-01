import downloader
import crawler
import os

whole_file_path = "d:\Z_Non_Program_Files\STUDY\VSCode\instagram-crawler\\"

f = open(whole_file_path + "wordset.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    
    print("in meta.py : " + line)

    cmd_crawler = "python " + whole_file_path + "crawler.py hashtag -t " + line + "-o ./output"
    cmd_downloader = "python " + whole_file_path + "downloader.py"
    os.system(cmd_crawler)
    print("json_download")
    downloader.json_download()

f.close()

