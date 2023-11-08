import os

def format_srt(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.srt'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(output_file, 'w', encoding='utf-8') as f_out:
                buffer = []
                for line in lines:
                    if line.strip().isdigit():
                        if buffer:
                            f_out.write(''.join(buffer) + '\n\n')
                            buffer = []
                    buffer.append(line)
                if buffer:
                    f_out.write(''.join(buffer) + '\n\n')

format_srt('./srt', './srt_formatted')
