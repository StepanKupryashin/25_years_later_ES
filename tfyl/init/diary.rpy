init: # Нужно запихнуть в screens

    screen tfyl_mail(mail=None, sender=None, remove=False):

        modal True

        default page = 0
        default maxpage = 0

        if mail:
            $ maxpage = len(mail)-1

        fixed:
            if not remove:

                at transform:

                    ypos 1.0
                    linear .5 ypos 0.0

                button background None action (Show("tfyl_mail", None, mail, remove=True) if page >= maxpage else SetScreenVariable("page", page+1))
            else:
                at transform:
                    ypos 0.0
                    linear .5 ypos 1.0

                timer 1 action Hide("tfyl_mail")


            if mail:
                add "mods/tfyl/gui/mail/open.png"

                text mail[page] font "mods/tfyl/fonts/mail_font.ttf" color "336" line_spacing -7 line_leading 0 size 32 xsize .3 ysize .7 xpos .27 ypos .1 anchor (.0, .0)

                if sender:
                    text sender font "mods/tfyl/fonts/mail_font.ttf" color "336" size 30 xpos .45 ypos .87
            else:
                add "mods/tfyl/gui/mail/inside.png"


    screen tfyl_diary():


        default show_mail_list = False


        key "K_TAB" action SetScreenVariable("show_mail_list", not show_mail_list)

        showif not show_mail_list and tfyl.mails:

            mousearea:
                area (0, 0, 150, 1.0)
                hovered SetScreenVariable("show_mail_list", True)
                unhovered SetScreenVariable("show_mail_list", False)

            imagebutton:

                idle "mods/tfyl/gui/mail/convert.webp"

                action SetScreenVariable("show_mail_list", True)

                at transform:

                    xoffset -400

                    on show:
                        alpha 0
                        ease 1 alpha 1
                        on hover:
                            ease .25 xoffset -350

                        on idle:
                            ease .25 xoffset -400
                    on hide:
                        alpha 1
                        ease 1 alpha 0

        else:

            mousearea:
                area (0, 0, 550, 1.0)
                hovered SetScreenVariable("show_mail_list", True)
                unhovered SetScreenVariable("show_mail_list", False)

            for i, mail in enumerate(tfyl.mails):
                imagebutton:
                    idle "mods/tfyl/gui/mail/convert.webp"
                    hover HBox("mods/tfyl/gui/mail/convert.webp", Text(mail))

                    action (SetScreenVariable("show_mail_list", False), Show("tfyl_mail", mail=tfyl.mails[mail]))
                    at transform:

                        yalign (i/(len(tfyl.mails)+.0))*.8


                        xoffset -300

                        on show:
                            xoffset -600
                            yalign 0.0
                            ease .3 xoffset -300
                            ease .5 yalign (i/(len(tfyl.mails)+.0))*.8

                            on hover:
                                ease .25 xoffset -100

                            on idle:
                                ease .25 xoffset -300

                        on hide:
                            xoffset -300
                            yalign (i/(len(tfyl.mails)+.0))*.8

                            ease .5 yalign .0
                            ease .3 xoffset -600



    # transform cd_transform:
    #     # This is run before appear, show, or hide.
    #     xalign 0.5 yalign 0.5 alpha 0.0
    #
    #     on appear:
    #         alpha 1.0
    #     on show:
    #         zoom .75
    #         linear .25 zoom 1.0 alpha 1.0
    #     on hide:
    #         linear .25 zoom 1.25 alpha 0.0
    #
    # screen countdown():
    #     default n = 3
    #
    #     vbox:
    #         textbutton "3" action SetScreenVariable("n", 3)
    #         textbutton "2" action SetScreenVariable("n", 2)
    #         textbutton "1" action SetScreenVariable("n", 1)
    #         textbutton "0" action SetScreenVariable("n", 0)
    #
    #     showif n == 3:
    #         text "Three" size 100 at cd_transform
    #     elif n == 2:
    #         text "Two" size 100 at cd_transform
    #     elif n == 1:
    #         text "One" size 100 at cd_transform
    #     else:
    #         text "Liftoff!" size 100 at cd_transform
