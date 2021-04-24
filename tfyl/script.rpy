# -*- coding: utf-8 -*-
label tfyl_start:

    $ tfyl = ModeStore()
    $ tfyl.day_time()


    scene bg black
    with fade2

    pause 3

    window show dissolve

    pause .3

    "Это было двадцать пять лет назад.{w} То время доживал пионерлагерь Совёнок, самый обычный, ничем не примечательный."
    "Он был любим за простоту и коллектив.{w} Из-за этого каждый новоприбывший хотел вернуться, ощутить ещё смену.{w} Таинственная магия?{w} Нет.{w} Просто такой лагерь.{w} С такими же простыми людьми.{w} Ничего сверхъестественного."
    "Но с уходом красной эпохи пришло затмение.{w} Жизнь покинула те территории и пионеры больше не возвращались."
    "О лагере забыли.{w} Воспоминания остались на фотографиях, а теплые моменты на пленке."
    "И я забыл.{w} Забыл каким я был пионером.{w} Но один день все изменил."

    window hide dissolve

    $ renpy.pause (1)

    scene intro_mail_table with fade3

    $ renpy.pause (.5)

    window show dissolve

    "Привет из прошлого ждал на пороге дома.{w} Выглаженный конверт со старыми марками и пионерским значком позади."
    "Все это оказалось на столе.{w} Я не сразу решил вскрывать его, сначала хотел изучить."
    "Как и потертый значек, то было прямиком с прошлого века.{w} Местами грязный, местами пожелтевший."
    "Минуя формы было написано имя…{w} Мое имя!"

    window hide dissolve

    $ renpy.pause (.2)

    show intro_mail_photo with dspr

    $ renpy.pause (.5)

    window show dissolve

    "Внутри оказалась записка и реставрированная фотография.{w} Тотчас я вспомнил откуда это.{w} Совёнок…"
    "Мысли бегали.{w} С каждой секундой я все сильнее пробирался в закрома памяти с надеждой вспомнить."

    window hide dissolve

    $ renpy.pause (.2)

    show intro_mail_page 1 with moveinbottom

    pause

    hide intro_mail_page with moveoutbottom

    $ renpy.pause (.55)

    show intro_mail_page 2 with moveinbottom

    pause

    window show dissolve

    "Кто-то просил помощь, не дать забыться лагерю.{w} Глупая просьба, как я посчитал тогда."

    window hide dissolve
    scene bg black with fade
    $ renpy.pause (1)
    window show dissolve

    "Записка вернулась в конверт, а я откинулся на стуле,{w} не имея желания помогать."

    window hide dissolve

    $ renpy.pause (1)

    scene intro_mail_table
    show intro_mail_photo
    show intro_mail_blood
    with fade2

    $ renpy.pause (.2)

    window show dissolve

    "К вечеру того же дня меня настиг второй конверт.{w} Тот был в крови, мятый{w}, и нес в себе одну мысль."

    show intro_mail_page 3 with moveinbottom

    "Лагерь требовал меня.{w} Оставив множество вопросов, пряча ответы где-то за своими стенами."
    "Минутное колебание и я…"
    "Я решился!"

    window hide dissolve
    stop music fadeout 3

    jump tfyl_gates
