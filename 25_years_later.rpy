init:

    $ mods["years_later_start"]=u"{font=mods/25_years_later/Caveat.ttf}{color=#640A0A}25 лет спустя{/color}{/font}"

    $ gate1 = False
    $ gate2 = False
    $ gate3 = False
    $ gate4 = False
    $ club1 = False
    $ club2 = False
    $ club3 = False
    $ club4 = False
    $ club5 = False
    $ big_stage1 = False
    $ big_stage2 = False
    $ big_stage3 = False
    $ small_stage1 = False
    $ small_stage2 = False
    $ small_stage3 = False
    $ small_stage4 = False
    $ ext_mus_club1 = False
    $ ext_mus_club2 = False
    $ ext_mus_club3 = False
    $ ext_mus_club4 = False
    $ in_mus_club1 = False
    $ in_mus_club2 = False
    $ in_mus_club3 = False
    $ in_mus_club4 = False
    $ in_mus_club5 = False
    $ in_mus_club6 = False

    image club1_1 = "mods/25_years_later/images/club/club1_1.png"
    image club1_2 = "mods/25_years_later/images/club/club1_2.png"
    image club1_3 = "mods/25_years_later/images/club/club1_3.png"
    image club1_4 = "mods/25_years_later/images/club/club1_4.png"
    image stage1_1_1 = "mods/25_years_later/images/big_stage/stage1_1.1.png"
    image stage1_2 = "mods/25_years_later/images/big_stage/stage1_2.png"
    image stage1_3 = "mods/25_years_later/images/big_stage/stage1_3.png"
    image stage1_1 = "mods/25_years_later/images/big_stage/stage1_1.png"
    image int_musclub_1_1 = "mods/25_years_later/images/in_mus_club/int_musclub_1.1.png"
    image int_musclub_1 = "mods/25_years_later/images/in_mus_club/int_musclub_1.png"
    image int_musclub_2 = "mods/25_years_later/images/in_mus_club/int_musclub_2.png"
    image int_musclub_3 = "mods/25_years_later/images/in_mus_club/int_musclub_3.png"
    image int_musclub_4 = "mods/25_years_later/images/in_mus_club/int_musclub_4.png"
    image bg_25_road = "mods/25_years_later/images/bg_25_road.png"
    image bg_25_gates = "mods/25_years_later/images/bg_25_gates.jpg"
    image bg_25_club = "mods/25_years_later/images/bg_25_club.png"
    image bg_25_2_1 = "mods/25_years_later/images/25_1.png"
    image bg_25_2_2 = "mods/25_years_later/images/25_2.png"
    image bg_25_2_3 = "mods/25_years_later/images/25_3.png"
    image bg_25_2_4 = "mods/25_years_later/images/25_4.png"
    image bg_25_2_5 = "mods/25_years_later/images/25_5.png"
    image bg_25_2_6 = "mods/25_years_later/images/25_6.png"
    image bg_25_chapter_1 = "mods/25_years_later/images/chapter/bg_25_chapter_1.png"
    image bg_25_chapter_2 = "mods/25_years_later/images/chapter/bg_25_chapter_2.png"
    image bg_ext_stage_big_ps = "mods/25_years_later/images/25_ext_stage_big_ps.png"
    image bg_ext_stage_normal_ps = "mods/25_years_later/images/25_ext_stage_normal_ps.png"
    image bg_25_mus_club = "mods/25_years_later/images/bg_25_mus_club.png"
    image int_musclub_25 = "mods/25_years_later/images/int_musclub_25.png"
    image window = "mods/25_years_later/images/window.png"
    image ext_polyana_night_25 = 'mods/25_years_later/images/ext_polyana_night_25.png'
    image ext_playground_night_25 = 'mods/25_years_later/images/ext_playground_night_25.png'
    image ext_playground_sunset_25 = 'mods/25_years_later/images/playground_sunset.jpg'
    #image geometry_model = Solid('#474747', xsize=2700, ysize=1600)
    $ teleport = "mods/25_years_later/music/teleport.mp3"
    $ start_25 = "mods/25_years_later/music/start_25.mp3"
    $ dark_music_25 = "mods/25_years_later/music/dark_music_25.ogg"
    $ ext_mus_club_mixdown = "mods/25_years_later/music/ext_mus_club_mixdown.ogg"
    $ other_25 = "mods/25_years_later/music/other_25.mp3"
    $ other_25_1 = "mods/25_years_later/music/other_25_1.mp3"
    $ mus_club = "mods/25_years_later/music/mus_club.mp3"
    $ latter_25 = "mods/25_years_later/music/latter_25.mp3"
    $ banzo = "mods/25_years_later/music/banzo.mp3"
    $ fight_25 = "mods/25_years_later/music/fight.mp3"
    $ latter_open = "mods/25_years_later/music/latter_open.mp3"
    $ list_open = "mods/25_years_later/music/list_open.mp3"
    $ evnening_25 = 'mods/25_years_later/music/evning_25.mp3'
###################sound###################
    $ komar_beep_25 = 'mods/25_years_later/sound/komar_beep.mp3'
    $ un_dive_25 = 'mods/25_years_later/sound/un_dive.mp3'
    $ me_dive_25 = 'mods/25_years_later/sound/me_dive.mp3'


transform beg_25:
    anchor (0.0, 0.0) pos (0.0, 0.0)
    linear 0.1 pos (-6, -5)
    linear 0.1 pos (0, 0)
    linear 0.1 pos (6, -5)
    linear 0.1 pos (0, 0)
    repeat


label years_later_start:
    $ renpy.scene('black')
    window hide
    with dissolve
    python:
        y_25_l__screens_save_act()
        set_mode_adv()
    call screen y_25_l_pre_menu
label years_later:
    $ save_name = '25 лет спустя'
    $ persistent.sprite_time = 'day'
    $ day_time()
    play music start_25 fadein 3
    $ renpy.pause (2)
    scene black with dissolve
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Это было двадцать пять лет назад. То время доживал пионерлагерь Совёнок, самый обычный, ничем не примечательный.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Он был любим за простоту и коллектив. Из-за этого каждый новоприбывший хотел вернуться, ощутить ещё смену. Таинственная магия? Нет. Просто такой лагерь. С такими же простыми людьми. Ничего сверхъестественного.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но с уходом красной эпохи пришло затмение. Жизнь покинула те территории и пионеры больше не возвращались.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но с уходом красной эпохи пришло затмение. Жизнь покинула те территории и пионеры больше не возвращались.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}О лагере забыли. Воспоминания остались на фотографиях, а теплые моменты на пленке.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И я забыл. Забыл каким я был пионером. Но один день все изменил.{/font}"
    window hide
    $ renpy.pause (1)
    scene bg_25_2_1
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Привет из прошлого ждал на пороге дома. Выглаженный конверт со старыми марками и пионерским значком позади.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Все это оказалось на столе. Я не сразу решил вскрывать его, сначала хотел изучить.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как и потертый значек, то было прямиком с прошлого века. Местами грязный, местами пожелтевший.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Минуя формы было написано имя... {w} Мое имя!{/font}"
    scene bg_25_2_2
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Внутри оказалась записка и реставрированная фотография.{w} Тотчас я вспомнил откуда это.{w} Совенок...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мысли бегали. С каждой секундой я все сильнее пробирался в закрома памяти с надеждой вспомнить.{/font}"
    scene bg_25_2_3
    with dissolve
    scene bg_25_2_4
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Кто-то просил помощь, не дать забыться лагерю. Глупая просьба, как я посчитал тогда.{/font}"
    window hide 
    scene black with dissolve
    $ renpy.pause (1)
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Записка вернулась в конверт, а я откинулся на стуле,{w} не имея желания помогать.{/font}"
    window hide 
    scene bg_25_2_5
    with dissolve
    $ renpy.pause (0.5)
    window show
    "{font=mods/25_years_Later/Caveat.ttf}К вечеру того же дня меня настиг второй конверт. Тот был в крови, мятый, и нес в себе одну мысль{/font}"
    scene bg_25_2_6
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Лагерь требовал меня. Оставив множество вопросов, пряча ответы где-то за своими стенами.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Минутное колебание и я...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я решился!{/font}"
    window hide
    stop music fadeout 18
    scene black
    with dissolve
    $ renpy.pause (3)
    scene bg_25_chapter_1
    with dissolve2
    $ renpy.pause (15)
    play music dark_music_25 fadein 3
    scene bg_25_road
    with dissolve
    window show 
    "{font=mods/25_years_Later/Caveat.ttf}Никогда бы не подумал что вернусь сюда. Особенно с такой целью. В голове ещё не могли уложиться те письма, а буря старых воспоминаний сильно нагружала голову.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Пространство расплывалось. Оно было не интересно. Только ближе к лагерю я стал замечать.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Потресканый асфальт давно не видал резины автомобилей, что ж говорить о ноге человека.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А бесконечные поля, они не изменились.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Безграничные, свободные. Цивилизация не тронула их.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Единственное что было, так это ЛЭП, передачи которой шли в лагерь. Те, проржавевшие и охваченные природой, лишь подтверждали мои мысли.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мысли о том, что стало с лагерем за это время.{/font}"
    window hide
    $ renpy.pause (1)
    scene bg_25_gates
    with dissolve
    window show 
    "{font=mods/25_years_Later/Caveat.ttf}Пеший маршрут подходил к концу. Издали показались парковка и ворота лагеря.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сколько я не бывал, но именно этот вид встречал пионеров, счастливых из-за конца длительного маршрута.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Последовательно счастье перерастало в нечто большее. Юнцы начинали беситься, а кто по старше - активно обсуждать планы. В те мгновения салон преображался.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как помню: В первую смену я прижался к вожатой и без конца задавал вопросы. Только что именно? Вряд ли скажу. Хоть убей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Момент истины наступил, когда я вплотную подошёл к этим скрипучим воротам. Их плачевное состояние ударило прямо в глаза.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Стены исписаны, бардюров не хватает, а асфальт: местами вырванный, местами провалившейся. Казалось, прошло куда больше времени, чем есть на самом деле.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Пеший маршрут подходил к концу. Издали показались парковка и ворота лагеря.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сколько я не бывал, но именно этот вид встречал пионеров, счастливых из-за конца длительного маршрута.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Последовательно счастье перерастало в нечто большее. Юнцы начинали беситься, а кто по старше - активно обсуждать планы. В те мгновения салон преображался.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как помню: В первую смену я прижался к вожатой и без конца задавал вопросы. Только что именно? Вряд ли скажу. Хоть убей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Момент истины наступил, когда я вплотную подошёл к этим скрипучим воротам. Их плачевное состояние ударило прямо в глаза.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Стены исписаны, бардюров не хватает, а асфальт: местами вырванный, местами провалившейся. Казалось, прошло куда больше времени, чем есть на самом деле.{/font}"
label gateee:
    if gate1 == True:
        if gate2 == True:
            if gate3 == True:
                jump gateee2
label menu_25:
    window hide
    call screen menu_25 with dissolve
screen menu_25:

    modal True tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/1_1.png"
        hover "mods/25_years_later/images/gates/1_2.png"
        hotspot (172, 728, 62, 138) action (Hide("menu"),Jump("gate_1"))
        hotspot (952, 248, 66, 140) action (Hide("menu"),Jump("gate_2"))
        hotspot (1810, 762, 70, 142) action (Hide("menu"),Jump("gate_3"))
label gate_1:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Каждая смена оставляла свой след на этой кирпичной кладке. Говорили - это к счастью.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}То происходило перед отъездом. Писали год, смену. Отъявленные же оставляли свой росчерк и рисунки.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Правда, те особо не расходились. Один кирпичик на одну смену, не более.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И таких кирпичиков - тьма. С десяток метров, если не ошибаюсь. Сколько пионеров вырастил Совёнок...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Внезапно, я загорелся желанием найти свою смену.{w}Только нашел совсем другое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}1983. Июль. Лена.{/font}"
    $ gate1 = True
    jump gateee
label gate_2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}По одному случаю лагерь изменил название на \"Совок\". Две буквы пропали в ночи и сколько не искали - не нашли.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Чья-то шутка, сельчан или самих пионеров, разошлась по лагерю и каждый хотел поглазеть. Смех-смехом, а недоразумение серьезное.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Поиски ничего не дали. Недоразумение подправили через неделю, когда подвезли новые буквы прямиком с завода.{/font}"
    $ gate2 = True
    jump gateee
label gate_3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Заросшая тропа вела на север. Там, в конце пути, стоял заброшенный лагерь.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вожатая рассказывала, что до времен Совёнка тот процветал, да и был не простым.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Снаружи - милые домики и личики, внутри - лабиринт темных, сырых коридоров.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сами гости не знали о них, лишь из-за пары трагедий объект рассекретили.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Забросили. Сответственно лагерь потерял смысл в маскировке и был оставлен. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Спустя время территорию оцепили: установили колючку, ветимы, и посадили пару караульных с псами. И те меры были недолгими.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ветхие конструкции начали заваливаться, а коридоры проседать под толщей земли. Некогда огромная сеть, превратилась в парочку проходов и комнат. Остальное завалило.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Такая история породила массу слухов, мол, духи буянят, что лагерь приютил в себе неупокоенные души, и всякое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но как бы оно не было - лагерь все равно наводил ужас. Даже сейчас.{/font}"
    $ gate3 = True
    jump gateee
label gateee2:
    window hide
    if gate4 == True:
        jump gateee3
    call screen menu_25_1
screen menu_25_1:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/2_1.png"
        hover "mods/25_years_later/images/gates/2_2.png"
        hotspot (172, 728, 62, 138) action Return("gate_1")
        hotspot (952, 248, 66, 140) action Return("gate_2")
        hotspot (1810, 762, 70, 142) action Return("gate_3")
        hotspot (324, 288, 146, 146) action Return("gate_4")
