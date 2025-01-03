team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / 2

def winner_definition() -> str:
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = f'Победа команды {team1_name}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = f'Победа команды {team2_name}!'
    else:
        challenge_result = 'Ничья!'
    return challenge_result


# Использование %
print('В команде %s участников: %s!' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %(team1)s и %(team2)s!' % {'team1': team1_num, 'team2': team2_num})

# Использование format()
print('Команда {} решила задач: {}!'.format(team2_name, score_2))
print('{team2} решили задачи за {tt1}с!'.format(tt1=team1_time, team2=team2_name))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {winner_definition()}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')