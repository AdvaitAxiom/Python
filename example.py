import pyjokes
import pyttsx3
jokes = pyjokes.get_jokes()
print(jokes)

engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()

print("Hello")
print('''
hello
      my 
      name
      is 
      alapan
      das
      ''')