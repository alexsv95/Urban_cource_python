from time import sleep

class User:
    def __init__(self, nickname: str, password, age: int):
        if isinstance(nickname, str):
            self.nickname = nickname
        else:
            raise ValueError
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError
        self.password = hash(str(password))


class Video:
    def __init__(self, title: str, duration: int | float, time_now: int = 0, adult_mode = False):
        if isinstance(title, str):
            self.title = title
        else:
            print('Параметр title поддерживает только строку')
        if isinstance(duration, (int, float)):
            self.duration = duration
        else:
            print(f'Параметр duration поддерживает только число')
        if isinstance(time_now, (int, float)):
            self.time_now = time_now
        else:
            print(f'Параметр time_now поддерживает только число')
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title


class UrTube:
    current_user = None

    def __init__(self):
        self.users = {}
        self.videos = {}

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = User(nickname, password, age)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname].password == hash(str(password)):
                self.current_user = self.users[nickname].nickname
            else:
                print('Введен не корректный пароль')
        else:
            print('Пользователь не найден')

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i.title not in self.videos:
                self.videos[i] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}
                # self.videos.append(i.title)

    def get_videos(self, search_word):
        found_video = []
        for video in self.videos.keys():
            for word in str(video).split():
                if search_word.lower() in word.lower():
                    found_video.append(video)
        return found_video

    def watch_video(self, title):
        found_result = False
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for key in self.videos.keys():
                if title == str(key):
                    found_result = True
                    adult_mode = self.videos[key].get('adult_mode')
                    if adult_mode is True and self.users[self.current_user].age < 18:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        duration = self.videos[key].get('duration')
                        for i in range(duration):
                            print(i, end=' ')
                            self.videos[key]['time_now'] = 0
                            sleep(1)
                        print('Конец видео')
                        break
            if found_result is False:
                return print(f'Видео с названием {title} не найдено')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    #
    # # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

