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
                        ease 4.0 xalign .3
                    choice:
                        ease 4.0 xalign .4
                    choice:
                        ease 4.0 xalign .5
                    choice:
                        ease 4.0 xalign .5
                    choice:
                        ease 4.0 xalign .7
                    repeat
                parallel:
                    choice:
                        ease 3 yalign .3
                    choice:
                        ease 3 yalign .4
                    choice:
                        ease 3.5 yalign .5
                    choice:
                        ease 3 yalign .5
                    choice:
                        ease 3 yalign .7
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

            textbutton "Начать" action Start('tfyl_start') at tfyl_button_hover
            textbutton "Загрузить" action ShowMenu('tfyl_load') at tfyl_button_hover
            textbutton "Настройки" action ShowMenu('tfyl_preferences') at tfyl_button_hover
            textbutton "Выход" action ShowMenu("tfyl_exit") at tfyl_button_hover


        add Solid("000"): # Заменяет fade
            at transform:
                alpha 0
                on show:
                    alpha 1.0
                    linear 1.0 alpha 0
                on replace:
                    alpha 1.0
                    linear 1.0 alpha 0


    screen tfyl_game_menu_selector():

        tag menu
        modal True

        style_prefix "tfyl"


        add "mods/tfyl/gui/game_menu.png" align (.5, .5)

        vbox:
            spacing 5
            align (.5, .5)

            textbutton "В главное меню" text_size 36 action MainMenu(confirm=True)
            textbutton "Сохранить" text_size 36 action ShowMenu('save')
            textbutton "Загрузить" text_size 36 action ShowMenu('tfyl_load')
            textbutton "Настройки" text_size 36 action ShowMenu('tfyl_preferences')
            textbutton "Выход" text_size 36 action ShowMenu("tfyl_exit")

    screen tfyl_exit():
        modal True
        tag menu

        style_prefix "tfyl"

        key "game_menu":
            action Return()

        use tfyl_menu_bg

        text "Ты хочешь уйти?":
            size 100
            style 'tfyl_button'
            xalign 0.7
            yalign 0.33

            antialias True
            kerning 2

        hbox:
            xpos 0.55
            ypos 0.55
            spacing 80

            textbutton "Да" text_size 70 action (Hide("tfyl_exit", fade), Function(tfyl__screens_diact), Start("tfyl_true_exit")) at tfyl_button_hover
            textbutton "Нет" text_size 70 action Return()  at tfyl_button_hover

        add Solid("000"):
            at transform:
                alpha 0
                on show:
                    alpha 1.0
                    linear 1.0 alpha 0
                on replace:
                    alpha 1.0
                    linear 1.0 alpha 0




    screen tfyl_say(who=None, what=""):

        window background None id "window":

            $ timeofday = persistent.timeofday

            if persistent.font_size == "large":

                imagebutton auto "mods/tfyl/gui/dialogue_box/backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

                add "mods/tfyl/gui/dialogue_box/dialogue_box_large.png" xpos 174 ypos 866

                imagebutton auto "mods/tfyl/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 883 action HideInterface()
                imagebutton auto "mods/tfyl/gui/dialogue_box/save_%s.png" xpos 1567 ypos 883 action ShowMenu('save')
                imagebutton auto "mods/tfyl/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
                imagebutton auto "mods/tfyl/gui/dialogue_box/load_%s.png" xpos 1682 ypos 883 action ShowMenu('load')

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
                imagebutton auto "mods/tfyl/gui/dialogue_box/load_%s.png" xpos 1682 ypos 933 action ShowMenu('load')

                if not config.skipping:
                    imagebutton auto "mods/tfyl/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 949 action Skip()
                else:
                    imagebutton auto "mods/tfyl/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 949 action Skip()

                text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2 font 'mods/tfyl/fonts/Caveat.ttf'
                if who:
                    text who id "who" xpos 194 ypos 931 size 28 line_spacing 2

