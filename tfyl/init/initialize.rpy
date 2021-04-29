# -*- coding: utf-8 -*-
init python:
    mods["tfyl_index"] =  u"{font=fonts/timesi.ttf}{size=40}25 Лет Спустя{/size}{/font}"

    tfyl_version = "0.21.04.28" # Версии менять тут
    class tfyl_FunctionCallback(Action): # А чем оно отличается от стандартной Function?
        ''' этот класс используется для экрана сохранений '''
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)

    class tfyl_LoadChapter(Action):
        """ Этот класс используется для загрузки
            глав, и определению были ли прочитаны прошлые главы.
        """
        def __init__(self, chapter, label):
            """
            chapter - название главы инициализации
            label - название первого лейбла главы
            """
            self.chapter = chapter
            self.label = label

        def __eq__(self, other):

            if other.__class__ != tfyl_LoadChapter:
                return False

            return self.chapter == other.chapter

        def get_sensitive(self):

            return renpy.seen_label(self.label)

        def __call__(self):

            # renpy.jump(self.chapter)

            Start(self.chapter)()

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

            self.mails = {}

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

        def add_mail(self, name, *pages):

            self.mails[name] = pages

            return pages

    class BooleanList(object):

        def __init__(self, size=1):

            self.__size__ = size

            self.__list__ = [False] * size

        def set_true(self, key):

            self[key] = True

        def __setitem__(self, key, value):

            self.__list__[key] = value

        def __getitem__(self, key):

            return self.__list__[key]

        def __nonzero__(self):

            return False if False in self.__list__ else True

        def __getslice__(self, i=0, j=0):

            return False if False in self.__list__[i : j or self.__size__] else True

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
                elif "images/intro" in file:
                    renpy.image("intro_mail_"+file_name.replace("_", " "),  # Письмо вот так обьявляется
                        im.Scale(file, 1920, 1080),
                        )
                elif not "gui" in file: # Компоненты меню обьявляются в самом меню
                    renpy.image(file.split("/")[-2]+" "+file_name,  # Ну а обычные ваши фончики фоточки обьявляются вот так
                        file,
                        )
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")): # Если хотите потусить под музычку
                globals()[file_name] = file # Разьяснения нужны?

# добавлю своих функций для замены экранов
    def tfyl_on_load_callback(slot):
        try:
            persistent.timeofday = persistent.tfyl_on_save_timeofday[slot][0]
            persistent.sprite_time = persistent.tfyl_on_save_timeofday[slot][1]
            persistent.font_size = persistent.tfyl_on_save_timeofday[slot][2]
            _preferences.volumes['music'] = persistent.tfyl_on_save_timeofday[slot][3]
            _preferences.volumes['sfx'] = persistent.tfyl_on_save_timeofday[slot][4]
            _preferences.volumes['voice'] = persistent.tfyl_on_save_timeofday[slot][5]
        except:
            pass
    def tfyl_on_save_callback(slot):
        if not persistent.tfyl_on_save_timeofday:
            persistent.tfyl_on_save_timeofday={}
        persistent.tfyl_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
    def tfyl__screen_save():
        for name in ["game_menu_selector","say", 'main_menu', 'quit','preferences', 'save', 'yesno_prompt', 'load']:
            renpy.display.screen.screens[("tfyl_old_"+name, None)] = renpy.display.screen.screens[(name, None)]
    def tfyl__screen_act():
        config.window_title = u"25 лет спустя Beta"
        config.name = "tfyl"
        config.version = tfyl_version
        save_name = '25 лет спустя'
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("tfyl_say", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("tfyl_game_menu_selector", None)]
        renpy.display.screen.screens[('main_menu', None)] = renpy.display.screen.screens[('tfyl_main_menu', None)]
        renpy.display.screen.screens[('quit', None)] = renpy.display.screen.screens[('tfyl_exit', None)]
        renpy.display.screen.screens[('preferences', None)] = renpy.display.screen.screens[('tfyl_preferences', None)]
        renpy.display.screen.screens[('save', None)] = renpy.display.screen.screens[('tfyl_save', None)]
        renpy.display.screen.screens[('load', None)] = renpy.display.screen.screens[('tfyl_load', None)]
        renpy.display.screen.screens[('yesno_prompt', None)] = renpy.display.screen.screens[('tfyl_yesno_prompt', None)]
        persistent._file_page = "tfyl_FilePage_1"
        _game_menu_screen = "tfyl_game_menu_selector"
        layout.LOADING = "Потерять несохраненые данные?"
        config.main_menu_music = "mods/tfyl/audio/music/latter_25.mp3"
        config.linear_saves_page_size = None
        config.mouse = {'default' : [("mods/tfyl/gui/misc/mouse.png",  0, 0)]}
    def tfyl__after_load_srceen():
        global save_name
        if save_name.find(u'25 лет спустя') != -1:
            tfyl__screen_act()
    config.after_load_callbacks.append(tfyl__after_load_srceen)
    def tfyl__screens_diact():
        try:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            for name in ["game_menu_selector","say", 'main_menu', 'quit', 'preferences', 'preferences', 'save', 'yesno_prompt', 'load']:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("tfyl_old_"+name, None)]
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
    def tfyl__screens_save_act():
        tfyl__screen_save()
        tfyl__screen_act()
    def tfyl_init():
        global tfyl
        tfyl = ModeStore()

        # renpy.show_screen("tfyl_check_version")

        set_mode_adv()
        _window_hide()

        tfyl__screens_save_act()

init:

    ### Трансформация бега
    transform tfyl_running():
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.1 pos (-6, -5)
        linear 0.1 pos (0, 0)
        linear 0.1 pos (6, -5)
        linear 0.1 pos (0, 0)
        repeat
# init python:
#
#     if persistent.tfyl_read_chapter == None:
#         persistent.tfyl_read_chapter = [False, False, False, False, False, False, False]
