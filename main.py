import pygame

pygame.init()

from random import randint, choice

# Начальные условия
WIDTH = 100  # Если ширина 365, а высота 274, то получаем 100010 точек.
HEIGHT = 100

quantity = 100  # Количество живых пикселей на поле
long_life = 100  # Сколько циклов живут пиксели
long_life_plus = 2  # Сколько циклов жизни плюсовать при согласии соседнего пикселя
no_kids_time = 1  # Минимальное время между рождениями

counter_no_kids_time_1 = no_kids_time
counter_no_kids_time_2 = no_kids_time
counter_no_kids_time_3 = no_kids_time

quantity_1 = 0  # Зануляем кол-во первых
quantity_2 = 0  # Зануляем кол-во вторых
iteration = 0  # Зануляем кол-во итераций
age_sum_1 = 0  # Зануляем сумму всех лет для 1х
age_sum_2 = 0  # Зануляем сумму всех лет для 2х
age_arithmetic_mean_1 = 0  # Зануляем средний ариф-й возраст 1х
age_arithmetic_mean_2 = 0  # Зануляем средний ариф-й возраст 2х
age_max_1 = 0  # Зануляем максимальный возраст 1х
age_max_2 = 0  # Зануляем максимальный возраст 2х
iteration_gameover = 0
t = 0
button_1_1 = 0  # Зануляем кнопки
button_1_2 = 0  # Зануляем кнопки
button_1_3 = 0  # Зануляем кнопки
button_1_4 = 0  # Зануляем кнопки
button_1_5 = 0  # Зануляем кнопки
button_1_6 = 0  # Зануляем кнопки
button_1_7 = 0  # Зануляем кнопки

# Выбор условий False или True
reproduce_insider_1 = True  # Размножаться со своими 1
reproduce_insider_2 = True  # Размножаться со своими 2
reproduce_outsider = True  # Размножаться с чужими

cooperate_insider_1 = False  # Сотрудничать со своими 1
cooperate_insider_2 = True  # Сотрудничать со своими 2
cooperate_outsider = False  # Сотрудничать с чужими

kill_outsider_1 = True  # Убивать соперника 1 (1е могут убивать 2х)
kill_outsider_2 = False  # Убивать соперника 2 (2е могут убивать 1х)
strong_kill_outsider = False  # У кого больше времени, тот и сильнее, тот и убивает соперника.
rob_kill_outsider_1 = False  # Забирать время убитого соперника 1 (1е могут забирать у 2х)
rob_kill_outsider_2 = False  # Забирать время убитого соперника 2 (2е могут забирать у 1х)

layout_scheme = 2  # Схема расположения точек. 1 - по краям поля. 2 - вперемешку.

