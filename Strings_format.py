
# Входные данные:
team1_num = 6                                              # Количество игроков в первой команде
team2_num = 6                                              # Количество игроков во второй команде
score1 = 40                                                # Количество решенных задач в первой команде
score2 = 42                                                # Количество решенных задач во второй команде
team1_time = 1552.512                                      # затраченное время
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2                                            # Среднее время решения
challenge_result_1 = 'Победа команды Мастера кода!'
challenge_result_2 = 'Победа команды Волшебники данных!'

print('Старый стиль:')
print("В команде Мастера кода участников: %s ! " % (team1_num))
print("В команде Волшебники данных участников: %s ! " % (team2_num))
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print()
print('Новый стиль (format):')
print("Команда Волшебники данных решила задач: {}!". format(score1))
print("Команда Мастера кода решила задач: {}!". format(score2))
print("Вcего было решено {} задач!". format(tasks_total))
print("Волшебники данных решили задачи за {0:.1f} c!". format(team2_time))
print("Мастера кода решили задачи за {0:.1f} c!". format(team1_time))

print()
print('Использование f-строк:')
print(f'Команды решили {score2} и {score1} задач.')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = challenge_result_1
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = challenge_result_2
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {(team2_time + team1_time)/tasks_total:.1f} секунды на задачу!.')
