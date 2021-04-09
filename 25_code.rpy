init python:
    class y_25_l_FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)
    def y_25_l_on_load_callback(slot):
        try:
            persistent.timeofday = persistent.y_25_l_on_save_timeofday[slot][0]
            persistent.sprite_time = persistent.y_25_l_on_save_timeofday[slot][1]
            persistent.font_size = persistent.y_25_l_on_save_timeofday[slot][2]
            _preferences.volumes['music'] = persistent.y_25_l_on_save_timeofday[slot][3]
            _preferences.volumes['sfx'] = persistent.y_25_l_on_save_timeofday[slot][4]
            _preferences.volumes['voice'] = persistent.y_25_l_on_save_timeofday[slot][5]
        except:
            pass
    def y_25_l_on_save_callback(slot):
        if not persistent.y_25_l_on_save_timeofday:
            persistent.y_25_l_on_save_timeofday={}
        persistent.y_25_l_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
    def y_25_l__screen_save():
        for name in ["game_menu_selector","say", 'main_menu', 'quit','preferences', 'save', 'yesno_prompt']:
            renpy.display.screen.screens[("y_25_l_old_"+name, None)] = renpy.display.screen.screens[(name, None)]
    def y_25_l__screen_act():
        config.window_title = u"25 лет спустя Beta"
        config.name = "25_years_later"
        config.version = "0.0.1"
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("y_25_l_say", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("y_25_l_game_menu_selector", None)]
        renpy.display.screen.screens[('main_menu', None)] = renpy.display.screen.screens[('y_25_l_main_menu', None)]
        renpy.display.screen.screens[('quit', None)] = renpy.display.screen.screens[('y_25_l_exit', None)]
        renpy.display.screen.screens[('preferences', None)] = renpy.display.screen.screens[('y_25_l_preferences', None)]
        renpy.display.screen.screens[('save', None)] = renpy.display.screen.screens[('y_25_l_save', None)]
        renpy.display.screen.screens[('load', None)] = renpy.display.screen.screens[('y_25_l_load', None)]
        renpy.display.screen.screens[('yesno_prompt', None)] = renpy.display.screen.screens[('y_25_l_yesno_prompt', None)]
        persistent._file_page = "y_25_l_FilePage_1"
        _game_menu_screen = "y_25_l__game_menu_selector"
        layout.LOADING = "Потерять несохраненые данные?"
        config.main_menu_music = "mods/25_years_later/music/latter_25.mp3"
        config.linear_saves_page_size = None
        config.mouse = {'default' : [("mods/25_years_later/images/mouse/mouse_25.png",  0, 0)]}
    def y_25_l__after_load_srceen():
        global save_name
        if save_name.find(u'25 лет спустя') != -1:
            y_25_l__screen_act()
    config.after_load_callbacks.append(y_25_l__after_load_srceen)
    def y_25_l__screens_diact():
        try:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            for name in ["game_menu_selector","say", 'main_menu', 'quit', 'preferences', 'preferences', 'save', 'yesno_prompt']:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("y_25_l_old_"+name, None)]
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            _main_menu_screen = "main_menu"
            _game_menu_screen = "game_menu_selector"
            config.mouse = {'default' : [("images/misc/mouse/1.png",  0, 0)]}
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
            persistent._file_page = 1
            renpy.music.stop("ambience")
            renpy.music.stop("music")
            renpy.music.stop("sound")
            renpy.play(music_list["blow_with_the_fires"], channel = "music")
        except:
            renpy.quit()
    def y_25_l__screens_save_act():
        y_25_l__screen_save()
        y_25_l__screen_act()
    style.y_25_l_menu_btn = Style(style.default)
    style.y_25_l_menu_btn.color = '#666565'
    style.y_25_l_menu_btn.hover_color = '#1B1A1A'
    style.y_25_l_menu_btn.font = 'mods/25_years_later/Caveat.ttf'
    style.y_25_l_menu_btn.size = 50
    style.y_25_l_menu_btn.outlines = [ (absolute(1), '#1B1A1A', absolute(1), absolute(1))] #DDDDDD
    ################################################################################
    style.y_25_l_save_load_button                            = Style(style.button)
    style.y_25_l_save_load_button.background                 = 'mods/25_years_later/gui/save_load/Save_Load_Button_idle.png'
    style.y_25_l_save_load_button.hover_background           = 'mods/25_years_later/gui/save_load/Save_Load_Button_hover.png'
    style.y_25_l_save_load_button.selected_background        = 'mods/25_years_later/gui/save_load/Save_Load_Button_selected.png'
    style.y_25_l_save_load_button.selected_hover_background  = 'mods/25_years_later/gui/save_load/Save_Load_Button_selected.png'
    style.y_25_l_save_load_button.selected_idle_background   = 'mods/25_years_later/gui/save_load/Save_Load_Button_selected.png'

