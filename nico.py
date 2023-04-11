import openai
import os
from dotenv import load_dotenv

def load_key():
    load_dotenv()
    my_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = my_key


prompt = """
Provide the sequence of steps needed to complete the task. 
You must answer the following questions about the task: 
1. What object is required for this task (give only the object)
2. Is this object typically found on a wall, the ceiling, the floor, or on another object?
3. Iff typically found on another object, what object (give only the object); otherwise, return "n/a"?
4. What action should I commit on the object (respond with one of use the actions "move", "push", "pull", "grab").
5. If move, where to? If push or pull, in what direction (give "up", "down", "right", "left", "forward", "backwards") and for what distance (give in "inches")?

Human: Open the fridge.

Steps:
1. The fridge handle.
2. The floor.
3. n/a
4. Pull.
5. Backwards. 24 inches.

Human: Kick a ball.

Steps:
1. The ball.
2. The floor.
3. n/a
4. Push.
5. Forward. 5 feet.

Human: Turn on the lights
"""
# res = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     n=1,
#     temperature=1,
#     max_tokens=200
# )

# for c in res.choices:
#     print(c.text)
# res.choices

if __name__ == "__main__":
    load_key()
