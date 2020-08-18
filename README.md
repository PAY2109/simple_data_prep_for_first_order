# simple_data_prep_for_first_order
This allows you to automatically prepare image and video for toying around with First Order Motion Model
https://colab.research.google.com/github/AliaksandrSiarohin/first-order-model/blob/master/demo.ipynb#scrollTo=SB12II11kF4c
# Dependencies
moviepy

# prepare_video.py
Crops, resizes and slices your video ("input.mp4") into 29 sec clips. Also saves corresponding audio clips so you could (manually) combine them after using Model.
# prepare_image.py
Finds face, crops and resizes ("input.png").
Code was mostly taken from here: https://gist.github.com/tilfin/98bbba47fdc4ac10c4069cce5fabd834 