label gate_4:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Именно здесь пионеры прощались с лагерем и между собой, ведь была вероятность, что посадят в разные автобусы. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Здесь ребят строили, пересчитывали, и напоследок одаривали напутственным словом. Среди тех была Ольга Дмитриевна. Вожатая нашего отряда. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Каждый раз и со слезами. Она к нам привыкла, даже несмотря на все ее слова... {/font}"
    window hide
    stop music fadeout 3
    play sound teleport
    $ renpy.pause (1)
    scene ext_camp_entrance_day
    show window
    with dspr
    play music music_list["lets_be_friends"] fadein 3
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...Автобусы стояли ровными рядами, смирно ожидая пионеров. Скоро они пробудятся, потому что последнее построение подошло к концу. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мы стояли на отшибе, где было не так громко, да и личного пространства куда больше. И вот, оставалось пять минут до разлуки. {/font}"
    show dv laugh pioneer at fleft
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Ребят, как всегда все потрясающе. Увидимся следующем летом? {/font}"
    show mi cry pioneer at left
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Обязательно!!! Как я без вас?! {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Слезы обычное дело, особенно при таком моменте. Мику не выдержала и ее глазки выпустили целый град, успокоить который решилась сама Алиса. {/font}"
    show sl normal pioneer at cleft
    with dspr
    sl "{font=mods/25_years_Later/Caveat.ttf}Мику. Мы уже сколько смен и все в одном отряде. Вот увидишь, мы опять будем вместе! {/font}"
    show us laugh pioneer at right
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Пожалуй, присоединюсь. А, Семён? А тебе есть что сказать? Засранец. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ульяна стояла ко мне ближе всех и, найдя удачный момент, подтолкнула своим плечом. Намекнула, что не время бездействовать. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Пока Славяна и Лена бросились успокаивать Мику, я собрался с силами и присоеденился к ним. {/font}"
    show dv normal pioneer at fleft
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Все-все. Я тебя навещу, как только смогу. Обещаю. {/font}"
    show mi sad pioneer at left
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Правда? {/font}"
    dv "{font=mods/25_years_Later/Caveat.ttf}Да. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику более или менее пришла в норму. Мы выпустили ее из объятий, но она все равно пыталась быть ближе. Пыталась насладиться этим мгновением. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}После этого внимание переключилось на Лену. Она максимально старалась показать, что безмятежна, однако красные глазки показали всю истину. {/font}"
    window hide
    hide dv
    hide mi
    hide sl
    hide us
    with dspr
    $ renpy.pause (0.5)
    show un sad pioneer at center
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Пока четверка отвлеклась разговорами, я быстренько переметнулся к Лене. Она дернулась, попыталась закрыть лицо руками, но я не позволил. {/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Лена. Не забывай слова Алисы. Мы ещё встретимся, здесь же. {/font}"
    un "{font=mods/25_years_Later/Caveat.ttf}Я-я слышала... А если что-то произойдет? Вдруг я или т-ты?.. {/font}"
    show un cry pioneer at center
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Зажмурив глаза, Лена пыталась сдержать слезы. Но они, одна за другой, начали скатываться по щекам. В конце Лена не выдержала и снова открылась. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В этих каплях я видел свое отражение. Настолько они чистые, где сдерживались истинные чувства. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я не хотел отпускать. Правда, иначе никак. Подождать бы чуток, когда окрепну и смогу приехать. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Придет тот момент, когда преграда в сотни километров рухнет! {/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Ничего не случится. Я о тебе все знаю. Если что, я тебя найду или напишу.{/font}"
    show un sad pioneer at center
    with dspr
    un "{font=mods/25_years_Later/Caveat.ttf}С-смотри мне. Приедь сюда в 83, ты меня понял?!{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Понял, Лен.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Лена достала платочек и начала приводить себя в порядок. Иногда я замечал улыбку, которая мимолётно проскакивала.{/font}"
    show sh normal_smile body at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Через секунду всех нас окрикнул Шурик. За ним еле-еле плелся Эл, который тянул два чемодана.{/font}"
    sh "{font=mods/25_years_Later/Caveat.ttf}Нас забыли. Посмотрите как Эл устал, он ведь хотел повидаться.{/font}"
    sl "{font=mods/25_years_Later/Caveat.ttf}Так а чего ты не помог ему?{/font}"
    show un normal pioneer at center
    with dspr
    show sh serious body at right
    with dspr
    sh "{font=mods/25_years_Later/Caveat.ttf}А вот нечего спорить и проигрывать. Сам себя наказал.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Уставший сбросил чемоданы. На них же присел и начал освежать себя газетой.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Славяна присела рядом она явно была обеспокоена его состоянием.{/font}"
    show mi smile pioneer at left
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}А чего внутри?{/font}"
    sh "{font=mods/25_years_Later/Caveat.ttf}Куча бумаг. Твоя тонкая душевная организация не поймет... По правде я сам в них ещё не разобрался.{/font}"
    show mi sad pioneer at left
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Оу-у. Поняла.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Кто-то крикнул, что отправка через пару минут. Наш небольшой отряд сразу взбодрился и снова замкнулся в круг.{/font}"
    window hide
    show dv laugh pioneer at fleft
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Так, пока не забыла. Я очень рада, что это лето я провела рядом с вами. Встречаемся тут, как в общем-то всегда.{/font}"
    show sl smile pioneer at cleft
    with dspr
    sl "{font=mods/25_years_Later/Caveat.ttf}Спасибо, Алис. С вами было очень круто.{/font}"
    show un smile pioneer at center
    with dspr
    un "{font=mods/25_years_Later/Caveat.ttf}Я вас всех люблю! Давайте вернёмся целыми и здоровыми.{/font}"
    window hide
    hide sh
    with dspr
    $ renpy.pause (0.2)
    show mt normal pioneer panama at fright
    with dspr
    mt "{font=mods/25_years_Later/Caveat.ttf}Стойте!!!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ольга Дмитриевна внезапно появилась из-за ворот и подбежала к нам. Ее руки держали фотоаппарат и небольшой, черный пакетик.{/font}"
    mt "{font=mods/25_years_Later/Caveat.ttf}Встаньте в одну линию. Ещё есть время!{/font}"
    show us laugh pioneer at right
    with dspr
    show mi smile pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Никто не возражал. Девушки построились в одну шеренгу, когда мы, присевшие, находились впереди. Фотоаппарат щелкнул, момент был запечатлен.{/font}"
    mt "{font=mods/25_years_Later/Caveat.ttf}А теперь все сюда. Возьмите магнитики, они для вас. На них прошлогодние вы. Такие красивые...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Транспорт взревел, приглашая пионеров к себе на борт. Под такой шумок мы разобрали магнитики и успели поблагодарить вожатую.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}После чего наш круг начал уменьшаться.{/font}"
    window hide
    hide sl
    hide dv
    with dspr
    show mi sad pioneer at left
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Сначала вожатая отвела Славяну и Алису...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}...Потом двух братьев...{/font}"
    window hide
    hide us
    with dspr
    show mi cry pioneer at left
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...И напоследок собралась забрать Лену с Ульяной...{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Лена...{/font}"
    un "{font=mods/25_years_Later/Caveat.ttf}Наступила та секунда... Ольга, подождите. Дайте пару секунд.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Она не возражала, все равно автобусы не уедут, пока не укомплектуются по полной. Поэтому у нас остались последние секунды.{/font}"
    show un cry pioneer close at center
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}З-закрой глазки, Семён. Пожалуйста. И не открывай их, пока вас не поведут.{/font}"
    show blink
    "{font=mods/25_years_Later/Caveat.ttf}Буквально мгновение и я почувствовал ее губы. Обычный поцелуй вызвал во мне бурю энергии. Я загорелся желанием бросить все и уехать с ней.{/font}"
    mt "{font=mods/25_years_Later/Caveat.ttf}Теперь вы Семен и Мику. Вам ехать вместе и ваш автобус последний.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Лена?! Как быстро все произошло... Ее автобус я видел, он покидал границы лагеря, скрываясь за бесконечными полями.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я стал разбитым, будто откололи два куска и сожгли.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Увидимся в 83...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику подошла ближе, обняла. Ее личико было заплаканное, видно, кто переживал больше всех...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}1983 год должен был стать для нас последним в этом лагере.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Лену я больше не видел. Письма от нее я не получал, а отправленные лично мной постоянно возвращались.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как и с другими... Я не мог выйти ни на кого. Так я потерял связь со всеми, так я потерял Лену...{/font}"
    window hide
    stop music fadeout 3
    play sound teleport
    $ renpy.pause (1)
    scene bg_25_gates with dspr
    play music dark_music_25 fadein 3

    $ gate4 = True
    jump gateee2
label gateee3:
    call screen menu_25_2
screen menu_25_2:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/gates/3_1.png"
        hover "mods/25_years_later/images/gates/3_2.png"
        hotspot (770, 828, 168, 80) action Return("club_1")
label club_1:
    window hide
    scene black with dissolve2
    $ renpy.pause (4)
    scene bg_25_club with dissolve2
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Через секунду я оказался по ту сторону ворот. Пионерлагерь предстал передо мной во всей своей брошенной красоте.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Пустым... Вспоминая лучшие времена, я понимал, насколько тут не хватает людей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А плачевное состояние такое непривычное... Смотришь на фотографию и реальность, понимаешь - это разные места. Атмосфера совсем иная.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сердце изливалось кровью, будто бы разорили родной дом. Настроение пропало. Неужели такое возможно?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ветер усилился, поднял листья и разнообразный мусор. Уволок к домику, такому разрисованному и незнакомому.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}После пионеров тут обитала шпана. Их обитель был помечен неким Васей, который оставил крупный текст на ближайшей стене: Это наше!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Именно это ожидало лагерь? Как же Артек, Орленок, да тот же Океан? Почему они живут, а этот нет?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Причину закрытия Совёнка я не мог знать, только предполагал. Надежда была на незнакомца, что он ответит на все мои вопросы.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но встретил меня очередной конверт. Теперь весь грязный, местами влажный.{/font}"
    $ renpy.pause (0.5)
    scene club1_1
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    $ renpy.pause (0.5)
    scene bg_25_club with dissolve
    play sound latter_open
    $ renpy.pause (6)
    scene club1_2
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open 
    $ renpy.pause (0.5)
    scene bg_25_club
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Записка в теперешний момент была информативней, ярче отражала суть помощи... Невольно я подумал о плохом.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Надежды на личную встречу рухнули. Неизвестный, как уверял, покажется, но в конце. В конце чего? Много вопросов...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Хотя бог с ними.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сама просьба бредовая: роль летописца в никому не нужном лагере. Имеет смысл, да.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Спокойствие пришло не сразу. Я старался убедить себя в смысле этих действий. И вроде успех, решился играть по правилам.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Главное дойти до конца, а там уж, либо я, либо незнакомец на все ответит...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Стараясь не утруждать себя лишними размышлениями, ноги сами привели к \"инструменту\". На столике, в метрах пятидесяти, лежал дневник и с десяток ручек.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ничего особенного: мягкая обложка, закладка и 365 страниц. Исключая корочку, там перечислялись места для посещения.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Первое и самое ближайшее - клубы. Центр всех кружков, множества мероприятий. Особенностью были плоды труда, которые так или иначе привлекали внимание общественности.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А после починки видеомагнитофона и лампового телевизора все сошли с ума, ведь распорядок дня пополнился на один пункт.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Бесконечный просмотр терминатора каждый вечер! Других кассет к сожалению не появлялось.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Этот бесявый момент сопроводил меня к зданию не похожему на старые \"клубы\".{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Надо свыкнуться, что современный Совёнок кардинально отличается от старого. Здесь больше с уклоном в постапокалипсис, который образовался из мрачной сказки.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Окна выбиты, дверцы нету. Покрытие, что сверху, почти все отсутствует.{/font}"
label bag:
    "{font=mods/25_years_Later/Caveat.ttf}Аварийное состояние сразу намекало, что лучше не заходить. Целее будешь.{/font}"
    jump club_center
label club_center:
    window hide
    if club1 == True:
        if club2 == True:
            if club3 == True:
                if club4 == True:
                    if club5 == True:
                        jump club_center1
    window hide
    call screen menu_club11 with dissolve
screen menu_club11:

    modal True tag menu
    imagemap:
        ground "mods/25_years_later/images/club/bg_25_club1_1.png"
        hover "mods/25_years_later/images/club/bg_25_club1_2.png"
        hotspot (118, 678, 62, 138) action (Hide("menu"),Jump("club10"))
        hotspot (174, 28, 62, 142) action (Hide("menu"),Jump("club2"))
        hotspot (850, 524, 62, 144) action (Hide("menu"),Jump("club3"))
        hotspot (1180, 746, 64, 136) action (Hide("menu"),Jump("club4"))
        hotspot (1806, 588, 62, 144) action (Hide("menu"),Jump("club5"))
label club10:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Живой уголок располагался прямо за зданием и собирал в себе дюжиную коллекцию. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Особое пристрастие вызывал у деток по-младше, любивших животинку.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Судя по рассказам ранее тут был голубятник. Именно в нем проследили ту самую любовь и Ольга Дмитриевна принялась за работу.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Под ее руководством два техника и другие рабочие отстроили вольеры. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Главную часть, разумеется, выполняла старшая. Из города она привезла домашних зверушек.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Остальное: заботу, питание, внимание организовали пионеры. Лишняя обязанность, да, но какое разнообразие в этом монотонном лагере.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А что теперь? Рваная сетка, сломанные временем домики, сбежавшие животные. Даже любимый кролик Ульяны сбежал.{/font}"
    $ club1 = True
    jump club_center
label club2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Особенное достояние находилось на крыше этого чудного здания. Создатели неизвестны, но подозревают двух друзей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Платформа собрала в себе множество конфликтов и была на грани сноса. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Во-первых небезопасно, во-вторых выговоры проверок.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вожатые собирались снести, пока не вступился Шурик. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Он-то установил поручни, укрепил опоры, в целом конструкция стала безопасной.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И вроде помогло. Пионеры уже оставили следы, некоторые - надписи. Все прекрасно...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Все равно снесли. Чердак закрыли на замок, а от бывшего наблюдательного поста остался единственный люк.{/font}"
    $ club2 = True
    jump club_center
label club3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Обойдя здание по кругу я сделал вывод, что все возможное вынесено, а невозможное побито и оторвано. Это же касалось помещений.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Через проем, где отсутствовала дверь, я наблюдал довольно длинный коридор. Все, что в нем осталось - плакаты и таблички с названием кружков.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Самая крайняя являлась \"Радиотехнической\". Обитель Эла и Шурика, гениев и изобретателей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Те не только по платам. Всякая другая работа, требующая трезвой головы и золотых рук, доставалась им.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вот и во мне увидели такие качества. Приглашали к себе, рассказывали о плюсах, будто тут рай. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Правда, одна деталь перечеркнула все.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Они не вылезают из помещения! Моменты на питание и туалет не считаю. Как так? Лето и за четырьмя стенами!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Во имя пляжа и девушек я, конечно же, отказался. Но общаться не перестал, как никак поддержка со стороны изобретателей дорогого стоит.{/font}"
    $ club3 = True
    jump club_center
label club4:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Помнится тут были списки о наборе и прочие объявления. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Здесь пионеры могли найти идеи, как разнообразить свой досуг.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Будь-то кружок или мероприятия на вечер. Неважно. Каждый день стэнд обновлял ассортимент новостей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И тут не без участия пионеров. Любой желающий мог прикрепить свой листок с приглашением.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Слав... Да, Славяна была ответственна за эту доску. Всякий раз она отсеивала бумагу не по теме, где-то корректировала, поправляла.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ответственно подходила к делу. Вот почему стэнд информирования до сих пор стоит.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ещё одна деталь вызвала во мне удивление - выцветшая фотография, держащаяся на одной кнопке. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Потрёпанная дождями, ветрами, чем угодно, но сохранившая оттенок того времени.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}На ней сцена и пионеры... Мику, да-да, она самая! И девушка с зелёной косой и цветочком...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Столь памятную вещицу я не стал брать. Она принадлежит истории этого лагеря, а не мне.{/font}"
    $ club4 = True
    jump club_center
label club5:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Святыня тех, кто когда-либо состоял в кружках. Всегда была закрыта на замок, а сейчас, увы, даже двери нет.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Там хранили материалы на стеллажах, и готовые подделки в деревянных ящиках. Причем последние передавались из смены в смену.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Если сделал, то будь добр оставить. Все равно нет ничего лучше опыта и приобретенных товарищей. Так говорили вожатые.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вот и скопилось барахлишко. Чего там только не водилось... {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Жаль, что вся коллекция собранная годами досталась мародерам.{/font}"
    $ club5 = True
    jump club_center
label club_center1:
    window hide
    call screen menu_club2 with dissolve
screen menu_club2:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/club/bg_25_club2_1.png"
        hover "mods/25_years_later/images/club/bg_25_club2_2.png"
        hotspot (118, 678, 62, 138) action (Hide("menu"),Jump("club10"))
        hotspot (174, 28, 62, 142) action (Hide("menu"),Jump("club2"))
        hotspot (850, 524, 62, 144) action (Hide("menu"),Jump("club3"))
        hotspot (1180, 746, 64, 136) action (Hide("menu"),Jump("club4"))
        hotspot (1806, 588, 62, 144) action (Hide("menu"),Jump("club5"))
        hotspot (1806, 346, 74, 144) action (Hide("menu"),Jump("club6"))
label club6:
    stop music fadeout 1
    $ renpy.pause (1)
    play music latter_25 fadein 1
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Довольно большой лист был прикреплен к берёзе, некогда посаженной двумя товарищами.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Поверх бумаги мигал диод, который, видимо, привлекал мое внимание. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Значит незнакомец надеялся, что я прочту это.{/font}"
    scene club1_3
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (0.5)
    scene club1_4
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (0.5)
    scene bg_25_club
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Я прекрасно помнил этих \"клубоседов\", оба жили отстранённо и только везунчикам удавалось узнать их секреты.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}С 82 больше их не видел. Как в последний день пожали друг другу руки, так разошлись.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Еще эти чемоданы. Я точно помню, что они были огромные, даже задавался в прошлом этим вопросом.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но теперь... Их больше нет...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сколько времени прошло, а потеря таких хороших людей как-то отражается на настроении.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В голову пришла мрачная, но вполне реальная мысль. А вдруг это не единственная бумага о смерти товарищей? {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Не хотелось бы читать их, ведь есть иллюзия, что у всех все хорошо. Зачем знать лишнее?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Только угодить себе не получится. Хочешь узнать ответы - играй по правилам. А незнакомец плавно, но к чему-то ведёт.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Главное держать себя в руках!{/font}"
label chapter2:
    window hide 
    stop music fadeout 18
    scene black
    with dissolve
    $ renpy.pause (3)
    scene bg_25_chapter_2
    with dissolve2
    $ renpy.pause (15)
    play music dark_music_25 fadein 3
    scene bg_ext_stage_big_ps with dissolve
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Следующим пунктом в моей карточке путешествий была обычная сцена. Если не изменяет память, то это самый север.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Интересно, имеется ли смысл от такого порядка?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Да и смотря на количество пунктов с уверенностью можно сказать, что я тут до ночи. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Забавно, может призрака увижу.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мысли отпустили меня перед самой сценой. Это одно из тех мест, где собиралась куча людей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Не просто так, разумеется. Каждый вечер тут происходило что-то интересное. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Под этим \"что-то\" чаще всего была замешана Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А эта девушка могла многое. Выступления на каждый день? Пожалуйста. Сыграть на дудке? Не вопрос. А можешь все остальное? Тьфу, делов то!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Может с молотком были проблемы. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Когда обвалилось покрытие, Мику собственноручно занялась ремонтом. Пока специалисты не сменили ее через один час.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Смеху было... И правильно - это грубый инструмент, а у нее опыт с другим, который нужно чувствовать. Вот и вся правда.{/font}"
    window hide
    $ renpy.pause (0.5)
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Сцена была как... Сцена! Ничего не изменилось и выглядела куда лучше клубов. Видимо, брать тут было нечего, а сам объект сильно не выделялся.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Хоть что-то. Появилась внезапная надежда, что площадь и домики целы. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ведь когда я шел особняком, издали казалось все целым и нетронутым.{/font}"
label big_stage:
    scene bg_ext_stage_big_ps with dissolve
    if big_stage1 == True:
        if big_stage2 == True:
            if big_stage3 == True:
                if small_stage1 == True:
                    if small_stage2 == True:
                        if small_stage3 == True:
                            if small_stage4 == True:
                                jump big_stage20
    window hide
    call screen menu235 with dissolve
screen menu235:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/big_stage/bg_stage1_1.png"
        hover "mods/25_years_later/images/big_stage/bg_stage1_2.png"
        hotspot (28, 718, 62, 136) action (Hide("menu"),Jump("big_stage1"))
        hotspot (932, 566, 58, 134) action (Hide("menu"),Jump("big_stage2"))
        hotspot (898, 946, 64, 134) action (Hide("menu"),Jump("big_stage3"))
        hotspot (442, 846, 270, 126) action (Hide("menu"),Jump("small_stage"))
label big_stage1:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Эта самая девчушка - Ульяна, не пришла на генеральную репетицию. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В назначенное время все были переодеты, подкрашены, а главной звёздочки все не было и не было.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Без главной роли смысл в тренировке отсутствовал. Участники представления разошлись в поисках безответственной.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику блуждала по лагерю, спрашивала о пропавшей. Без результатов.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Девушку хватило отчаяние, ведь проблемы из ничего. Как выступать завтра? Где эта чертовка?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Та объявилась вечером, вся грязная, а в руках она держала свой костюм.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Местами рваный, в других более или менее заштопаный.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ульяна раскаялась, что бесилась в костюме пока не появились дыры. Потом пыталась всё исправить. Не получилось. Вот и пришла с повинной.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику вздохнула с облегчением, улыбка снова растянулась на ее лице. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вместе с подругой, они поставили нормальные заплатки.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}На следующий день, как помню, представление прошло без единого замечания. Инцидент был исчерпан.{/font}"
    $ big_stage1 = True
    jump big_stage
