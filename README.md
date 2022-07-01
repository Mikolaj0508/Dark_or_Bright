# Dark_or_Bright

Original name of this task is "Are you afraid of the dark". It is Scala language programming task. Mostly it is used for recruitment process. In this case it is written in Python. 

Main goal of this programe is to classify image to be dark or bright. Programe should read all images from specified path, processed it and then give it back to specified folder. Processed images should have changed name. For example, if originally image's name was perfectly_white.png, after processing it should be perfectly_white_bright_100.png. Number in image's name depends on score, if image is perfectly white a 100 is given, else when it is perfectly dark a 0 is given. So programe has to evaluate this score. The "bright" or "dark" in name is given depending on treshhold which is specified in config.ini as well as input and output path.

Input folder is "flat" so it does not have any subfolders. It contents only .png and .img.
