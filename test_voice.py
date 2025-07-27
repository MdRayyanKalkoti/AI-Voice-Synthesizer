#Check what voices has been installed from your PC ( To download go to Settings -> Time -> languages & period )

"""
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(f"Voice: {voice.name} - ID: {voice.id}")
    """

# Test Code input voice ( select from output )


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Print all voices to know what's available
for index, voice in enumerate(voices):
    print(f"{index}. {voice.name} - ID: {voice.id}")

# Pick a specific voice (e.g., female voice like Zira, or male like David)
# You can also manually test different index numbers (0, 1, 2, ...)
selected_voice = voices[0]  # change this index based on printed output

# Set the selected voice
engine.setProperty('voice', selected_voice.id)

# Confirm the selected voice is set (optional debug print)
print(f"\n✅ Using voice: {selected_voice.name}")

# Speak a test line
engine.say("This is a test using the selected voice.")
engine.runAndWait()




# What You'll See in Output (Example):

# Voice: Microsoft David Desktop - English (United States) - ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\...
# Voice: Microsoft Zira Desktop - English (United States) - ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\...
# Voice: Microsoft Mark - English (United States) - ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\...

