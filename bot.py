#!./venv/bin/python
import cmd
import os
from openai import OpenAI
from dotenv import load_dotenv
import models

load_dotenv()

api_key = os.getenv("CHAT_GPT_API_KEY")
client = OpenAI(api_key=api_key)

class Console(cmd.Cmd):

    __messages = []

    def default(self, line):
        line = f"ask {line}"
        cmd.Cmd.onecmd(self, line)
    
    def do_ask(self, line):
        self.__messages.append({"role": "user", "content": line})
        response = client.chat.completions.create(
            model="gpt-4",
            messages=self.__messages
        )
        reply = response.choices[0].message.content
        self.__messages.append({"role": "assistant", "content": reply})
        print(reply)
    
    def do_continue(self, line):
        for key, value in models.storage.all().items():
            self.__messages.append(value)
        line = f"ask can we continue from where we stopped?"
        cmd.Cmd.onecmd(self, line)
    
    def do_clear(self, line):
        os.system('cls')
        return True
    
    def do_quit(self, line):
        for messages in self.__messages:
            models.storage.new(messages)
            models.storage.save()
        return True


if __name__ == "__main__":
    new_console = Console()
    new_console.prompt = "$ "
    new_console.cmdloop()
