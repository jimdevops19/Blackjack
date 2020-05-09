from tkinter import LEFT,Y

#Argumetns for Deisng:
table_font = 'Courier New'

background_color = '#006600'

font_small  = (table_font,24)
font_medium = (table_font,36)
font_large  = (table_font,60)

#Buttons:
button_args = {
    'fg': '#FFFFFF',
    'font' : font_small
}


#Arguments for packing
pack_left_and_fill_y = {
    'side' : LEFT,
    'fill' : Y
}

#Frame properties
hightlight_frame_with_white = {
    'highlightthickness' : 1,
    'highlightcolor' : '#FFFFFF',
    'highlightbackground' : '#FFFFFF'
}
