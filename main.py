import time

# La scritta ASCII che incollerai
ascii_art = """                                                    
  ▄▄█▀▀▀█▄█ ▄▄█▀▀██▄ ▀███▀▀▀██▄ ▀███▀▀▀███▀████▀███▄   ▀███▀
▄██▀     ▀███▀    ▀██▄ ██    ▀██▄ ██    ▀█  ██   ███▄    █  
██▀       ▀█▀      ▀██ ██     ▀██ ██   █    ██   █ ███   █  
██        ██        ██ ██      ██ ██████    ██   █  ▀██▄ █  
██▄       ██▄      ▄██ ██     ▄██ ██   █  ▄ ██   █   ▀██▄█  
▀██▄     ▄▀██▄    ▄██▀ ██    ▄██▀ ██     ▄█ ██   █     ███  
  ▀▀█████▀  ▀▀████▀▀ ▄████████▀ ▄██████████████▄███▄    ██                                             
"""

# La scritta ASCII del canale Telegram
ascii_channel = """     
  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW+++++++******@WWWWWWWWWWWW@:::.:..:..@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.,,,,.,,,,,,,:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW++***+*******@WWWWWWWWWWWW@::::...:..@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.,,,,.,,,,,.,.WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW++*++*****#**@WWWWWWWWWWWWW:::::..:..WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW,,.,,.,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW++*+++****#**@WWWWWWWWWWWWW:::::..:..WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW,,.,,.,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW++*++*****##*@WWWWWWWWWWWW@:::.:..:..@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW...,,:,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW++*+++****#**@WWWWWWWWWWWW@:::::..:..@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.,,,,:,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW@W@W@+****##*@WWWWWWWWWWWWWW@@@@..:..,.,WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@@@,,,,,.,:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW@@WW@+****#**@WWWWWWWWWWWWWWWWW#..:...,.WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@#@*W,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW@W@@+****#**@WWWWWWWWWWWWW@@W@#..:...,,WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@###@ ,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW@WW@*****#**@WWWWWWWWWWWWWWWWW@:.:...,.WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@#@#W ,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@WW*****#**@WWWWWWWWWWWWWW@@@W..:..,..WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWW#@WWW# ,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@WW*############@###*#WWWWWWWW::+::...WWWWWWWW+++++++++*******WWWWWWWW##@#@@####@###*#WWWWWWWW++++++:+::*,,.....:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****##******#+++++WWWWW@W@..:..,,,WWWWWWWW,.......::+::::+WWWWWWWW**#*******#+++++WWWWWWWW:.:...,.,,.,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#******+*+++++WWWWW@@W..:..,,,WWWWWWWW,.......::+::+++WWWWWWWW**#******+*+++++WWWWWWWW:.:...,.,,.,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#*******#+++++WWWWW@@W..:..,,,WWWWWWWW,.......::+::+++WWWWWWWW**#*******#+++++WWWWWWWW..:...,.,,.,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****###***+**+++++WWWWW@@W..:..,,.WWWWWWWW.,.....:::+:::::WWWWWWWW**#*#***+**+++++WWWWWWWW..:..,,.,,.,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW++***#******+*+++++WWWWW@@@..:...,.WWWWWWWW,,......::::::::WWWWWWWW**#******+*+++++WWWWWW@W:.:...,,,,.,,,,,.,.WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#*#@@@@@@+*++*:+*WW@@W..:...,.WWWWW,,,.,...#@W@@@:::+:++*WW***#*#*#@@@@@@+*++*:+*WW:::..:..#@@@W*,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#**@W@W@@+++++:++WW@@W..:..,,,WWWWW,,,.,...@@WWW#:::++++*WW*****#**@W@W@@+++++::+WW:::..:..**@#@*,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@+****#**@W@@W@+++++:++WW@@W:.:..,,,WWWWW,,,.,...@@WWW@::+++++*WW*****#**@W@@W@+++++:++WW:::..:..*#W@W*,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW*****#**@WWWW@++++++++WWWW@..:.....WWWWW,,,.,...@W@WW@:::::++*WW+****#**@WWWW@++++++:+WW:::..:..@@#@@@,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW@@*****#**@WWWW@+++++:++WW@@#:.:..,..WWWWW,,,.,...@@#@@@:::::++*WW+****#**@WWWW@+++++:++WW:::..:..@@#@#W,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****##*@WWWW@+++++:++WW@@@..:..,..WWWWW,,,.,...@W*@@@::::+++*WW*****#**@WWWW@+++++:++WW:::..:.:@@+**W ,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#**@WWWW@+++++:++WW@W@..:..,,,WW@@@,,,.,...WWWWW#::+::++*W@*****#**@WWWW@+++++:++WW:::..:..WWW#@@,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@+****##*@WWWW@+++++:++WW@@#..:..,,,WW@@W,,,.,...WWW@#@::+::++*W@+****##*@WWWW@+++++:++@@:::..:..WWW#*@,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@+****#**@WWWW@+++++:++WW@W#..:..,,,WW@@W,,,.,...WWW@#@::+::++*@@+****##*@WWWW@+++++:++@@.::..:..WWW#*W,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#**WWWWW@+++++:++WW@W@:.:..,,,WWW@W,,,.,...WWW@W@::+++++*W@*****#**WWWWW@+++++::+@@.::..:..WWW@#@,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW+****#*#WWWWW@+++++:++WW@WW..:..,,,WWW@#,,,.,...WWWWW@::+++++*WW*****#*#WWWWW@+++++::+W@:::..:..WWW@W#,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW*######*@WWWW@*****++*WW@WW::+::...WWWWW.....:::WWWWW@+++++***WW*######*@WWWW@*****+**WW+++::+::WWWWWW.....:::WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@*****#**@WWWW@++++++++WW@W@..:...,.WWW#W.,,.,...WWW@@@::+:+++*@@*****#**@WWWW@+++++++*@W:::..:..WWW@#@,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW*****#**@WWWW@+++++:++WW@@@:::..,..WWW#@,,,.,...WWW@@@::::+++*WW*****#**@WWWW@+++++::*@W:::..:..WWW@@@,,,,,..:WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW@+****##*@WWWW@+++++:+*WW@@W..:...,,WWW@+,,,.,...WWW@@#:::++++*W@*****#**@WWWW@+++++:++@@:::..:..WWW#W* ,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW@@*****#**@WW@W@+++++:++WW@@@..:...,,WWW#+.,,.,...WWW@@#::::+++*W@+****#**@WW@W@+++++:++@#:::..:..WWW#@*,,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW@@+****#**@WWWW@+++++::+WW@@W..:...,,WWW@#,,,.,...WWW@@@:::++++*W@*****#**@WWWW@+++++:++W@:::..:..WWW@W# ,,,,...WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@*++****#*****++*+++++@WWWW:::..:.....,,.@###W,,.....:::::::++@WWW@W@@**#*****++*+++++@W@W@@@@..:.:.,,,,.,,,,,.....WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@++*****#********+*+++WWWWW::..::...,.,,.@+*#W..:.....::+::::+WWWW@WW@**#********+*+++WWW@@@@W..:...,.,,.,,,,,..:..WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@+++****#*#******+++++WWWWW:::..:...,.,,.@*@#W,.......::+::+:+WWWW@WWW**#********+++++WWW@@@@W..:...,.,,.,,,,,.,...WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@+++****###*****#+++++WWWWW:::..:...,.,,.@W@@#........::+::+++WWWWW@W@**##******#+++++WWWWWWW@..:...,.,,.,,,,,.,...WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@+++****#*#******+++++WWWWW:::..:...,.,,.#WW@*........::+:::::WWWWW@W@**#********+++++WWW@WWW#..:...,.,,.,,,,,.,...WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@++**+*+******++#+++++WWWWW:.:.:.:.,.,,,.@@@@+.,......::::::::WWWW@WW@********++#+++++WWW@@W@#:::::,,,,,,,,,,,.,:..@WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWW@W@@@W@W@#@#WWWWWW@##@@WW@@@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@WWW@#@@@W@@#@@@W@@WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW@@W@WWW@W@WWWWWW@@@@WWWWWW@@@@##@@@WW@*WWWWWW@*##W@@W@#@@@W@WWWWWWWWWW@WW@W@WWWW@@@@WWWWWWWWWW@@@W@WW@###W@WW@###WWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW@@@W@WW@WWWWWWW@W@@@W@WWWWW@W@@###W#WW@*WWWWW@W*#*@@WW@*@#@@@@WWWWWWWWW@WWWWWWW@W@@@W@WWWWWWW@@##@@@@W@*@*@#@@@+#*WWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW@@WW@W@WWWWWWWWWWWWWWWWWWWWW@W#@@W@WWW#WWWWWW@#@#@@@W@#@@@WW@WWWWWWWWW@WWWWWWWWWWWWWWWWWWWWW@W#@@W@WW@*##W@WW@#@#WWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@W@@#@@@WWWWW@@@@W@@@@@W@@@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@W@@@@@@@W#@##@@@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWW@WWWW@WWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@@@WWWW@@@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@W@@WWWW@W@@W@@@@@@@@@@@WW@@@@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@@@@###########******+*++++++++*+******###########@@@@@@@@@@@@@@@@@@@##########******@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WW@WWWWWWW#WWWWWWWW@WWW@WWWWWWWWWW@WWWWWW+@WWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@@WWW#@WWWW**:WW#:W@.+@W.,W+#@@W.#WWW:WW@@WW:WWW##W@@*@@#@W@@WWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WWWW+WWWW*@.WW##WW:,WW**WWW:WW.#WW::WW@@@#:WWW@#WW**@W#WW#WWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WWW#WWWW@*@:@W+*@,#W,W+:W..*.@W#@.#:WW:@WW+WWW@@W*@*WW##@@@WWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWW@WWWWW@@WW@W#WWWWWWW@WWW@WW@WWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW##WWWWWWWWWW@@WWWW@WWWWWWWWWWWWWW@@WWWWW@@WW#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW*WWW@+@@@@WW:@W+*WWW WW::WWW.WW+*.@.+W@##WW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW#WWWW#@WWWWWW+@W**WWW,WW+:WWW,WW*+.#:+WW**W*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@@WWWWWWWWWWWW@WW@WWW@WWWWWWW#WWW@@W@W@W@WW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWW@WWWWWWWWW@WW@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@WW@WWWWWWW@@WWWWWWWWWWW@WWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@#WWW#WWWWWW:@:W#+W.:,@@WWW,,@:WWW@W..*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW*@WWW@@WWWW:.WW##WW@,@WWW@W,,WWWWWW+:#@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW##WWW#WWWWWW.*#W:#W**,.W@WWW,+*WWWW@+.@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWW@WWW@WWWWWWWWWWWW@WWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW*WWWWWWWW@::WWWWW@WWW@WWW@WWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@*WWW##WWWWW:**W@:@*#,:@WWWW,+*@WW@W,#@WW#@W*+@@##WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW#*@WW@+WWWWW:.WW#@WWW,@WWW@W.,W@WWWW.:W@*@W@@+WW##WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@*WWW@@WWW@W:@:W*@W.+,@WWWWW.@:WWWWW:@:@W#W+#++WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@W@WWW@W+W@*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWW@WW@WWWWWW@WWWWWW@WW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW#@WWW@WWWWW@:WWWW@W@W@WWWWWW@WWWWWW.W:#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW+#WWW@+WWWWW::W@#*WWW,:WWWWW,:W@WWW.W:#@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW#@WW@@WWWWW::WW*@W@@..@WWWW,.@W@WW.W:WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@@WW@WW@WWWW@WWWWWW@WW@WWWWWWWWWWWW@W@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWW@WWWWWW@@WWWWWWWWWWWWW@WWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWW@@WWWWWWWWW@WWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW+@WWW*WWWWW@.@:W##W.:.@WWW@..@.WWW@::W:@@@+:+W*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW##WWW@W@WWWW..W@##W@@,@WWWWW,.WWWWWW.:W@**@:@:+@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW*#WWW#@WWWWW:##W:@W** :WWWWW *#WWWWW.##WW@W:W@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW++WWWWWWWW@::WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW*WWW@@W@WWW.*@W#:W**.:WWWWW,+#WWWW##:W@@+@@:#@W*#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWW+WWWWW:.WW##WWW,@WWWWW,,WWWWWW@:@W#@@@:+WW*#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW*@WWWWWWWWWW:@.W*#W.:,@WWWWW,W.WWWW:::WW#@+W+W+WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW##WWWWWWWWW@:W@WWWWWWWWWWWWWWWW@WWWW@WWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW**WWWW+WWWW@:+W@#*WWW.+WWWWW,:WWWWW@.:@W@#@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@#WWW@@W@WWW:+WW*#@W@,.WWWWW,:WWWWW*..WW@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@WWWWWWWWWWW@W@WWW@WWWWWW@W@@W@WWWWW@@@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWW@WW@WWWWWWWWWWWWWWW@@WWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@#@WW#WWWWWW:W.W#*W.:,@WWW@,.W.WWW@.W:WW**WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW##WWW@@@WWW@:.@W@#WWW WWWWWW,,W@WW.:..*W##WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@*WW@*WWWWWW:##W:#W+*,:WWWW@,**@@W*.#:WW++WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWW.W@WWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@WWWWWWWWWW@W@@W@WW@@@@@WWWWWWWWW@WWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@W+@WWWWWWWW.:@WWWWWWWW@@WWWWW@WWWWW+:WWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@@@@*WW@+WWWW.@@..WW.*@@*.WW@.W@::WWWW#W+*W@@W@W@#@@#@@W@@***WWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWW+WWW@*WWW.@@*#W+,,WW+WWWW.@W**WWWW#@@#W##W@@##W*#@WW##***WWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWW@W+WWWWWWWWW+@W++@W:W.@*.WWW:WW*:WWW+.W@#@+@@*W*@W@@@WW@W+*#WWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWW@@WWWWWWWWWWWW@WWWW@WWWWWWWWW@WWWWWW@WWWWWWWW@W*#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@@@@@@@@@@@@@@@@@@@@@#@##@##@#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWW@WWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
   """

# Funzione principale
def main():
    print(ascii_art)  # Stampa la scritta ASCII iniziale

    # Pausa per un effetto di attesa
    time.sleep(1)

    # Stampa le opzioni
    print("1. Prova")
    print("2. Test")

    # Prendi l'input dell'utente
    scelta = input("Scegli un'opzione (1 o 2): ")

    if scelta == "1":
        # Se l'utente sceglie "1", stampa il messaggio del canale
        print(ascii_channel)
        print("Il mio canale Telegram @executedban")
    elif scelta == "2":
        # Se l'utente sceglie "2", stampa un altro messaggio
        print("Hai scelto 'Test'.")
    else:
        # Se l'input non è valido
        print("Scelta non valida, prova di nuovo.")

if __name__ == "__main__":
    main()
