import os
import csv
from moviepy.editor import VideoFileClip

# 対象のフォルダ
target_folder = "./mov"

# 出力するCSVファイル名
output_csv = "output.csv"

# フォルダ内の動画ファイルを取得
videos = [f for f in os.listdir(target_folder) if f.endswith('.mp4')]

# CSV出力のためのリスト
output_data = [['動画ファイル名', '分数']]

# 動画の時間を取得してリストに追加
for video in videos:
    video_path = os.path.join(target_folder, video)
    clip = VideoFileClip(video_path)
    duration = int(clip.duration) // 60 + (1 if int(clip.duration) % 60 > 30 else 0)
    output_data.append([video, duration])

# CSVに出力
with open(output_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

print(f"CSVファイル {output_csv} への出力が完了しました。")
