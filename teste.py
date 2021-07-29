import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

usuario = os.getenv("user")
senha = os.getenv("passwd")

print(usuario)
print(senha)