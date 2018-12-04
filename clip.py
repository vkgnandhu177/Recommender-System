import os
import json
import string
import random
import subprocess
import multiprocessing


save_dir = '/'
# importing required modules
from zipfile import ZipFile
 
# specifying the zip file name
file_name = "clipvideos.zip"
 
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
 
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')

start_time = time.time()
filename = "data/video_datafile"
fileObject = open(filename,'r')
lst = pickle.load(fileObject)
print("--- %s seconds ---" % (time.time() - start_time))
print 

df_video = pd.DataFrame(lst)
df_video

filename = "data/channels_datafile"
fileObject = open(filename,'r')
lst = pickle.load(fileObject)

df_channel = pd.DataFrame(lst)
df_channel

df_new = pd.concat([df_video,df_category],axis=1,join="inner")
df_new

df_new.columns

df_new["description_length"] = df_new.description.apply(lambda x : len(x.split(" ")))

def find_http(lst):
    return len([1 for i in lst if 'http' in i])
    
df_new["http_in_descp"] = df_new.description.apply(lambda x : find_http(x.split(" ")))

def tag_in_desc(df):
    
    if df.tags != None :
        a = [x.lower() for x in df.tags]
        b = df.description.lower()
        return len([i for i in a if i in b])
    else:
        return 0
df_new["tags_in_desc"] = df_new.apply(tag_in_desc,axis=1)

df_new["video_title_length"] = df_new.title.apply(lambda x : len(x.split(" ")))

def videos_in_title(df):
    if df.tags != None :
        a = [x.lower() for x in df.tags]
        b = df.title.lower()
        return len([i for i in a if i in b])
    else:
        return 0
df_new["videos_in_title"] = df_new.apply(tag_in_desc,axis=1)

def len_video(x):
    if x ==None:
        return 0
    else:
        return len(x)
df_new["No_of_videos"] = df_new.videos.apply(lambda x : len_videos(x))

df_new["video_title_length"] = df_new.videoTitle.apply(lambda x : len(x.split(" ")))

df_new["video_description_length"] = df_new.VideoDescription.apply(lambda x : len(x.split(" ")))

df_new = df_new.drop(['funny, devotional, Shayari, Songs, Motivational, Ugc, wishes'],axis=1)

df_new

df_new.to_csv("dataset/clipdata.csv",header=True,index=False)

df_new = pd.read_csv("dataset/clipdata.csv")

df_new["viewCount/category_video"] = df_new.apply(lambda x: (x["viewCount"])/x["category_video"],axis=1)

df_new["viewCount/video_length"] = df_new.apply(lambda x: (x["viewCount"])/x["video_length"],axis=1)

df_new["viewCount/http_in_descp"] = df_new.apply(lambda x: (x["viewCount"]+1)/(x["http_in_descp"]+1),axis=1)

df_new["viewCount/NoOfvideos"] = df_new.apply(lambda x: (x["viewCount"]+1)/(x["No_of_videos"]+1),axis=1)

df_new["subscriberCount/videoCount"] = df_new.apply(lambda x: (x["wid_video"]+1)/(x["category_video"]+1),axis=1)

df_new["categoryViewCount/categoryVideoCount"] = df_new.apply(lambda x:( x["category_ViewCount"]+1)/(x["category_videoCount"]+1),axis=1)

df_new.columns

final_features = ['funny, devotional, Shayari, Songs, Motivational, Ugc, wishes'
       u'viewCount', 'commentCount', 'viewCount/category_length', 'viewCount/video_length',
       'viewCount/http_in_descp', 'subscriberCount/videoCount', 'CategoryViewCount/CategoryVideoCount']

df_final = df_new[final_features]

df_final.describe()

df_final.to_csv("dataset/clipdata_final.csv",header=True,index=False)