############################################################
    screen tfyl_save():
        key "game_menu":
            action NullAction()
        key "K_ESCAPE" action (Hide('tfyl_save', Dissolve(1.0)), Return())
        tag menu
        modal True

        use tfyl_menu_bg

        window at tfyl_on_show_authors_menu:
            textbutton '>' xalign 0.95 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
                action ShowMenu('tfyl_preferences')

            textbutton '<' xalign 0.05 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
                action ShowMenu('tfyl_load')

            textbutton 'Закрыть' xalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" at tfyl_button_hover:
                action (Hide('tfyl_save', Dissolve(1.0)), Return())
            textbutton ["Сохранить игру"]:
                text_style "tfyl_button_text"
                style "tfyl_button_text"
                ypos 850
                xalign 0.2
                action ( tfyl_FunctionCallback(tfyl_on_save_callback, selected_slot), FileSave(selected_slot))
            textbutton ["Удалить"]:
                text_style "tfyl_button_text"
                style "tfyl_button_text"
                xalign 0.8
                ypos 850
                action FileDelete(selected_slot)
            vbox:
                xalign 0.070
                yalign 0.35
                grid 1 9:
                    for i in range(1, 10):
                        textbutton str(i):
                            xpos 36
                            style "tfyl_button_text"
                            text_style "tfyl_button_text"
                            text_size 60
                            action (FilePage("tfyl_FilePage_"+ str(i)), SetVariable("selected_slot", False))
            grid 4 3:
                xpos 0.12
                ypos 0.15
                xmaximum 0.81
                ymaximum 0.65
                transpose False
                xfill True
                yfill True
                for i in range(1, 13):
                    fixed:
                        add FileScreenshot(i):
                            xpos 10
                            ypos 10
                        button:
                            action SetVariable("selected_slot", i)
                            xfill False
                            yfill False
                            style "tfyl_save_load_button"
                            fixed:
                                text ( "%s." % i
                                       + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                       + "\n" +FileSaveName(i)):
                                    style "tfyl_save_load_button"
                                    xpos 15
                                    ypos 15

        add Solid("000"):
            at transform:
                alpha 0
                on show:
                    alpha 1.0
                    linear 1.0 alpha 0

                on replace:
                    alpha 1.0
                    linear 1.0 alpha 0

    screen tfyl_load():
        key "game_menu":
            action NullAction()
        key "K_ESCAPE" action (Hide('tfyl_load', Dissolve(1.0)), Return())
        tag menu
        modal True

        use tfyl_menu_bg

        $ layout.LOADING = "Потерять несохраненые данные?"
        window at tfyl_on_show_authors_menu:

            textbutton '<' xalign 0.05 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
                action ShowMenu('tfyl_preferences')

            if not main_menu:
                textbutton '>' xalign 0.95 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
                    action ShowMenu('tfyl_save')

            textbutton 'Закрыть' xalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" at tfyl_button_hover:
                action (Hide('tfyl_load', Dissolve(1.0)), Return())
            textbutton ["Загрузить игру"]:
                text_style "tfyl_button_text"
                style "tfyl_button_text"
                ypos 850
                xalign 0.2
                action (tfyl_FunctionCallback(tfyl_on_load_callback, selected_slot), FileLoad(selected_slot))

            textbutton ["Удалить"]:
                text_style "tfyl_button_text"
                style "tfyl_button_text"
                xalign 0.8
                ypos 850
                action FileDelete(selected_slot)
            vbox:
                xalign 0.070
                yalign 0.35
                grid 1 9:
                    for i in range(1, 10):
                        textbutton str(i):
                            xpos 36
                            style "tfyl_button_text"
                            text_style "tfyl_button_text"
                            text_size 60
                            action (FilePage("tfyl_FilePage_"+ str(i)), SetVariable("selected_slot", False))
            grid 4 3:
                xpos 0.12
                ypos 0.15
                xmaximum 0.81
                ymaximum 0.65
                transpose False
                xfill True
                yfill True
                for i in range(1, 13):
                    fixed:
                        add FileScreenshot(i):
                            xpos 10
                            ypos 10
                        button:
                            action SetVariable("selected_slot", i)
                            xfill False
                            yfill False
                            style "tfyl_file_slots_button"
                            fixed:
                                text ( "%s." % i
                                       + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                       + "\n" +FileSaveName(i)):
                                    style "tfyl_file_slots_button"
                                    xpos 15
                                    ypos 15
        add Solid("000"):
            at transform:
                alpha 0
                on show:
                    alpha 1.0
                    linear 1.0 alpha 0

                on replace:
                    alpha 1.0
                    linear 1.0 alpha 0


    style tfyl_file_slots_button is default:
        background "mods/tfyl/gui/file_slots/file_slots_idle.png"
        hover_background "mods/tfyl/gui/file_slots/file_slots_hover.png"
        selected_background "mods/tfyl/gui/file_slots/file_slots_selected.png"
    transform tfyl_on_show_authors_menu:
        on hide:
            xalign 0.5
            yalign 0.5
            linear 2.5 xoffset 2000
    transform tfyl_on_show_main_menu:
        xpos -10 subpixel True
        ease 1 xalign 0.1
        on hide:
            xalign 0.1
            ease 2 xoffset -10

