# import cv2
# import os
# import matplotlib.pyplot as plt
# from tqdm import tqdm
#
#
# def get_video_duration(video_path):
#     cap = cv2.VideoCapture(video_path)
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     duration = frame_count / fps
#     cap.release()
#     return duration
#
#
# def process_lrs2_dataset(dataset_path):
#     video_durations = {}
#
#     for speaker_folder in tqdm(os.listdir(dataset_path)):
#         speaker_path = os.path.join(dataset_path, speaker_folder)
#         if os.path.isdir(speaker_path):
#             for video_filename in os.listdir(speaker_path):
#                 video_path = os.path.join(speaker_path, video_filename)
#
#                 # 仅处理包含 "mouth" 的视频文件
#                 if os.path.isfile(video_path) and video_filename.endswith(".mp4") and "mouth" in video_filename:
#                     # 使用说话人的文件夹名称和视频文件名作为唯一标识
#                     unique_identifier = f"{speaker_folder}_{video_filename}"
#                     duration = get_video_duration(video_path)
#                     video_durations[unique_identifier] = duration
#
#     return video_durations
#
#
# # 指定LRS2数据集的根目录
# # lrs2_dataset_path = '/media/se/902C4B8E2C4B6E72/AVEC-master/datasets/LRS2/mvlrs_v1/main'
# lrs2_dataset_path = '/media/se/902C4B8E2C4B6E72/AVEC-master/datasets/LRS3/trainval'
# durations = process_lrs2_dataset(lrs2_dataset_path)
#
# # 绘制时长信息的条形图
# video_identifiers = list(durations.keys())
# durations_values = list(durations.values())
#
# plt.figure(figsize=(10, 6))
# plt.bar(video_identifiers, durations_values, color='blue')
# plt.xlabel('Video Identifier')
# plt.ylabel('Duration (seconds)')
# plt.title('LRS3 Dataset Video Durations (Only "mouth" videos)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()


import cv2
import os
import matplotlib.pyplot as plt
from tqdm import tqdm


def get_video_duration(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    cap.release()
    return duration


def categorize_duration(duration):
    if duration < 2.0:
        return "Less than 2 seconds"
    elif 2.0 <= duration <= 4.0:
        return "2-4 seconds"
    else:
        return "More than 4 seconds"


def process_lrs2_dataset(dataset_path):
    duration_categories = {"Less than 2 seconds": 0, "2-4 seconds": 0, "More than 4 seconds": 0}

    for speaker_folder in tqdm(os.listdir(dataset_path)):
        speaker_path = os.path.join(dataset_path, speaker_folder)
        if os.path.isdir(speaker_path):
            for video_filename in os.listdir(speaker_path):
                video_path = os.path.join(speaker_path, video_filename)

                # 仅处理包含 "mouth" 的视频文件
                if os.path.isfile(video_path) and video_filename.endswith(".mp4") and "mouth" in video_filename:
                    duration = get_video_duration(video_path)
                    category = categorize_duration(duration)
                    duration_categories[category] += 1

    return duration_categories


# 指定LRS2数据集的根目录
lrs2_dataset_path = '/media/se/902C4B8E2C4B6E72/AVEC-master/datasets/LRS3/test'
categories_count = process_lrs2_dataset(lrs2_dataset_path)

# 绘制时长类别的条形图
categories = list(categories_count.keys())
counts = list(categories_count.values())

plt.figure(figsize=(8, 5))
plt.bar(categories, counts, color='green')
plt.xlabel('Video Duration Category')
plt.ylabel('Number of Videos')
plt.title('LRS3 Dataset Video Duration Categories (Only "mouth" videos)')
plt.tight_layout()
plt.show()