label big_stage2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Выступления наводняли сцену каждый вечер. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Те выделялись заголовком, тематикой и сценарием. Каждый раз принося что-то новое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Более масштабные, совмещающие в себе разные номера, репитировались неделями. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Соответственно их показывали один раз за смену, максимум два.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В эти дни сцена расцветала. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Прожектора с разноцветными стеклами освещали пространство. А голос ведущей, представлявший участников, разносился по всему Совенку.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Зрители молчали. Немногие осмеливались говорить. Лишь в промежутках толпа могла аплодировать.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Особые авации звучали в конце, когда участники, во главе с Мику, выходили на поклон.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ее любили вместе с ее творчеством...{/font}"
    $ big_stage2 = True
    jump big_stage
label big_stage3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Тут и спали, устраивали пикники, играли в шахматы. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вроде кажется - простое сидение, только на самом деле - это универсальное изобретение человечества.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Можно не поверить, но они были связаны с играми. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Московские прятки, к примеру, где прячущимся нужно добежать до места и три раза постучать. В нашем случае постучать по скамье.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Игра простая, но кардинально отличается от обычных игр. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Здесь прячешься, бегаешь, прорабатываешь стратегии. Вон какой ворох возможностей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Первое и второе было, пожалуй, про Ульяну. Девочка отлично справлялась с четвертью игры, но как добежать и постучать...{w} Все! Капут!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Зачем думать в играх?! Они ведь созданы, чтобы расслабиться, отвлечься. А тут на тебе! Так считала проказница.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Прятки надоели ей, потому что постоянно быть водой не было в ее интересах.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}{/font}"
    $ big_stage3 = True
    jump big_stage
label small_stage:
    scene bg_ext_stage_normal_ps with dissolve
    window hide
    call screen menu_small_stage1 with dissolve
screen menu_small_stage1:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/mele_stage/bg_stage2_1.png"
        hover "mods/25_years_later/images/mele_stage/bg_stage2_2.png"
        hotspot (46, 536, 68, 132) action (Hide("menu"),Jump("small_stage1"))
        hotspot (576, 550, 82, 146) action (Hide("menu"),Jump("small_stage2"))
        hotspot (1708, 614, 62, 138) action (Hide("menu"),Jump("small_stage3"))
        hotspot (1022, 780, 60, 140) action (Hide("menu"),Jump("small_stage4"))
        hotspot (448, 860, 276, 126) action (Hide("menu"),Jump("big_stage"))
label small_stage1:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Или проще - закулисье. Место, где происходило абсолютно все. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тут тебе и хранилище и гримерная и примерочная. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Из-за такого множества внутри нельзя было расходиться. А ещё это полотно от потолка до пола внушало замкнутость.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Без него строение казалось пустым и невероятно большим.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Декорации и прочий реквизит кочевали из смены в смену. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Само собой пионеры могли пополнять склад своими творениями, но выбрасывать... Тут не все так просто.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику была до жути барахольщицей. Ей было жалко что-то выбрасывать, даже если это превращалось в прах, нет беды - починим.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}От того все захламлялось. Сейчас уж с этим проблем нет - все, что не прикручено, улетело по рукам.{/font}"
    $ small_stage1 = True
    jump small_stage
label small_stage2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Ящик был создан для пожертвований, но не деньгами, а сладостями. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Такое вознаграждение для героев сцены придумали сами пионеры.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ограничений не было. Со временем, за отсутствием полагаемого, стали дарить все съестное: булки, треугольник молока, фрукты.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Таким образом короб заполнялся по середину. Еды с лихвой хватало на чай, даже оставалось. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И Мику придумала довольно интересную идею.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}По окончанию представления накрывался общий стол (Можно сказать - скамья). И все то, что приносили, успешно съедалось.{/font}"
    $ small_stage2 = True
    jump small_stage
label small_stage3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Главный стэнд, который содержал информацию о выступлениях, находился правее сцены{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}К особым мероприятиям он преображался.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Большой холст натягивали от угла к углу, тематически оформленный, он содержал в себе время и небольшую информацию.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Конечно, заполняла все Мику. Ее рука выводила особый стиль. Если честно, то у неё было уникально все.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Даже рабочий стол. Рояль бывал обеденным, письменным, по случаю становился верстаком. Именно на нем рисовались все афиши.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Может это сыграло свою роль?{/font}"
    $ small_stage3 = True
    jump small_stage
label small_stage4:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Фотоальбом лежал на вырванных страницах с фотографиями. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Его состояние видало лучшие времена, и брать в руки грозило последствиями.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Зелёный, узорчатый. Владелец - Лена. Она не однократно показывала содержимое. Гордилась, что завела его с приезда.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Там тебе яркие моменты, ребята, которые больше не появлялись в лагере, эмоции. Одним словом - память.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как видно, хрупкая она. Не восстановишь. В голове не удержишь. Приходится запечатлять и хранить.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А что до Лены? Просто так она бы не оставила личное. Значит, что-то произошло...{w} Нечто срочное...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Другие предметы, не имеющие ценности для мародеров, доказывали это.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Казалось, что пионеры пропали в один миг и жизнь в лагере остановилась. Жутко.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но какая чрезвычайная ситуация могла такое?! Опять догадки...{w} Ещё одни вопросы!{/font}"
    $ small_stage4 = True
    jump small_stage
label big_stage20:
    window hide
    call screen menu_big_stage2 with dissolve
screen menu_big_stage2:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/big_stage/bg_stage3_1.png"
        hover "mods/25_years_later/images/big_stage/bg_stage3_2.png"
        hotspot (28, 718, 62, 136) action (Hide("menu"),Jump("big_stage1"))
        hotspot (932, 566, 58, 134) action (Hide("menu"),Jump("big_stage2"))
        hotspot (898, 946, 64, 134) action (Hide("menu"),Jump("big_stage3"))
        hotspot (1536, 876, 62, 160) action (Hide("menu"),Jump("big_stage4"))
        hotspot (442, 846, 270, 126) action (Hide("menu"),Jump("small_stage"))
label big_stage4:
    stop music fadeout 1
    $ renpy.pause (1)
    play music latter_25 fadein 1
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Очередной и не последний. Тот ждал меня на самом краю сцены.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В спешке я раскупорил его. Руки подрагивали, будто жаждали момент тысячу лет.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}На самом деле желание было другое. Узнать, несёт ли он ту судьбу, как у двух братьев...{/font}"
    scene stage1_1_1
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    $ renpy.pause (0.5)
    scene bg_ext_stage_big_ps with dissolve
    play sound latter_open
    $ renpy.pause (6)
    scene stage1_1
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene stage1_2
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene stage1_3
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    window show
    "{font=mods/25_years_Later/Caveat.ttf}АЭС... Я совсем не подозревал, что она стоит в этой области. Осознание пришло так... Поздно.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Странно, что после тревоги ребят не вернули. Разве что, утечка? Нееет, предупреждений ведь не было на подходе.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вдруг сами родители не отпустили детей? И из-за отсутствия приезжающих лагерь то прикрыли. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Эта версия больше походила на правду.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Уже какие-то точки в вопросах. Продвижение! Но чем меня сможет удивить лагерь? Вроде бы ответил на главное.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Хотя нет. Помощь же ещё. Незнакомка, как видно из письма, хочет, чтобы я не дал забыться лагерю.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Интересно, что она скажет по окончанию. Что сделает с моими записями?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Письмо, как и другие, я убрал в карман джинс. Авось и пригодится, нечего разбрасывать рукопись...{/font}"
    window hide
    stop music fadeout 2
    $ renpy.pause (2)
    play music ext_mus_club_mixdown fadein 2
    scene bg_25_mus_club
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Следующим пунктом воспоминаний стал домик на окраине. Воистину восхитительное место, даже почти не тронутое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В номинации \"Красивейших зданий\" побеждал именно он. Леса позади и немного стиля \"модерн\" отличали его.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Та же библиотека. Из воспоминаний довольно хлипкий объект, который был в аварийном состоянии. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Может, его снесли и соорудили новый. Не знаю. Последний год я пропустил.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Факт в том, что Мику следила за своим обителем. В том числе - окружение, вся эта красота ее рук дела.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Да, заросло, но дух того времени все равно отличался. Даже если закрыть глаза, то можно вслушаться, прочуствовать.{/font}"
label ext_mus_club:
    scene bg_25_mus_club
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}{/font}"
    if ext_mus_club1 == True:
        if ext_mus_club2 == True:
            jump ext_mus_club5
    window hide
    call screen menu_ext_mus_club with dissolve
screen menu_ext_mus_club:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club1_1.png"
        hover "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club1_2.png"
        hotspot (312, 558, 72, 128) action (Hide("menu"),Jump("ext_mus_club1"))
        hotspot (828, 562, 68, 130) action (Hide("menu"),Jump("ext_mus_club2"))
label ext_mus_club1:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Одно из прекрасных видов деревьев - Яблоня. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Жаль, что плоды не успевали созревать из-за климата. Да и не в них дело.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Все великолепие таилось в цветение. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сама Мику говорила, что этот процесс вдохновлял. Не только ее, но и художников с веранды.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Можно представить, сколько холстов занимало это чудо. Сколько музыки сыграно глядя на нее.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}За это ее благодарили: наносили побелку, вскапывали землицу вокруг. В особо жаркие и сухие дни - поливали.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И до сих пор растет... Даже успела расцвести...{/font}"
    $ ext_mus_club1 = True
    jump ext_mus_club
label ext_mus_club2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Прямо у парадной двери, на веранде, располагалось пристанище художников. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Раньше они занимались там, пока не случилась стычка.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Чья была идея совместить два кружка, чьи условия для работы кардинально отличаются? Видимо, садисты постарались.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Из-за инструментов художники становились не в себе. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Многие конфликты на почве \"А давайте тише! Товарищи!\", переливались в пакости.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Все было до тех пор, пока не изменили время работы кружков. Вроде бы конфликт исчерпан, раз занимаются в разное время.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Новая буря возникла после короткого затишья. Две стороны стали бороться за домик, точнее, за его принадлежность.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Музыкальный отвечал просто - \"Мы раньше основались здесь\". {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Когда художники контратаковали - \"Домик был построен специально для нас. Но заселились вы!\"{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Туз в рукаве вторых не дал особого преимущества. Они оставили веранду, приспособив ее как склад.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Отныне их расположение постоянно менялось. Кочевали. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Можно сказать - это пошло им на пользу. Ведь работа в разных местах - нескончаемый материал. {/font}"
    $ ext_mus_club2 = True
    jump ext_mus_club
label ext_mus_club5:
    if ext_mus_club3 == True:
        if ext_mus_club4 == True:
            jump ext_mus_club6
    window hide
    call screen menu_ext_mus_club2 with dissolve
screen menu_ext_mus_club2:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club2_1.png"
        hover "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club2_2.png"
        hotspot (312, 558, 72, 128) action (Hide("menu"),Jump("ext_mus_club1"))
        hotspot (828, 562, 68, 130) action (Hide("menu"),Jump("ext_mus_club2"))
        hotspot (882, 854, 156, 160) action (Hide("menu"),Jump("ext_mus_club3"))
        hotspot (1708, 488, 150, 142) action (Hide("menu"),Jump("ext_mus_club4"))
label ext_mus_club3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Алиса всегда отвергала учения Мику. Считая ее уроки небольше, чем обычный бред.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Однако ее мнение не воспринимали. Утверждали, что завидует девка. Ведь Мику добилась всего через упорный труд.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Только не с той связались. Алиса не потерпела такого равнодушия, взяла гитару и отправилась в гости...{/font}"
    window hide
    stop music fadeout 3
    play sound teleport
    $ renpy.pause (1)
    scene ext_musclub_day
    show window
    with dspr
    play music banzo fadein 3
    show dv smile pioneer at left
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...Многие ребята следовали за Двачевской. Сегодня ее ожидал бой о котором, конечно, она всех уведомила.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Не скажу, что стадный инстинкт, но в толпу я влился без промедления. Слишком интриговала схватка. Особенно ее исход.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Про навыки Алисы я знал немногое: самоучка, которая вышла из тени. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Когда Мику совсем наоборот, была профессиональной, открыта публике.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Толпа, следовавшая следом, активно обсуждала все самое интересное. Были ставки. Были и шутки. Другие умудрялись осуждать.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Только все угомонились, когда появился домик на окраине. Специально отстали, чтобы дать поговорить девушкам наедине.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Реакция соперницы была незамедлительной. Та выбежала из домика, крикнув:{/font}"
    show mi normal pioneer at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Что случилось?! Алиса?!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Невозмутимость. Рыжеволосая шла, пока между ними не осталось около десятка метров. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В это время из домика выскочили ученики. Те сразу облепили крыльцо, посматривая с детским любопытством.{/font}"
    show mi scared pioneer at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Ребята? Вы чего?!{/font}"
    show dv angry pioneer at left
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Решим все сейчас{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Алиса вскинула гитару. Молниеносно стала перебирать струны, от чего игра казалось живой.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Местами агрессивной. С каждой секундой темп повышался, пальцы, можно сказать, стирались в кровь. Но свою дерзкую, собственного сочинения, она закончила.{/font}"
    show dv laugh pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Хлопки с двух сторон поддержали ее. Эта игра далась непросто, капельки пота тому подтверждение.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}С тех же сторон пионеры стали призывать Мику. Намекали взять гитару и включиться в дуэль. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Возражений не было. Раз толпа требует, почему бы не сыграть?{/font}"
    show mi normal pioneer at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Народ стал рассеиваться вокруг девушек, замыкая их в кольце. Мику едва успела метнуться за инструментом и встать на изготовку.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Без предупреждения игра началась. Мику приступила легко, струны отчеканили изящество. Не было того напора, как у Алисы.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Инструментал заставил кружиться в танце. Но внезапно движения изменились. Звучание перестало веять романтикой. Начался бой!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Толпа взбудоражилась, когда нежный цветок покрылся шипами. Сама Алиса ахнула от удивления.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Последний аккорд посеял мурашки по коже. Девушка протянула его, упав на колени.{/font}"
    show mi shy pioneer at right
    show dv angry pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Тяжёлое дыхание затмили аплодисменты. Такая игра! Какой талант! Алиса аж побагровела.{/font}"
    dv "{font=mods/25_years_Later/Caveat.ttf}Продолжим!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Неожиданно, колонки зашипели. Алиса улыбнулась, хлопнула в ладоши, и поймала новую электрогитару. Уровень был повышен.{/font}"
    show mi scared pioneer at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Мику оживилась, заметалась. Обновить инструмент не было возможности. Негоже ведь дуэлисту покидать арену.{/font}"
    show dv smile pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Смятение в лице Мику ободрило Алису. Сладость победы уже была на кончике языка, оставалось закончить и принимать лавры.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но не тут-то было!{/font}"
    show mi smile pioneer at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Мику влезла своей игрой и сбила Алису.{/font}"
    show dv angry pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Ошеломленная таким ходом, она быстро сориентировалась и продолжила. Гневно посматривая в сторону соперницы.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Как свет и тьма, как дьявол и ангел. Они противостояли друг другу, но Алиса, благодаря колонкам, полностью затмила игру подруги. Пока не перестала.{/font}"
    show dv shy pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Силы покинули. Современная гитара требовала большего усердия. Вот почему на публике осталась одна Мику.{/font}"
    show mi shy pioneer at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Вскоре и она перестала. Обе устали за эти полчаса, их пальцы требовали отдыха. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но пионеры не ждали, каждый кричал одно из двух имён.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Чье имя громче, та и побеждала... Минуточку. Да тут не определишься!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я пытался понять победителя. Все тщетно. Очевидно, что обе сыграли на ничью.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Ничья! Ничья! Все кричим - ничья!!!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Остальные подхватили. Алиса взбесилась, сжала что есть силы гитару, но потом расслабилась. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Она выполнила свою задачу: заявила о себе и поставила подругу на место.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А Мику наоборот улыбалась. Ей было в радость выступить, даже по такой причине.{/font}"
    show dv angry pioneer at left
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Сема. А ты чего мое имя не кричал?!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Двачевская зыркнула в мою сторону. Кажись, я провинился в ее глазах, раз не болел за нее.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Так я считал голоса!{/font}"
    show dv laugh pioneer at left
    with dspr
    dv "{font=mods/25_years_Later/Caveat.ttf}Что?! Голоса?!{w} Да я тебя сейчас!{w} Да куда ж ты? Я пошутила!..{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}...Мои пятки сверкали в направлении площади. Ну, а что? У Алисы крепкий удар, как и ее нрав.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Это как с огнем играться в комнате с газами. Эффект один. Вот почему я целые сутки прятался.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Может быть пару...{/font}"
    window hide 
    stop music fadeout 3
    play sound teleport
    $ renpy.pause (1)
    scene bg_25_mus_club with dspr
    play music ext_mus_club_mixdown fadein 3
    $ ext_mus_club3 = True
    jump ext_mus_club5