# Кусок отвечающий за появление точек по половинам экрана
A = [[0] * (WIDTH + 1) for _ in range(HEIGHT + 1)]  # Зануляем матрицу
if layout_scheme == 1:
    q = 0
    while q < (quantity // 2):
        x = randint(1, (WIDTH // 2))
        y = randint(1, HEIGHT)
        if A[y][x] == 0:
            A[y][x] = long_life * 10 + 1
            q += 1

    while q < quantity:
        x = randint((WIDTH // 2 + 1), WIDTH)
        y = randint(1, HEIGHT)
        if A[y][x] == 0:
            A[y][x] = long_life * 10 + 2
            q += 1

# Кусок отвечающий за появление точек равномерно по экрану
if layout_scheme == 2:
    q = 0
    while q < quantity:
        x = randint(1, WIDTH)
        y = randint(1, HEIGHT)
        if A[y][x] == 0:
            if (q % 2) == 0:
                A[y][x] = long_life * 10 + 1  # "Это красные. Если число не четное, то их будет больше на один."
            else:
                A[y][x] = long_life * 10 + 2
        q += 1

screen = pygame.display.set_mode((WIDTH * 4 + 600, HEIGHT * 4 + 130))  # Запускает появление экрана

# НАЧАЛО ОСНОВНОГО ЦИКЛА
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            from sys import exit  # обязательно писать, что бы не ругался при закрытии файла.

            exit()

    screen.fill(("black"))  # Убирает следы прошлого
    pygame.time.delay(0)  # Задержка

    iteration += 1  # Для счетчика кол-ва итераций

    # Отсчет времени до следующего разрешения размножаться. Иначе забомбучивает все на первом же ходу.
    counter_no_kids_time_1 -= 1
    if counter_no_kids_time_1 < 1:
        counter_no_kids_time_1 = 1

    counter_no_kids_time_2 -= 1
    if counter_no_kids_time_2 < 1:
        counter_no_kids_time_2 = 1

    counter_no_kids_time_3 -= 1
    if counter_no_kids_time_3 < 1:
        counter_no_kids_time_3 = 1

    # Выбираем место с которого разрешаем размножаться. Иначе все размножение будет в левом верхнем углу.
    x_no_kids_time_1 = randint(1, WIDTH)
    y_no_kids_time_1 = randint(1, HEIGHT)
    x_no_kids_time_2 = randint(1, WIDTH)
    y_no_kids_time_2 = randint(1, HEIGHT)
    x_no_kids_time_3 = randint(1, WIDTH)
    y_no_kids_time_3 = randint(1, HEIGHT)

    # Выводим на экран показатели
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    font_title = pygame.font.SysFont('microsofttaile', 50)
    if (iteration // 100) % 2 == 0:
        title = font_title.render("PIXEL ", 1, RED, BLACK)  # Выводим на экран кол-во итераций
        screen.blit(title, (380, 5))
        title = font_title.render("LIFE", 1, GREEN, BLACK)  # Выводим на экран кол-во итераций
        screen.blit(title, (520, 5))
    else:
        title = font_title.render("PIXEL ", 1, GREEN, BLACK)  # Выводим на экран кол-во итераций
        screen.blit(title, (380, 5))
        title = font_title.render("LIFE", 1, RED, BLACK)  # Выводим на экран кол-во итераций
        screen.blit(title, (520, 5))

    font1 = pygame.font.SysFont('None', 40)
    # Вот какие шрифты использовал microsofttaile bloodcyrillic areal
    if (quantity_1 > 0 or quantity_2 > 0):
        iteration_ = font1.render("ШАГ: " + str(iteration), 1, (128, 128, 128),
                                  BLACK)  # Выводим на экран кол-во итераций
        screen.blit(iteration_, (420, 480))
        iteration_gameover = iteration
    else:
        font_gameover = pygame.font.SysFont('microsofttaile', 150)
        if (iteration // 10) % 2 == 0 and iteration > 10:
            title = font_gameover.render("GAME ", 1, RED, BLACK)  # Выводим на экран кол-во итераций
            screen.blit(title, (60, 150))
            title = font_gameover.render("OVER", 1, GREEN, BLACK)  # Выводим на экран кол-во итераций
            screen.blit(title, (560, 150))
        if (iteration // 10) % 2 != 0 and iteration > 10:
            title = font_gameover.render("GAME ", 1, GREEN, BLACK)  # Выводим на экран кол-во итераций
            screen.blit(title, (60, 150))
            title = font_gameover.render("OVER", 1, RED, BLACK)  # Выводим на экран кол-во итераций
            screen.blit(title, (560, 150))
        iteration_ = font1.render("ШАГ: " + str(iteration_gameover), 1, (128, 128, 128),
                                  BLACK)  # Выводим на экран кол-во итераций
        screen.blit(iteration_, (420, 480))

    # Вот какие шрифты использовал microsofttaile bloodcyrillic areal
    if quantity_1 > 0:
        follow_RED = font_title.render(str(quantity_1), 1, BLACK, RED)  # Выводим на экран кол-во первых
        screen.blit(follow_RED, (110, 20))

    if quantity_2 > 0:
        follow_GREEN = font_title.render(str(quantity_2), 1, BLACK, GREEN)  # Выводим на экран кол-во вторых
        screen.blit(follow_GREEN, (810, 20))

        # Выводим на экран средний возраст первых
    font = pygame.font.SysFont('None', 25)
    if quantity_1 > 0:
        age_arithmetic_mean_1 = int(age_sum_1 / quantity_1)
        pygame.draw.rect(screen, RED,
                         (15, 110, 275, 35))
        age_arithmetic_mean__RED = font.render("Cредний возраст: " + str(age_arithmetic_mean_1), 1, BLACK, RED)
        screen.blit(age_arithmetic_mean__RED, (50, 120))
        age_arithmetic_mean_1 = 0
        age_sum_1 = 0

    # Выводим на экран максимальный возраст первых
    if age_max_1 > 0:
        pygame.draw.rect(screen, RED,
                         (15, 150, 275, 35))
        age_max_RED = font.render("Макс-ый возраст: " + str(age_max_1), 1, BLACK, RED)
        screen.blit(age_max_RED, (50, 160))
        age_max_1 = 0

    # Выводим на экран средний возраст вторых
    if quantity_2 > 0:
        age_arithmetic_mean_2 = int(age_sum_2 / quantity_2)
        pygame.draw.rect(screen, GREEN,
                         (710, 110, 275, 35))
        age_arithmetic_mean__GREEN = font.render("Cредний возраст: " + str(age_arithmetic_mean_2), 1, BLACK, GREEN)
        screen.blit(age_arithmetic_mean__GREEN, (750, 120))
        age_arithmetic_mean_2 = 0
        age_sum_2 = 0

    # Выводим на экран максимальный возраст вторых
    if age_max_2 > 0:
        pygame.draw.rect(screen, GREEN,
                         (710, 150, 275, 35))
        age_max_GREEN = font.render("Макс-ый возраст: " + str(age_max_2), 1, BLACK, GREEN)
        screen.blit(age_max_GREEN, (750, 160))
        age_max_2 = 0

    if quantity_1 > 0:
        # Выводим левую кнопку - Размножаться со своими
        font = pygame.font.SysFont('None', 22)
        coordinates_square = (20, 195, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 5, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if reproduce_insider_1 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if reproduce_insider_1 == False:
                reproduce_insider_1 = True
            else:
                reproduce_insider_1 = False

        text_RED = font.render("Размножаться со своими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Размножаться с чужими
        coordinates_square = (20, 235, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 5, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if reproduce_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if reproduce_outsider == False:
                reproduce_outsider = True
            else:
                reproduce_outsider = False

        text_RED = font.render("Размножаться с чужими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Сотрудничать со своими
        coordinates_square = (20, 275, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 5, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if cooperate_insider_1 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if cooperate_insider_1 == False:
                cooperate_insider_1 = True
            else:
                cooperate_insider_1 = False

        text_RED = font.render("Сотрудничать со своими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Сотрудничать с чужими
        coordinates_square = (20, 315, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 5, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if cooperate_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if cooperate_outsider == False:
                cooperate_outsider = True
            else:
                cooperate_outsider = False

        text_RED = font.render("Сотрудничать с чужими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Уничтожать соперника
        coordinates_square = (20, 355, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 5, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if kill_outsider_1 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if kill_outsider_1 == False:
                kill_outsider_1 = True
            else:
                kill_outsider_1 = False
                strong_kill_outsider = False
                rob_kill_outsider_1 = False

        text_RED = font.render("Уничтожать соперника", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Выживает сильнейший
        coordinates_square = (50, 395, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 35, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if strong_kill_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if strong_kill_outsider == False:
                strong_kill_outsider = True
                kill_outsider_1 = True
            else:
                strong_kill_outsider = False

        text_RED = font.render("Выживает сильнейший", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

        # Выводим левую кнопку - Забрать время соперника
        coordinates_square = (50, 435, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 35, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if rob_kill_outsider_1 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, RED,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if rob_kill_outsider_1 == False:
                rob_kill_outsider_1 = True
                kill_outsider_1 = True
            else:
                rob_kill_outsider_1 = False

        text_RED = font.render("Забрать время соперника", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_RED, (coordinates_square[0] + 35, coordinates_square[1] + 6))

    quantity_1 = 0

    if quantity_2 > 0:
        # Выводим правую кнопку - Размножаться со своими
        font = pygame.font.SysFont('None', 22)
        coordinates_square = (955, 195, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 245, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if reproduce_insider_2 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if reproduce_insider_2 == False:
                reproduce_insider_2 = True
            else:
                reproduce_insider_2 = False

        text_GREEN = font.render("Размножаться со своими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Размножаться с чужими
        coordinates_square = (955, 235, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 245, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if reproduce_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if reproduce_outsider == False:
                reproduce_outsider = True
            else:
                reproduce_outsider = False

        text_GREEN = font.render("Размножаться с чужими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Сотрудничать со своими
        coordinates_square = (955, 275, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 245, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if cooperate_insider_2 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if cooperate_insider_2 == False:
                cooperate_insider_2 = True
            else:
                cooperate_insider_2 = False

        text_GREEN = font.render("Сотрудничать со своими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Сотрудничать с чужими
        coordinates_square = (955, 315, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 245, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if cooperate_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if cooperate_outsider == False:
                cooperate_outsider = True
            else:
                cooperate_outsider = False

        text_GREEN = font.render("Сотрудничать с чужими", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Уничтожать соперника
        coordinates_square = (955, 355, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 245, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if kill_outsider_2 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if kill_outsider_2 == False:
                kill_outsider_2 = True
            else:
                kill_outsider_2 = False
                strong_kill_outsider = False
                rob_kill_outsider_2 = False

        text_GREEN = font.render("Уничтожать соперника", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Выживает сильнейший
        coordinates_square = (925, 395, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 215, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if strong_kill_outsider == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if strong_kill_outsider == False:
                strong_kill_outsider = True
                kill_outsider_2 = True
            else:
                strong_kill_outsider = False

        text_GREEN = font.render("Выживает сильнейший", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

        # Выводим правую кнопку - Забрать время соперника
        coordinates_square = (925, 435, 25, 25)
        pygame.draw.rect(screen, (15, 15, 15),
                         (coordinates_square[0] - 215, coordinates_square[1] - 5, coordinates_square[2] + 250,
                          coordinates_square[3] + 10))
        pygame.draw.rect(screen, (128, 128, 128),
                         (coordinates_square[0] - 2, coordinates_square[1] - 2, coordinates_square[2] + 4,
                          coordinates_square[3] + 4))

        if rob_kill_outsider_2 == False:
            pygame.draw.rect(screen, (255, 255, 255),
                             coordinates_square)
        else:
            pygame.draw.rect(screen, GREEN,
                             coordinates_square)

        pos = pygame.mouse.get_pos()
        buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()

        if pos[0] > coordinates_square[0] and pos[0] < (coordinates_square[0] + coordinates_square[2]) and pos[1] > \
                coordinates_square[1] and pos[1] < (
                coordinates_square[1] + coordinates_square[3]) and buttonLeft == True:
            if rob_kill_outsider_2 == False:
                rob_kill_outsider_2 = True
                kill_outsider_2 = True
            else:
                rob_kill_outsider_2 = False

        text_GREEN = font.render("Забрать время соперника", 1, (128, 128, 128), (25, 25, 25))
        screen.blit(text_GREEN, (coordinates_square[0] - 200, coordinates_square[1] + 6))

    quantity_2 = 0

    for x in range(1, WIDTH + 1):  # прогоняем по горизонту - Х
        for y in range(1, HEIGHT + 1):  # прогоняем по вертикали - Y

            if A[y][x] < 20:  # Пиксель погибает, если у него завершилось время
                A[y][x] = 0
                # pygame.draw.circle(screen, "black", (x*4+300, y*4), 2)
            else:
                A[y][x] -= 10

            # Считаем сколько первых
            if (A[y][x] % 10) == 1:  # х и у не перепутанны, просто так считаются в таком порядке
                quantity_1 += 1
            # Считаем сколько вторых
            if (A[y][x] % 10) == 2:  # х и у не перепутанны, просто так считаются в таком порядке
                quantity_2 += 1

            if (A[y][x] % 10) == 1:
                age_sum_1 += (A[y][x] // 10)  # Считаем общий возраст 1х
            if (A[y][x] % 10) == 2:
                age_sum_2 += (A[y][x] // 10)  # Считаем общий возраст 2х

            if (A[y][x] % 10) == 1 and age_max_1 < (A[y][x] // 10):
                age_max_1 = (A[y][x] // 10)  # Считываем максимальный возраст 1х
            if (A[y][x] % 10) == 2 and age_max_2 < (A[y][x] // 10):
                age_max_2 = (A[y][x] // 10)  # Считываем максимальный возраст 2х

            # Кусок отвечающий за закрашивание
            if (A[y][x] % 10) == 1:  # х и у не перепутанны, просто так считаются в таком порядке
                pygame.draw.circle(screen, "red", (x * 4 + 300, y * 4 + 65), 2)
            if (A[y][x] % 10) == 2:  # х и у не перепутанны, просто так считаются в таком порядке
                pygame.draw.circle(screen, "green", (x * 4 + 300, y * 4 + 65), 2)

            # Кусок продлевающий жизнь при встрече
            if x > 0 and y > 0 and x < (WIDTH) and y < (HEIGHT) and A[y][x] > 0:
                if (A[y][x] % 10) == 1 and cooperate_insider_1 == True:
                    if (A[y][x + 1] % 10) == 1 or (A[y + 1][x + 1] % 10) == 1 or (A[y + 1][x] % 10) == 1 or (
                            A[y + 1][x - 1] % 10) == 1 or (A[y][x - 1] % 10) == 1 or (A[y - 1][x - 1] % 10) == 1 or (
                            A[y - 1][x] % 10) == 1 or (A[y - 1][x + 1] % 10) == 1:
                        A[y][x] += long_life_plus * 10

                if (A[y][x] % 10) == 2 and cooperate_insider_2 == True:
                    if (A[y][x + 1] % 10) == 2 or (A[y + 1][x + 1] % 10) == 2 or (A[y + 1][x] % 10) == 2 or (
                            A[y + 1][x - 1] % 10) == 2 or (A[y][x - 1] % 10) == 2 or (A[y - 1][x - 1] % 10) == 2 or (
                            A[y - 1][x] % 10) == 2 or (A[y - 1][x + 1] % 10) == 2:
                        A[y][x] += long_life_plus * 10

                if (A[y][x] % 10) > 0 and cooperate_outsider == True:
                    if (A[y][x + 1] % 10) + (A[y][x] % 10) == 3 or (A[y + 1][x + 1] % 10) + (A[y][x] % 10) == 3 or (
                            A[y + 1][x] % 10) + (A[y][x] % 10) == 3 or (A[y + 1][x - 1] % 10) + (A[y][x] % 10) == 3 or (
                            A[y][x - 1] % 10) + (A[y][x] % 10) == 3 or (A[y - 1][x - 1] % 10) + (A[y][x] % 10) == 3 or (
                            A[y - 1][x] % 10) + (A[y][x] % 10) == 3 or (A[y - 1][x + 1] % 10) + (A[y][x] % 10) == 3:
                        A[y][x] += long_life_plus * 10

                        # Кусок (который пишлось дописать только для крайнего правого столбца и нижнего ряда) продлевающий жизнь при встрече
            if x > 0 and y > 0 and (x == (WIDTH) or y == (HEIGHT)) and A[y][x] > 0:
                if (A[y][x] % 10) == 1 and cooperate_insider_1 == True:
                    if (A[y][x - 1] % 10) == 1 or (A[y - 1][x - 1] % 10) == 1 or (A[y - 1][x] % 10) == 1:
                        A[y][x] += long_life_plus * 10

                if (A[y][x] % 10) == 2 and cooperate_insider_2 == True:
                    if (A[y][x - 1] % 10) == 2 or (A[y - 1][x - 1] % 10) == 2 or (A[y - 1][x] % 10) == 2:
                        A[y][x] += long_life_plus * 10

                if (A[y][x] % 10) > 0 and cooperate_outsider == True:
                    if (A[y][x - 1] % 10) + (A[y][x] % 10) == 3 or (A[y - 1][x - 1] % 10) + (A[y][x] % 10) == 3 or (
                            A[y - 1][x] % 10) + (A[y][x] % 10) == 3:
                        A[y][x] += long_life_plus * 10

                        # Кусок рождения пикселя
            if x == x_no_kids_time_1 and y == y_no_kids_time_1:
                counter_no_kids_time_1 = 0
            if x == x_no_kids_time_2 and y == y_no_kids_time_2:
                counter_no_kids_time_2 = 0
            if x == x_no_kids_time_3 and y == y_no_kids_time_3:
                counter_no_kids_time_3 = 0

            if x > 0 and y > 0 and x < (WIDTH) and y < (HEIGHT) and A[y][x] > 0:
                if (A[y][x] % 10) == 1 and reproduce_insider_1 == True and counter_no_kids_time_1 == 0:
                    if (A[y][x + 1] % 10) == 1 or (A[y + 1][x + 1] % 10) == 1 or (A[y + 1][x] % 10) == 1 or (
                            A[y + 1][x - 1] % 10) == 1 or (A[y][x - 1] % 10) == 1 or (A[y - 1][x - 1] % 10) == 1 or (
                            A[y - 1][x] % 10) == 1 or (A[y - 1][x + 1] % 10) == 1:
                        if A[y][x + 1] == 0 or A[y + 1][x + 1] == 0 or A[y + 1][x] == 0 or A[y + 1][x - 1] == 0 or A[y][
                            x - 1] == 0 or A[y - 1][x - 1] == 0 or A[y - 1][x] == 0 or A[y - 1][x + 1] == 0:
                            place_birth = 1
                            while place_birth == 1:
                                q = 0
                                q = randint(1, 8)
                                if q == 1 and A[y][x + 1] == 0:
                                    A[y][x + 1] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 2 and A[y + 1][x + 1] == 0:
                                    A[y + 1][x + 1] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 3 and A[y + 1][x] == 0:
                                    A[y + 1][x] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 4 and A[y + 1][x - 1] == 0:
                                    A[y + 1][x - 1] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 5 and A[y][x - 1] == 0:
                                    A[y][x - 1] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 6 and A[y - 1][x - 1] == 0:
                                    A[y - 1][x - 1] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 7 and A[y - 1][x] == 0:
                                    A[y - 1][x] = long_life * 10 + 1
                                    place_birth -= 1

                                if q == 8 and A[y - 1][x + 1] == 0:
                                    A[y - 1][x + 1] = long_life * 10 + 1
                                    place_birth -= 1

                            counter_no_kids_time_1 = no_kids_time

                if (A[y][x] % 10) == 2 and reproduce_insider_2 == True and counter_no_kids_time_2 == 0:
                    if (A[y][x + 1] % 10) == 2 or (A[y + 1][x + 1] % 10) == 2 or (A[y + 1][x] % 10) == 2 or (
                            A[y + 1][x - 1] % 10) == 2 or (A[y][x - 1] % 10) == 2 or (A[y - 1][x - 1] % 10) == 2 or (
                            A[y - 1][x] % 10) == 2 or (A[y - 1][x + 1] % 10) == 2:
                        if A[y][x + 1] == 0 or A[y + 1][x + 1] == 0 or A[y + 1][x] == 0 or A[y + 1][x - 1] == 0 or A[y][
                            x - 1] == 0 or A[y - 1][x - 1] == 0 or A[y - 1][x] == 0 or A[y - 1][x + 1] == 0:
                            place_birth = 1
                            while place_birth == 1:
                                q = 0
                                q = randint(1, 8)

                                if q == 1 and A[y][x + 1] == 0:
                                    A[y][x + 1] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 2 and A[y + 1][x + 1] == 0:
                                    A[y + 1][x + 1] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 3 and A[y + 1][x] == 0:
                                    A[y + 1][x] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 4 and A[y + 1][x - 1] == 0:
                                    A[y + 1][x - 1] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 5 and A[y][x - 1] == 0:
                                    A[y][x - 1] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 6 and A[y - 1][x - 1] == 0:
                                    A[y - 1][x - 1] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 7 and A[y - 1][x] == 0:
                                    A[y - 1][x] = long_life * 10 + 2
                                    place_birth -= 1

                                if q == 8 and A[y - 1][x + 1] == 0:
                                    A[y - 1][x + 1] = long_life * 10 + 2
                                    place_birth -= 1

                            counter_no_kids_time_2 = no_kids_time

                if reproduce_outsider == True and counter_no_kids_time_3 == 0:
                    if ((A[y][x + 1] % 10) != (A[y][x] % 10) and A[y][x + 1] > 0) or (
                            (A[y + 1][x + 1] % 10) != (A[y][x] % 10) and A[y + 1][x + 1] > 0) or (
                            (A[y + 1][x] % 10) != (A[y][x] % 10) and A[y + 1][x] > 0) or (
                            (A[y + 1][x - 1] % 10) != (A[y][x] % 10) and A[y + 1][x - 1] > 0) or (
                            (A[y][x - 1] % 10) != (A[y][x] % 10) and A[y][x - 1] > 0) or (
                            (A[y - 1][x - 1] % 10) != (A[y][x] % 10) and A[y - 1][x - 1] > 0) or (
                            (A[y - 1][x] % 10) != (A[y][x] % 10) and A[y - 1][x] > 0) or (
                            (A[y - 1][x + 1] % 10) != (A[y][x] % 10) and A[y - 1][x + 1] > 0):
                        if A[y][x + 1] == 0 or A[y + 1][x + 1] == 0 or A[y + 1][x] == 0 or A[y + 1][x - 1] == 0 or A[y][
                            x - 1] == 0 or A[y - 1][x - 1] == 0 or A[y - 1][x] == 0 or A[y - 1][x + 1] == 0:
                            place_birth = 1
                            while place_birth == 1:
                                q = 0
                                q = randint(1, 8)
                                if q == 1 and A[y][x + 1] == 0:
                                    A[y][x + 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 2 and A[y + 1][x + 1] == 0:
                                    A[y + 1][x + 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 3 and A[y + 1][x] == 0:
                                    A[y + 1][x] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 4 and A[y + 1][x - 1] == 0:
                                    A[y + 1][x - 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 5 and A[y][x - 1] == 0:
                                    A[y][x - 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 6 and A[y - 1][x - 1] == 0:
                                    A[y - 1][x - 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 7 and A[y - 1][x] == 0:
                                    A[y - 1][x] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                                if q == 8 and A[y - 1][x + 1] == 0:
                                    A[y - 1][x + 1] = long_life * 10 + (A[y][x] % 10)
                                    place_birth -= 1

                            counter_no_kids_time_3 = no_kids_time

            # Кусок уничтожения
            if x > 0 and y > 0 and x < (WIDTH) and y < (HEIGHT) and A[y][x] > 0 and (
                    kill_outsider_1 == True or kill_outsider_2 == True):
                number_neighbors_outsider = 0
                if A[y][x + 1] > 0 and (A[y][x + 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y + 1][x + 1] > 0 and (A[y + 1][x + 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y + 1][x] > 0 and (A[y + 1][x] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y + 1][x - 1] > 0 and (A[y + 1][x - 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y][x - 1] > 0 and (A[y][x - 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y - 1][x - 1] > 0 and (A[y - 1][x - 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y - 1][x] > 0 and (A[y - 1][x] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1
                if A[y - 1][x + 1] > 0 and (A[y - 1][x + 1] % 10) != (A[y][x] % 10):
                    number_neighbors_outsider += 1

                # Условия уничтожения для первой команды
                if number_neighbors_outsider > 0 and (A[y][x] % 10) == 1 and kill_outsider_1 == True:
                    survivor = number_neighbors_outsider
                    while survivor == number_neighbors_outsider:
                        q = 0
                        q = randint(1, 8)

                        if q == 1 and A[y][x + 1] > 0 and (A[y][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y][x + 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y][x + 1] // 10) * 10
                                    A[y][x + 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y][x + 1] // 10) * 10
                                A[y][x + 1] = 0
                            survivor -= 1

                        if q == 2 and A[y + 1][x + 1] > 0 and (A[y + 1][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x + 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y + 1][x + 1] // 10) * 10
                                    A[y + 1][x + 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y + 1][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y + 1][x + 1] // 10) * 10
                                A[y + 1][x + 1] = 0
                            survivor -= 1

                        if q == 3 and A[y + 1][x] > 0 and (A[y + 1][x] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y + 1][x] // 10) * 10
                                    A[y + 1][x] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y + 1][x] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y + 1][x] // 10) * 10
                                A[y + 1][x] = 0
                            survivor -= 1

                        if q == 4 and A[y + 1][x - 1] > 0 and (A[y + 1][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x - 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y + 1][x - 1] // 10) * 10
                                    A[y + 1][x - 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y + 1][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y + 1][x - 1] // 10) * 10
                                A[y + 1][x - 1] = 0
                            survivor -= 1

                        if q == 5 and A[y][x - 1] > 0 and (A[y][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y][x - 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y][x - 1] // 10) * 10
                                    A[y][x - 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y][x - 1] // 10) * 10
                                A[y][x - 1] = 0
                            survivor -= 1

                        if q == 6 and A[y - 1][x - 1] > 0 and (A[y - 1][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x - 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y - 1][x - 1] // 10) * 10
                                    A[y - 1][x - 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y - 1][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y - 1][x - 1] // 10) * 10
                                A[y - 1][x - 1] = 0
                            survivor -= 1

                        if q == 7 and A[y - 1][x] > 0 and (A[y - 1][x] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y - 1][x] // 10) * 10
                                    A[y - 1][x] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y - 1][x] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y - 1][x] // 10) * 10
                                A[y - 1][x] = 0
                            survivor -= 1

                        if q == 8 and A[y - 1][x + 1] > 0 and (A[y - 1][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x + 1] // 10):
                                    if rob_kill_outsider_1 == True:
                                        A[y][x] += (A[y - 1][x + 1] // 10) * 10
                                    A[y - 1][x + 1] = 0
                                else:
                                    if rob_kill_outsider_2 == True:
                                        A[y - 1][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_1 == True:
                                    A[y][x] += (A[y - 1][x + 1] // 10) * 10
                                A[y - 1][x + 1] = 0
                            survivor -= 1

                            # Условия уничтожения для второй команды
                if number_neighbors_outsider > 0 and (A[y][x] % 10) == 2 and kill_outsider_2 == True:
                    survivor = number_neighbors_outsider
                    while survivor == number_neighbors_outsider:
                        q = 0
                        q = randint(1, 8)

                        if q == 1 and A[y][x + 1] > 0 and (A[y][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y][x + 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y][x + 1] // 10) * 10
                                    A[y][x + 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y][x + 1] // 10) * 10
                                A[y][x + 1] = 0
                            survivor -= 1

                        if q == 2 and A[y + 1][x + 1] > 0 and (A[y + 1][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x + 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y + 1][x + 1] // 10) * 10
                                    A[y + 1][x + 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y + 1][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y + 1][x + 1] // 10) * 10
                                A[y + 1][x + 1] = 0
                            survivor -= 1

                        if q == 3 and A[y + 1][x] > 0 and (A[y + 1][x] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y + 1][x] // 10) * 10
                                    A[y + 1][x] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y + 1][x] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y + 1][x] // 10) * 10
                                A[y + 1][x] = 0
                            survivor -= 1

                        if q == 4 and A[y + 1][x - 1] > 0 and (A[y + 1][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y + 1][x - 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y + 1][x - 1] // 10) * 10
                                    A[y + 1][x - 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y + 1][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y + 1][x - 1] // 10) * 10
                                A[y + 1][x - 1] = 0
                            survivor -= 1

                        if q == 5 and A[y][x - 1] > 0 and (A[y][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y][x - 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y][x - 1] // 10) * 10
                                    A[y][x - 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y][x - 1] // 10) * 10
                                A[y][x - 1] = 0
                            survivor -= 1

                        if q == 6 and A[y - 1][x - 1] > 0 and (A[y - 1][x - 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x - 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y - 1][x - 1] // 10) * 10
                                    A[y - 1][x - 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y - 1][x - 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y - 1][x - 1] // 10) * 10
                                A[y - 1][x - 1] = 0
                            survivor -= 1

                        if q == 7 and A[y - 1][x] > 0 and (A[y - 1][x] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y - 1][x] // 10) * 10
                                    A[y - 1][x] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y - 1][x] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y - 1][x] // 10) * 10
                                A[y - 1][x] = 0
                            survivor -= 1

                        if q == 8 and A[y - 1][x + 1] > 0 and (A[y - 1][x + 1] % 10) != (A[y][x] % 10):
                            if strong_kill_outsider == True:
                                if (A[y][x] // 10) >= (A[y - 1][x + 1] // 10):
                                    if rob_kill_outsider_2 == True:
                                        A[y][x] += (A[y - 1][x + 1] // 10) * 10
                                    A[y - 1][x + 1] = 0
                                else:
                                    if rob_kill_outsider_1 == True:
                                        A[y - 1][x + 1] += (A[y][x] // 10) * 10
                                    A[y][x] = 0
                            else:
                                if rob_kill_outsider_2 == True:
                                    A[y][x] += (A[y - 1][x + 1] // 10) * 10
                                A[y - 1][x + 1] = 0
                            survivor -= 1

                        # Кусок отвечающий за перемещение
    for x in range(1, WIDTH + 1):  # прогоняем по горизонту - Х
        for y in range(1, HEIGHT + 1):  # прогоняем по вертикали - Y
            if A[y][x] > 0:  # х и у не перепутанны, просто так считаются в таком порядке
                q = 0
                q = randint(1, 8)
                if q == 1 and x < (WIDTH) and A[y][x + 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x += 1
                    A[y][x] = -z
                elif q == 2 and x < (WIDTH) and y < (HEIGHT) and A[y + 1][x + 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x += 1
                    y += 1
                    A[y][x] = -z
                elif q == 3 and y < (HEIGHT) and A[y + 1][x] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    y += 1
                    A[y][x] = -z
                elif q == 4 and x > 1 and y < (HEIGHT) and A[y + 1][x - 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x -= 1
                    y += 1
                    A[y][x] = -z
                elif q == 5 and x > 1 and A[y][x - 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x -= 1
                    A[y][x] = -z
                elif q == 6 and x > 1 and y > 1 and A[y - 1][x - 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x -= 1
                    y -= 1
                    A[y][x] = -z
                elif q == 7 and y > 1 and A[y - 1][x] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    y -= 1
                    A[y][x] = -z
                elif q == 8 and x < (WIDTH) and y > 1 and A[y - 1][x + 1] == 0:
                    z = A[y][x]
                    A[y][x] = 0
                    x += 1
                    y -= 1
                    A[y][x] = -z

                # Прогонем матрицй на конвертацию - в +. Так же вычетаем из жизни 1. Проверяем и обнуляем умерших.
    for x in range(1, WIDTH + 1):  # прогоняем по горизонту - Х
        for y in range(1, HEIGHT + 1):  # прогоняем по вертикали - Y
            if A[y][x] < 0:  # х и у не перепутанны, просто так считаются в таком порядке
                A[y][x] = -A[y][x]

    pygame.display.update()


