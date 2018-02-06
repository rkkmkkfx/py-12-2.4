import os

path_name = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    migrations_dir = os.path.join(current_dir, path_name)
    migrations = [filename for filename in os.listdir(migrations_dir) if filename.endswith('.sql')]
    while True:
        founded = []
        query = input('Введите строку: ')
        for migration in migrations:
            with open(os.path.join(migrations_dir, migration)) as f:
                data = f.read()
                if query in data:
                    print(migration)
                    founded.append(migration)
        print('Всего: ', len(founded))