label ext_mus_club4:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Где лучше всего прятаться от лишнего внимания? Правильно - в домике на окраине.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А если хочешь побыть наедине с собой, то дерево на окраине в самый раз.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тот случай был перед дискотекой...{/font}"
    window hide
    stop music fadeout 1
    play sound teleport
    $ renpy.pause (1)
    scene ext_musclub_day
    show window
    show mi normal pioneer
    with dspr
    show window with dspr
    play music music_list["farewell_to_the_past_full"] fadein 1
    window show
    mi "{font=mods/25_years_Later/Caveat.ttf}Отдыхаешь?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я знал чей это голос и зачем он здесь.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Примерно за неделю лагерь узнал о масштабной дискотеке. Это событие вызвало бурю эмоций и массу прочего.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Основная часть готовила костюмы, потому что в этот день о форме забывали напрочь. Меньшинство занималось приготовлениями и поиском пластинок.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сценарий мероприятия составляла сама Мику. Ей доверяли это дело. А что до меня?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я не хотел участвовать. Настроение располагало к другому.{/font}"
    show mi sad pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Семеша! Ты пропустишь все самое интересное! О, слышишь? Вставай!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сцена была не слишком далеко и пробный запуск музыки отдался эхом.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я чувствовал как взволнована подруга. Ей же начинать вечер, но оставлять меня она не собиралась. Считала своим долгом разбудить.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Не пойду я. Иди уже, не опаздывай.{/font}"
    show mi shy pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Ноль понимания. Вместо этого я почувствовал лёгкую щекотку, из-за чего открыл глаза.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Девушка склонилась надо мной, ее косы были в миллиметре от моего лица. Но ее это не смущало, наоборот, она прибавила темп.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Мику! Да пре... Хватит! Вахаха.{/font}"
    show mi smile pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Видишь как действует? Уже проснулся. Да что ж ты! Хватит извиваться, вставааай!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Щекотка возымело свое. Мику оставила попытки, отошла, и стала наблюдать как я встаю.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Только тогда я увидел ослепительную улыбку девушки. Ее шелковистое платье, парфюм, дурманили голову. Она была превосходна.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В сравнение с ней я был обычным свинопасом. Те тоже отдыхают где попало, а ещё они мятые, с плохим запашком.{/font}"
    show mi sad pioneer
    with dspr
    me "{font=mods/25_years_Later/Caveat.ttf}Нет... Я не пойду. Не могу...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Я постыдился своего вида. Постыдился, что отнимаю время у такой прелестной. Но все равное мое мнение не изменится, хоть под ружье ставь.{/font}"
    mi "{font=mods/25_years_Later/Caveat.ttf}Почему? Что не так? Ты же говорил, что пойдешь...{/font}"
    th "{font=mods/25_years_Later/Caveat.ttf}...Говорил специально, чтобы отстали. А сейчас, из-за того что я плохо скрылся, все, расхлебывай новую кашу.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику помрачнела, отвела взгляд. Она поглаживала свою руку, старалась утешить, но не получалось. Я наблюдал как ей становится хуже.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Мику. Я-я не хочу идти. Просто я не люблю эти вечеринки, танцы. Не привык. Ну... Не начинай!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Слез не было, были действия. Она уселась на том самом месте у яблони, заключила руки в замок.{/font}"
    show mi upset pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Нельзя так. Я тоже не пойду. Будет не справедливо если все будут веселиться, а ты грустить.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}А как твоя речь?!{/font}"
    show mi normal pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Без нее начнут.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вспомнишь, как она готовилась. Все эти многие часы, чтобы без запинки, да с выражением! Будет прахом?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Уговоры не действовали, а просто уйти я не смог. Как никак она моя подруга, не бросать после того, что она сделала.{/font}"
    show mi sad pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Семеш, ты как сам не свой. Без настроения? Что-то случилось?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Музыка, которая была для ожидания, сменилась торжественной. Будто не дискотека, а открытие торгового центра.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику подпрыгнула, но не поддалась. Она все так же сидела.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Начинается! Беги!!!{/font}"
    show mi smile pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Только с тобой. Семён, я правда хочу, чтобы ты повеселился. Не сторонись меня, пошли.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И она протянула руку.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Моя реакция была неожиданной. Я принял ее. Помог встать. Привести в порядок.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вместе мы побежали к сцене. Та самая улыбка вновь украсила личико Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Благодаря ей я пришел на дискотеку. Благодаря ей я сблизился с Леной.{/font}"
    window hide
    stop music fadeout 2
    play sound teleport
    $ renpy.pause (1)
    scene bg_25_mus_club with dspr
    play music ext_mus_club_mixdown fadein 2
    $ ext_mus_club4 = True
    jump ext_mus_club5
label ext_mus_club6:
    window hide   
    call screen menu_ext_mus_club3 with dissolve
screen menu_ext_mus_club3:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club3_1.png"
        hover "mods/25_years_later/images/ext_mus_club/bg_ext_mus_club3_2.png"
        hotspot (312, 558, 72, 128) action (Hide("menu"),Jump("ext_mus_club1"))
        hotspot (828, 562, 68, 130) action (Hide("menu"),Jump("ext_mus_club2"))
        hotspot (882, 854, 156, 160) action (Hide("menu"),Jump("ext_mus_club3"))
        hotspot (1708, 488, 150, 142) action (Hide("menu"),Jump("ext_mus_club4"))
        hotspot (958, 590, 158, 66) action (Hide("menu"),Jump("in_clu"))
label in_clu:
    scene int_musclub_25
    with dissolve
    play music mus_club fadein 2
    window show
    "{font=mods/25_years_Later/Caveat.ttf}В недалёком прошлом меня бы встретила музыка, сейчас же, кроме скрипа и собственного дыхания, стояла мертвая тишина.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Здесь хлопьями витала пыль. Солнечные лучи едва просачивались сюда, пробиваясь сквозь многолетний слой грязи.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Впервые за долгое время я оказался внутри здания. Тут было все таким брошенным и единственное, что напоминало о прошлом, так это оставленные вещи.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Их было немного, но главное украшение в лице рояля до сих пор стояло тут. Это не может не радовать{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Именно он дал понять чувства Мику, да и вообще многих. Оставлять все: от друзей до масштабных планов. Вернуться в городскую жизнь, начать лето, не побоюсь слова, с нового листа.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тут не только отпечаток остается, а целый след. В случае с Мику и вовсе - тень на всю жизнь.{/font}"
    window hide
label in_mus_club:
    if in_mus_club1 == True:
        if in_mus_club2 == True:
            if in_mus_club3 == True:
                if in_mus_club4 == True:
                    jump in_mus_club10
    window hide
    call screen menu_in_mus_club1 with dissolve
screen menu_in_mus_club1:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/in_mus_club/int_musclub1_1.png"
        hover "mods/25_years_later/images/in_mus_club/int_musclub1_2.png"
        hotspot (22, 892, 64, 134) action (Hide("menu"),Jump("in_mus_club1"))
        hotspot (446, 618, 62, 130) action (Hide("menu"),Jump("in_mus_club2"))
        hotspot (316, 360, 66, 136) action (Hide("menu"),Jump("in_mus_club3"))
        hotspot (768, 558, 64, 132) action (Hide("menu"),Jump("in_mus_club4"))
label in_mus_club1:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Чулан - не иначе как комната досуга смешанная со спальней. Сочетание этого прекрасно подходило в комнатку на десять квадратов.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тут тебе диван, стеллаж с книгами, изюминкой был патефон, который часто притаскивали на дискотеки.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Хах. Да-да, музыка там тягостная и слишком старперская, но почему-то нашим нравилось. Было что-то в этом джазе.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Нередки случаи когда музыка играла в тех самых четырех стенах. Мику любила все делать под нее, даже засыпать.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Спустя время комнатка распахнула двери ребятам из кружка. После длительных тренировок всегда было приятно посидеть, разговаривая на отвлеченные темы.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику даже попросила сделать косметический ремонт, а то вид рваных обоев, ну, никак не вдохновлял. Правда, на том был конец.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ремонт прекратили, а бывшую комнатку оборудовали под склад. \"Все для нужд лагеря, не более!\" - говорили они.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Старую мебель, которая ещё состояла в описи, прикрыли именно там.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Всячину, безделушки, материалы, разложили по коробкам. Ими же заставили все свободное пространство{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Некогда уютная комнатка просто умерла на глазах. И реакция Мику была ясна: она больше не открывала дверь в то помещение, старалась найти альтернативу.{/font}"
    $ in_mus_club1 = True
    jump in_mus_club
label in_mus_club2:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Эта корочка имела в себе не только личные записи, но и целый ворох прочего.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Заметки. Из-за плотных дней голова, конечно же, уставала и память была дырявой. Пронумерованные записи избавляли от этой боли.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Эскизы, сценарии по мероприятиям, заготовленные речи. Список можно продолжать до бесконечности.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но главная мысль в том, что эта вещица облегчала жизнь. Вот почему он находился всегда под рукой Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Интересный вопрос - \"Откуда я это все знаю?\". Все очень просто. Подруга сама показывала его содержимое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Не всем, только приближенным лицам. Причем личное всегда перелистывали.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сейчас, как видно, препятствий не было. Дневник цел, лишних глаз нет. Только я и потаённое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Соблазн присутствовал, да только постыдился я за свои мысли и намерения. Как-то это неправильно. Нужды нет.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вместо этого я спрятал его. Вдруг явится другой \"Семён\" и не постесняется прочитать личные записи?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Нет. Такого не стоит допускать.{/font}"
    $ in_mus_club2 = True
    jump in_mus_club
label in_mus_club3:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Какие-то фотографии были прикреплены к доске, конечно, время потрепало их.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Отсыревшие, где изображение разбиралось с трудом. Многие попросту отсеивались. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вот почему из всего разнообразия осталась троица.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Каждая картинка несла в себе какой-то смысл. Вот, группа пионеров после соревнований... Постой, да это же не группа!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Молодой Семён, лёжа на траве, просто улыбается и смотрит в объектив. Его окружение - мои подруги. Такие же румяные и энергичные.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Беззаботное было времечко. Прошли спортивно-массовые, обсудил с кем-то, а потом иди живи!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Про эту самую жизнь была следующая фотография. Здесь показан случай уж точно связанный не со мной.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Девушка, та самая с зелёной косой, была довольно скрьезной. Рядом с ней находилась девчушка чуть младше, ее отличали каштановые волосы и брошь.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Находились обе у заброшенного лагеря. Одна перерезала проволку, пока другая внимательно наблюдала. Значит, всё-таки без меня смогли пробраться.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И вот третья: Мику наслаждалась ароматом букета под заходящим солнцем.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Фотография впечатляла. Такая выдержанная, что глаз не налюбуется.{/font}"
    $ in_mus_club3 = True
    jump in_mus_club
label in_mus_club4:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}По местным меркам этот рояль сейчас стоит чуть больше миллиона. Все благодаря его возрасту и истории.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику купила его ровно за сто рублей на блошином рынке. Вроде бы средняя цена, а играет как премиум класс.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Никогда не понимал отличия в звуках, вроде бы разница минимальная. Но для таких как Мику мое \"минимально\", растет в других прогрессиях.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Далее инструмент благополучно передали Совенку. Как дар и наследие после Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тем вечером домик на окраине был переполнен пионерами, всех интересовала та самая жемчужина. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}К тому же многие надеялись, что увидят ее в деле.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Даже гадать не надо кто сделал первую пробу. Мику сыграла для всех, убедив, что инструмент прекрасен.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}С этим же намекнула про вступление в музыкальный кружок. Доказала, что он не стоит на месте, постоянно обновляясь и совершенствуясь.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И кружок забился новыми подопечными. Причем их стало больше, чем доступных мест.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но Мику не переживала, ведь ее идея \"научить музыке каждого\" была превыше всего.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Так появились выступления и прочие искусства. Лагерь оживился именно благодаря пиар-компании Мику.{/font}"
    $ in_mus_club4 = True
    jump in_mus_club
label in_mus_club10:
    if in_mus_club5 == True:
        if in_mus_club6 == True:
            jump in_mus_club20
    window hide
    call screen menu_in_mus_club2 with dissolve
screen menu_in_mus_club2:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/in_mus_club/int_musclub2_1.png"
        hover "mods/25_years_later/images/in_mus_club/int_musclub2_2.png"
        hotspot (22, 892, 64, 134) action (Hide("menu"),Jump("in_mus_club1"))
        hotspot (446, 618, 62, 130) action (Hide("menu"),Jump("in_mus_club2"))
        hotspot (316, 360, 66, 136) action (Hide("menu"),Jump("in_mus_club3"))
        hotspot (768, 558, 64, 132) action (Hide("menu"),Jump("in_mus_club4"))
        hotspot (170, 186, 160, 146) action (Hide("menu"),Jump("in_mus_club5"))
        hotspot (1010, 670, 148, 146) action (Hide("menu"),Jump("in_mus_club6"))
