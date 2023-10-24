using System;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // binフォルダ内部
        string folderPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "txt");
        ConvertTxtToSrtInFolder(folderPath);
    }

    static List<string> ConvertTxtToSrt(string txtContent)
    {
        string[] lines = txtContent.Split('\n');
        List<string> srtLines = new List<string>();

        for (int i = 0; i < lines.Length; i++)
        {
            string line = lines[i].Trim();
            string timePattern = @"(\d{2}:\d{2}:\d{2}:\d{2}) - (\d{2}:\d{2}:\d{2}:\d{2})";

            if (Regex.IsMatch(line, timePattern))
            {
                // タイムコードの行
                string startTime = Regex.Match(line, timePattern).Groups[1].Value.Replace(":", ",");
                string endTime = Regex.Match(line, timePattern).Groups[2].Value.Replace(":", ",");
                srtLines.Add($"{(i / 2) + 1}");
                srtLines.Add($"{startTime}0 --> {endTime}0");
            }
            else if (!string.IsNullOrWhiteSpace(line))
            {
                // 発話テキストの行
                srtLines.Add(line);
            }
        }

        return srtLines;
    }

    static void ConvertTxtToSrtInFolder(string folderPath)
    {
        string[] txtFiles = Directory.GetFiles(folderPath, "*.txt");

        foreach (string txtFile in txtFiles)
        {
            string txtContent = File.ReadAllText(txtFile, Encoding.UTF8);
            List<string> srtLines = ConvertTxtToSrt(txtContent);

            // .txtを.srtに変更して保存
            string srtFile = Path.ChangeExtension(txtFile, ".srt");
            File.WriteAllLines(srtFile, srtLines, Encoding.UTF8);
        }
    }
}
