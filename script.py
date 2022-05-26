import csv


class Script:
    def __init__(self):
        self.user_data = {
            'name': 'Mathias',
            'age': '30',
            'gender': 'male',
            'bio': 'male',
        }
        self.user = {}
        try:
            with open('test.txt', 'r') as readFile:
                reader = csv.reader(readFile, delimiter=':')
                users = dict(reader)
                self.names = set(users.keys())
        except:
            self.names = set()

    def command_prompt(self):
        while True:
            command, *args = input('Enter command: ').split(' ')
            if command not in {'GET', 'SET', 'UNSET', 'NUMEQUALTO', 'END', 'BEGIN', 'COMMIT', 'ROLLBACK'}:
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
        elif command == 'BEGIN':
            self._begin_transaction()
        elif command == 'COMMIT':
            self._commit_transaction()
        elif command == 'ROLLBACK':
            self._rollback_transaction()
        elif command == 'END':
            self._end()

    def _get(self, key=None):
        # constant time 0(1)
        try:
            print(self.user_data[key])
        except:
            print('Not found!!!')

    def _set(self, key=None, value=None):
        # constant time 0(1)
        self.user_data[key] = value

    def _unset(self, key=None):
        # constant time 0(1)
        try:
            self.user_data.pop(key)
        except:
            print('Not found!!!')

    def _numequalto(self, value=None):
        # linear time 0(n)
        result = 0
        for key in self.user_data:
            if self.user_data[key] == value:
                result += 1
        print(result)

    def _begin_transaction(self):
        print("Begin transaction ...")
        name = input('Enter name: ')
        password = input('Enter password: ')
        self.user[name] = password

    def _commit_transaction(self):
        name = next(reversed(self.user))
        password = self.user[name]
        if self._numequalto(self.user, password) == 0:
            print('NO TRANSACTION')
        else:
            with open('test.txt', 'a', newline='') as fappend:
                writer = csv.writer(fappend, delimiter=':')
                writer.writerow([name, password])

    def _rollback_transaction(self):
        name = next(reversed(self.user))
        password = self.user[name]
        if self._numequalto(self.user, password) == 0:
            print('NO TRANSACTION')
        else:
            self.user.pop(name)

    def _end(self):
        exit()


if __name__ == '__main__':
    script = Script()
    script.command_prompt()
