import pyaudio
import wave
import sys

# Parameters for recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1             # Number of audio channels (1 for mono)
RATE = 44100             # Sampling rate (44.1kHz)
CHUNK = 1024             # Chunk size (number of audio frames per buffer)
RECORD_SECONDS = 1000      # Duration of the recording (in seconds)
WAVE_OUTPUT_FILENAME = "output.wav"  # Output filename

def record_audio():
    audio = pyaudio.PyAudio()

    try:
        # Start recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print("Recording...")
        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Recording finished")

    except KeyboardInterrupt:
        print("\nRecording interrupted by user")
    finally:
        # Stop recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio to a WAV file
        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    record_audio()