transform y_25_l_btn_anim:
    parallel:
        on idle:
            easeout_back 0.75 zoom 1.0
        on hover:
            easein_back 0.75 zoom 1.25
        on update:
            easeout_back 0.75 zoom 1.0
    parallel:
        on idle:
            easein 0.75 alpha 1.0
        on hover:
            easein 0.75 alpha 0.5
        on update:
            easein 0.75 alpha 1.0
transform bg_trans_25:
    zoom 1.0 align (0.5, 0.5)
    block:
        ease 3.0 zoom 1.2 align (0.3, 0.6)
        ease 3.0 zoom 1.3 align (0.4, 0.5)
        ease 3.0 zoom 1.4 align (0.2, 0.4)
        ease 3.0  zoom 1.5 align (0.4, 0.4)
        repeat 
transform y_25_l_on_show_authors_menu:
    on hide:
        xalign 0.5 
        yalign 0.5
        linear 2.5 xoffset 2000
transform y_25_l__on_show_main_menu:
    xpos -10 subpixel True     
    ease 1 xalign 0.1     
    on hide:
        xalign 0.1     
        ease 2 xoffset -10
screen y_25_l_pre_menu:
    timer 0.001 action ((Hide("y_25_l_pre_menu", transition=fade3), MainMenu(confirm=False)))     
screen y_25_l_main_menu:
    tag menu 
    modal True 
    key 'game_menu':
        action NullAction()
    add im.Blur('mods/25_years_later/images/menu_bg_25.png', 1.5) at bg_trans_25
    vbox align(0.1, 0.5) spacing 20 at y_25_l__on_show_main_menu:
        textbutton 'Начать' style 'y_25_l_menu_btn' text_style 'y_25_l_menu_btn' action Start('years_later') at y_25_l_btn_anim
        textbutton 'Загрузить' style 'y_25_l_menu_btn' text_style 'y_25_l_menu_btn' action ShowMenu('load') at y_25_l_btn_anim
        textbutton 'Настройки' style 'y_25_l_menu_btn' text_style 'y_25_l_menu_btn' action ShowMenu('preferences') at y_25_l_btn_anim
        textbutton 'Выход' style 'y_25_l_menu_btn' text_style 'y_25_l_menu_btn' action ShowMenu('y_25_l_exit') at y_25_l_btn_anim
screen y_25_l_say:

    window background None id "window":

        $ timeofday = persistent.timeofday

        if persistent.font_size == "large":

            imagebutton auto "mods/25_years_later/images/dialogue_box/backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

            add "mods/25_years_later/images/dialogue_box/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton auto "mods/25_years_later/images/dialogue_box/hide_%s.png" xpos 1508 ypos 883 action HideInterface()
            imagebutton auto "mods/25_years_later/images/dialogue_box/save_%s.png" xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto "mods/25_years_later/images/dialogue_box/menu_%s.png" xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/25_years_later/images/dialogue_box/load_%s.png" xpos 1682 ypos 883 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/25_years_later/images/dialogue_box/forward_%s.png" xpos 1735 ypos 924 action Skip()
            else:
                imagebutton auto "mods/25_years_later/images/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1 font 'mods/25_years_Later/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

        elif persistent.font_size == "small":

            imagebutton auto "mods/25_years_later/images/dialogue_box/backward_%s.png" xpos 38 ypos 949 action ShowMenu("text_history")

            add "mods/25_years_later/images/dialogue_box/dialogue_box.png" xpos 174 ypos 916

            imagebutton auto "mods/25_years_later/images/dialogue_box/hide_%s.png" xpos 1508 ypos 933 action HideInterface()
            imagebutton auto "mods/25_years_later/images/dialogue_box/save_%s.png" xpos 1567 ypos 933 action ShowMenu('save')
            imagebutton auto "mods/25_years_later/images/dialogue_box/menu_%s.png" xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/25_years_later/images/dialogue_box/load_%s.png" xpos 1682 ypos 933 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/25_years_later/images/dialogue_box/forward_%s.png" xpos 1735 ypos 949 action Skip()
            else:
                imagebutton auto "mods/25_years_later/images/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2 font 'mods/25_years_Later/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 931 size 28 line_spacing 2

