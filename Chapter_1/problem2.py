import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''I am a tech-focused learner with a strong interest in programming and real-world problem solving. I work with languages like Python and Java, and I enjoy building practical projects that can be applied in real scenarios.

I am comfortable using tools like VS Code and continuously improving my development environment and coding practices. I actively solve coding problems to strengthen my logic and analytical thinking.

Along with programming, I also stay updated with technology trends and make informed decisions when it comes to tech products.

My goal is to grow as a developer by building impactful projects and gaining hands-on experience.''')
engine.runAndWait()