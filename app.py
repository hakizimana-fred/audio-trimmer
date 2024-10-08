from pydub import AudioSegment
import os

def trim_mp3(input_file, output_file, start_time, end_time):
    """
    Trim an MP3 file and export the trimmed part.
    
    :param input_file: Path to the input MP3 file
    :param output_file: Path to save the trimmed MP3 file
    :param start_time: Start time in milliseconds
    :param end_time: End time in milliseconds
    """
    audio = AudioSegment.from_mp3(input_file)
    trimmed_audio = audio[start_time:end_time]
    trimmed_audio.export(output_file, format="mp3")

def main():
    input_file = input("Enter the path to the input MP3 file: ")
    
    if not os.path.exists(input_file):
        print("Error: The input file does not exist.")
        return

    while True:
        start_time = int(input("Enter start time in milliseconds: "))
        end_time = int(input("Enter end time in milliseconds: "))
        
        if start_time >= end_time:
            print("Error: Start time must be less than end time.")
            continue
        
        output_file = input("Enter the path for the output MP3 file: ")
        
        trim_mp3(input_file, output_file, start_time, end_time)
        print(f"Trimmed audio saved to {output_file}")
        
        another = input("Do you want to trim another part? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()