screen y_25_l_game_menu_selector:

    $ timeofday = persistent.timeofday

    modal True


    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add "mods/25_years_later/images/g_menu/ingame_menu.png" xalign 0.5 yalign 0.5
    imagemap:

        if _preferences.language == "spanish":
            auto "mods/25_years_later/images/g_menu/ingame_menu_es_%s.png" xalign 0.5 yalign 0.5
        elif _preferences.language == "italian":
            auto "mods/25_years_later/images/g_menu/ingame_menu_it_%s.png" xalign 0.5 yalign 0.5
        elif _preferences.language == "english":
            auto "mods/25_years_later/images/g_menu/ingame_menu_en_%s.png" xalign 0.5 yalign 0.5
        elif _preferences.language == "chinese":
            auto "mods/25_years_later/images/g_menu/ingame_menu_ch_%s.png" xalign 0.5 yalign 0.5
        else:
            auto "mods/25_years_later/images/g_menu/ingame_menu_%s.png" xalign 0.5 yalign 0.5
        hotspot (171, 127, 319, 33) focus_mask None clicked MainMenu()
        hotspot (214, 173, 228, 35) focus_mask None clicked ShowMenu('save')
        hotspot (218, 214, 218, 38) focus_mask None clicked ShowMenu('load')
        hotspot (209, 258, 238, 36) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (269, 301, 119, 29) focus_mask None clicked ShowMenu('y_25_l_exit')
screen y_25_l_preferences:
    tag menu
    modal True 
    key "game_menu":
        action NullAction()
    key "K_ESCAPE" action (Hide('y_25_l_preferences', Dissolve(1.0)), Return())
    add im.Blur('mods/25_years_later/images/menu_bg_25.png', 1.5) at bg_trans_25
    text 'Настройки':
        style "y_25_l_menu_btn"
        align(0.5,0.007)
        size 80
        text_align 0.5
        antialias True
    if not main_menu:
        textbutton '>' xalign 0.95 yalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
            action ShowMenu('y_25_l_save', Dissolve(1.0))
        textbutton '<' xalign 0.05 yalign 0.5 style  "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
            action ShowMenu('y_25_l_load', Dissolve(1.0))
    vbox align (0.2,0.5):
        text "Режим экрана" style "y_25_l_menu_btn" size 45 xalign 0.5
        hbox spacing 10 xalign 0.5:
            textbutton "Оконный" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action Preference("display","window")
            textbutton "Полноэкранный" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action Preference("display","fullscreen")
        null height 40
        text "Пропускать" style "y_25_l_menu_btn" size 45 xalign 0.5
        hbox spacing 10 xalign 0.5:
            textbutton "Всё" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action Preference("skip","all")
            textbutton "Что увидел" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action Preference("skip","seen")
        null height 40
        text "Размер шрифта" style "y_25_l_menu_btn" size 45 xalign 0.5
        hbox spacing 10 xalign 0.5:
            textbutton "Обычный" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action SetField(persistent,"font_size","small")
            textbutton "Большой" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action SetField(persistent,"font_size","large")
        null height 40
        text "Скорость текста" style "y_25_l_menu_btn" size 45 xalign 0.5
        null height 10
        bar value Preference("text speed") xalign 0.5 maximum (442,42):
            right_bar im.Scale('mods/25_years_later/gui/preferences/bar_1.png', 442, 42)
            left_bar im.Scale('mods/25_years_later/gui/preferences/bar_2.png', 442, 42)
            thumb im.Scale('mods/25_years_later/gui/preferences/thumb.png', 15, 46)
    vbox align (0.8,0.5):
        text "Автопереход" style "y_25_l_menu_btn" size 45 xalign 0.5
        null height 10
        hbox spacing 10 xalign 0.5:
            textbutton "Включить" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action [If(preferences.afm_time == 0,true=Preference("auto-forward time", 20)),Preference("auto-forward after click","enable"),SelectedIf(preferences.afm_time != 0 or preferences.afm_after_click == "enable")]
            textbutton "Выключить" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
                action [Preference("auto-forward time", 0),Preference("auto-forward after click","disable"),SelectedIf(preferences.afm_time == 0 or preferences.afm_after_click == "disable")]
        bar value Preference("auto-forward time") xalign 0.5 maximum (442,42):
            right_bar im.Scale('mods/25_years_later/gui/preferences/bar_1.png', 442, 42)
            left_bar im.Scale('mods/25_years_later/gui/preferences/bar_2.png', 442, 42)
            thumb im.Scale('mods/25_years_later/gui/preferences/thumb.png', 15, 46)
        null height 40
        text "Музыка" style "y_25_l_menu_btn" size 45 xalign 0.5
        null height 10
        bar value Preference("music volume") xalign 0.5 maximum (442,42):
            right_bar im.Scale('mods/25_years_later/gui/preferences/bar_1.png', 442, 42)
            left_bar im.Scale('mods/25_years_later/gui/preferences/bar_2.png', 442, 42)
            thumb im.Scale('mods/25_years_later/gui/preferences/thumb.png', 15, 46)
        null height 40
        text "Звуки" style "y_25_l_menu_btn" size 45 xalign 0.5
        null height 10
        bar value Preference("sound volume") xalign 0.5 maximum (442,42):
            right_bar im.Scale('mods/25_years_later/gui/preferences/bar_1.png', 442, 42)
            left_bar im.Scale('mods/25_years_later/gui/preferences/bar_2.png', 442, 42)
            thumb im.Scale('mods/25_years_later/gui/preferences/thumb.png', 15, 46)
        null height 40
        text "Эмбиент" style "y_25_l_menu_btn" size 45 xalign 0.5
        null height 10
        bar value Preference("voice volume") xalign 0.5 maximum (442,42):
            right_bar im.Scale('mods/25_years_later/gui/preferences/bar_1.png', 442, 42)
            left_bar im.Scale('mods/25_years_later/gui/preferences/bar_2.png', 442, 42)
            thumb im.Scale('mods/25_years_later/gui/preferences/thumb.png', 15, 46)
        null height 40
        textbutton "Без звука" text_size 35 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" xalign 0.5 at y_25_l_btn_anim:
            action Preference("all mute", "toggle")
    textbutton 'Назад':
        style 'y_25_l_menu_btn'
        text_style 'y_25_l_menu_btn'
        text_size 60
        xpos 30
        ypos 950
        action (Hide('y_25_l_preferences', Dissolve(1.0)), Return())
        at y_25_l_btn_anim
