import os
import re

folder_path = "./txt"

def convert_txt_to_srt(txt_content):
    lines = txt_content.split('\n')
    srt_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        time_pattern = r'(\d{2}:\d{2}:\d{2}:\d{2}) - (\d{2}:\d{2}:\d{2}:\d{2})'

        if re.match(time_pattern, line):
            # タイムコードの行
            start_time = re.search(time_pattern, line).group(1).replace(':', ',')
            end_time = re.search(time_pattern, line).group(2).replace(':', ',')
            srt_lines.append(str(i // 2 + 1))
            srt_lines.append(f'{start_time}0 --> {end_time}0')
        elif line.strip():
            # 発話テキストの行
            srt_lines.append(line)

        i += 1

    return srt_lines

def convert_txt_to_srt_in_folder(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), 'r', encoding='utf-8') as file:
            txt_content = file.read()
        
        srt_lines = convert_txt_to_srt(txt_content)

        # .txtを.srtに変更して保存
        srt_file = os.path.splitext(txt_file)[0] + '.srt'
        with open(os.path.join(folder_path, srt_file), 'w', encoding='utf-8') as file:
            file.write('\n'.join(srt_lines))

if __name__ == '__main__':
    # binフォルダ内部
    # folder_path = os.path.join(os.path.dirname(__file__), 'txt')
    convert_txt_to_srt_in_folder(folder_path)
