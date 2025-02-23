from dotenv import load_dotenv
import os


load_dotenv()


my_var = os.getenv("MY_VAR")
print(f"My variable: {my_var}")
