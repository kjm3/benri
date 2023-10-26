import os

def format_srt(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.srt'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()

            formatted_lines = []
            entry = []
            for line in lines:
                line = line.strip()
                if not line:
                    if entry:
                        formatted_lines.append('\n'.join(entry))
                        entry = []
                else:
                    entry.append(line)

            if entry:
                formatted_lines.append('\n'.join(entry))

            with open(output_file, 'w', encoding='utf-8') as f:
                for i, entry in enumerate(formatted_lines):
                    if i % 3 == 2:
                        # テキスト部分の改行を削除
                        entry = entry.replace('\n', ' ')
                    f.write
