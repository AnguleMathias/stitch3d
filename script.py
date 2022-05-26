class Script:
    def __init__(self):
        self.user_data = {
            'name': 'Mathias',
            'age': '30',
            'gender': 'male',
            'bio': 'male',
        }

    def command_prompt(self):
        while True:
            command, *args = input('Enter command: ').split(' ')
            if command not in {'GET', 'SET', 'UNSET', 'NUMEQUALTO', 'END'}:
                print('error')
                continue
            else:
                self.handle_command(command, args)

    def handle_command(self, command, args=None):
        if command == 'GET':
            self._get(*args)
        elif command == 'SET':
            self._set(*args)
        elif command == 'UNSET':
            self._unset(*args)
        elif command == 'NUMEQUALTO':
            self._numequalto(*args)
        elif command == 'END':
            self._end()

    def _get(self, key=None):
        try:
            print(self.user_data[key])
        except:
            print('Not found!!!')

    def _set(self, key=None, value=None):
        self.user_data[key] = value

    def _unset(self, key=None):
        try:
            self.user_data.pop(key)
        except:
            print('Not found!!!')

    def _numequalto(self, value=None):
        result = 0
        for key in self.user_data:
            if self.user_data[key] == value:
                result += 1
        print(result)

    def _end(self):
        exit()


if __name__ == '__main__':
    script = Script()
    script.command_prompt()
