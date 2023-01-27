print("Media Convertor - Build By @KhuramKTS")
import subprocess
try:
    input_file = input("Enter the name of a media file with path: ")

    output_format = input("Enter the desired format for the output file (e.g. mp3, wav, etc.): ")
    output_file = input_file.split(".")[0] + "." + output_format

    subprocess.run(["ffmpeg", "-i", input_file, output_file])
    print("File converted successfully to: " + output_file)

except Exception as e:
    print(e)

print("Media Convertor - Build By @KhuramKTS")
input("Press any key to exit...")
