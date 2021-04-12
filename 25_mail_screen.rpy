init python:
    text_mail = []
    def mail_txt_print(text, head=''):
        text_mail.append((text, head))
        renpy.restart_interaction()
    def mail_txt_clear():
        text_mail.clear()
        renpy.restart_interaction()
init:
    image tfyl_convert = 'mods/25_years_later/images/ruka_konvert.png'
    image tfyl_mail = 'mods/25_years_later/images/ruka_pismo_25.png' 



screen tfyl_mail():
    on 'hide':
        action Function(mail_txt_clear)
    tag tfyl modal False
    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return(), Function(mail_txt_clear)
    frame:
        background 'tfyl_mail'
        window:
            background None
            for txt, head in text_mail:
                if head != '':
                    text '%s'% head xpos 700 ypos 110  font 'mods/25_years_later/mail_font.ttf' color '#020e39' bold True size 30
                    text '%s' % txt xpos 520 xmaximum 580 ypos 200 font 'mods/25_years_later/mail_font.ttf' color '#020e39' bold True size 25
                else:
                    text '%s' % txt xpos 520 xmaximum 580 ypos 100 font 'mods/25_years_later/mail_font.ttf' color '#020e39' bold True size 25

screen tfyl_interactive(btn, x, y, label):
    tag tfyl modal True
    if btn != 'em':
        imagebutton auto('mods/25_years_later/images/interactive/'+btn+'_%s.png') xpos x ypos y action Call(label)
    else:
        imagebutton auto('mods/25_years_later/images/interactive/'+btn+'_%s.png') xpos x ypos y action Jump(label)