screen y_25_l_exit:
    key "game_menu":
        action NullAction()
    key "K_ESCAPE" action (Hide('y_25_l_exit', Dissolve(1.0)), Return())

    modal True
    add im.Blur('mods/25_years_later/images/menu_bg_25.png', 1.5) at bg_trans_25
    text "Ты хочешь уйти?":
        style 'y_25_l_menu_btn'
        size 100
        text_align 0.5
        xalign 0.7
        yalign 0.33
        antialias True
        kerning 2
    textbutton "Да" at y_25_l_btn_anim:
        style 'y_25_l_menu_btn'
        text_style 'y_25_l_menu_btn'
        xalign 0.55
        yalign 0.55
        action [Hide("y_25_l_exit", Dissolve(1.0)),Function(y_25_l__screens_diact), ShowMenu('main_menu')]
    textbutton "Нет":
        style 'y_25_l_menu_btn'
        text_style 'y_25_l_menu_btn'
        xalign 0.73
        yalign 0.55
        action [ Hide("y_25_l_exit", Dissolve(1.0)), Return()]
        at y_25_l_btn_anim
screen y_25_l_save:
    key "game_menu":
        action NullAction()
    key "K_ESCAPE" action (Hide('y_25_l_save', Dissolve(1.0)), Return())
    tag menu
    modal True
    window at y_25_l_on_show_authors_menu:
        add im.Blur('mods/25_years_later/images/menu_bg_25.png', 1.5) at bg_trans_25
        textbutton '>' xalign 0.95 yalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
            action ShowMenu('y_25_l_load', Dissolve(1.0))
        textbutton '<' xalign 0.05 yalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
            action ShowMenu('y_25_l_preferences', Dissolve(1.0))
        textbutton 'Закрыть' xalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
            action (Hide('y_25_l_save', Dissolve(1.0)), Return())
        textbutton ["Сохранить игру"]:
            text_style "y_25_l_menu_btn"
            style "y_25_l_menu_btn"
            ypos 850
            xalign 0.2
            action ( y_25_l_FunctionCallback(y_25_l_on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton ["Удалить"]:
            text_style "y_25_l_menu_btn"
            style "y_25_l_menu_btn"
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
                        style "y_25_l_menu_btn"
                        text_style "y_25_l_menu_btn"
                        text_size 60 
                        action (FilePage("y_25_l_FilePage_"+ str(i)), SetVariable("selected_slot", False))
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
                        style "y_25_l_save_load_button"
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                style "y_25_l_save_load_button"
                                xpos 15
                                ypos 15
screen y_25_l_load:
    key "game_menu":
        action NullAction()
    key "K_ESCAPE" action (Hide('y_25_l_load', Dissolve(1.0)), Return())
    tag menu
    modal True
    $ layout.LOADING = "Потерять несохраненые данные?"
    window at y_25_l_on_show_authors_menu:
        add im.Blur('mods/25_years_later/images/menu_bg_25.png', 1.5) at bg_trans_25
        if not main_menu:
            textbutton '>' xalign 0.95 yalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
                action ShowMenu('y_25_l_preferences', Dissolve(1.0))
            textbutton '<' xalign 0.05 yalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" text_size 80 at y_25_l_btn_anim:
                action ShowMenu('y_25_l_save', Dissolve(1.0))
        textbutton 'Закрыть' xalign 0.5 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn" at y_25_l_btn_anim:
            action (Hide('y_25_l_load', Dissolve(1.0)), Return())
        textbutton ["Загрузить игру"]:
            text_style "y_25_l_menu_btn"
            style "y_25_l_menu_btn"
            ypos 850
            xalign 0.2
            action (y_25_l_FunctionCallback(y_25_l_on_load_callback, selected_slot), FileLoad(selected_slot))

        textbutton ["Удалить"]:
            text_style "y_25_l_menu_btn"
            style "y_25_l_menu_btn"
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
                        style "y_25_l_menu_btn"
                        text_style "y_25_l_menu_btn"
                        text_size 60
                        action (FilePage("y_25_l_FilePage_"+ str(i)), SetVariable("selected_slot", False))
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
                        style "y_25_l_save_load_button"
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                style "y_25_l_save_load_button"
                                xpos 15
                                ypos 15
screen y_25_l_yesno_prompt:#FFFEFE
    tag menu modal True  
    add 'mods/25_years_later/gui/yes_no/yesno_promt.png'
    text _(message) text_align 0.5 yalign 0.46 xalign 0.5 color "#FFFFFF" font 'mods/25_years_later/Caveat.ttf' size 25
    textbutton translation_new["Yes"] text_size 60 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn"  yalign 0.65 xalign 0.3 action yes_action at y_25_l_btn_anim
    textbutton translation_new["No"] text_size 60 style "y_25_l_menu_btn" text_style "y_25_l_menu_btn"  yalign 0.65 xalign 0.7 action Return() at y_25_l_btn_anim
label gateee:
    if gate1 == True:
        if gate2 == True:
            if gate3 == True:
                jump gateee2
    call screen menu_25
label menu_25:
    scene bg_25_gates
    call screen menu_25
screen menu_25:

    modal True tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/1_1.png"
        hover "mods/25_years_later/images/gates/1_2.png"
        hotspot (172, 728, 62, 138) action (Hide("menu"),Jump("gate_1"))
        hotspot (952, 248, 66, 140) action (Hide("menu"),Jump("gate_2"))
        hotspot (1810, 762, 70, 142) action (Hide("menu"),Jump("gate_3"))

label gateee2:
    if gate4 == True:
        jump gate_5
screen menu_25_1:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/2_1.png"
        hover "mods/25_years_later/images/gates/2_2.png"
        hotspot (172, 728, 62, 138) action Return("gate_1")
        hotspot (952, 248, 66, 140) action Return("gate_2")
        hotspot (1810, 762, 70, 142) action Return("gate_3")
        hotspot (324, 288, 146, 146) action Return("gate_4")

label menu_25_1:
screen vmenu_summer:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/3_1.png"
        hover "mods/25_years_later/images/gates/3_2.png"
        hotspot (674, 824, 160, 90) action Return("club_1")
