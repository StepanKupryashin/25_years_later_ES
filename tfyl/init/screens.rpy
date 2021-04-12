# -*- coding: utf-8 -*-
init:
    style tfyl_button is default
    style tfyl_button_text is default:
        color '#666565'
        hover_color '#1B1A1A'
        font 'mods/tfyl/fonts/Caveat.ttf'
        size 50
        outlines [( 1, '#1B1A1A', 1, 1)]

    style tfyl_frame is default

    transform tfyl_button_hover:
        on idle:
            ease .75 zoom 1 alpha .8
        on hover:
            ease .75 zoom 1.2 alpha 1.0

    screen tfyl_menu_bg():
        add im.Blur("mods/tfyl/gui/main_menu.png", 1.5):
            at transform:
                zoom 1.2 xalign .4 yalign .4
                parallel:
                    choice:
                        ease 15 zoom 1.4
                    choice:
                        ease 15 zoom 1.2
                    repeat
                parallel:
                    choice:
                        ease 5.0 xalign .4
                    choice:
                        ease 5.0 xalign .45
                    choice:
                        ease 5.0 xalign .5
                    choice:
                        ease 5.0 xalign .55
                    choice:
                        ease 5.0 xalign .6
                    repeat
                parallel:
                    choice:
                        ease 3.5 yalign .4
                    choice:
                        ease 3.5 yalign .45
                    choice:
                        ease 4.0 yalign .5
                    choice:
                        ease 3.5 yalign .55
                    choice:
                        ease 3.5 yalign .6
                    repeat

    screen tfyl_main_menu():

        tag menu
        modal True

        style_prefix "tfyl"

        key "game_menu":
            action NullAction()


        use tfyl_menu_bg

        vbox:
            spacing 20
            xpos .05
            yalign .5

            textbutton "Начать" action (Hide("menu", fade3), Jump("tfyl_start")) at tfyl_button_hover
            textbutton "Загрузить" action ShowMenu('tfyl_load') at tfyl_button_hover
            textbutton "Настройки" action ShowMenu('tfyl_preferences') at tfyl_button_hover
            textbutton "Выход" action ShowMenu("tfyl_exit", full=False) at tfyl_button_hover


    screen tfyl_game_menu_selector():

        tag menu
        modal True

        style_prefix "tfyl"


        add "mods/tfyl/gui/game_menu.png" align (.5, .5)

        vbox:
            spacing 5
            align (.5, .5)

            textbutton "В главное меню" text_size 36 action ShowMenu("tfyl_exit", full=False)
            textbutton "Сохранить" text_size 36 action ShowMenu('save')
            textbutton "Загрузить" text_size 36 action ShowMenu('tfyl_load')
            textbutton "Настройки" text_size 36 action ShowMenu('tfyl_preferences')
            textbutton "Выход" text_size 36 action ShowMenu("tfyl_exit")

    screen tfyl_exit(full=True):
        modal True
        tag menu

        style_prefix "tfyl"

        key "game_menu":
            action Return()

        use tfyl_menu_bg

        text "Ты хочешь уйти?":
            size 100

            xalign 0.7
            yalign 0.33

            antialias True
            kerning 2

        hbox:
            xpos 0.55
            ypos 0.55
            spacing 80

            textbutton "Да" text_size 70 action (Hide("tfyl_exit", fade), (Quit(False) if full else Jump("tfyl_true_exit"))) at tfyl_button_hover
            textbutton "Нет" text_size 70 action Return()  at tfyl_button_hover


    screen tfyl_say(who=None, what=""):

        $ timeofday = persistent.timeofday

        window id "window":
            background None

        if persistent.font_size == "large":

            imagebutton auto "mods/tfyl/gui/dialogue_box/backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

            add "mods/tfyl/gui/dialogue_box/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton auto "mods/tfyl/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 883 action HideInterface()
            imagebutton auto "mods/tfyl/gui/dialogue_box/save_%s.png" xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto "mods/tfyl/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/tfyl/gui/dialogue_box/load_%s.png" xpos 1682 ypos 883 action ShowMenu('tfyl_load')

            if not config.skipping:
                imagebutton auto "mods/tfyl/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 924 action Skip()
            else:
                imagebutton auto "mods/tfyl/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1 font 'mods/tfyl/fonts/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

        elif persistent.font_size == "small":

            imagebutton auto "mods/tfyl/gui/dialogue_box/backward_%s.png" xpos 38 ypos 949 action ShowMenu("text_history")

            add "mods/tfyl/gui/dialogue_box/dialogue_box.png" xpos 174 ypos 916

            imagebutton auto "mods/tfyl/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 933 action HideInterface()
            imagebutton auto "mods/tfyl/gui/dialogue_box/save_%s.png" xpos 1567 ypos 933 action ShowMenu('save')
            imagebutton auto "mods/tfyl/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/tfyl/gui/dialogue_box/load_%s.png" xpos 1682 ypos 933 action ShowMenu('tfyl_load')

            if not config.skipping:
                imagebutton auto "mods/tfyl/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 949 action Skip()
            else:
                imagebutton auto "mods/tfyl/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2 font 'mods/tfyl/fonts/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 931 size 28 line_spacing 2


    screen tfyl_load():

        style_prefix "tfyl"
        modal True
        tag menu

        key "game_menu":
            action NullAction()
        key "K_ESCAPE" action Return()

        use tfyl_menu_bg

        $ FilePage("tfyl_FilePage_1")()
        $ selected_slot = False

        # textbutton 'Закрыть' xalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
        #     action Return()
        # textbutton ["Загрузить игру"]:
        #     text_style "y_25_l_menu_btn"
        #     style "y_25_l_menu_btn"
        #     ypos 850
        #     xalign 0.2
        #     action (tfyl.change_time, FileLoad(selected_slot))


        # grid 4 3:
        #     xpos 0.12
        #     ypos 0.15
        #     xmaximum 0.81
        #     ymaximum 0.65
        #     transpose False
        #     xfill True
        #     yfill True
        #     for i in range(1, 13):
        #         fixed:
        #             add FileScreenshot(i):
        #                 xpos 10
        #                 ypos 10
        #             button:
        #                 action SetVariable("selected_slot", i)
        #                 xfill False
        #                 yfill False
        #                 style "tfyl_file_slots_button"
        #                 fixed:
        #                     text ( "%s." % i
        #                            + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
        #                            + "\n" +FileSaveName(i)):
        #                         xpos 15
        #                         ypos 15

        textbutton '>' xalign 0.95 yalign 0.5 text_size 80 at tfyl_button_hover:
            action ShowMenu("preferences")
        textbutton '<' xalign 0.05 yalign 0.5 text_size 80 at tfyl_button_hover:
            action ShowMenu("preferences" if main_menu else "save")

    style tfyl_file_slots_button is default:
        background "mods/tfyl/gui/file_slots/file_slots_idle.png"
        hover_background "mods/tfyl/gui/file_slots/file_slots_hover.png"
        selected_background "mods/tfyl/gui/file_slots/file_slots_selected.png"

    screen tfyl_preferences():

        style_prefix "tfyl"
        modal True
        tag menu

        key "game_menu":
            action NullAction()
        key "K_ESCAPE" action Return()

        use tfyl_menu_bg

        label "Настройки"

        vbox align (0.2,0.5):
            text "Режим экрана" size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Оконный" text_size 35 at tfyl_button_hover:
                    action Preference("display","window")
                textbutton "Полноэкранный" text_size 35 at tfyl_button_hover:
                    action Preference("display","fullscreen")
            null height 40
            text "Пропускать" size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Всё" text_size 35 at tfyl_button_hover:
                    action Preference("skip","all")
                textbutton "Что увидел" text_size 35 at tfyl_button_hover:
                    action Preference("skip","seen")
            null height 40
            text "Размер шрифта" size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Обычный" text_size 35 at tfyl_button_hover:
                    action SetField(persistent,"font_size","small")
                textbutton "Большой" text_size 35 at tfyl_button_hover:
                    action SetField(persistent,"font_size","large")
            null height 40
            text "Скорость текста" size 45 xalign 0.5
            null height 10
            bar value Preference("text speed") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
        vbox align (0.8,0.5):
            text "Автопереход" size 45 xalign 0.5
            null height 10
            hbox spacing 10 xalign 0.5:
                textbutton "Включить" text_size 35 at tfyl_button_hover:
                    action [If(preferences.afm_time == 0,true=Preference("auto-forward time", 20)),Preference("auto-forward after click","enable"),SelectedIf(preferences.afm_time != 0 or preferences.afm_after_click == "enable")]
                textbutton "Выключить" text_size 35 at tfyl_button_hover:
                    action [Preference("auto-forward time", 0),Preference("auto-forward after click","disable"),SelectedIf(preferences.afm_time == 0 or preferences.afm_after_click == "disable")]
            bar value Preference("auto-forward time") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            text "Музыка" size 45 xalign 0.5
            null height 10
            bar value Preference("music volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            text "Звуки" size 45 xalign 0.5
            null height 10
            bar value Preference("sound volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            text "Эмбиент" size 45 xalign 0.5
            null height 10
            bar value Preference("voice volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            textbutton "Без звука" text_size 35 xalign 0.5 at tfyl_button_hover:
                action Preference("all mute", "toggle")

        textbutton '>' xalign 0.95 yalign 0.5 text_size 80 at tfyl_button_hover:
            action ShowMenu("load" if main_menu else "save")
        textbutton '<' xalign 0.05 yalign 0.5 text_size 80 at tfyl_button_hover:
            action ShowMenu("load")

    screen tfyl_check_version():

        # Этот экран нужен что бы восстанавливать все остальные экраны мода

        $ scr = renpy.get_screen("say")
        if scr:
            $ scr = scr.screen_name[0]
            if scr != "tfyl_say":
                $ tfyl_after_load()


    screen tfyl_choice(items, *args):


        for caption, action, chosen in items:

            if action:
                textbutton caption pos (action.args[0] if action.args else (.5, .5)) action action style "tfyl_choice_button" text_style "tfyl_choice_button_text"

    style tfyl_choice_button is default
    style tfyl_choice_button_text is default:

        font "fonts/PressStart2P.ttf"
        size 150
        color "A44"
        hover_color "F88"




label tfyl_index:

    stop music fadeout 3
    scene bg black with fade2
    play music tfyl_main_theme fadein 4

    $ tfyl_init()
    window hide
    pause .3

    call screen tfyl_main_menu with fade2

    pause
    jump tfyl_index

label tfyl_true_exit:

    window hide dissolve
    stop music fadeout 3
    scene black with fade
    pause 1
    $ MainMenu(confirm=False)()
