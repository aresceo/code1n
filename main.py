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

# Funzione principale
def main():
    print(ascii_art)  # Stampa la scritta ASCII

    # Pausa per un effetto di attesa
    time.sleep(1)

    # Stampa i punti
    print("1. Prova")
    print("2. Test")

if __name__ == "__main__":
    main()
