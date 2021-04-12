# -*- coding: utf-8 -*-
init python:
    mods["tfyl_index"] =  u"{font=fonts/timesi.ttf}{size=40}25 Лет Спустя{/size}{/font}"

    tfyl_version = "0.21.04.10" # Версии менять тут

    class ModeStore(object):
        """ Класс для хранения данных мода """

        is_persistent = {}

        def __init__(self):

            object.__setattr__(self, "__dict__", {})

            if persistent.is_persistent:
                self.is_persistent = persistent.is_persistent
            else:
                persistent.is_persistent = self.is_persistent = {}

            self.__dict__.update(self.is_persistent)
            self.timeofday = "day"

        def __setattr__(self, key, value):
            self.__dict__[key] = value
            if key in self.is_persistent:
                self.is_persistent[key] = value

        def __delattr__(self, key):
            del self.__dict__[key]
            if key in self.is_persistent:
                del self.is_persistent[key]

        def add_persistent(self, key): # Пока я не вижу смысла что то пихать в персистент, но оставлю на потом
            if key in self.__dict__:
                self.is_persistent[key] = self.__dict__[key]
                return True
            self.is_persistent[key] = None

        def change_time(self, target=None):
            target = target or self.timeofday
            if target == "day":
                self.night_time()
            elif target == "sunset":
                self.sunset_time()
            else:
                self.day_time()

        def day_time(self):
            day_time()
            persistent.sprite_time = "day"
            self.timeofday = "day"

        def sunset_time(self):
            sunset_time()
            persistent.sprite_time = "sunset"
            self.timeofday = "sunset"

        def night_time(self):
            night_time()
            persistent.sprite_time = "night"
            self.timeofday = "night"


    # class ShowTfyl(Action):
    #
    #     def __init__(self, _screen):
    #         self._screen = _screen
    #
    #     def __eq__(self, other):
    #         if other.__class__ != self.__class__:
    #             return False
    #         return self._screen == other._screen
    #
    #     def __call__(self):
    #         Show("tfyl_menu_navigation", dissolve_fast, self._screen)()
    #         # renpy.show_screen("tfyl_menu_navigation", dissolve_fast, self._screen)
    #


    def make_sprite_timed(image):
        return ConditionSwitch(
            "persistent.sprite_time == 'sunset'",
            im.MatrixColor(
                image,
                im.matrix.tint(0.94, 0.82, 1.0) # При свете дня...
            ),
            "persistent.sprite_time == 'night'",
            im.MatrixColor(
                image,
                im.matrix.tint(0.63, 0.78, 0.82) # Во тьме ночной...
            ),
            True, # Но на случаи когда ни туда ни сюда, выходит обычное изображение
            image
        )


    for file in renpy.list_files(): # Что, новомодное объявление файлов хотите? Ну смотрите, даже разьясню что это за бублик
        if "tfyl" in file: # Проверяет от нашего ли мода этот файл
            file_name = os.path.splitext(os.path.basename(file))[0] # Достаем имя файла

            if file.endswith((".png", ".jpg", ".webp")): # Фильтр на изображения

                if "sprites" in file and  not "composite" in file: # Если он в директории спрайтов, то по красоте с матрицой добавляет спрайт # За исключением компонентных спрайтов, они будут обьявлены дальше
                    renpy.image( # По факту, так же обьявляет изображение, но реализуемо подругому. Не забудьте использовать bg cg и подобную херотеть в названии папок
                        file_name.replace("_", " "), # имя по которому будем обращаться
                        make_sprite_timed(file)
                    )
                elif not "gui" in file: # Компоненты меню обьявляются в самом меню
                    renpy.image(file.split("/")[-2]+" "+file_name,  # Ну а обычные ваши фончики фоточки обьявляются вот так
                        file,
                        )
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")): # Если хотите потусить под музычку
                globals()[file_name] = file # Разьяснения нужны?



    def tfyl_init():
        global tfyl
        tfyl = ModeStore()

        renpy.show_screen("tfyl_check_version")

        set_mode_adv()
        _window_hide()

        tfyl_after_load()

    def tfyl_after_load():
        global save_name

        config.window_title = u"25 Лет Спустя"
        config.name = "25_years_later"
        config.version = tfyl_version


        config.game_main_transition = config.main_game_transition = fade

        save_name = '25 лет спустя'

        for scrn in ["game_menu_selector", "say", "load", "preferences"]: # Лучше не заменять настройки и т.д., ломает другие моды
            renpy.display.screen.screens[(scrn, None)] = renpy.display.screen.screens[("tfyl_"+scrn, None)]

        layout.LOADING = "Потерять несохраненые данные?" # Не работает оно нехрена, но как коммент оставлю

        config.mouse = {'default' : [("mods/tfyl/gui/misc/mouse.png",  0, 0)]}
