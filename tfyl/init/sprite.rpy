init -1:   
     
    image sv surprise2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/surprise2(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/surprise2(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/surprise2(F).png") )
    
    image sv surprise2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/nor/surprise2(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/surprise2(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/surprise2(N).png") )
    
    image sv surprise2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/surprise2(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/surprise2(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/surprise2(C).png") )
    
    image sv scared pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/scared(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/scared(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/1_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/scared(F).png") )
    
    image sv scared pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/nor/scared(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/scared(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/1_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/scared(N).png") )
    
    image sv scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/scared(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/scared(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/1_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/scared(C).png") )
        
    image sv shy2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy(F).png") )
    
    image sv shy2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/shy_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/nor/shy(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/shy_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/far/shy(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/shy_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/normal/shy(N).png") )
    
    image sv shy2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/1/close/shy(C).png") )
    
    image sv shy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/shy(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/shy(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/shy(C).png") )
            
    image sv shy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/shy(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/shy(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/shy(N).png") )  
    
    image sv shy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/shy(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/shy(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/shy(F).png") )
    
    image sv smile1 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/smile1(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/smile1(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/smile1(N).png") )  
    
    image sv smile1 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/smile1(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/smile1(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/smile1(F).png") )
    
    image sv smile1 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/smile1(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/smile1(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/smile1(C).png") )
    
    image sv sorrow pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/2_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png") )  
    
    image sv sorrow pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/2_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png") )
    
    image sv sorrow pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/2_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png") )
    
    image sv cry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/sorrow(N).png") )  
    
    image sv cry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/sorrow(F).png") )
    
    image sv cry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/sorrow(C).png") )
    
    image sv cry_smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_smile(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_smile(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/normal/cry_smile(N).png") ) 
    
    image sv cry_smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_smile(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_smile(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/far/cry_smile(F).png") )
    
    image sv cry_smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_smile(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_smile(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/2/close/cry_smile(C).png") )
    
    image sv happy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/happy(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/happy(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/happy(N).png") )   
    
    image sv happy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/happy(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/happy(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/happy(F).png") )
    
    image sv happy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/happy(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/happy(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/happy(C).png") )
    
    image sv laugh pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/laugh(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/laugh(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/laugh(N).png") )   
    
    image sv laugh pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/laugh(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/laugh(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/laugh(F).png") )
    
    image sv laugh pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/laugh(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/laugh(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/laugh(C).png") )
    
    image sv serious pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/serious(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/serious(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/serious(N).png") ) 
    
    image sv serious pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/serious(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/serious(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/serious(F).png") )
    
    image sv serious pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/serious(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/serious(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/serious(C).png") )
            
    image sv smile2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/smile2(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/smile2(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/3_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/normal/smile2(N).png") )  
    
    image sv smile2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/smile2(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/smile2(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/3_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/far/smile2(F).png") )
    
    image sv smile2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/smile2(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/smile2(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/3_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/3/close/smile2(C).png") )
                
    image sv angry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/angry(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/angry(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/angry(N).png") )   
    
    image sv angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/angry(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/angry(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/angry(F).png") )
    
    image sv angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/angry(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/angry(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/angry(C).png") )
                    
    image sv calm pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/calm(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/calm(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/calm(N).png") )    
    
    image sv calm pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/calm(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/calm(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/calm(F).png") )
    
    image sv calm pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/calm(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/calm(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/calm(C).png") )
                    
    image sv grin pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/grin(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/grin(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/grin(N).png") )    
    
    image sv grin pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/grin(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/grin(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/grin(F).png") )
    
    image sv grin pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/grin(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/grin(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/grin(C).png") )
    
    image sv indif pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/indifference(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/indifference(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/indifference(N).png") )    
    
    image sv indif pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/indifference(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/indifference(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/indifference(F).png") )
    
    image sv indif pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/indifference(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/indifference(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/indifference(C).png") )
        
    image sv rage pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/rage(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/rage(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/rage(N).png") )    
    
    image sv rage pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/rage(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/rage(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/rage(F).png") )
    
    image sv rage pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/rage(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/rage(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/rage(C).png") )
            
    image sv sad pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/sad(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/sad(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/sad(N).png") ) 
    
    image sv sad pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/sad(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/sad(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/sad(F).png") )
    
    image sv sad pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/sad(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/sad(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/sad(C).png") )
    
    image sv shocked2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/shocked2(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/shocked2(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/4_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/normal/shocked2(N).png") )    
    
    image sv shocked2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/shocked2(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/shocked2(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/4_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/far/shocked2(F).png") )
    
    image sv shocked2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/shocked2(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/shocked2(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/4_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/4/close/shocked2(C).png") )
        
    image sv muse pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/muse(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/muse(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/muse(N).png") )    
    
    image sv muse pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/muse(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/muse(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/muse(F).png") )
    
    image sv muse pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/muse(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/muse(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/muse(C).png") )
            
    image sv smile3 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/smile3(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/smile3(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/smile3(N).png") )  
    
    image sv smile3 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/smile3(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/smile3(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/smile3(F).png") )
    
    image sv smile3 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/smile3(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/smile3(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/smile3(C).png") )
    
    image sv scared2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/scared2(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/scared2(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/scared2(N).png") )  
    
    image sv scared2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/scared2(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/scared2(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/scared2(F).png") )
    
    image sv scared2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/scared2(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/scared2(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/scared2(C).png") )
    
    image sv surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/surprise(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/surprise(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/surprise(N).png") )    
    
    image sv surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/surprise(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/surprise(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/surprise(F).png") )
    
    image sv surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/surprise(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/surprise(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/surprise(C).png") )
    
    image sv OMG pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/OMG(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/OMG(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/5_position(N).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/normal/OMG(N).png") ) 
    
    image sv OMG pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/OMG(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/OMG(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/5_position(F).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/far/OMG(F).png") )
    
    image sv OMG pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/OMG(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/OMG(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/5_position(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/5/close/OMG(C).png") )
    
    image pi1 normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(C).png",(0,0), "mods/tfyl/images/sprites/composite/sveta/pi/close/normal(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(C).png",(0,0), "mods/Dirtysummer/image/sprites/pi/close/normal(C).png") )
    
    image pi2 normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png") )
    
    image pi3 normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png") )
    
    image pi4 normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(C).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(C).png") )
    
    image pi1 normal normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png") )
    
    image pi2 normal normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png") )
    
    image pi3 normal normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(N).png") )
    
    image pi4 normal normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/normal/pi4(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/normal/normal(N).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/normal/pi4(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/normal/normal(N).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/normal/pi4(N).png",(0,0), "mods/tfyl/images/sprites/composite/pi/normal/normal(N).png") )
    
    image pi1 normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi1(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png") )
    
    image pi2 normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi2(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png") )
    
    image pi3 normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi3(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png") )
    
    image pi4 normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/pi/close/pi4(F).png",(0,0), "mods/tfyl/images/sprites/composite/pi/close/normal(F).png") )
    
    image lu normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png") )
    
    image lu angry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png") )
    
    image lu smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png") )
    
    image lu normal tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png") )
    
    image lu angry tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png") )
    
    image lu smile tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png") )
    
    image lu normal swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_normal.png") )
    
    image lu angry swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_angry.png") )
    
    image lu smile swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_1_smile.png") )
    
    image lu cry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png") )
    
    image lu guilty pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png") )
    
    image lu scared pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png") )
    
    image lu shy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png") )
    
    image lu surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png") )
    
    image lu cry tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png") )
    
    image lu guilty tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png") )
    
    image lu scared tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png") )
    
    image lu shy tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png") )
    
    image lu surprise tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png") )
    
    image lu cry swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_cry.png") )
    
    image lu guilty swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_guilty.png") )
    
    image lu scared swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_scared.png") )
    
    image lu shy swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_shy.png") )
    
    image lu surprise swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_2_surprise.png") )
    
    image lu laugh pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png") )
    
    image lu sad pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png") )
    
    image lu shocked pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png") )
        
    image lu laugh tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png") )
    
    image lu sad tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png") )
    
    image lu shocked tshirt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png") )
        
    image lu laugh swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_laugh.png") )
    
    image lu sad swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_sad.png") )
    
    image lu shocked swim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/normal/lu_3_shocked.png") )
    
      
    image lu normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png") )
    
    image lu angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png") )
    
    image lu smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png") )
    
    image lu normal tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png") )
    
    image lu angry tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png") )
    
    image lu smile tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png") )
    
    image lu normal swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_normal.png") )
    
    image lu angry swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_angry.png") )
    
    image lu smile swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_1_smile.png") )
    
    image lu cry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png") )
    
    image lu guilty pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png") )
    
    image lu scared pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png") )
    
    image lu shy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png") )
    
    image lu surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png") )
    
    image lu cry tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png") )
    
    image lu guilty tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png") )
    
    image lu scared tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png") )
    
    image lu shy tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png") )
    
    image lu surprise tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png") )
    
    image lu cry swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_cry.png") )
    
    image lu guilty swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_guilty.png") )
    
    image lu scared swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_scared.png") )
    
    image lu shy swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_shy.png") )
    
    image lu surprise swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_2_surprise.png") )
    
    image lu laugh pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png") )
    
    image lu sad pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png") )
    
    image lu shocked pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png") )
        
    image lu laugh tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png") )
    
    image lu sad tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png") )
    
    image lu shocked tshirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png") )
        
    image lu laugh swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_laugh.png") )
    
    image lu sad swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_sad.png") )
    
    image lu shocked swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/far/lu_3_shocked.png") )
    
    
    image lu normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png") )
    
    image lu angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png") )
    
    image lu smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png") )
    
    image lu normal tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png") )
    
    image lu angry tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png") )
    
    image lu smile tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png") )
    
    image lu normal swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_normal.png") )
    
    image lu angry swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_angry.png") )
    
    image lu smile swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_1_smile.png") )
    
    image lu cry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png") )
    
    image lu guilty pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png") )
    
    image lu scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png") )
    
    image lu shy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png") )
    
    image lu surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png") )
    
    image lu cry tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png") )
    
    image lu guilty tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png") )
    
    image lu scared tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png") )
    
    image lu shy tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png") )
    
    image lu surprise tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png") )
    
    image lu cry swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_cry.png") )
    
    image lu guilty swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_guilty.png") )
    
    image lu scared swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_scared.png") )
    
    image lu shy swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_shy.png") )
    
    image lu surprise swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_2_surprise.png") )
    
    image lu laugh pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png") )
    
    image lu sad pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png") )
    
    image lu shocked pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_pioneer.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png") )
        
    image lu laugh tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png") )
    
    image lu sad tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png") )
    
    image lu shocked tshirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_tshirt.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png") )
        
    image lu laugh swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_laugh.png") )
    
    image lu sad swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_sad.png") )
    
    image lu shocked swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png",(0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_swim.png", (0,0), "mods/tfyl/images/sprites/composite/luna/close/lu_3_shocked.png") )
    
    
    image mix normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_normal.png") )
    
    image mix smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_smile.png") )
    
    image mix surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/normal/mix_1_surprise.png") )
    
        
    image mix normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_normal.png") )
    
    image mix smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_smile.png") )
    
    image mix surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/far/mix_1_surprise.png") )
    
    
    image mix normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_normal.png") )
    
    image mix smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_smile.png") )
    
    image mix surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/Michael/close/mix_1_surprise.png") )
    
    
    image co normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_normal.png") )
    
    image co grin pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_grin.png") )
    
    
    image co normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/normal/ax_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_normal.png") )
    
    image co grin pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/far/ax_1_grin.png") )
    
        
    image co normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_normal.png") )
    
    image co grin close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/coach/close/ax_1_grin.png") )
    
    
    image gf smile normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_smile.png") )
    
    image gf angry normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/grand/normal/de_1_angry.png") )
    
        
    image gf smile close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/ax_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/ax_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_smile.png") )
    
    image gf angry close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_body.png",(0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_body.png", (0,0), "mods/tfyl/images/sprites/composite/grand/close/de_1_angry.png") )
    
    
    
