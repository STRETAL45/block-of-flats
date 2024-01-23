import time

import pygame
import sys
import sqlite3

pygame.init()

screen = pygame.display.set_mode((1023, 571))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

def main_menu():
    background_image = pygame.image.load("img/photo_2023-12-25_18-16-43.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    start()
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        screen.blit(background_image, (0, 0))

        play_button = font.render("Играть", True, WHITE)
        play_button_rect = play_button.get_rect(center=(500, 300))
        exit_button = font.render("Выход", True, WHITE)
        exit_button_rect = exit_button.get_rect(center=(500, 400))

        screen.blit(play_button, play_button_rect)
        screen.blit(exit_button, exit_button_rect)

        pygame.display.flip()

def start():
    win_width = 1023
    win_height = 571
    win = pygame.display.set_mode((win_width, win_height))
    bg_color = (255, 255, 255)
    text_color = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    text = font.render("Майск.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.fill(text_color)
    win.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

    win.fill(text_color)
    text = font.render("20:00, Ленинский район, окраина города.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

    win.fill(text_color)
    text = font.render("Полицейская машина подъезжает к многоэтажному зданию.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)
    text = font.render("Очередное убийство.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 1.8))
    win.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

    win.fill(text_color)
    text = font.render("Ваша задача - найти убийцу.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)
    text = font.render("Или убийц.", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 30))
    win.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

    win.fill(text_color)
    text = font.render("Опросите соседей", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)
    text = font.render("Осмотрите всё, что только можно", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 30))
    win.blit(text, text_rect)
    text = font.render("И не забудьте про улики, разбросанные по зданию", True, bg_color)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 60))
    win.blit(text, text_rect)
    pygame.display.update()

    time.sleep(5)

    game()


def game():
    win_width = 1023
    win_height = 571
    win = pygame.display.set_mode((win_width, win_height))

    bg_img = pygame.image.load('img/photo_2023-12-25_18-19-23.jpg')
    img2 = pygame.image.load('img/2.2.png')
    img3 = pygame.image.load('img/3.png')
    button_img = pygame.image.load('img/3.png')
    key_img = pygame.image.load("img/key.png")
    police_img = pygame.image.load("img/police.png")
    knopka_img = pygame.image.load("img/knopka.png")
    koridor = pygame.image.load("img/koridor.png")
    view_img = pygame.image.load("img/view.png")
    next_img = pygame.image.load("img/next.png")
    room = pygame.image.load("img/room.png")
    kitchen = pygame.image.load("img/kitchen.png")
    room2 = pygame.image.load("img/room2.png")
    hat = pygame.image.load("img/hat.png")
    men_dead = pygame.image.load("img/men.png")
    picture = pygame.image.load("img/im.png")
    locate_kit = pygame.image.load("img/locate2.png")
    women = pygame.image.load("img/women.png")
    locate3 = pygame.image.load("img/locate3.png")
    murder = pygame.image.load("img/old.png")
    paper = pygame.image.load("img/paper.png")
    paper2 = pygame.image.load("img/paper2.png")
    wfinal = pygame.image.load("img/wall.png")
    wfinal2 = pygame.image.load("img/wall2.png")
    women_final = pygame.image.load("img/women_final.png")
    killer_final = pygame.image.load("img/killer_murder.png")
    murder_final = pygame.image.load("img/murder_final.png")
    red_women = pygame.image.load("img/red_kwomen.png")
    red_murder = pygame.image.load("img/red_murder.png")
    red_killer = pygame.image.load("img/red_killer.png")
    final_foto = pygame.image.load("img/final_foto.png")

    red_w_x = 675
    red_w_y = 255

    red_m_x = 466
    red_m_y = 253

    red_k_x = 270
    red_k_y = 263

    bg_x = 0
    bg_y = 0
    img2_x = 700
    img2_y = 100
    img3_x = 250
    img3_y = 300
    button_x = 400
    button_y = 250
    key_img_x = 0
    key_img_y = 0
    police_img_x = 150
    police_img_y = 110
    knopka_img_x = 900
    knopka_img_y = 40
    koridor_x = 0
    koridor_y = 0
    view_img_x = 50
    view_img_y = 480
    next_img_x = 873
    next_img_y = 480
    room_x = 0
    room_y = 0
    kitchen_x = 0
    kitchen_y = 0
    room2_x = 0
    room2_y = 0
    hat_x = 370
    hat_y = 370
    men_x = 260
    men_y = 280
    p_x = 500
    p_y = 280
    locate_kit_x = 0
    locate_kit_y = 0
    women_x = 800
    women_y = 140
    locate3_x = 0
    locate3_y = 0
    murder_x = 800
    murder_y = 140
    paper_x = 660
    paper_y = 200
    wall_x = 0
    wall_y = 0

    show_img3 = False
    show_text2 = False
    show_button = False
    show_img2 = True
    show_img2_2 = False
    show_key = False
    kor = False
    hat_show = True
    hat_dialog = False
    kor_dialog = False
    men = False
    men_dialog = False
    room_dialog = False
    kitchen_dialog = False
    kitc = False
    room_img = False
    room2_show = False
    room2_dialog = False
    room2_im = False
    picture_dialog = False
    locate_kit_img = False
    women_dialog = False
    show_women = False
    police_dialog = False
    view_dialog = False
    women_dialog2 = False
    police_dialog2 = False
    women_dialog3 = False
    locatee_3 = False
    show_murder = False
    dialog_murder = False
    dialog_mp = False
    dialog_murder2 = False
    dialog_mp2 = False
    dialog_murder3 = False
    show_paper = False
    paper_dialog = False
    locate4 = False
    locate5 = False
    answer1 = False
    answer2 = False
    answer3 = False
    locate6 = False

    def redraw_game_window():
        win.blit(bg_img, (bg_x, bg_y))
        if show_img2:
            win.blit(img2, (img2_x, img2_y))
        if show_img3:
            win.blit(img3, (img3_x, img3_y))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Житель 1", True, (255, 255, 255))
            win.blit(text, (img3_x + 5, img3_y - 40))
            if not show_text2:
                text = font.render("Боже, наконец-то вы приехали!", True, (0, 0, 0))
                win.blit(text, (img3_x + 40, img3_y + 40))
                text = font.render("Я - соседка погибшего.", True, (0, 0, 0))
                win.blit(text, (img3_x + 40, img3_y + 70))
                text = font.render("Это я вас вызвала.", True, (0, 0, 0))
                win.blit(text, (img3_x + 40, img3_y + 100))
            else:
                text = font.render("Берите ключи и быстрее в", True, (0, 0, 0))
                win.blit(text, (img3_x + 40, img3_y + 40))
                text = font.render("квартиру!", True, (0, 0, 0))
                win.blit(text, (img3_x + 40, img3_y + 70))
        elif show_button:
            win.blit(police_img, (police_img_x, police_img_y))
            win.blit(button_img, (button_x, button_y))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Полицейский", True, (255, 255, 255))
            win.blit(text, (button_x + 5, button_y - 40))
            text = font.render("Что? Какие ключи?", True, (0, 0, 0))
            win.blit(text, (button_x + 40, button_y + 40))
            text = font.render("Что здесь происходит?", True, (0, 0, 0))
            win.blit(text, (button_x + 40, button_y + 70))
        elif show_img2_2:
            win.blit(img3, (img3_x, img3_y))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Житель 1", True, (255, 255, 255))
            win.blit(text, (img3_x + 5, img3_y - 40))
            text = font.render("Ой, простите. Просто покойный - ", True, (0, 0, 0))
            win.blit(text, (img3_x + 40, img3_y + 30))
            text = font.render("человек очень занятой.", True, (0, 0, 0))
            win.blit(text, (img3_x + 40, img3_y + 60))
            text = font.render("Часто уезжал надолго.", True, (0, 0, 0))
            win.blit(text, (img3_x + 40, img3_y + 90))
            text = font.render("Вот и оставлял мне ключи.", True, (0, 0, 0))
            win.blit(text, (img3_x + 40, img3_y + 120))
            text = font.render("Он у нас известный ботаник!", True, (0, 0, 0))
            win.blit(text, (img3_x + 40, img3_y + 150))
        if show_key:
            win.blit(key_img, (key_img_x, key_img_y + 50))
            win.blit(knopka_img, (knopka_img_x, knopka_img_y))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Добавлена новая улика. Ключи.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 500)))
        pygame.display.update()

    def show_black_screen_with_number():
        bg_color = (255, 255, 255)
        text_color = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        text = font.render("КВАРТИРА 32", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.fill(text_color)
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        text = font.render("ПРИХОЖАЯ", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        pygame.display.update()
        show_black_screen_with_number2()

    def show_black_screen_with_number2():
        if kor:
            win.blit(koridor, (koridor_x, koridor_y))
            win.blit(next_img, (next_img_x, next_img_y))
            win.blit(view_img, (view_img_x, view_img_y))
            if kor_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Странно... Вещи не тронуты. ", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Кому же потребовалось", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("убивать старика?", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
            if hat_show:
                hat2 = pygame.transform.scale(hat, (70, 70))
                win.blit(hat2, (hat_x, hat_y))
        pygame.display.update()

    def show_hat_dialog():
        if hat_dialog:
            hat2 = pygame.transform.scale(hat, (500, 500))
            win.blit(hat2, (300, 0))
            win.blit(knopka_img, (knopka_img_x, knopka_img_y))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Добавлена новая улика. Старая шапка.", True, (0, 0, 0))
            win.blit(text, text.get_rect(center=(win_width // 2, 501)))
            text = font.render("Видимо, преступник забыл ее здесь.", True, (0, 0, 0))
            win.blit(text, text.get_rect(center=(win_width // 2, 530)))

        pygame.display.update()

    def show_room():
        if room_img:
            win.blit(room, (room_x, room_y))
            win.blit(next_img, (next_img_x, next_img_y))
            win.blit(view_img, (view_img_x, view_img_y))
            if room_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Порезы на теле не глубокие.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Скорее всего использовали", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("кухонный нож. Надо бы", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
                text = font.render("опросить соседей.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 130))
            if men:
                men_dead2 = pygame.transform.scale(men_dead, (300, 150))
                win.blit(men_dead2, (men_x, men_y))
        pygame.display.update()

    def show_men_dialog():
        if men_dialog:
            win.blit(knopka_img, (knopka_img_x, knopka_img_y))
            men_dead2 = pygame.transform.scale(men_dead, (500, 250))
            win.blit(men_dead2, men_dead2.get_rect(center=(win_width // 2, 300)))
            text = font.render("Добавлена новая улика. Труп мужчины.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 460)))
            text = font.render("На теле заметны ножевые ранения.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 490)))
            text = font.render("Предположительное время смерти: 01:00.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 520)))
        pygame.display.update()

    def show_kitchen():
        if kitc:
            win.blit(kitchen, (kitchen_x, kitchen_y))
            win.blit(next_img, (next_img_x, next_img_y))
            win.blit(view_img, (view_img_x, view_img_y))
            if kitchen_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("На столе уже остывшая", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("еда. Две тарелки, видимо,", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("он кого-то ждал...", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
        pygame.display.update()

    def show_room2():
        if room2_show:
            win.blit(room2, (room2_x, room2_y))
            win.blit(next_img, (next_img_x, next_img_y))
            win.blit(view_img, (view_img_x, view_img_y))
            if room2_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Пустой цветочный горшок.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Много книг по ботанике. Хм...", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("Газета за прошлую неделю", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
                text = font.render("Прорыв в ботанике.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 130))
            if room2_im:
                win.blit(final_foto, (p_x, p_y))
        pygame.display.update()

    def show_picture():
        if picture_dialog:
            win.blit(knopka_img, (knopka_img_x, knopka_img_y))
            picture2 = pygame.transform.scale(picture, (300, 300))
            win.blit(picture2, picture2.get_rect(center=(win_width // 2, 300)))
            text = font.render("Добавлена новая улика. Фотография", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 460)))
            text = font.render("На снимке изображен еще живой владелец", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 490)))
            text = font.render("квартиры и кто-то еще...", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 520)))
        pygame.display.update()

    def black_screen2():
        bg_color = (255, 255, 255)
        text_color = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        text = font.render("Вы покидаете квартиру. Пришло время опросить соседей.", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.fill(text_color)
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        text = font.render("КВАРТИРА 22", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        pygame.display.update()
        show_locate2()

    def show_locate2():
        if locate_kit_img:
            locate_kit2 = pygame.transform.scale(locate_kit, (1024, 571))
            win.blit(locate_kit2, (locate_kit_x, locate_kit_y))
            if show_women:
                win.blit(women, (women_x, women_y))
            if women_dialog:
                win.blit(img3, (img3_x, img3_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 2", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Добрый вечер!", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
                text = font.render("Чем могу помочь?", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 70))
            if police_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Я тут по делу вашего соседа... ", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Прошлой ночью его убили. У вас", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("очень тонкие стены. Вы ничего", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
                text = font.render("странного не слышали?", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 130))
            if view_dialog:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                win.blit(view_img, (view_img_x, view_img_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("На кухне нет ничего необычного.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Да и женщина выглядит", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("приветливой. На столе ", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
                text = font.render("пачка снотворного. Пустая.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 130))
            if women_dialog2:
                win.blit(img3, (img3_x, img3_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 2", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Знаете... Все было тихо. Хотя я", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
                text = font.render("очень крепко сплю. Могла", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 70))
                text = font.render("и не услышать, как кто-то", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 100))
                text = font.render("входил в 32 квартиру.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 130))
            if police_dialog2:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Хорошо. Спасибо.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Если что-то узнаете, обязательно", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
                text = font.render("сообщите.", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 100))
            if women_dialog3:
                win.blit(view_img, (view_img_x, view_img_y))
                win.blit(next_img, (next_img_x, next_img_y))
                win.blit(img3, (img3_x, img3_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 2", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Буду только рада.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
        pygame.display.update()

    def black_screen3():
        bg_color = (255, 255, 255)
        text_color = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        text = font.render("Пора возвращаться в участок.", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.fill(text_color)
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        text = font.render("Как вдруг вы замечаете...", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        show_locate3()

        pygame.display.update()

    def show_locate3():
        if locatee_3:
            win.blit(locate3, (locate3_x, locate3_y))
            if show_murder:
                win.blit(murder, (murder_x, murder_y))
            if dialog_murder:
                win.blit(img3, (img3_x, img3_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 3", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Здравствуйте...", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
                text = font.render("Вы уже уходите?", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 70))
                text = font.render("Так быстро?", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 100))
            if dialog_mp:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Да. А вы собственно говоря...", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
                text = font.render("Кто?", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 70))
            if dialog_murder2:
                win.blit(img3, (img3_x, img3_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 3", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Я - близкий друг Сергея. Был", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
                text = font.render("им. Я слышал, что произошло.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 70))
                text = font.render("Он был моим коллегой.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 100))
                text = font.render("Часто работали вместе.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 130))
            if dialog_mp2:
                win.blit(police_img, (police_img_x, police_img_y))
                win.blit(button_img, (button_x, button_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Полицейский", True, (255, 255, 255))
                win.blit(text, (button_x + 5, button_y - 40))
                text = font.render("Вы знаете что произошло?", True, (0, 0, 0))
                win.blit(text, (button_x + 40, button_y + 40))
            if dialog_murder3:
                win.blit(img3, (img3_x, img3_y))
                win.blit(next_img, (next_img_x, next_img_y))
                font = pygame.font.SysFont(None, 40)
                text = font.render("Житель 3", True, (255, 255, 255))
                win.blit(text, (img3_x + 5, img3_y - 40))
                text = font.render("Ничем не могу помочь.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 40))
                text = font.render("Простите.", True, (0, 0, 0))
                win.blit(text, (img3_x + 60, img3_y + 70))
            if show_paper:
                win.blit(paper, (paper_x, paper_y))
        if paper_dialog:
            win.blit(locate3, (locate3_x, locate3_y))
            win.blit(knopka_img, (knopka_img_x, knopka_img_y))
            win.blit(paper2, paper2.get_rect(center=(win_width // 2, 250)))
            font = pygame.font.SysFont(None, 40)
            text = font.render("Добавлена новая улика. Записка должников.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 481)))
            text = font.render("Интересно, что это за числа.", True, (255, 255, 255))
            win.blit(text, text.get_rect(center=(win_width // 2, 511)))
        pygame.display.update()

    def black_screen4():
        bg_color = (255, 255, 255)
        text_color = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        text = font.render("Теперь точно пора возвращаться в участок.", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.fill(text_color)
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        text = font.render("Пока вы едете в участок, в машине играет радио.", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        text = font.render("Новое морозостойкое растение было создано в России, в городе Майск.", True, bg_color)
        text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        win.fill(text_color)
        show_locate4()
        pygame.display.update()

    def show_locate4():
        winer = [1, 2]
        answer_game = []
        if locate4:
            win.blit(wfinal, (wall_x, wall_y))
            win.blit(next_img, (next_img_x, next_img_y))
            conn = sqlite3.connect('items.db')
            cursor = conn.cursor()
            cursor.execute("SELECT path FROM items")
            images_data = cursor.fetchall()

            li1 = [(35, 270), (260, 270), (460, 270), (660, 270), (880, 270)]
            loaded_images = [pygame.image.load(image[0]) for image in images_data]
            for i in range(len(loaded_images)):
                win.blit(loaded_images[i], li1[i])


        if locate5:
            win.blit(wfinal2, (wall_x, wall_y))
            win.blit(next_img, (next_img_x, next_img_y))

            win.blit(killer_final, (270, 263))
            win.blit(murder_final, (466, 253))
            win.blit(women_final, (675, 255))
            if answer1:
                win.blit(red_killer, (270, 263))
                answer_game.append(1)
                pygame.display.update()

            if answer2:
                win.blit(red_murder, (466, 253))
                answer_game.append(2)
            pygame.display.update()

            if answer3:
                win.blit(red_women, (675, 255))
                answer_game.append(3)
                pygame.display.update()

            if locate6:
                if winer == sorted(answer_game):
                    bg_color = (255, 255, 255)
                    text_color = (0, 0, 0)
                    font = pygame.font.Font(None, 36)
                    text = font.render("ПОБЕДА!", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
                    win.fill(text_color)

                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT COUNT(*) FROM items')
                    count = cursor.fetchone()[0]
                    text = font.render(f"Найдено улик: {count}/5", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 50))
                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    c = conn.cursor()
                    c.execute('DELETE FROM items')
                    conn.commit()
                    conn.close()
                elif sorted(answer_game) == [1, 3] or sorted(answer_game) == [2, 3] or answer_game == [1] or answer_game == [2]:
                    bg_color = (255, 255, 255)
                    text_color = (0, 0, 0)
                    font = pygame.font.Font(None, 36)
                    text = font.render("УБИЙЦА ОСТАЛСЯ НА СВОБОДЕ!", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
                    win.fill(text_color)

                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT COUNT(*) FROM items')
                    count = cursor.fetchone()[0]
                    text = font.render(f"Найдено улик: {count}/5", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 50))
                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    c = conn.cursor()
                    c.execute('DELETE FROM items')
                    conn.commit()
                    conn.close()
                else:
                    bg_color = (255, 255, 255)
                    text_color = (0, 0, 0)
                    font = pygame.font.Font(None, 36)
                    text = font.render("УБИЙЦЫ ОСТАЛИСЬ НА СВОБОДЕ!", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
                    win.fill(text_color)
                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT COUNT(*) FROM items')
                    count = cursor.fetchone()[0]
                    text = font.render(f"Найдено улик: {count}/5", True, bg_color)
                    text_rect = text.get_rect(center=(win_width // 2, win_height // 2 + 50))
                    win.blit(text, text_rect)
                    conn = sqlite3.connect('items.db')
                    c = conn.cursor()
                    c.execute('DELETE FROM items')
                    conn.commit()
                    conn.close()



        pygame.display.update()




    run = True
    click_count = 0
    women_count = 0
    murder_count = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (show_img2 and img2_x < mouse_x < img2_x + img2.get_width()
                        and img2_y < mouse_y < img2_y + img2.get_height()):
                    click_count += 1
                    if click_count == 3:
                        show_img2 = False
                        show_img3 = False
                        show_text2 = False
                        show_button = True
                    else:
                        if not show_img3 and click_count == 1:
                            show_img3 = True

                        elif show_img3 and click_count == 2:
                            show_text2 = not show_text2

                    if click_count == 5:
                        show_key = True
                        show_img2 = False
                        show_img3 = False
                        show_text2 = False
                        show_button = False
                        show_img2_2 = False
                        conn = sqlite3.connect('items.db')
                        cursor = conn.cursor()
                        object_name = "ключ"
                        cursor.execute("SELECT * FROM items WHERE name=?", (object_name,))
                        existing_object = cursor.fetchone()
                        if existing_object is None:
                            new_object = ("ключ", "img/final_key.png")
                            cursor.execute('INSERT INTO items (name, path) VALUES (?, ?)', new_object)
                        conn.commit()
                        conn.close()

                elif show_button and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    click_count += 1
                    if click_count == 4:
                        show_img2_2 = True
                        show_img2 = True
                        show_img3 = False
                        show_text2 = False
                        show_button = False

                elif (show_key and knopka_img_x < mouse_x < knopka_img_x + knopka_img.get_width() and
                      knopka_img_y < mouse_y < knopka_img_y + knopka_img.get_height()):
                    show_key = False
                    click_count += 1
                    if click_count == 6:
                        kor = True
                    show_black_screen_with_number()

                elif (hat_show and hat_x < mouse_x < hat_x + pygame.transform.scale(hat, (500, 500)).get_width() and
                      hat_y < mouse_y < hat_y + pygame.transform.scale(hat, (500, 500)).get_height()):
                    hat_dialog = True
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    object_name = "шапка"
                    cursor.execute("SELECT * FROM items WHERE name=?", (object_name,))
                    existing_object = cursor.fetchone()

                    if existing_object is None:
                        new_object = ("шапка", "img/final_hat.png")
                        cursor.execute('INSERT INTO items (name, path) VALUES (?, ?)', new_object)
                    conn.commit()
                    conn.close()
                    show_hat_dialog()

                elif (hat_dialog and knopka_img_x < mouse_x < knopka_img_x + knopka_img.get_width() and
                      knopka_img_y < mouse_y < knopka_img_y + knopka_img.get_height()):
                    show_black_screen_with_number2()

                elif (kor and view_img_x < mouse_x < view_img_x + view_img.get_width() and
                      view_img_y < mouse_y < view_img_y + view_img.get_height()):
                    kor_dialog = True
                    hat_show = False
                    show_black_screen_with_number2()

                elif kor_dialog and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    kor_dialog = False
                    hat_show = True
                    show_black_screen_with_number2()

                elif (room_img and men and men_x < mouse_x < men_x + men_dead.get_width() and
                      men_y < mouse_y < men_y + men_dead.get_height()):
                    men_dialog = True
                    men = False

                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    object_name = "труп"
                    cursor.execute("SELECT * FROM items WHERE name=?", (object_name,))
                    existing_object = cursor.fetchone()

                    if existing_object is None:
                        new_object = ("труп", "img/men_final.png")
                        cursor.execute('INSERT INTO items (name, path) VALUES (?, ?)', new_object)
                    conn.commit()
                    conn.close()
                    show_hat_dialog()
                    show_men_dialog()

                elif (room_img and men_dialog and knopka_img_x < mouse_x < knopka_img_x + knopka_img.get_width() and
                      knopka_img_y < mouse_y < knopka_img_y + knopka_img.get_height()):
                    men = True
                    show_room()

                elif (room_img and view_img_x < mouse_x < view_img_x + view_img.get_width() and
                      view_img_y < mouse_y < view_img_y + view_img.get_height()):
                    room_dialog = True
                    men = False
                    show_room()

                elif room_dialog and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    men = True
                    room_dialog = False
                    show_room()

                elif kitc and view_img_x < mouse_x < view_img_x + view_img.get_width() and view_img_y < mouse_y < view_img_y + view_img.get_height():
                    kitchen_dialog = True
                    show_kitchen()

                elif kitc and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    kitchen_dialog = False
                    show_kitchen()

                elif room2_show and view_img_x < mouse_x < view_img_x + view_img.get_width() and view_img_y < mouse_y < view_img_y + view_img.get_height():
                    room2_dialog = True
                    room2_im = False
                    show_room2()

                elif room2_show and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    room2_dialog = False
                    room2_im = True
                    show_room2()

                elif locate_kit_img and show_women and women_x < mouse_x < women_x + women.get_width() and women_y < mouse_y < women_y + women.get_height() or (
                        locate_kit_img and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height()) and view_dialog == False:
                    women_count += 1
                    if women_count == 1:
                        women_dialog = True
                    if women_count == 2:
                        women_dialog = False
                        show_women = False
                        police_dialog = True
                    if women_count == 3:
                        show_women = True
                        police_dialog = False
                        women_dialog2 = True
                    if women_count == 4:
                        show_women = False
                        women_dialog2 = False
                        police_dialog2 = True
                    if women_count == 5:
                        show_women = True
                        police_dialog2 = False
                        women_dialog3 = True
                    show_locate2()

                elif (women_dialog3 and view_img_x < mouse_x < view_img_x + view_img.get_width() and
                      view_img_y < mouse_y < view_img_y + view_img.get_height()):
                    show_women = False
                    view_dialog = True
                    women_dialog3 = False
                    show_locate2()

                elif view_dialog and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height():
                    show_women = True
                    women_dialog3 = True
                    view_dialog = False
                    show_locate2()

                elif (locatee_3 and murder_x < mouse_x < mouse_x + murder.get_width() and
                      murder_y < mouse_y < murder_y + murder.get_height()) or (
                        locatee_3 and police_img_x < mouse_x < police_img_x + police_img.get_width() and police_img_y < mouse_y < police_img_y + police_img.get_height() and dialog_murder is False and
                        dialog_murder2 is False and dialog_murder3 is False):
                    murder_count += 1
                    if murder_count == 1:
                        dialog_murder = True
                    if murder_count == 2:
                        dialog_murder = False
                        show_murder = False
                        dialog_mp = True
                        show_paper = False
                    if murder_count == 3:
                        dialog_murder2 = True
                        show_murder = True
                        dialog_mp = False
                        show_paper = True
                    if murder_count == 4:
                        dialog_murder2 = False
                        show_murder = False
                        dialog_mp2 = True
                        show_paper = False
                    if murder_count == 5:
                        dialog_mp2 = False
                        show_murder = True
                        dialog_murder3 = True
                        show_paper = True
                    show_locate3()

                elif(show_paper and paper_x < mouse_x < paper_x + paper.get_width() and
                      paper_y < mouse_y < paper_y + paper.get_height()):
                    paper_dialog = True
                    locatee_3 = False
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    object_name = "записка"
                    cursor.execute("SELECT * FROM items WHERE name=?", (object_name,))
                    existing_object = cursor.fetchone()

                    if existing_object is None:
                        new_object = ("записка", "img/final_paper.png")
                        cursor.execute('INSERT INTO items (name, path) VALUES (?, ?)', new_object)
                    conn.commit()
                    conn.close()
                    show_locate3()

                elif (paper_dialog and knopka_img_x < mouse_x < knopka_img_x + knopka_img.get_width() and
                      knopka_img_y < mouse_y < knopka_img_y + knopka_img.get_height()):
                    locatee_3 = True
                    paper_dialog = False
                    show_locate3()

                if (room2_im and p_x < mouse_x < p_x + final_foto.get_width() and
                      p_y < mouse_y < p_y + final_foto.get_height()):
                    picture_dialog = True
                    conn = sqlite3.connect('items.db')
                    cursor = conn.cursor()
                    object_name = "картина"
                    cursor.execute("SELECT * FROM items WHERE name=?", (object_name,))
                    existing_object = cursor.fetchone()

                    if existing_object is None:
                        new_object = ("картина", "img/final_foto.png")
                        cursor.execute('INSERT INTO items (name, path) VALUES (?, ?)', new_object)
                    conn.commit()
                    conn.close()
                    show_picture()

                if (picture_dialog and knopka_img_x < mouse_x < knopka_img_x + knopka_img.get_width() and
                      knopka_img_y < mouse_y < knopka_img_y + knopka_img.get_height()):
                    picture_dialog = False
                    show_room2()

                if locate5 and red_k_x < mouse_x < red_k_x + red_killer.get_width() and red_k_y < mouse_y < red_k_y + red_killer.get_height():
                    answer1 = True
                    show_locate4()

                if locate5 and red_m_x < mouse_x < red_m_x + red_murder.get_width() and red_m_y < mouse_y < red_m_y + red_murder.get_height():
                    answer2 = True
                    show_locate4()

                if locate5 and red_w_x < mouse_x < red_w_x + red_women.get_width() and red_w_y < mouse_y < red_w_y + red_women.get_height():
                    answer3 = True
                    show_locate4()

                if locate4 and next_img_x < mouse_x < next_img_x + next_img.get_width() and next_img_y < mouse_y < next_img_y + next_img.get_height():
                    locate5 = True
                    locate4 = False
                    show_locate4()


                elif next_img_x < mouse_x < next_img_x + next_img.get_width() and next_img_y < mouse_y < next_img_y + next_img.get_height() and view_dialog is False and locate4 is False:
                    click_count += 1
                    if click_count == 7:
                        kor = False
                        hat_dialog = False
                        hat_show = False
                        men = True
                        room_img = True
                        show_room()
                    if click_count == 8:
                        room_img = False
                        men = False
                        kitc = True
                        show_kitchen()
                    if click_count == 9:
                        kitc = False
                        room2_show = True
                        room2_im = True
                        show_room2()
                    if click_count == 10:
                        room2_im = False
                        room2_show = False
                        locate_kit_img = True
                        show_women = True
                        black_screen2()
                    if click_count == 11:
                        locate_kit_img = False
                        show_women = False
                        locatee_3 = True
                        show_murder = True
                        show_paper = True
                        black_screen3()
                    if click_count == 12:
                        locatee_3 = False
                        locate4 = True
                        black_screen4()
                    if click_count == 13:
                        locate6 = True
                        show_locate4()


        if click_count < 6:
            redraw_game_window()



main_menu()