#####################################
    screen tfyl_preferences():

        style_prefix "tfyl"
        modal True
        tag menu

        key "game_menu":
            action NullAction()
        key "K_ESCAPE" action Return()

        use tfyl_menu_bg

        vbox align (0.2,0.5):
            text "Режим экрана" style 'tfyl_button' size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Оконный" text_size 35 at tfyl_button_hover:
                    action Preference("display","window")
                textbutton "Полноэкранный" text_size 35 at tfyl_button_hover:
                    action Preference("display","fullscreen")
            null height 40
            text "Пропускать" style 'tfyl_button' size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Всё" text_size 35 at tfyl_button_hover:
                    action Preference("skip","all")
                textbutton "Что увидел" text_size 35 at tfyl_button_hover:
                    action Preference("skip","seen")
            null height 40
            text "Размер шрифта" style 'tfyl_button' size 45 xalign 0.5
            hbox spacing 10 xalign 0.5:
                textbutton "Обычный" text_size 35 at tfyl_button_hover:
                    action SetField(persistent,"font_size","small")
                textbutton "Большой" text_size 35 at tfyl_button_hover:
                    action SetField(persistent,"font_size","large")
            null height 40
            text "Скорость текста" style 'tfyl_button' size 45 xalign 0.5
            null height 10
            bar value Preference("text speed") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
        vbox align (0.8,0.5):
            text "Автопереход" style 'tfyl_button'  size 45 xalign 0.5
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
            text "Музыка" style 'tfyl_button' size 45 xalign 0.5
            null height 10
            bar value Preference("music volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            text "Звуки" style 'tfyl_button' size 45 xalign 0.5
            null height 10
            bar value Preference("sound volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            text "Эмбиент" style 'tfyl_button' size 45 xalign 0.5
            null height 10
            bar value Preference("voice volume") xalign 0.5 maximum (442,42):
                right_bar im.Scale('mods/tfyl/gui/preferences/bar_1.png', 442, 42)
                left_bar im.Scale('mods/tfyl/gui/preferences/bar_2.png', 442, 42)
                thumb im.Scale('mods/tfyl/gui/preferences/thumb.png', 15, 46)
            null height 40
            textbutton "Без звука" text_size 35 xalign 0.5 at tfyl_button_hover:
                action Preference("all mute", "toggle")

        if not main_menu:
            textbutton '<' xalign 0.05 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
                action ShowMenu('save')
        textbutton '>' xalign 0.95 yalign 0.5 style "tfyl_button_text" text_style "tfyl_button_text" text_size 80 at tfyl_button_hover:
            action ShowMenu('tfyl_load')

        add Solid("000"):
            at transform:
                alpha 0
                on show:
                    alpha 1.0
                    linear 1.0 alpha 0
                on replace:
                    alpha 1.0
                    linear 1.0 alpha 0


    screen tfyl_choice(items, *args):

        $ imagebutton_sprites = {"?": "mods/tfyl/gui/interactive/q_%s.png", "!": "mods/tfyl/gui/interactive/em_%s.png", "me": "mods/tfyl/gui/interactive/message_%s.png", "ar": "mods/tfyl/gui/interactive/ar_%s.png"}

        for caption, action, chosen in items:

            if action:
                if caption in imagebutton_sprites:
                    imagebutton:
                        auto imagebutton_sprites[caption]
                        style "tfyl_choice_button"
                        align (action.args[0] if action.args else (.5, .5))

                        action action

                else:
                    textbutton caption align (action.args[0] if action.args else (.5, .5)) action action style "tfyl_choice_button" text_style "tfyl_choice_button_text"

    style tfyl_choice_button is default
    style tfyl_choice_button_text is default:

        font "fonts/PressStart2P.ttf"
        size 150
        color "A44"
        hover_color "F88"

    screen tfyl_yesno_prompt:
        tag menu modal True
        add 'mods/tfyl/gui/yes_no/yesno_promt.png'
        text _(message) text_align 0.5 yalign 0.46 xalign 0.5 color "#FFFFFF" font 'mods/tfyl/fonts/Caveat.ttf' size 25
        textbutton translation_new["Yes"] text_size 60 style "tfyl_button" text_style "tfyl_button"  yalign 0.65 xalign 0.3 action yes_action at tfyl_button_hover
        textbutton translation_new["No"] text_size 60 style "tfyl_button" text_style "tfyl_button"  yalign 0.65 xalign 0.7 action Return() at tfyl_button_hover



    screen tfyl_backdrop(chapter, chapter_name, bg, *images):

        add im.MatrixColor(bg, im.matrix.desaturate())

        hbox:
            spacing -200
            for ch in images:
                add im.MatrixColor(ch, im.matrix.desaturate())

        add "mods/tfyl/gui/misc/window.png"

        frame:
            background None#Solid("944")

            at transform:



                on show:
                    xpos .2
                    ypos .1
                    alpha .6
                    parallel:
                        ease 4 xpos .0 ypos .0
                    parallel:
                        linear 2 alpha 1

            add Solid("444", xsize=2210):
                rotate -30
                rotate_pad False

            vbox:
                pos (.55, .4) anchor (0, 0)
                text str(chapter) + " Глава:" font "mods/tfyl/fonts/mail_font.ttf" size 140 color "000"
                text "«"+chapter_name+"»" xoffset 40 font "mods/tfyl/fonts/mail_font.ttf"  line_spacing -80 line_leading 0 xsize .4 size 140 color "000"

        add Solid("000"):
            at transform:
                on show:
                    alpha 1.0
                    ease .5 alpha 0

        timer 6 action Hide("tfyl_backdrop", fade2)

    screen tfyl_old_filter():

        add "mods/tfyl/gui/misc/window.png"

    screen tfyl_mail_in_hand(txt=None, remove=False, sender=None):

        fixed:
            if not remove:
                at transform:

                    ypos 1.0
                    linear .5 ypos 0.0
            else:
                at transform:
                    ypos 0.0
                    linear .5 ypos 1.0

                timer 1 action Hide("tfyl_mail_in_hand")


            if txt:
                add "mods/tfyl/gui/mail/open.png"

                text txt font "mods/tfyl/fonts/mail_font.ttf" color "336" line_spacing -7 line_leading 0 size 32 xsize .3 ysize .7 xpos .27 ypos .1 anchor (.0, .0)

                if sender:
                    text sender font "mods/tfyl/fonts/mail_font.ttf" color "336" size 30 xpos .45 ypos .87
            else:
                add "mods/tfyl/gui/mail/inside.png"



    screen mouse_pos():

        $ m = renpy.get_mouse_pos()

        textbutton str((round(float(m[0])/1920.0, 3), round(float(m[1])/1080.0, 3))):
            background None
            keysym "game_menu"

            action Show("mouse_pos")



label tfyl_index:

    stop music fadeout 3
    scene bg black with fade2
    window hide

    $ tfyl__screens_save_act()


    return
    # call screen tfyl_to_main_menu
    # screen tfyl_to_main_menu:
    #     timer 0.001 action ((Hide("tfyl_to_main_menu", transition=fade3), MainMenu(confirm=False)))


label tfyl_true_exit:

    window hide dissolve
    stop music fadeout 3
    scene black with fade
    pause 1

    $ MainMenu(confirm=False)()
