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
 ▓█████▒██   ██▒ ▓█████  ▄████▄  █    ██ ▄▄▄█████▓ ▓█████▓█████▄  ▄▄▄▄    ▄▄▄      ███▄    █ 
 ▓█   ▀▒▒ █ █ ▒░ ▓█   ▀ ▒██▀ ▀█  ██  ▓██▒▓  ██▒ ▓▒ ▓█   ▀▒██▀ ██▌▓█████▄ ▒████▄    ██ ▀█   █ 
 ▒███  ░░  █   ░ ▒███   ▒▓█    ▄▓██  ▒██░▒ ▓██░ ▒░ ▒███  ░██   █▌▒██▒ ▄██▒██  ▀█▄ ▓██  ▀█ ██▒
 ▒▓█  ▄ ░ █ █ ▒  ▒▓█  ▄▒▒▓▓▄ ▄██▓▓█  ░██░░ ▓██▓ ░  ▒▓█  ▄░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██▓██▒  ▐▌██▒
▒░▒████▒██▒ ▒██▒▒░▒████░▒ ▓███▀ ▒▒█████▓   ▒██▒ ░ ▒░▒████░▒████▓ ░▓█  ▀█▓▒▓█   ▓██▒██░   ▓██░
░░░ ▒░ ▒▒ ░ ░▓ ░░░░ ▒░ ░░ ░▒ ▒  ░▒▓▒ ▒ ▒   ▒ ░░   ░░░ ▒░  ▒▒▓  ▒ ░▒▓███▀▒░▒▒   ▓▒█░ ▒░   ▒ ▒ 
░ ░ ░  ░░   ░▒ ░░ ░ ░     ░  ▒  ░░▒░ ░ ░     ░    ░ ░ ░   ░ ▒  ▒ ▒░▒   ░ ░ ░   ▒▒ ░ ░░   ░ ▒░
    ░   ░    ░      ░   ░        ░░░ ░ ░   ░          ░   ░ ░  ░  ░    ░   ░   ▒     ░   ░ ░ 
░   ░   ░    ░  ░   ░   ░ ░        ░              ░   ░     ░     ░            ░           ░    
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
