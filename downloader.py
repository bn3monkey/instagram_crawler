import json
import os
import errno
import urllib.request
import os.path

file_path = "d:\Z_Non_Program_Files\STUDY\VSCode\instagram-crawler\\"

def get_filenum(image_path) : 
    count = 1
    image_num_path = image_path + "\count.txt"
    if os.path.isfile(image_num_path) : 
        f = open(image_num_path, 'r')
        data = f.read()
        count = int(data)
        f.close()

    result = count
    count += 1
    f = open(image_num_path, 'w')
    f.write(str(count))
    f.close()
    return str(result)

def make_directory(directory_path) :

    try:
        if not(os.path.isdir(directory_path)):
            os.makedirs(os.path.join(directory_path))

    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

def json_download() : 

    with open(file_path + 'output') as data_file:    
        data = json.load(data_file)
    data_file.close()

    image_tag_set = {}

    count = 0
    for image in data :
        count += 1
        print("Download Image : " + str(count))
        content = image["content"]

        splited_content = content.split(':')
        if splited_content[0] != "Image may contain" :
            continue
        tokenized_content = splited_content[1].split(',')
        for tokenized in tokenized_content :
            final_tokenized = tokenized.split('and')
            for image_tag in final_tokenized :
                image_tag = image_tag.strip()
                image_path = file_path + 'tags\\' +image_tag
                if image_tag in image_tag_set : 
                    image_tag_set[image_tag] += 1
                else :
                    image_tag_set[image_tag] = 1
                    make_directory(image_path)
                image_name = image_path + '\\' + get_filenum(image_path) + ".png"
                urllib.request.urlretrieve(image["img_url"], image_name)
                print("----------- " + image_tag +" ------------")
                print("from " + image["img_url"])
                print("to " + image_name)
                print("-----------------------------------------")


if __name__ == "__main__" :
    print("json_download")
    json_download()    
    