label in_mus_club5:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}У Мику был самый длинный язык. Причем его не тянули, девушка сама могла ляпнуть лишнего и не заметить.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}С этим я был знаком. Один случай тому подтверждение.{/font}"
    window hide
    stop music fadeout 1
    play sound teleport
    $ renpy.pause (1)
    play music music_list["dance_of_fireflies"] fadein 1
    scene int_dining_hall_people_day
    show window
    show mi sad pioneer
    with dspr
    window show
    me "{font=mods/25_years_Later/Caveat.ttf}Яблоко будешь?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Очередная трапеза в столовой. Опять этот оркестр из приборов и посуды, опять те же самые блюда. Все одно и тоже.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Да. Вкусно. Полезно. Но разнообразия нет.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Хорошо хоть не гречка, а то от нее начинает тошнить. Скоро начнёт от перловки, но ее, благо, не так часто готовят.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Возможно из-за этого рацион Мику перешёл на лёгкие продукты. Молочка, фрукты, овощи.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сейчас она ковыряла салат из зелени, помидора, огурца. Легче - зимний салат, который любят подавать летом.{/font}"
    mi "{font=mods/25_years_Later/Caveat.ttf}Нет, спасибо. Аппетита нет, сам скушай.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику так не перестала ковырять тарелку, лишь отвела взгляд на мгновенье. Что-то ее беспокоило? Неужели все из-за стрепни?{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Испортили?{/font}"
    show mi upset pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}М? Нет-нет. Там совсем другое. Я до сих пор не могу переварить.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику вышла из транса и обратила внимание на меня, жующего, с обляпанными щеками. Именно из-за этого она улыбнулась.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Другое в желудке? Гудрон проглотила что ли, раз переварить не можешь?{/font}"
    show mi smile pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Скажешь тоже... Мне признались в чувствах, вот!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Вот это попадон! От удивления я поперхнулся и чуть ли не уронил стол.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А когда пришел в ясность, переспросил:{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Признались? Кто?!{/font}"
    show mi shy pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Девушка на миг покраснела, да и с ответом затянула. Видимо понимала, что сказала лишнего и старалась закрыть тему.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Может Санёк с северной части лагеря? Вы с ним знакомы, и вроде бы он питает чувства.{/font}"
    window hide
    show mi surprise pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Мику округлила глаза. Неужели я разгадал их романс?{/font}"
    mi "{font=mods/25_years_Later/Caveat.ttf} Чтооо?! Я даже не знала о чувствах! Почему я узнаю последней?!{/font}"
    th "{font=mods/25_years_Later/Caveat.ttf}Ага. Разгадал. Сейчас я еще разгадаю свой разговор с ним и Мику. И как так, Семён, теперь вопросы задаёт она, а не ты?{/font}"
    show mi smile pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Стороны поменялись. Краснел уже я, когда Мику серьезным взглядом пронзала меня.{/font}"
    hide mi
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Конец обеденного часа спас меня. Все встали, задвинули стулья и понеслись к Моечному окну. Воспользовавшись ситуацией я рванул следом за всеми.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Очередь!!! Причем те двадцать человек настолько слабо растекаются, что смысл в побеге пропал.{/font}"
    show mi smile pioneer far
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Семеша! Подождёшь меня у выхода.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Все это время она дышала мне в спину... Сейчас же ехидно улыбалась, потому что понимала мое состояние...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}...Интервал между сдачей посуды стал более адекватным. Примерно двадцать секунд было для побега.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Однако бежать я не стал. Лагерь мал, пересечься с ней довольно просто. Зачем испытывать судьбу?{/font}"
    window hide
    $ renpy.pause (1)
    scene ext_dining_hall_near_day
    show window
    show mi smile pioneer
    with dissolve
    window show
    mi "{font=mods/25_years_Later/Caveat.ttf}Подождал. Я очень рада.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Наша очередная встреча была на выходе из столовой. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Место для личного общения не очень, слишком большая текучка. Но ты попробуй выбрать, когда за тебя решили.{/font}"
    show mi upset pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Понимаю... Если хочешь не рассказывай. Я не могу тебя заставить.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Подруга облокотилась о соседнию колонну. Ее поведение меня удивляло.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Конечно, рассказывать больше я не планировал. Но просто сказать нет было бы неправильно.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Нечего рассказывать кроме этого. Выговорился он, а потом сразу перевел тему. Все.{/font}"
    show mi shy pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}А чегооо побежал?{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Да это я просто рассказывать не хотел...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Маневр, чтобы не потерять расположение обеих сторон, сработал на отлично. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Остаётся доказать Саньку, что я ляпнул про чувства случайно и дело в шляпе.{/font}"
    show mi smile pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Тогда ладно. Спасибо за компанию, я к себе. Увидимся вечером!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И она пошла как ни в чем не бывало. Понимает, что я ещё не спрашивал о признании. А сейчас самое время!{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Мику. Ты не забыла рассказать кое о чем?{/font}"
    show mi happy pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Она повернулась, сделав непонимающие лицо. Будто сама невинность, покачала головой.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}То что было в столовой. Забыла уже?{/font}"
    show mi upset pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Я все помню. Не было никаких секретов!{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Какие секреты?! Я даже слова не сказал о них.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Тут же обернулась, понимая, что вновь сказала лишнего. Пошла прочь, но теперь поманила за собой.{/font}"
    window hide
    $ renpy.pause (1)
    scene ext_path_day
    show window
    show mi smile pioneer
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Путь лежал к домику на окраине. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сейчас мы шли другой дорогой, через небольшой подлесок. Здесь можно срезать дорогу на минут десять.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Птичьи трели были усладой для ушей. Они раслабляли под бесконечными тенями, скрывавших от палящего солнца. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Эта прогулка придавала сил не хуже, чем послеобеденный сон.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику молчала, тихо перебирая ножками. Давить на нее не было смысла, все равно расскажет. Дело то времени.{/font}"
    show mi shy pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Только никому, а то я сгорю от стыда..{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Само собой.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Девушка остановилась, припала к дереву. Через минуту она держала листок, который, судя по всему, не в первый раз мяли.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Затем просунула его в мои руки, сказав:{/font}"
    show mi smile pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Я не смогла дочитать. Может боюсь. Не знаю. Мне хватило первых строк...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Признание было довольно большим. Красивый почерк вырисовывал каждую буковку, делая стиль уникальным.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Само содержание было выдержано. Тут он описал свои восхищения, благодарность за столь весомую работу и не навязчиво намекнул про свои чувства.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Целый поэт! Правда, о таких людях я не слышал, видимо, не заявили о себе. {/font}"
    show mi happy pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}А жаль, этому лагерю нужны ребята в помощь редакции.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но это все. Ни подписей, ни имён, кажется, что текст не дописали. Тогда я вопросительно посмотрел на Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Она хихикнула и перевернула лист. Соль мне в ухо! Да тут ещё добротная половина!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Здесь уже больше действий. Он призывал встретится через год и именно в этом лагере. Извинялся, что не познакомился лично.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В конце размашистая роспись буквой - \"С\". Теперь точно все.{/font}"
    show mi laugh pioneer
    with dspr
    me "{font=mods/25_years_Later/Caveat.ttf}Мне б написали такое. Мое сердце не выдержало бы.{/font}"
    show mi shy pioneer
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Мику покраснела, а бумажку поспешно убрала. Судя по всему она прочитала все, а не \"пару строк\".{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Планируешь встретиться с ним?!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Не ожидая ответа, я вновь задал вопрос. От чего привел Мику в ступор. Уверен, она сама не знала.{/font}"
    show mi surprise pioneer
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Я-я-я? Да нет. Не-е собиралась...{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Узнаем через год. Я лично буду следить за тобой. Хе-хе.{/font}"
    hide mi
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Мику это не понравилось. Она отлипла от своего места и как рванула в сторону домика, что пятки сверкали.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И всё-таки в глубине души я ревновал. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Этот \"С\" показался воспитанным и пунктуальным, но немудрено, что он обычный мачо. Влюбит в себя, поиграется, а после оставит одну.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Нет. Такого не стоит допускать. Надо будет обязательно с ним познакомиться...{/font}"
    window hide
    play sound teleport
    stop music fadeout 1
    $ renpy.pause (1)
    play music mus_club fadein 1
    scene int_musclub_25
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...Я до сих пор его не знал. Что это за человек и какой он внутри. Эх, все больше жалею, что меня не оказалось в 83 году.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику неопытна в любви. Любой мог наговорить чепухи, а она поверит. Лично у меня присутствовал такой горький опыт.{/font}"
    $ in_mus_club6 = True
    jump in_mus_club10
label in_mus_club6:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Домик на окраине находился, как ни странно, на окраине лагеря. Это название к нему привилось ещё с незапамятных времён.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Место несильно примечательно раз находится особняком. Но здесь, лично мое мнение, есть чуть ли не лучший способ скоротать время...{/font}"
    window hide
    stop music fadeout 1
    play sound teleport
    $ renpy.pause (1)
    play ambience ambience_music_club_day fadein 1
    scene int_musclub_day
    show window
    show mi normal pioneer at right
    show us normal pioneer at left
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...В помещении стояла мертвая тишина. Единственное, что не давало сойти с ума - трели птиц снаружи.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ульянка, сидевшая по левую сторону рояля, тряслась на месте. Этот застой негативно сказывался на сангвинике.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мику наоборот, внимательно следила за нашим поведением, то и дело бросая взгляд на подругу, потом на меня.{/font}"
    show mi smile pioneer at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Твоя очередь, Семёша.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Она была настойчивой, раз повторила это во второй раз. Но я не мог решится...{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Сейчас на руках у нас пять карт: по две у меня с Ульяной, одна у Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Дело в том, что меньше половины - это козыри. Дама червей и туз соответственно. У меня первое.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Остаток: девятка и шестерка пик, вторая шестерка бубен.{/font}"
    show us angry pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Скинуть шестерку бубен и держаться козыря - не вариант. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}С большой долей вероятности они разыграют свои карты, оставив меня с одним червем.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Положить козырь... А если у нее туз и она отобьется? Тут меня лишь спасет ее последняя карта, которая, надеюсь, девятка.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Множество вариаций, медлить уже нет смысла.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Рука осторожно вытащила мелкую карту, положила недалеко от Ульяны. Девочка сразу оживилась.{/font}"
    show us smile pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Девятка покрыла шестерку. Бито. Теперь победа зависела от одного туза.{/font}"
    show mi happy pioneer at right
    play music music_list["eat_some_trouble"] fadein 3
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Следующая карта...{w} Шестерка! Черт! И долгожданный козырь помог Мику выйти из дураков. Обида за свой же выбор поглотила меня.{/font}"
    us "{font=mods/25_years_Later/Caveat.ttf}Спасибо, Семён, за шестеру. Выручил несказанно! Вахаха.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}И Ульяна засмеялась во весь голос. Потом кто-то цыкнул и снова тишина. Я уже не обращал внимания на то что происходит.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но это же игра? Чего я так расстроился? А, точно, желания... Целых два от девиц.{/font}"
    show mi sad pioneer at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Семеш, ты же понимаешь? С тебя два желания...{/font}"
    mi "{font=mods/25_years_Later/Caveat.ttf}...но если нет настроения, то давай без них.{/font}"
    show us angry pioneer at left
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Вторую часть она выдавила из себя более тихо, не навязчиво. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Однако эти слова вызвали в Ульянка бурю негатива. Она воскликнула и обратилась к Мику.{/font}"
    show us grin pioneer at left
    with dspr
    me "{font=mods/25_years_Later/Caveat.ttf}Я сделаю. Сделаю.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ульяна сразу замолчала. Нужный мне эффект был достигнут.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Мини-девочка сразу переключилась на меня. Говорить не спешила, потому что желание требовало раздумий.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}В то время Мику убрала карты, протёрла рояль и присоединилась к нашей компании, стоящей около выхода.{/font}"
    show us laugh2 pioneer at left
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Отжимания! И-и-и со мной на спине! Во как.{/font}"
    me "{font=mods/25_years_Later/Caveat.ttf}Что?! У нас тут физкультура?! Сколько раз?..{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Опять раздумия, правда в этот раз она быстрее выдавила из себя двузначное число. Каким я, конечно же, не был доволен.{/font}"
    show mi normal pioneer at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Много, Ульян, давай меньше. Он не сможет!{/font}"
    show us laugh pioneer at left
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Пятьдесят раз и не смочь?! Он парень или кто? Даже я смогу!{/font}"
    hide us
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Через секунду Ульяна была в упоре лёжа и демонстративно начала считать. Причем упражнение она делала правильно, без особых усилий.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Последние три ей удалось сделать с трудом. Тяжёлое дыхание охватило девушку и вместе с пылающим лицом доказывало, что она устала.{/font}"
    show us grin pioneer at left
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Вот...{w} Ты это...{w} Также, но со мной...{w} Понял?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Из-за одышки речь была не связной, правда понять ее не составило проблем.{/font}"
    show us smile pioneer close at left
    show mi sad pioneer at right
    with dspr
    "{font=mods/25_years_Later/Caveat.ttf}Я кивнул. Стал медленно опускаться на руки, почувствовав с какой жалостью смотрит на меня Мику.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Она, как и я, понимала, что такое количество для меня нереальное особенно с Ульяной на спине. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Однако возражений не было, ведь таковы правила.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Севшая Ульянка сразу прибавила в сложности. И когда руки адаптировались к ситуации - я начал.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Первая десятка прошла без проблем. Однако чем ближе я становился к цели, тем больше убеждался - сил не хватит.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Руки стали ходить ходуном, а тело трястись. Река из пота плавно впадала в море подо мной. Казалось, что с позором нырну в него.{/font}"
    window hide
    play sound sfx_fall_wood_floor
    with vpunch
    $ renpy.pause (0.5)
    show us surp1 pioneer at left
    show mi surprise pioneer close at right
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Так и случилось на 26. Руки предательски ослабли и тело прижало к полу. Ульянка хохотала. Мику понеслась на помощь.{/font}"
    show mi sad pioneer close at right
    with dspr
    mi "{font=mods/25_years_Later/Caveat.ttf}Говорила же меньше!{/font}"
    show us smile pioneer at left
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Мвехехе. Это мое желание, сколько захотела, столько и сказала. Продолжим?{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Что-либо сказать я не мог, сил не хватало. И вроде бы после этого Ульяна сжалилась, сказав:{/font}"
    show us normal pioneer at left
    with dspr
    us "{font=mods/25_years_Later/Caveat.ttf}Отдыхай, слабак. Мику твое желание следующее...{/font}"
    window hide
    play sound teleport
    stop music fadeout 1
    $ renpy.pause (1)
    play music mus_club fadein 1
    scene int_musclub_25
    with dissolve
    window show
    "{font=mods/25_years_Later/Caveat.ttf}...В отличие от Ульяны, задача Мику была в разы легче. Просто потереть клавиши влажной тряпкой.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}А что до Ульяны? Отомстил ей при следующей победе, когда заставил убираться в зале. Всё-таки я смеялся последним..{/font}"
    $ in_mus_club5 = True
    jump in_mus_club10
label in_mus_club20:
    window hide
    call screen menu_in_mus_club3 with dissolve
screen menu_in_mus_club3:

    modal False tag menu
    imagemap:
        ground "mods/25_years_later/images/in_mus_club/int_musclub3_1.png"
        hover "mods/25_years_later/images/in_mus_club/int_musclub3_2.png"
        hotspot (22, 892, 64, 134) action (Hide("menu"),Jump("in_mus_club1"))
        hotspot (446, 618, 62, 130) action (Hide("menu"),Jump("in_mus_club2"))
        hotspot (316, 360, 66, 136) action (Hide("menu"),Jump("in_mus_club3"))
        hotspot (768, 558, 64, 132) action (Hide("menu"),Jump("in_mus_club4"))
        hotspot (170, 186, 160, 146) action (Hide("menu"),Jump("in_mus_club5"))
        hotspot (1010, 670, 148, 146) action (Hide("menu"),Jump("in_mus_club6"))
        hotspot (1610, 410, 46, 134) action (Hide("menu"),Jump("in_mus_club7"))
label in_mus_club7:
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Упустить следующий маячок не представлялось возможным. Тот мигал, прикрепленный к окну.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Под ним находился конверт. С очередными словами от незнакомца, несущими судьбу пионера. Вскрывать не хотелось. Не хотелось ничего знать!{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Но руки сами полезли вперёд. Оторвали конверт, вскрыли, достав оттуда рукописный лист.{/font}"
    $ renpy.pause (1)
    scene int_musclub_1_1
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    $ renpy.pause (0.5)
    scene int_musclub_25 with dissolve
    play sound latter_open
    $ renpy.pause (6)
    scene int_musclub_1
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene int_musclub_2
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene int_musclub_3
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene int_musclub_4
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}...{/font}"
    play sound list_open
    $ renpy.pause (1)
    scene int_musclub_25
    with dissolve
    "{font=mods/25_years_Later/Caveat.ttf}Мику... Я ожидал подобное, но эти слова резанули так глубоко... На миг мои чувства пропали.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}У нее были идентичные проблемы c адаптацией. Она справилась, потом помогла мне. Мы были лучшими друзьями и все из-за схожостей.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Ещё странно. О ее концертах я слыхал, но чтоб о трагедии... Как так? Я не был в ту минуту... Не сумел попрощаться! Кто ж знал?..{/font}"
    window hide
    stop music fadeout 3
    $ renpy.pause (3)
    play music fight_25 fadein 3
    play sound sfx_fall_wood_floor
    with vpunch
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Руки отпустили рукописи, слабость повалила меня на деревянный паркет.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Именно сейчас я расслышал, как кто-то играет на рояле. Навязчивая мелодия и страшная.{/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Каждый выдох - пар. Пространство вокруг стало холодным.{w} Что-то сейчас произойдет. {/font}"
    "{font=mods/25_years_Later/Caveat.ttf}Дрож прошла по телу. Я быстро схватил письмо и прыгнул к выходу.{/font}"
    window hide
    $ renpy.pause (0.5)
    scene bg_25_mus_club
    with dspr
    window show
    "{font=mods/25_years_Later/Caveat.ttf}Потом побежал, оставляя домик позади.{/font}"
    window hide 
    scene bg_25_mus_club at beg_25
    with dissolve 
    jump tf_yl_chapter3

#глава 3 (кодил СТЕПАН4ик)
label tf_yl_chapter3: 
    $ save_name = '25 лет спустя. 3 глава. "Бесконечная игра".'
    window hide 
    stop music fadeout 18
    scene black
    with dissolve
    $ renpy.pause (3)
    #scene bg_25_chapter_3
    #with dissolve2
    $ renpy.pause (15)
    #play music dark_music_25 fadein 3
    with dissolve
    scene ext_polyana_night_25 
    play music evnening_25 fadein 2 
    with dissolve2
    window show 
    "Ноги несли меня неизвестно куда.{w} Сердце колотилось бешено.{w} В тот момент мне хотелось сбежать."
    "То есть свалить хоть куда, лишь бы дальше отсюда!{w} Но почему-то я не понимал где выход."
    "В отличие от прошлого меня - усталость дала о себе знать.{w} Остановился, начал жадно хватать воздух."
    "Потом бегло осмотрелся.{w} Я оказался чуть севернее домика, где смешанный лес."
    'Тихое место, скрывавшее под собой кучу развлечений.'
    'А все почему?{w} Простор для фантазий и отсутствие надзирателей брали свое.{w} Из маленьких головушек рождалось нечто.'
    'И не всегда безопасное.{w} Дитё легко получало ссадины и ушибы.{w} Вследствие чего пришли меры.'
    'Стену перенесли.{w} Свою популярность это место потеряло, ведь самое вкусное осталось по ту сторону.'
    'Но вскоре все изменилось.{w} Ульяна не могла смириться с потерей, всеми силами пытаясь придумать лазейку.'
    'И придумала!{w} Точнее нашла.{w} Довольно длинный тоннель,{w} заваленный с обеих сторон, проходил прямо под лагерем.'
    'Начало брал у домика на окраине.{w} Тамошний люк скрывался под паркетом и далеко не каждый мог его увидеть.'
    'Мику знала, но не рассказывала.{w} Ульяна открыла завесу тайн, когда убиралась из-за желания.'
    'Исследования вывели нас к заброшенному зданию, прямиком за стеной.{w} Люк также был в полу, но накрыт старым, узорчатым ковром.'
    'Вот и все.{w} Двухметровая кладка с кольями осталась позади,{w} а проход,{w} в тайне от вожатых, стал пользоваться популярностью.'
    'Но никто не выяснил куда ведет этот тоннель.{w} Были предположения, что к подземному объекту,{w} из-за которого случился сыр-бор.'
    'Спуск в недра я не одобрял.{w} Нет гарантии, что там безопасно,{w} да и без фонаря...{w} Лучше под солнышком.{w} Тут жизнь!'
    'Особенно сейчас, когда стена не доставляла проблем.{w} Сквозь обвалившеюся часть, я смог оказаться по ту сторону.'
    "Силы снова примкнули. Погони я не заметил, пока тут прохлаждался."
    "Чуйка говорила направляться к воротам и дать деру.{w} Любопытство же наоборот просило продолжения, ответы."
    "Я поддался второму. Не исключено, что это причудилось."
    call screen tfyl_interactive('q', 875, 665, 'tf_yl_chapter3.yama')
    call screen tfyl_interactive('message', 50, 410, 'tf_yl_chapter3.flashback')
    call screen tfyl_interactive('q', 200, 640, 'tf_yl_chapter3.base')
    call screen tfyl_interactive('message', 1340, 860, 'tf_yl_chapter3.flashback_2')
    call screen tfyl_interactive('q', 585, 795, 'tf_yl_chapter3.bonfire')
    call screen tfyl_interactive('message', 760, 220, 'tf_yl_chapter3.pond')
    call screen tfyl_interactive('em', 1650, 330, 'tf_yl_chapter3.convert')
    



label .yama:
    window hide 
    scene ext_polyana_night_25
    'Особенностью этого места была яма,{w} глубина которой измерялась десятками метров.'
    'За свое существование она собрала немало слухов.{w} И если отсеивать более бредовые и сказочные, то нарисовалась легенда.'
    'Связана та с секретными коммуникациями старого лагеря.{w} Те самые истории, где большинство тоннелей попросту завалило, отразились именно здесь.'
    'Не обошлось без странностей.{w} Дно было чистым!{w} Просевшая земля испарилась неведомым образом,{w} давая любопытным глазкам мутную картину.'
    'Бетонные стены, арматурины.{w} Свет еле-еле разьедал кромешную тьму.'
    'Вот ещё одна странность этого места.'
    'Ни солнце, ни мощный фонарь,{w} все попытки заканчивались однообразно.{w} Пока аттракциону не пришел конец.'
    'Яму заделали деревянными балками и железным кругом.{w} Все ради безопасности, конечно.'
    window hide 
    return 

label .flashback:
    'Старый лагерь являлся конфетой, получить которую мог не каждый.'
    'Между сокровенным и тобой находились километры колючей проволки.{w} Если пройти их, то возникало другое препятствие...'
    $ _window_hide(dissolve)
    stop music fadeout 2 
    play sound teleport fadein 1
    scene bg ext_polyana_sunset # or night так и не понял
    show window
    with flash
    play ambience ambience_camp_center_evening fadein 2
    '...Алиса разложила карту местности, где черным по-цветному нарисованы какие-то метки.'
    'Эти почеркушки - многочисленные препятствия, большинство которых относилось к природным.'
    'Пример - топь, занимавшая половину всей площади.{w} Человеческими ограждениями интересовались мало.{w} Их прохождение занимало не более пяти минут.'
    'Остальные пунктиры я не смог разобрать.{w} Расшифровку в правом нижнем углу загораживал Шурик.'
    'Он внимательно рассматривал детали, как и Алиса. Ульяна же полностью наоборот - бегала глазами, стараясь показать умный вид.'
    'Я был где-то посередине. Подготовка, лично для меня, не имела смысла. Это как пережёвывать кашу по двадцать раз.'
    show sh surprise pioneer at right with dissolve 
    sh "Кто это тебе подсунул, Алиса?"
    'Тишину размышлений прервал Шурик. Когда его очки в очередной раз скатились, он сразу оживился.'
    show dv guilty pioneer2 at left with dissolve 
    dv "Ребята побывавшие там...{w} Что-то не так?"
    show sh normal pioneer with dspr 
    sh "Все так.{w} Просто тут каждый сантиметр проработан.{w} Не верится, что они обошли все это."
    window hide 
    hide sh 
    hide dv 
    with dissolve
    window show 
    'И вновь тишина.{w} Два собеседника уткнулись в карту и бубнили что-то под нос.{w} Мое терпение тотчас лопнуло.'
    'Я отошёл и присел на поваленное бревно.{w} Товарищи сразу обратили внимание, особенно Ульяна. Ее состояние чем-то напоминало мое.'
    show dv angry pioneer2 far with dspr 
    dv 'И куда ты ушел?!' with hpunch 
    'К Алисе прильнула кровь, и ее глаза распахнулись горячим пламенем.' 
    th 'Сразу видно - ей не по нраву, что она работает, а какой-то Семён ступни разминает.'
    'Вместо того чтобы встать и подойти, заняться делом. Я выдавил из себя одно слово:'
    me 'Отдыхать...'
    play music music_list["pile"] fadein 2 
    show dv rage pioneer2 with dspr
    'Подруга тут же направилась в мою сторону.{w} Режим "самосохранения" сработал.{w} Я поспешно встал и начал набирать дистанцию.'
    dv 'Отдыхать?!' with hpunch
    dv 'А составлять маршрут кто будет?!' with hpunch
    dv 'Я?!' with hpunch
    dv 'Иди сюда!' with hpunch
    window hide 
    hide dv with dissolve
    $ renpy.pause(2,hard=True)
    sh 'А-алиса.' 
    extend ' Стоп-стоп!' with hpunch 
    extend ' Давайте без этой ерунды.' 
    extend ' Черт!' with vpunch
    extend ' Карта!!!' with hpunch
    'Внезапно в ЛЕСУ поднялся небольшой ветерок и карта, как перина, взлетела, зацепившись за ближайшую ветку.'
    'Шурик побежал к ней,{w} а за ним Алиса.{w} Теперь он был целью номер один.'
    window hide 
    show  us upset pioneer with dissolve 
    us "Капец ему.{w} Как думаешь?"
    hide us with dissolve
    window hide
    $ renpy.pause(2, hard=True)
    window show 
    'Ульяна совершенно спокойно сидела по левую руку, пока я прятался за деревом.' 
    'Я не мог не согласиться.{w} Шурик ещё не знал опасности и себе спокойно снимал карту.{w} Пока хищник не оказался за спиной.'
    'Чувствуя дыхание, тело медленно обернулось. Алиса стояла почти вплотную, улыбаясь в предвкушении.'
    sh 'Нет!' with hpunch 
    extend ' Стой!' with hpunch 
    extend ' Я хотел сказать...'
    dv 'Что ты хотел сказать?{w} Ну?' 
    sh 'Я-я-я...' 
    extend ' Да раз Семену не чем заняться, то пусть проникнет на склад!' with hpunch
    th 'Вылет через лобовое!{w} Это что ещё за смена сторон такая?!' 
    th 'Вот он...'
    'Местный склад обладал неплохим ассортиментом всего.{w} Множество предметов для нашего похода находилось именно там.'
    'Те же самые болотники, фонари и прочие инструменты.{w} Без первого ты не дойдешь, а без второго просто не найдешь что-либо ценное.'
    'Но была загвоздка.{w} Все это необходимо забрать и, после экспедиции, вернуть.{w} Причем нельзя стать замеченным, иначе все, дыры подлатают, и вынос станет не возможным.'
    'Вся эта ответственность ложилась на плечи. Её-то и боялись.{w} Если случится конфуз, то половина лагеря припомнит тебя добрым словом.'
    'Никому такое не надо, вот и боремся.'
    window hide 
    $ renpy.pause(2, hard=True)
    stop music fadeout 2
    'Временное затишье, похоже, Алиса думала над словами Шурика.{w} Настало время выхода.'
    'Я покинул укрытие и направился к парочке. Уж лучше отхватить и признать вину, чем думать над проникновением и дальнейшим выносом.'
    'Все это приправляют слова Шурика.{w} Появилось горячее желание ответить ему.'
    me ' Мы же хотели через лотерею!{w} Какого черта он говорит про меня?'
    show sh rage pioneer at right  with dissolve 
    sh 'Работать надо!' with hpunch
    extend ' Пока мы стояли, думали над планом, ты ничего не сказал!' with vpunch
    me 'Да у кого-то тушка большая!' with vpunch 
    extend ' Из-за нее я ни черта не видел!' with vpunch 
    'Накал страстей оборвала Алиса, которая громко воскликнула.{w} Ее раздражение пропало и вернулась та самая, которая всем нравится.'
    show dv normal pioneer2 at left with dissolve  
    dv 'Оба пойдете.{w} Так будет правильно.'
    show sh scared pioneer at right with dspr 
    'Оба переглянулись взглядами и уставились на Алису.{w} Добавлять было нечего, потому что остолбенели.'
    dv 'Возражений не?..'
    show sh rage pioneer at right  with dissolve 
    sh - 'Я же помогал. Почему я должен идти с ним!?' with vpunch 
    extend 'Он ведь ничего не сделал.'
    'Алиса спокойно прошла между нами и занялась картой, которую благополучно забрала у Шурика.'
    dv 'Возражений вижу нет...{w} Шурик, я не дурочка,{w} твои глупые вопросы и нелепые комментарии не являются работой.'
    sh 'Но я думал!' with vpunch
    'Внезапный смех со стороны Ульяны дал волю чувствам.{w} Алиса также начала хохотать{w} и я,{w} не имея на то причин, присоединился к ним.'
    show dv smile pioneer2 at left with dspr 
    $ renpy.pause(2,hard=True)
    show sh serious pioneer at right with dspr 
    window hide  
    $ renpy.pause(2,hard=True)
    hide dv 
    hide sh 
    with dissolve 
    'Шурик понял свое положение. Отлип от дерева и лёгким движением руки поманил за собой.'
    me 'Пошли с нами,{w} Алис?'
    dv 'А?{w} Нет.{w} Разделяйте этот геморрой между собой. А мне, спасибо, не надо.'
    'Напарник уже скрипнул люком и начал спускаться.{w} Это было сигналом и я, без замедлений, побежал следом...'
    '...Тот факт, что лотерею отменили, не отразился на мне из-за помощника.{w} К ночи мы готовились усердно.'
    'И только с мисс фортуной нам удалось забрать необходимое.{w} Вся эта паника чуть не рассекретила нас.{w} Адреналина было в достатке.'
    'Но выносить - не возвращать.' 
    'Однако это совсем другая история...'
    stop ambience fadeout 2
    scene ext_polyana_night_25 with fade 
    window hide 
    return
label .base:
    play music evnening_25 fadein 2 
    $ _window_hide(dissolve)
    scene ext_polyana_night_25 with fade2
    window show 
    'Игра со времен палеозоя{w}: строй домик из всех возможных ресурсов, а потом заполни мебелью.{w} Причем конец всегда был определен - полный снос.'
    'Этакое окончание появилось недавно.{w} Все из-за отбитых пальцев, заноз, ранок.{w} Вожатые устали не обращать внимание и приняли меры.'
    'После этого игра перестала доставлять удовольствие {w}- "Зачем же делать, если все равно снесут"{w} - и была тихо забыта.'
    'Время шло.{w} Строительный мусор так и валялся среди мха и папоротников, а бывшие конструкции напоминали о себе забитыми гвоздями и кусками дощечек.'
    'Пока не явилась Ульяна со своими друзьями.{w} Они нашли подходящее местечко и построили уютный домик.'
    'Там стены приколотили между деревьев,{w} крыльцо поставили,{w} а чердак возвысили.'
    'Выглядел, правда, хлипко.{w} Но ты попробуй за такие сроки уложиться.'
    'Тем и привлек внимание пионеров,{w} которые достали доски с молотками и понеслись в бой.'
    'Всякая маскировка пропала.{w} Домики, увы, снесли ещё раз.{w} На том развлечение закрылось и больше никто не строил.'
    window hide 
    return 
label .flashback_2: 
    stop music fadeout 2
    play ambience ambience_camp_center_evening fadein 2 
    'Благодаря маленькой договоренности, повара варили нам освежающий напиток.{w} Летний, ягодный морс.'
    'Правда, ингредиенты приносились с нашей стороны.{w} Ради одного литра, бывало, мог блуждать полдня...'
    $ _window_hide(dissolve)
    play sound teleport fadein 1
    scene bg ext_polyana_sunset # or night так и не понял
    show window
    with flash 
    '...Славяна была на отдалении, примерно десяти метров. Она молчаливо склонялась над каждым кустиком, бережно срывая ягодку за ягодкой.'
    'Она получала наслаждение.{w} А я, вымазанный в соку ягод, до сих пор не мог осилить половину банки.'
    th 'Черника-земляника. Хоть песню придумывай и под неё собирай.'
    'Я плавал в мыслях и всячески хотел отречься от однообразной реальности. Большую часть размышлений, конечно, составлял морс.'
    'Этот восхитительный вкус одурманил меня.{w} И ради одного стакана я...{w} Продал себя в рабство?'
    th 'Множество часов ради 200 грамм?{w} Настолько я дешёвый!?'
    show sl shy pioneer with dissolve
    sl 'Семён. Ты чего ягодки кушаешь?{w} Так у тебя никогда не наберётся.'
    'Славяна отвлеклась от сборов и посмотрела на меня красным румянцем.{w} Но этот прекрасный вид заставил меня подпрыгнуть на месте.'
    'Вкус ягод отчётливо остался на языке.{w} Банка на том же уровне.' 
    th 'То есть я пожинал ягодки пока думал?!'
    'Славяна прочитала меня как открытую книгу,{w} хихикнула{w}, и движением показала вытереть губы.{w} Я сразу послушался.'
    me 'Задумался...{w} Прости. А ягоды ничего.'
    'Шутка помогла мне оправиться.{w} Однако чувство, что я выгляжу полным идиотом, никуда не ушло.'
    hide sl with dissolve
    'Но Славяна,{w} судя по всему{w}, не думала об этом.{w} Вместо этого она достала горсть ягод и опрокинула в себя.'
    sl 'И прада! Вкушнааа!'
    'С набитым ртом она поделилась своим мнением.{w} Чем-то походила на меня...{w} То есть нелепо и смешно.'
    'Тем вызвала смех.{w} Сама Славяна сдерживалась, она ещё не до конца прожевала.{w} И ей это давалось нелегко.'
    me '...'
    extend ' И я так выглядел?!' with hpunch
    extend '  Хехехе.'
    show sl laugh pioneer with dissolve
    sl 'Угу.{w} Вах.{w} Как же трудно смеяться с набитым ртом!{w} Семён!{w} Тебя трудно копировать!'
    show sl shy pioneer
    $ renpy.transition(dissolve, layer="master")
    extend 'Не могу...'
    th 'Хотелось сказать про свою уникальность, однако, передумал.{w} С моей стороны это будет звучать слишком высокомерно.'
    'Поэтому я просто пожал плечами, мол, ничего не знаю, таким родился.{w} Славяна, приняв это, быстренько встала и, не скрывая улыбки, продолжила:'
    sl 'Всегда такой смешной... Спасибо, что согласился помочь.{w} Очень выручил.'
    hide sl with dissolve
    'Она встряхнула свои косы, заправилась.{w} Эта девушка всегда удивляла своим порядком.'
    'А это очень нравилось старшим.{w} Они видели в подруге взрослого человека, которому могли доверять.'
    'Можно подумать, что потеряли девку, слишком рано повзрослела.{w} Да нет!{w} Она сохранила качества юных лет.{w} Осталось свежей, полной сил и желаний.'
    me 'Выручить-то выручил. Но сколько нам ещё собирать?'
    show sl shy pioneer with dissolve
    sl 'Устал что ли? Можешь посидеть...'
    play sound komar_beep_25 
    me 'Нет-нет-нет!{w} Какой сидеть?!{w} Слышишь это?'
    'Комариный писк.{w} Причем его было так много, будто вертолет кружил над твоей головой и пытался приземлиться.'
    'Они жаждали пиршества и потому летели к нам.{w} Собственно, защиты от них не было.{w} Отрава лежала в комоде вожатой, а рубашка, из-за хлопка, не доставляла проблем кровососущим.'
    show sl surprise pioneer with dissolve 
    sl 'Так много?!{w} Но до вечера...{w} Семён?{w} Почему так пасмурно?'
    hide sl with dissolve
    'Любимая погода гадов царствовала над куполом. Её появление можно объяснить тем, что мы, кроме как искать ягоды, ни на что не обращали внимания.'
    'Время пролетело, а с ним появились многочисленные облака, скрывавшие пылающее солнце.'
    me 'Столько хватит ягод?'
    sl 'Надеюсь да.{w} Пошли в лагерь!'
    'Руки бегали по всему телу, отгоняли комаров.{w} Но хоть измахайся - все равно найдется тот, кто достанет.'
    'Почесывая именно такие места я, вместе со Славяной, бегом направились к лагерю.{w} Благо до него бежать, как мне до умывальников.'
    us 'Да никого...'
    extend ' Ай! Что за?!' with hpunch
    extend ' Облава, Паш!' with hpunch 
    extend ' Бежим!' with hpunch
    'Из-за ближайшей малины выскочила Ульяна с другом.{w} Приметив нас, оба, сразу же рванули в сторону лагеря.'
    show sl normal pioneer with dissolve
    sl 'Эй!{w} Ульяна!{w} Вы куда? Убежали...'
    show sl angry pioneer
    $ renpy.transition(dissolve, layer="master")
    extend ' Семён, откуда они выскочили?'
    me 'Вон оттуда. Видишь малину?'
    hide sl with dissolve
    'Славяна кивнула. После чего медленно, прямиком за мной, стала приближаться к месту побега.'
    'От Ульяны я ждал много чего, но это...{w} Сервелат, хлеб и треугольник молока.{w} Они тут пикник устроили?{w} Не похоже.'
    sl 'Ах. Мы помешали их свиданию. Семён, вот что мы за люди?'
    me 'Свидание с колбаской?{w} И чтоб Ульяна влюбилась?{w} Не смеши...'
    'Кроме засохших обьедков найти что-нибудь полезное мне не удалось.{w} Зато я выдвинул неплохую гипотезу.'
    me 'Подкармливают кого-то.{w} Однозначно.{w} Может, животинку какую.'
    'Славяна чуть ли не засмеялась во весь голос.{w} Она тотчас показала пальцем на треугольник молока...'
    me 'Может животные настолько поумнели, что умеют открывать их?'
    sl 'Хах.{w} Миллионы лет эволюции, чтоб открывать пачку молока?{w} Да-да.{w} Генетика посмеялась от души.{w} Хе-хе-хе.'
    me 'Не хотел бы я такую эволюцию...'
    play sound komar_beep_25 
    'Шутка удалась, но посмеяться не успели - укусы комаров дали о себе знать.'
    'Ещё этот гром.{w} Благодаря ему мы быстренько развернулись и побежали к домику на окраине, ближайшему месту с крышей над головой...'
    scene bg ext_polyana_sunset at beg_25
    stop ambience fadeout 2
    $ _window_hide(dissolve)
    stop sound
    scene ext_polyana_night_25 with fade 
    window hide 
    return




label .bonfire:
    play music evnening_25 fadein 2 
    scene ext_polyana_night_25 with fade2
    window show 
    'В традициях лагеря всегда присутствовал костёр.{w} Место, где ты временно забывал цивилизацию, полностью отдаваясь природе.'
    'Тут раскрывались твои первобытные навыки{w}: разожги костёр, поспи под деревом, займись собирательством.'
    'Правда, кроме первого, всем этим занимались в лагере.{w} Единственной изюминкой в походе являлся костёр.'
    'Нет лучше еды с открытого огня и песен от тепла.{w} Особенно в сумерки, когда вокруг пугающая темнота, пронзающая самых отважных.'
    'Здесь, у огонька, ты чувствовал безопасность.{w} А под длительные рассказы и гитарные струны ощущал комфорт.'
    'Не хватало только ночёвки.{w} Вожатые напрочь отвергали эту идею из-за риска потерять подопечных.'
    'Про дежурства совсем не заикались, ведь никто не хотел стоять всю ночь.'
    'Так и завелась привычка.{w} Раз-два за смену пионеров могли вывести на прогулку.{w} С утра до позднего вечера.'
    window hide 
    return



label  .pond:
    'Где-то на северо-востоке существовал небольшой пруд.{w} Неглубокий, с песком на дне.{w} Казалось, что он искусственный и сделан специально для старого лагеря.'
    'Это подтверждали заброшенные хибары, созданные для переодевания и хранения всячины.'
    'В остальном - незабвенная красота.{w} Одинокая и забытая всеми{w}, кроме одной Лены...'
    stop music fadeout 2 
    $ _window_hide(dissolve)
    play sound teleport fadein 1
    scene black
    play ambience ambience_camp_center_evening fadein 2 
    show window
    with flash 
    '... Уже полчаса меня вели с черной повязкой.{w} Глаза бегали туда-сюда, искали просвет.{w} Безуспешно.'
    'Единственный ориентир это рука и слова Лены.{w} Она вела меня неизвестно куда, и все под предлогом "Сюрприза".'
    'Я не был параноиком, но внезапно накатил страх.{w} А вдруг сюрприз для меня обернется чем-то плохим?'
    th 'Ну, нет, это ж Лена!' with vpunch 
    extend ' Она не сможет.'
    'К тому же она бережно предупреждала о всяких препятствиях, минимизируя столкновения.'
    'Так пленных не ведут.{w} Значит, все хорошо?'
    un "Пришли! Дай-ка сниму повязку."
    scene bg ext_polyana_day
    show window 
    with flash
    play music music_list["what_do_you_think_of_me"] fadein 2 
    'Солнце ударило в глаза, и мир открылся.{w} Бескрайние поля средь которых расстилался небольшой, чистый пруд.{w} Здешние деревья обходили это место, создавая неописуемый очаг.'
    'Пока я наслаждался этим, Лена обошла и села на импровизированный лежак из хвои.{w} Она украдкой посмотрела на меня и также уставилась на этот фон.'
    me "Гор не хватает...{w} Как ты нашла это место?"
    'Вопрос был очевиден.{w} Но ответ вызывал любопытство, ведь расстояние между лагерем и местом пара километров.'
    show un smile pioneer with dissolve
    un "Гуляла.{w} Сам знаешь, что природу люблю{w} и тут, по счастливой случайности, нашла это место."
    'Вновь обратила внимание.{w} Только теперь она смотрела на меня, стоящего в паре шагов.'
    show un shy pioneer with dissolve 
    un "Тебе нравится?"
    'Ответа не требовалось.{w} Мои глаза, которые до сих пор любовались картиной, ответили на вопрос.'
    hide un with dissolve
    'После любования я обратил внимание на Лену.{w} Она посматривала на меня и интенсивно работала с альбомом.'
    me "Ты чт?.." with hpunch
    un "Не двигайся!"
    'Вот и попал в ловушку.{w} Лена наверняка приступила к рисованию и теперь, как остолоп, я обязан стоять и потеть под палящим солнцем.'
    'Откуда она взяла все это - другой вопрос.{w} Больше всего меня привлекли движения ее рук, настолько плавно и четко, будто рисовала шедевр.'
    'Ее глаза следовали за карандашом и, изредка, останавливались, оценивая общую картину.'
    me "Ну, Лен. Дай в туалет сходить."
    un "Не-а. Пока не закончу нельзя двигаться!"
    'И ведь ослушаться нельзя...{w} Хотя бы головой можно мотать, Лена, вроде, была не против.'
    'Благодаря этому мне удалось хоть как-то убить время.{w} Разумеется, я мог начать диалог, но нужен ли он сейчас подруге?{w} Другой вопрос.{w} Творческим личностям приятна тишина.'
    th "Ох, черт. Как скучно!"
    window hide 
    scene  black with dissolve
    show text '{font=mods/25_years_Later/Caveat.ttf}{size=50}Спустя полчаса{/size}{/font}' at truecenter 
    $ renpy.pause(3, hard=True) 
    scene bg ext_polyana_sunset 
    show window 
    with fade3
    window show 
    'Все везде чесалось, а мошкара, как пираньи, крутились вокруг меня.{w} Для них я был шведским столом, просто выбирай где кусать.'
    'Ещё этот "зов природы".{w} Мысленно я присмотрел ближайшие кусты и представил, как я там блаженно...'
    un 'Все!' with hpunch 
    extend ' Готово!' with hpunch
    extend ' Ты как там?!'
    'Команда наполнила меня энергией, мышцы снова разогрелись.{w} Первое, что я сделал, так это начал растирать укусы.'
    me 'Пойдет...{w} Всего искусали, видела?'
    'Лена обратила внимание на ногу.{w} Множество красных точек, которые начинались от пятки и заканчивались у колена.{w} Не зная ситуации, я бы предположил, что попал в ядовитый плющ.'
    show un surprise pioneer with dissolve
    un 'Я сильно увлеклась.{w} Прости-прости. Не получился сюрприз, божечки...'
    hide un with dissolve
    'Она заметалась, но быстро сориентировалась.{w} Достала бутылку и быстро опрокинула на мои ноги.'
    'Холодок унял чесотку. Даже краснота немного спала.{w} А Лена, смотрю, знает толк.'
    un 'Лучше?'
    me 'Лучше. Ой...' with vpunch 
    extend ' Я сейчас!'
    'Одна проблема заменилась другой.{w} Как только внутри придавило, ноги сами помчались к кустам.'
    'Лена стояла столбом, видимо, поняла куда я так спешу.{w} Улыбка на все лицо явно подтверждало это.'
    window hide 
    scene  black with dissolve
    show text '{font=mods/25_years_Later/Caveat.ttf}{size=50}Спустя 15 минут{/size}{/font}' at truecenter 
    $ renpy.pause(3, hard=True) 
    scene bg ext_polyana_sunset
    show window 
    with fade3
    window show 
    'Слышишь, как Лена ныряет и начинает наслаждаться вододицей, так сразу становится обидно.{w} Как бы тоже хочется!'
    'Напряжение отпустило.{w} Организму стало легко и я, сделав все черные дела, отправился к подруге.'
    un 'Смотрю все.{w} Давай, Семён, присоединяйся!'
    me 'Конечн... Во, вынырнула.{w} Конечно, сейчас.'
    'Скинул с себя одежду по-армейски.{w} Обтягивающие плавки давно были на мне, потому что недавно наслаждался утренним солнцем.'
    'Лена все ныряла и около десятка секунд исследовала глубины.{w} Потом выныривала и по новой.'
    'А когда увидела меня, крикнула:'
    un 'Ну же, давай с разбегу!'
    'Как отказать такой милой даме? Я попрыгал на месте, немного потянулся и, разогрев ноги, побежал.'
    
    'Прыжок был быстрым.{w} Бомбочка не удалась и то, что успел изобразить, нельзя назвать словами.{w} Но больше смахивало на человека, который падает с высоты.'
    'Водоем скрыл меня.{w} От своего неудачного прыжка я словил испуг и как можно скорее вынырнул.{w} Лена вновь рассмеялась.'
    me 'Это просто... Не повезло.{w} Я ж мастер доныривать!'
    un 'Мвехехе.{w} Я видела.{w} Но можешь ещё раз попробовать, считай я забыла неудачу.'
    th 'И к чему я это сказал? Семён, обдумывай слова, хоть иногда.'
    'Себя я упрекал, но делать было нечего.'
    'Ноги снова почувствовали почву,я медленно шел к месту разбега.'
    me 'Иду-иду. Увидишь, что я могу.'
    un 'Стой!' with hpunch 
    extend ' С-семен, у тебя нога!'
    th - 'Нога? Что с ней? О, чертов-старый!'
    'Дно, как оказалось, я достал.{w} Оно прошлось по мне, как терка по сыру.{w} Где-то царапины, а где-то содранная кожа.{w} Все это украшало левую ногу, правая, как оказалась, была ещё цела.'
    un 'Стой на месте...{w} Я быстро!'
    'Она как можно скорее вылезла.{w} Милая, в купальнике, подбежала к форме и активно начала рыться в кармашках.{w} В конце вынула рулончик бинта.'
    'Откуда он у нее взялся там - неизвестно, да и не имеет значения.'
    me 'Да не надо. Сама заживёт.'
    un 'Я знаю, что сама может зажить.{w} Но это необходимо!{w} К тому же если заметит вожатая...'
    'Продолжать она не стала, ибо понимаем. Ко всяким царапинам, особенно гематомам, любят придираться.{w} Не дай бог ты ещё подрался, все, поднимают родителей, партию.'
    'А тебя, дорогого агрессора, могут увезти.{w} Потом забудешь, что такое пионерлагеря.'
    'Поэтому придираться не стал.'
    'Лена крепко-крепко затянула бинт.{w} Ранки начали щипаться, и дискомфорт был на лицо.'
    me 'Чего так от бинта щипет?!'
    un 'М?{w} Да он с присыпкой, чтобы быстрее ранка зарубцевались.{w} Вот.{w} Все, готово!'
    'Лена закончила, встала, отошла.{w} На месте ее работы оказался красивый бант, который стягивал два конца.'
    'Я ощупал ранки сквозь бинт, помассировал ногу и вновь обратился к Лене.'
    me 'Когда снять?'
    show un smile2 pioneer with dissolve
    un 'Вечером.{w} Главное водой не забудь промыть.{w} Хорошо?'
    me 'Хорошо. Спасибо, Лен.'
    hide un with dissolve
    'Лена сразу спрятала глазки, заключила руки в замок и отвернула голову. Появился мягкий румянец'
    un 'П-пожалуйста... Давай посмотрим, что я нарисовала?'
    me 'А давай. Чур я первый на ту лежанку!'
    'В тот день нас стали искать, а нас это не волновало.{w} Все невзгоды ушли, и мы наслаждались компанией друг друга.'
    'Лена даже привыкла к моему обществу, не боялась находиться вблизи.{w} После той прогулки мы стали ближе...'
    stop ambience fadeout 2 
    scene ext_polyana_night_25 with fade 
    window hide 
    return 
label .convert:
    stop music fadeout 4
    play music evnening_25 fadein 2  
    scene ext_polyana_night_25 with fade
    window show  
    'Конверты стали для меня неотъемлемой частью этого приключения.{w} После прочтения они намекали найти следующее место из списка.'
    'Незнакомец подкармливал мой интерес и не менее голодное любопытство.{w} Играл как с мышкой, ведя по лабиринтам.'
    'И новый конверт.{w} Одни мысли о них...'
    window hide 
    show tfyl_convert
    with dissolve
    $ renpy.pause(2, hard=True)
    hide tfyl_convert
    with dissolve
    $ mail_txt_print('Спустя два года лагерь позволил себя увидеть. Все это время я откладывала поездку и поняла, что зря...\nЛюди построили. Они же и разобрали. От лагеря остались одни воспоминания и холодные здания. Но я видела нечто больше...\nВторую жизнь. Тут все можно было восстановить, да и АЭС, которая неподалеку, перестала функционировать. Вот она возможность!\nЖаль, но помощи я не дождалась. Все мои рассказы вызвали один вопрос: Для чего?\nРаскрывать прелесть лагеря я не стала. Не поймут. Они ведь тут не жили. Да и то, что я видела, посчитают бредом.') 
    call screen tfyl_mail
    $ mail_txt_print('Поэтому начала одна. Восстановление заняло больше полутора года, если не считать зиму. В эту пору я уезжала и оставляла заместо себя друга\nОн топил здания через кочегарку и жил тут. Весной я сменяла его и так по кругу. Пока не случилось это...\nОбход лагеря завершался ночью, потом отбой на восемь часов с последующим подъемом. За это время случился налет, видимо, они следили за моим распорядком\nПроснулась. Увидела разрушения и просто отчаялась. Они вынесли все, а то что не смогли попросту сломали!\nПроснулась. Увидела разрушения и просто отчаялась. Они вынесли все, а то что не смогли попросту сломали!\n')
    call screen tfyl_mail
    'Последствия от вандалов сохранились по всему лагерю, отличия лишь в степени тяжести.{w} Ещё бы понять смысл в их действиях...'
    'Обогатиться обычным ресурсом?{w} Скорее да, чем нет.{w} Ещё подходит то, что они нашли в этом лагере свое пристанище.{w} Ну, место где можно делать все что угодно.'
    'А неизвестную, путем порчи построенного, хотели выгнать с лагеря.{w} Эх. Множество вариантов событий, среди которых один правильный.{w} Жаль, что во всех девушка столкнулась с такой проблемой.'
    'Я ощущал ее эмоции в тот день.{w} Злобу на преступников, а потом на себя, что не уследил.{w} Затем пустоту.{w} Все начинать с нуля...'
    'Это вызывало восхищение.{w} Немногим удастся сохранить желание после такого, а ей удалось.{w} Правда результат...'
    'Тут произошло нечто большее, чем просто вандалы.{w} Но кто же?'
    play music fight_25 fadein 2 
    'Внезапно, откуда-то из леса я ощутил присутствие.{w} После чего шаги подтвердили чувство.'
    'Они были недалеко, метров 50 не больше.{w} Этот кто-то хорошо скрывался, раз я до сих пор не мог его увидеть.'
    'Все что я сделал - это стоял и махал головой в разные стороны, чтобы не упустить силуэт.{w} Потом понял, что сбегать то никто не собирается.'
    'Нечто шло прямо ко мне, шаги увеличивали обороты, стали чётче.{w} Дальнейшие действия были ясны.'
    scene  ext_polyana_night_25 at beg_25
    $ renpy.pause(3,hard=True)
    scene  black with fade3 
    'Я развернулся и сразу побежал, хоть куда, лишь бы подальше.{w} Периодически оглядывался, убеждаясь, что погони нет.'
    stop music fadeout 5
    'Сбавил темп.{w} Правда, кряхтение с той стороны помогло выжать последние силы.'
    'Я оказался на футбольном поле.{w} До леса тут около 600-700 метров и это расстояние вызвало у меня серьезную усталость.'
    'Даже склонившись над землёй и жадно глотая воздух, я не прекращал наблюдать за лесом.{w} Только там никого не было.{w} Звуки исчезли.'
    'Сразу вспомнился "Я" из первой записки.{w} Блуждающий по лагерю, как ходячий труп без мотивации.{w} Ересь.{w} Но в лесу то что было?!'
    'Точно не животное, уверяю.{w} Это человек.{w} Сто процентов человек!{w} Ох, надеюсь я не схожу с ума...'
    'Темнота отошла, как только начался дождь.{w} Тело охладилось, одежда немного отсырела, а дневник, невероятным чудом, остался сухим.'
    window hide 
    $ renpy.pause(3,hard=True)
    window show 
    'Я лежал.{w} Как долго был без сознания не могу сказать, но через час должен наступить вечер.'
    'Голова гудела.{w} Я мало что осознавал, но основное помнил на зубок.{w} Один вопрос крутился в голове - как очутился на земле.'
    'Встал, отряхнулся и обратил внимание на лес.{w} Вроде ничего, можно выдохнуть.'
    'Но мои ноги понеслись прямо под трибуны. Единственное доступное укрытие, которое было в поле зрения.'
    'Осадки не усиливались.{w} Для многих это противный дождь, как бы он есть и как бы он не ощущается.'
    'Для меня он был как ни кстати лучше чем ливень.{w} Тот бы промочил мои записи и меня самого, а уж с сырой одеждой, простите, заболеть не так уж и трудно.'
    'Под трибунами трава была суше.{w} Здесь можно было отдохнуть и переждать напасть.'
    'От верхней одежды избавился, сидеть в ней не комфортно.{w} Ещё хотелось костра, тепла от его языков.'
    'Нельзя.{w} Хрен его знает кого он может привлечь.{w} Вдруг тот нежелатель отправится сюда?{w} Нет-нет.'
    'Вместо этого я заглянул в дневник.' 
    'Сделал записи и посмотрел на следующею точку.{w} А она, на счастье мне, оказалась в паре метрах.{w} Футбольное поле.'
    scene  ext_playground_night_25 with fade3
    play music evnening_25 fadein 2
    'Здесь был диод, который обозначил конверт.{w} Правда, спешить к нему я не стал, лучше дополнить дневник и тогда уж вскрывать.'

label .competition:
    scene  ext_playground_night_25 with fade
    'Совёнок не единственный лагерь в этой области.{w} Существовала пара других, конечно, менее масштабных.'
    'И один день в сезоне объединял их.{w} Соревнования походили на олимпийские игры, правда, с уклоном для развлечения.'
    'Призы были для каждого, да и план был переписан.{w} Все для детишек, все для их развлечения.'
    'Ну и куда же без символа.{w} Где-то в сторонке всегда плясала переодетая сова, которая поддерживала наших.'
    'Эти кричалки написала Славяна.{w} Каждая отличалась и легко оседала в голове.'
    'Даже Ульяна умудрялась учить все за 5 минут.{w} Во время дисквалификации она быстро преображалась, чтобы быть ближе к ребятам.'
    'И так происходило с утра до позднего вечера.{w} Это время состояло не только из спортивно-массовой, но и отдыха, трапезы и прочих развлечений.'
    'Среди тех были показы настоящих профессионалов, прославившихся в региональных состязаниях.'
    'Был и мировой уровень, но это сотня к одному.{w} Как повезет.{w} Жаль, что таких не застал.'
    'Зато я застал марафон на 3 километра.{w} Как помню себя дохлого на финише, так смеяться охота.'
    'Если поискать, то можно найти фотографию сделанную Леной.{w} Она была штатным фотографом и занималась стенгазетой.'
    '"Жизнь Совёнка".{p=1.5} Так называлась.{w} Была популярна у наших и приезжих...'
    'Особенное внимание уделялось финалу мероприятия, когда подводились итоги.'
    'Побеждал всегда "Совёнок".{w} Звучит, конечно, патриотично, но это правда.{w} Ещё бы в своих записях я стал врать, ага...'


label .learning_hand_combat:
    scene  ext_playground_night_25 with fade
    'Такой секции в лагере не водилось, были безобидные на подобии: футбола, тенниса.'
    'Однако,{w} как по графику,{w} каждый сезон сюда приезжал Алексей, тренер, обучивший немало юнош.'
    'Он предлагал освоить армейский рукопашный, который отличался простотой, но эффективностью в бою.'
    'Таким заинтересовался и я.{w} Ходил все три дня, пока он не уехал.'
    'Что сказать?{w} За этот срок я успел отработать пару приемов.{w} Они нехитрые, даже Ульяна смогла освоить.'
    'Да.{w} Эта девчонка занималась вместе со мной, хотела спарринг.{w} Правда, сразу перехотела, когда ее оппонентом стала кукла.'
    'Вообще ставить двух пионеров друг против друга было запрещено.{w} Тут, спрашивается, а как отрабатывать удары?{w} Да все очень просто.'
    'Правила созданы, чтобы их нарушать.{w} Поэтому Алексей предлагал следующее:'
    '"Ночью.{w} В заброшенной части лагеря.{w} Один."'
    'Из его уст это звучало зловеще.{w} Дай волю фантазии и тут можно соорудить множество пугающих теорий.{w} Плюс его физиономия Джейсона Вурхиза...'
    'На самом деле мы встречались на площадке между двух домиков.{w} Там нас экипировали так, чтобы на теле не оставалось синяков.{w} После чего пускали в бой...'
    'Честно?{w} Меня хватало не больше, чем на 10 минут.{w} Слишком много сил отнимает схватка.'
    'А сейчас я ничего уже не помню...{w} Найти бы его.{w} Он вроде как ещё жив, вон, в газетах частенько появляется вместе с какой-то девушкой.'
    'Примерно моего возраста...{w} С короткой стрижкой.{w} Черт{p=1.5}, выглядела та потрясающе...'



label .revenge:
    scene  ext_playground_night_25 with fade
    'У Ульяны была привычка тащить не свое.{w} Чаще всего она делала это для смеха,{w} иногда, для более масштабных планов.'
    'Тот случай не был исключением, когда она сперла мои плавки из душевых кабинок.{w} Те минуты были для меня очень напряжёнными...'
    $ _window_hide(dissolve)
    play sound teleport fadein 1
    stop music fadeout 2 
    scene ext_playground_sunset_25
    show window
    with flash 
    sh 'Ты уверен?{w} Из-за одних плавок ты {b}НАСТОЛЬКО{/b} готов отыграться?'
    'Мы скрывались за одним из множества кустов.{w} Отсюда был отличный вид на мои заготовки.'
    'Черт с этими плавками.{w} Этот момент я ждал куда больше {p=1.5}, а белье...{w} Оно стало гранью.{w} Сейчас повеселимся.'
    'Главное, чтоб Шурик молчал.{w} Он, конечно, молодец{w}, но если совесть его сожрёт...{w} Уж, лучше не думать.'
    'А может отправить его?{w} Ну-ка...'
    me 'Слушай{w}, Шурик{w}, давай кабанчиком за транзистором.{w} Он нужен{w}, срочно.'
    'Шурик недоуменно посмотрел на меня, как на дурака, сквозь очки.{w} Теперь я понял, что послать его будет сложной задачей.'
    sh 'Транзистор?{w} Все и так готово.{w} Для чего он тебе?'
    me 'Чтоб ты спросил...{w} Ладно, тихо.{w} Не суйся из кустов лишний раз.'
    'Шурик кивнул и снова переключился на футбольное поле.{w} Сейчас был вечер, пионеры любо собирались на пляже, либо на сцене.{w} Здесь, как исключение, могла появиться пара тройка, чтобы поиграть в футбол, но не более.'
    'Ульяна обязательно придет переодеться в пионерскую форму.{w} Нет.{w} Воровать ее я не собирался.{w} Тут было кое-что получше.'
    'Первое с чем она столкнется - замок.{w} Он потребует усилий, чтобы открыться.{w} Следующими будут бутерброды, которые она обязательно съест.{w} Горчица не подведёт.'
    'Отсюда вытекает отсутствие воды.{w} Я не садист, оставил бутылочку на трибунах, да так, что её просто невозможно не заметить.'
    'Плавно переходим к форме, которая обработана чесоточным порошком.{w} Спасибо Шурику за синтез.'
    'Ах, да, ещё одна деталь.{w} Один носок мы специально забросили на плафон, который на высоте двух с половиной Ульян.'
    th 'Вот такой небольшой сюрприз...'
    sh 'Ты чего уставился в одну точку?{w} Она идёт{p=1.5}, тссс.'
    'Ульяна беззаботно шла к нашему складу.{w} Оставались секунды до веселья{w}, я чувствовал.'
    sh 'Ай.{w} Семён.{w} Там кто-то по спине ползает, сними!{w} Кусается!'
    'Ульяна начала работать с дверью, как только Шурик заныл.{w} Переключившись на него, я понял, что наша позиция, ой, какая нехорошая.'
    'По его спине бегали муравьи.{w} Соответственно их дом был неподалеку и если подумать, то...'
    th 'Он прямо под Шуриком!{w} Как так не заметить?' with vpunch
    'Я начал отряхивать его.{w} Видел, как он хочет встать, почесаться, но терпел.'
    us 'Эй.{w} Дверь?{w} Совсем рухлядью стала?!{w} Кххх.' 
    us 'Да, емае!' with vpunch 
    'Мое внимание металось туда-сюда.{w} То Шурика спасай, то за Ульяной приглядывай.{w} И все же я отдал предпочтение первому.'
    me 'Переползи за меня, только тихо.{w} Она ещё может нас услышать.'
    sh 'Да-да.{w} Сейчас.'
    'Он послушался.{w} Перекинув ногу и руку за меня{w}, Шурик надеялся проскочить надо мной.'
    'Ульяна в то время пинала дверь, трясла, давила на ключ.{w} Но потом, как ни в чем не бывало, выдохнула и сказала:'
    us 'Ай, ладно.{w} Завтра Шурик вскроет.{w} Тьфу.'
    th 'Э-это как понимать?!' with vpunch 
    th 'Не честно!' with vpunch  
    'Шурик оказался по другое плечо и, увидев как Ульяна скрывается за трибунами, что-то пробубнил.'
    me 'Как так?{w} Вообще все к коту под хвост!{w} Ладно-ладно.{w} Она завтра попросит открыть дверь.{w} Ещё есть шанс!'
    sh 'И-и-и?'
    me 'Что "И-и-и?", Она назвала твое имя.{w} Вскроешь, а потом повеселимся.'
    'И вроде бы ничего не потеряно, но откладывать не хотелось.{w} Испытать те эмоции, которые предвкушал уже множество часов...'
    play sound sfx_hiding_in_bush
    'Мы встали.{w} Скоро должен быть горн на ужин{w}, да и эти насекомые достали{w}. Собрались уходить, пока не услышали шуршания в кустах.'
    play sound sfx_body_bump
    'Смачный шлепок пришелся по Шурику.{w} Яйцо, которое попало в затылок, лопнуло, и его содержимое плавно стекало с головы.'
    'Я отреагировал.{w} Перепрыгнул через куст и оказался за деревом.{w} Яйцо, которое назначалось мне, отчаянно шлепнулось об дерево.'
    'Шурик последовал моему примеру и оказался за деревом в паре метрах от меня.'
    me 'Ульяна нашла.{w} Ух, где она?{w} Ничерта не вижу.'
    sh 'Зачем искать, валим!' with vpunch
    'Шурик дернулся с места и побежал в сторону поля.{w} Но пара других яиц все же настигла его...'
    me 'Выбрался...{w} Надо было по команде, болван...'
    'Я понял, что кидаются двое.{w} Но вот откуда, хрен поймешь, они постоянно меняют позиции.'
    'А значит возьмут меня в круг и не будет выхода...'
    'Вспышка слева.{w} Яйцо вновь попало в дерево, только теперь скорлупа прошлась по лицу.{w} Нужно действовать!'
    me 'Я согласен на переговоры!{w} Сдаюсь.'
    dv 'Сдался Фриц, посмотрите!{w} Ульяна, тащи веревку!'
    'Старый дуэт...{w} Как я не смог догадаться.{w} А вообще, получается, что мы играли в их игру, а не они в нашу.'
    'Алиса шла со стороны убежавшего.{w} Ульяна шуршала где-то позади.{w} Правильно я думал, что в кругу.{w} И правильно сдался, а то бы выхватил от Алисы...'
    dv 'Твой товарищ слинял, но ты не беспокойся.{w} Нам тебя хватит.{w} А его завтра поймаем.'
    me 'Я весь ваш...'
    extend ' Ага, обойдетесь!' with vpunch
    scene bg ext_path_sunset at beg_25 
    show window 
    with flash
    play sound sfx_bush_leaves
    'Я подскочил и побежал в сторону кустов.{w} Алиса тоже была не промах, быстро размахнулась и кинула вслед.'
    'Промах.{w} Яйцо пролетело выше.{w} Но следующее не за горами, нужно убегать!'
    dv 'Стой, не уйдешь!'
    'Почему-то я чувствовал адреналин, будто за мной устроена настоящая погоня, не на жизнь, а на смерть.'
    'И это чувство мне нравилось.{w} Сейчас я планировал пробежать через площадь и скрыться.{w} Но сначала сбежать с этого мини-леса!'
    'Ульяна выскочила справа и яйцо, которое она кинула, попало мне прямо в плечо.{w} Затем достала следующее, размахнулась, и снова попала.'
    'Оглянулся. За мной бежала Алиса, а Ульяна, скорее всего, была внезапностью. То есть они меня загоняют как дичь? Хрена у них тактика!'
    th 'Хоп!' 
    play sound sfx_body_bump
    extend  ' Ещё одно яйцо мимо!' with vpunch
    play sound sfx_body_bump
    extend ' И ещё одно!' with vpunch 
    play sound sfx_body_bump
    extend ' И третье!' with vpunch
    play sound sfx_body_bump
    th 'Ой, а четвертое попало.{w} Прямо по затылку!' with vpunch
    scene ext_playground_sunset_25
    show window 
    with fade2
    'Лес остался позади.{w} Мои ноги почувствовали асфальт.{w} Он мне и дал понять, что Алиса меня нагоняет.'
    us 'Алиса!{w} Я Шурика поймала!{w} Давай сюда, пытать!'
    'Крикнула Ульяна.{w} Алиса остановилась и крикнула мне вслед:'
    dv 'Повезло тебе.{w} Хух, беги-беги.{w} Все равно достану!'
    scene ext_playground_sunset_25 at beg_25
    show window 
    with fade 
    'И я убежал, позабыв о Шурике, позабыв о нашем плане.{w} Все равно он расколется...'
    scene black with fade3

label .teacher:
    scene ext_playground_night_25 with fade 
    'Был ярким представителем бездельников.{w} На своей работе он должен быть дружелюбным, поддерживать в детишках тонус, а по факту лошадь едет задом наперед.'
    'Запирался у себя в домике, спал до обеда.{w} На поле, конечно, не появлялся.{w} При этом умудрялся не попадаться, что вызывало как минимум странность.'
    'Вот тут Ульяна решила{w}: пора восторжествовать справедливости.{w} И началась охота на физрука.'
    'Первое время шли откровенные приколы, которые забавляли.{w} Позже начали собирать доказательства.'
    'Решили обойтись одной камерой, но фотографии, как доказательства, не подошли.{w} Решили записать видео.'
    'Тоже отказали.{w} На третий раз мы решили привести вожатую, ее-то слова наверняка послушают{w}, пока не узнали кое-что важное.'
    'Физрук брат ответственного за лагерь.{w} Вот почему все доказательства отклонялись и даже вожатая, как говорила, бессильна в этом случае.'
    'Ольга Дмитриевна поблагодарила нас{w}, пообещав, что разберётся с проблемой лично.{w} И, кстати, не оплошала.{w} Физрука выгнали, появилось вакантное место.'
    'Я до сих пор не знаю, занял ли его кто-нибудь к 83 году.{w} Если да, то надеюсь{w}, что он был нормальным человеком.'
label .convert_2:
    scene ext_playground_night_25
    with fade 
    play music evnening_25 fadein 2 
    'Надутый кожаный мяч, лежащий посреди поля, привлек меня мигающим диодом.'
    'Содержимое было в моих руках, но я не торопился читать.{w} Чувство, будто за мной следят, внезапно появилось и усилилось.'
    'Дождь шел.{w} Неожиданный туман у леса привлек мое внимание и я потерял дар речи.{w} Там был человеческий силуэт!'
    'Судя по всему в пионерской форме.{w} Он следил за мной, а сейчас медленно пожирал изнутри.'
    window hide 
    show blink 
    with dissolve
    $ renpy.pause(2, hard=True)
    scene  black with flash_red
    window show 
    'Глаза вспыхнули красным.{w} Уши пронзил визг, после чего множество голосов твердило{w}: Старый лагерь.'
    stop music fadeout 2
    'Мышцы ослабли, я свалился на землю.{w} Вернулась родная тишина, ой, какое наслаждение.'
    window hide 
    scene  ext_polyana_night_25 with fade3 
    window show 
    'Нечто пропало также внезапно, как и появилось.{w} Туман рассеялся, дождь успокоился, дав солнцу просвет.'
    'Я уселся на траве.{w} Около получаса переваривал произошедшее, наблюдая за тем лесом.{w} Но никто больше не появился.'
    'Одно могу сказать - это был я, только молодой.'
    'Как понял? Чувства доказали, потому что {b}ЭТО{/b} было мне не незнакомо, а наоборот, будто я знал всю свою жизнь.'
    'Страх отступил.{w} Конверт, который разваливался от сырости требовал скорейшего чтения.'
    window hide 
    show tfyl_convert
    pause(3)
    hide tfyl_convert
    pause(2)
    $ mail_txt_print('Ульяну мы считали сорванцом, но кто им не был? Наверняка все совершали безумные действия не думая о последствиях...\nОднако лагерь воспитал Ульяну. Нет, не сделал идеальным роботом, выполнящий любые задачи. Скорее появилось чувство ответственности и порядочности...\nПоследний год выдался у нее весьма насыщенный. То зверушек покормит, то помощником будет, то уберется...\nА веселье никуда не пропадало. Только отрывалась она над двумя братьями, а  по тебе, увы, она очень сильно скучала и обещала при встрече навалять...', '"Юная сердцем"')
    call screen tfyl_mail
    $ mail_txt_print('Когда лагерь умер, Ульяна не смогла смириться с такой утратой. Она хотела заполнить эту пустоту и спустя время устроилась вожатой в другой, более крупный пионерлагерь...\nТуда она принесла игры "Совёнка", некоторые традиции и мероприятия. Желание сделать атмосферу схожей с нашей было у нее в крови...\nИ сделала! Благодаря этому она стала старшей. Она даже была ответственной за отряд, который приезжал тем же составом каждый год...\nИ не было тут место тоске, пока красная эпоха не ушла. Лагерь не выдержал и его постигла та же судьба, что и "Совёнка"...')
    call screen tfyl_mail
    $ mail_txt_print('Она пережила такую потерю во второй раз. Ее сердце опустело и с тех пор она разорвала все связи...\nНе было мотивации что-то создавать, ведь все равно рухнет. Единственное, что ей стало нравится - рукопись\nОна стала писать. Многие года она посвящала себя перу и знаниям. Около десятка книг есть в ее исполнении, которые разошлись по нашей державе...\nПоследняя была о лагерях. Вдохновлённая ею же, Ульяна отправилась в лагерь, обычной вожатой. Она сумела дать себе последний шанс...\nИ он не подвёл. Она сумела оставить свой след, который до сих пор существует. Жаль, что ее с нами нет...')
    call screen tfyl_mail
    $ mail_txt_print('Год назад Ульяна разбилась на мотоцикле. Она ехала после закрытия смены, холодной ночью. Один автомобиль занесло и хрупкое тело отбросило в сторону...\nВрачи констатировали мгновенную смерть из-за множества переломов...\nУльяна. Ты всегда для меня будешь юной, полной амбиций и желаний. Спи сладко.')
    call screen tfyl_mail
    return
