#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, _):
        """Exit the console."""
        return True  # Returning True exits the cmd loop

    # Alias for exit
    do_quit = do_EOF

    def help_quit(self) -> None:
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

