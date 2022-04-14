# Добавление
insert_new_episodes = '''INSERT INTO series(name, episodes, length, start_year, end_year, genre_id, status)
    VALUES (%s, %s,  %s, to_date(%s, 'YYYY-01-01'), to_date(%s, 'YYYY-01-01'), %s, %s)'''

to_will_watch = (
    f'INSERT INTO will_watch(series_id) (SELECT id FROM series WHERE name = %s)'
)

# выбираем сериалы, которых нет ни в одной активности
non_activity = '''SELECT name FROM series WHERE id NOT IN (
SELECT series_id FROM activity UNION SELECT series_id FROM will_watch
)'''

# сериал в смотрю
to_watching = '''
INSERT INTO activity(status, series_id, episodes)
VALUES('watching', (SELECT id FROM series WHERE name = %s), %s);
DELETE FROM will_watch WHERE series_id = %s; '''  # todo: уточнить перенос параметров

# Обновление
# добавление серии в просмотренные
add_episodes = '''UPDATE activity SET episodes = episodes + %s
WHERE series_id = (SELECT id FROM series WHERE name = %s)'''

# изменение кол-ва эпизодов в сериале
change_eps_amount = f'UPDATE series SET episodes = episodes + %s WHERE name = %s'

# изменение статуса сериала
change_show_stat = f'UPDATE series SET status = %s WHERE name = %s'

# изменение статуса сериала
to_cancelled = f"UPDATE activity SET status = 'cancelled' WHERE series_id = (SELECT id FROM series WHERE name = %s)"

to_completed = f"UPDATE activity SET status = 'completed' WHERE series_id = %s"

# изменение статуса просмотра мануально
change_activity_stat = f'UPDATE activity SET status = %s WHERE series_id = (SELECT id FROM series WHERE name = %s)'

completed_check = '''
SELECT activity.series_id, activity.episodes as watched, series.episodes as all_eps
FROM activity JOIN series ON activity.series_id = series.id
WHERE activity.status = 'watching' AND series.status = false
'''

# Выборки
# сколько сериалов смотришь on air
count_eps_onair = '''
SELECT count(*) FROM activity JOIN series ON activity.series_id = series.id
WHERE activity.status = 'watching' AND series.status = true'''

# сколько сериалов смотришь dead
count_eps_dead = '''
SELECT count(*) FROM activity JOIN series ON activity.series_id = series.id
WHERE activity.status = 'watching' AND series.status = false'''

# сколько и каких сериалов смотришь, просмотрено, в процессе, будешь смотреть
count_shows_groups = '''
SELECT status, count(*) FROM activity GROUP BY status
UNION
SELECT 'will_watch' as status, count(*) FROM will_watch;'''

count_all = '''SELECT 'Всего: ' as status, count(activity.*) + count(will_watch.*) as Количество 
FROM activity FULL JOIN will_watch ON activity.series_id = will_watch.series_id;'''

# сколько сериалов по жанрам смотришь
shows_by_genre = '''
SELECT genre.name, count(*) as amount FROM activity
JOIN series ON activity.series_id = series.id
JOIN genre ON series.genre_id = genre.id
GROUP BY genre.id'''

# сериалы по статусам
shows_willwatch = f'SELECT name FROM series JOIN will_watch ON will_watch.series_id = series.id'
shows_watching = "SELECT name FROM series JOIN activity ON activity.series_id = series.id " \
                 "WHERE activity.status = 'watching';"
shows_cancelled = "SELECT name FROM series JOIN activity ON activity.series_id = series.id " \
                  "WHERE activity.status = 'cancelled';"
shows_completed = "SELECT name FROM series JOIN activity ON activity.series_id = series.id " \
                  "WHERE activity.status = 'completed';"

# сериалы по году
shows_by_year = '''
SELECT name FROM series
WHERE (start_year >= to_date(%s, 'YYYY-MM-DD'))
AND (end_year <= to_date(%s, 'YYYY-MM-DD'))'''

# с форматированием года
shows_by_year_nice = '''
SELECT name, date_part('year', to_date('2020-01-01', 'YYYY')) as year
FROM series
WHERE to_date('2020-01-01', 'YYYY-MM-DD')
BETWEEN start_year AND end_year'''

# сколько времени всего насмотрено
time_spend = '''
SELECT justify_interval(sum(activity.episodes * series.length))
FROM activity JOIN series ON series.id = activity.series_id'''

# сколько времени осталось
time_left = '''
SELECT justify_interval(sum((series.episodes - activity.episodes) * series.length))
FROM activity JOIN series ON series.id = activity.series_id
WHERE series.id IN (select series_id from activity) '''

# сколько времени на каждое просмтренное
time_each_show = '''
SELECT series.name as "Название", justify_interval(activity.episodes * series.length) as "Потраченное время",
justify_interval((series.episodes - activity.episodes) * series.length) as "Оставшееся время"
FROM activity JOIN series ON series.id = activity.series_id'''
