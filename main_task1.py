#функция вычисления кто быстрее, заяц или черепаха(Задание "Кто быстрее"")
def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0
    for s in hare_distances:
        hare_all += s
    turtle_all = 0
    for s in turtle_distances:
        turtle_all += s
    if hare_all < turtle_all:
        result = "черепаха"
    elif hare_all > turtle_all:
        result = "заяц"
    else:
        result = "одинаково"
    return result


#Функция нахождения числа, встречающегося в списке чаще всего(Задание «Голосование»)
def vote(votes: list):
    max_count = 0
    max_el = 0
    for el in votes:
       if votes.count(el) > max_count:
          max_el = el
          max_count = votes.count(el)
    return max_el

#функция к заданию Рекордсмены: находим самый продолжительный и самый короткий курс по программированию»
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def max_min_course(courses: list, mentors: list, durations: list):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration": duration}
        courses_list.append(course_dict)
    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if durations[index] == max(durations):
            maxes.append(index)
        elif durations[index] == min(durations):
            minis.append(index)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])
    for id in maxes:
        courses_max.append(courses_list[id]['title'])
    return (f"Самый короткий курс(ы): {''.join(courses_min)} - {durations[minis[0]]} месяца(ев)",
            f"Самый длинный курс(ы): {', '.join(courses_max)} - {durations[maxes[0]]} месяца(ев)")

