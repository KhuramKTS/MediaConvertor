print("Media Convertor - Build By @KhuramKTS")
import subprocess

input_file = input("Enter the name of a video file with path: ")
output_file = input_file.split(".")[0] + ".mp3"

subprocess.run(["ffmpeg", "-i", input_file, output_file])
print("File converted successfully to: " + output_file)

print("Media Convertor - Build By @KhuramKTS")
input("Press any key to exit...")
