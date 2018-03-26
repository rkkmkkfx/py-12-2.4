import os

path_name = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_files_with_str(string, files):
    founded = []
    for file in files:
        with open(os.path.join(migrations_dir, file)) as f:
            data = f.read()
            if string in data:
                founded.append(migration)
    return founded


if __name__ == '__main__':
    migrations_dir = os.path.join(current_dir, path_name)
    migrations = [filename for filename in os.listdir(migrations_dir) if filename.endswith('.sql')]
    while True:
        query = input('Введите строку: ')
        migrations = get_files_with_str(query, migrations)
        for migration in migrations:
            print(migration)
        print('Всего: ', len(migrations))
