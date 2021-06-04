# Код был автосгенерирован утилитой от https://github.com/Mikan-DS

init:

    # Спрайты
    image ad 1 dress angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_angry.png"
)
    image ad 1 dress dislike = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_dislike.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_dislike.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_dislike.png"
)
    image ad 1 dress grin = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_grin.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_grin.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_grin.png"
)
    image ad 1 dress laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_laugh.png"
)
    image ad 1 dress normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_normal.png"
)
    image ad 1 dress sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_sad.png"
)
    image ad 1 dress serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_serious.png"
)
    image ad 1 dress shocked = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_shocked.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_shocked.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_shocked.png"
)
    image ad 1 dress smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile.png"
)
    image ad 1 dress smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_dress_smile1.png"
)
    image ad 1 gloves = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_gloves.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_gloves.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_gloves.png"
)
    image ad 1 pioneer angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_angry.png"
)
    image ad 1 pioneer dislike = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_dislike.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_dislike.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_dislike.png"
)
    image ad 1 pioneer grin = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_grin.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_grin.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_grin.png"
)
    image ad 1 pioneer laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_laugh.png"
)
    image ad 1 pioneer normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_normal.png"
)
    image ad 1 pioneer sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_sad.png"
)
    image ad 1 pioneer serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_serious.png"
)
    image ad 1 pioneer shocked = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_shocked.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_shocked.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_shocked.png"
)
    image ad 1 pioneer smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile.png"
)
    image ad 1 pioneer smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_pioneer_smile1.png"
)
    image ad 1 sport angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_angry.png"
)
    image ad 1 sport dislike = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_dislike.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_dislike.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_dislike.png"
)
    image ad 1 sport grin = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_grin.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_grin.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_grin.png"
)
    image ad 1 sport laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_laugh.png"
)
    image ad 1 sport normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_normal.png"
)
    image ad 1 sport sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_sad.png"
)
    image ad 1 sport serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_serious.png"
)
    image ad 1 sport shocked = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_shocked.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_shocked.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_shocked.png"
)
    image ad 1 sport smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile.png"
)
    image ad 1 sport smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_sport_smile1.png"
)
    image ad 1 swim angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_angry.png"
)
    image ad 1 swim dislike = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_dislike.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_dislike.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_dislike.png"
)
    image ad 1 swim grin = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_grin.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_grin.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_grin.png"
)
    image ad 1 swim laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_laugh.png"
)
    image ad 1 swim normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_normal.png"
)
    image ad 1 swim sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_sad.png"
)
    image ad 1 swim serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_serious.png"
)
    image ad 1 swim shocked = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_shocked.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_shocked.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_shocked.png"
)
    image ad 1 swim smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile.png"
)
    image ad 1 swim smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_1_swim_smile1.png"
)
    image ad 2 dress cry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_cry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_cry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_cry.png"
)
    image ad 2 dress fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_fear.png"
)
    image ad 2 dress laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_laugh.png"
)
    image ad 2 dress ponder = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_ponder.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_ponder.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_ponder.png"
)
    image ad 2 dress sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_sad.png"
)
    image ad 2 dress shy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_shy.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_shy.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_shy.png"
)
    image ad 2 dress smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile.png"
)
    image ad 2 dress smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_smile1.png"
)
    image ad 2 dress surprised = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_surprised.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_surprised.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_dress_surprised.png"
)
    image ad 2 gloves = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_gloves.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_gloves.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_gloves.png"
)
    image ad 2 pioneer cry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_cry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_cry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_cry.png"
)
    image ad 2 pioneer fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_fear.png"
)
    image ad 2 pioneer laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_laugh.png"
)
    image ad 2 pioneer ponder = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_ponder.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_ponder.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_ponder.png"
)
    image ad 2 pioneer sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_sad.png"
)
    image ad 2 pioneer shy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_shy.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_shy.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_shy.png"
)
    image ad 2 pioneer smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile.png"
)
    image ad 2 pioneer smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_smile1.png"
)
    image ad 2 pioneer surprised = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_surprised.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_surprised.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_pioneer_surprised.png"
)
    image ad 2 sport cry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_cry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_cry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_cry.png"
)
    image ad 2 sport fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_fear.png"
)
    image ad 2 sport laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_laugh.png"
)
    image ad 2 sport ponder = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_ponder.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_ponder.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_ponder.png"
)
    image ad 2 sport sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_sad.png"
)
    image ad 2 sport shy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_shy.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_shy.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_shy.png"
)
    image ad 2 sport smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile.png"
)
    image ad 2 sport smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_smile1.png"
)
    image ad 2 sport surprised = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_surprised.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_surprised.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_sport_surprised.png"
)
    image ad 2 swim cry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_cry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_cry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_cry.png"
)
    image ad 2 swim fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_fear.png"
)
    image ad 2 swim laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_laugh.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_laugh.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_laugh.png"
)
    image ad 2 swim ponder = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_ponder.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_ponder.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_ponder.png"
)
    image ad 2 swim sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_sad.png"
)
    image ad 2 swim shy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_shy.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_shy.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_shy.png"
)
    image ad 2 swim smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile.png"
)
    image ad 2 swim smile1 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile1.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile1.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_smile1.png"
)
    image ad 2 swim surprised = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_surprised.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_surprised.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_2_swim_surprised.png"
)
    image ad 3 dress angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_angry.png"
)
    image ad 3 dress fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_fear.png"
)
    image ad 3 dress quilty = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_quilty.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_quilty.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_quilty.png"
)
    image ad 3 dress rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_rage.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_rage.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_rage.png"
)
    image ad 3 dress sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_sad.png"
)
    image ad 3 dress serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_serious.png"
)
    image ad 3 dress smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_smile.png"
)
    image ad 3 dress trouble = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_trouble.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_trouble.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_dress_trouble.png"
)
    image ad 3 gloves = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_gloves.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_gloves.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_gloves.png"
)
    image ad 3 pioneer angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_angry.png"
)
    image ad 3 pioneer fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_fear.png"
)
    image ad 3 pioneer guilty = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_guilty.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_guilty.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_guilty.png"
)
    image ad 3 pioneer rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_rage.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_rage.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_rage.png"
)
    image ad 3 pioneer sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_sad.png"
)
    image ad 3 pioneer serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_serious.png"
)
    image ad 3 pioneer smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_smile.png"
)
    image ad 3 pioneer trouble = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_trouble.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_trouble.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_pioneer_trouble.png"
)
    image ad 3 sport angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_angry.png"
)
    image ad 3 sport fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_fear.png"
)
    image ad 3 sport guilty = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_guilty.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_guilty.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_guilty.png"
)
    image ad 3 sport rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_rage.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_rage.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_rage.png"
)
    image ad 3 sport sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_sad.png"
)
    image ad 3 sport serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_serious.png"
)
    image ad 3 sport smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_smile.png"
)
    image ad 3 sport trouble = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_trouble.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_trouble.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_sport_trouble.png"
)
    image ad 3 swim angry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_angry.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_angry.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_angry.png"
)
    image ad 3 swim fear = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_fear.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_fear.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_fear.png"
)
    image ad 3 swim guilty = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_guilty.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_guilty.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_guilty.png"
)
    image ad 3 swim rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_rage.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_rage.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_rage.png"
)
    image ad 3 swim sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_sad.png"
)
    image ad 3 swim serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_serious.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_serious.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_serious.png"
)
    image ad 3 swim smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_smile.png"
)
    image ad 3 swim trouble = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_trouble.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_trouble.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/ad/normal/ad_3_swim_trouble.png"
)
    image vasan adidas = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/tfyl/images/sprites/vasan/vasan adidas.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/tfyl/images/sprites/vasan/vasan adidas.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/tfyl/images/sprites/vasan/vasan adidas.png"
)



    # Разные изображения
    image bg ext_tfyl_musclub = "mods/tfyl/images/bg/ext_tfyl_musclub.png"
    image bg int_tfyl_musclub = "mods/tfyl/images/bg/int_tfyl_musclub.png"
    image bg playground_sunset = "mods/tfyl/images/bg/playground_sunset.jpg"
    image bg tfyl_beach = "mods/tfyl/images/bg/tfyl_beach.png"
    image bg tfyl_boat_stantion = "mods/tfyl/images/bg/tfyl_boat_stantion.png"
    image bg tfyl_clubs = "mods/tfyl/images/bg/tfyl_clubs.png"
    image bg tfyl_dining_hall = "mods/tfyl/images/bg/tfyl_dining_hall.png"
    image bg tfyl_ext_house_of_dv = "mods/tfyl/images/bg/tfyl_ext_house_of_dv.png"
    image bg tfyl_gates = "mods/tfyl/images/bg/tfyl_gates.jpg"
    image bg tfyl_house_of_mt = "mods/tfyl/images/bg/tfyl_house_of_mt.jpg"
    image bg tfyl_house_of_un = "mods/tfyl/images/bg/tfyl_house_of_un.png"
    image bg tfyl_library = "mods/tfyl/images/bg/tfyl_library.png"
    image bg tfyl_playground = "mods/tfyl/images/bg/tfyl_playground.png"
    image bg tfyl_polyana = "mods/tfyl/images/bg/tfyl_polyana.png"
    image bg tfyl_road = "mods/tfyl/images/bg/tfyl_road.png"
    image bg tfyl_square = "mods/tfyl/images/bg/tfyl_square.png"
    image bg tfyl_stage = "mods/tfyl/images/bg/tfyl_stage.png"
    image bg tfyl_stage_near = "mods/tfyl/images/bg/tfyl_stage_near.png"
    image intro_mail_blood = "mods/tfyl/images/intro/blood.png"
    image intro_mail_page 1 = "mods/tfyl/images/intro/page_1.png"
    image intro_mail_page 2 = "mods/tfyl/images/intro/page_2.png"
    image intro_mail_page 3 = "mods/tfyl/images/intro/page_3.png"
    image intro_mail_photo = "mods/tfyl/images/intro/photo.png"
    image intro_mail_table = "mods/tfyl/images/intro/table.png"


    # Аудио
    python: # выглядит красивее чем $ перед каждой строкой
        Phobos_Base = "mods/tfyl/audio/music/Phobos_Base.mp3"
        banzo = "mods/tfyl/audio/music/banzo.mp3"
        dark_music_25 = "mods/tfyl/audio/music/dark_music_25.ogg"
        evnening_25 = "mods/tfyl/audio/music/evnening_25.mp3"
        ext_mus_club_mixdown = "mods/tfyl/audio/music/ext_mus_club_mixdown.ogg"
        fight_25 = "mods/tfyl/audio/music/fight_25.mp3"
        latter_25 = "mods/tfyl/audio/music/latter_25.mp3"
        mus_club = "mods/tfyl/audio/music/mus_club.mp3"
        other_25 = "mods/tfyl/audio/music/other_25.mp3"
        other_25_1 = "mods/tfyl/audio/music/other_25_1.mp3"
        start_25 = "mods/tfyl/audio/music/start_25.mp3"
        tfyl_miku_song = "mods/tfyl/audio/music/tfyl_miku_song.ogg"
        komar_beep = "mods/tfyl/audio/sfx/komar_beep.mp3"
        latter_open = "mods/tfyl/audio/sfx/latter_open.mp3"
        list_open = "mods/tfyl/audio/sfx/list_open.mp3"
        me_dive = "mods/tfyl/audio/sfx/me_dive.mp3"
        sfx_solemn_horn = "mods/tfyl/audio/sfx/sfx_solemn_horn.ogg"
        teleport = "mods/tfyl/audio/sfx/teleport.mp3"
        un_dive = "mods/tfyl/audio/sfx/un_dive.mp3"
