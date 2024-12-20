import time
import telebot

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
  ▄▄▄▄▄        ▄▄▄▄      ▄▄▄▄▄▄▄▄ ███████ ████████   ▄█▄  ▄█▄   
  ███  ██      ████    ▀██▄▄▄█████████████ ██▄▄█████   ██   ███  
  ██    ██    ▄██▄  ▄███████████████▀████████████████████  █████ 
 ██     ██   ▄██▀ ██   ▀███▀ ███████████  ██████████  ▄████████
 ████████   ▄██▀  ██▄▄█▀    ██▀   ██████  ▄██████████▄ ███████
██        ██    ██ ███████▄   ██████ █████ ██████████ ▄██▀   
 ███▄   ███▄    ██ ██ ███▄ ▄█▀    ▀████  ███▄▄██████████      
      ▀▀███▀   ▀▀▀  ██████████▄▄▄▄██▀  ▀███████████████▄ █     
"""

# Funzione per cercare il tag nel canale Telegram
def check_tag_in_channel(bot, chat_id, tag):
    try:
        # Recupera i messaggi dal canale
        for message in bot.get_chat_administrators(chat_id):
            if tag in message.text:
                return True  # Se il tag è presente in uno dei messaggi
        return False  # Se il tag non è trovato
    except Exception as e:
        print(f"Errore durante la ricerca del tag nel canale: {e}")
        return False

# Funzione per gestire la scelta dell'utente
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

        # Chiedi all'utente di inserire un tag di Telegram
        tag = input("Inserisci un tag di Telegram (ad esempio @hotchatita): ")

        # Collega il bot e verifica il tag
        bot_token = "7030942765:AAFZjTcFtRFzKWcUkNXkL9r7ePhIS5Xu8WY"  # Sostituisci con il token del tuo bot
        chat_id = "-1002297768070"  # Sostituisci con il tuo ID del canale

        # Crea un oggetto bot
        bot = telebot.TeleBot(bot_token)

        # Verifica se il tag è presente nei messaggi
        tag_present = check_tag_in_channel(bot, chat_id, tag)

        if tag_present:
            print(f"Il tag {tag} è stato trovato nel canale!")
        else:
            print(f"Il tag {tag} NON è stato trovato nel canale.")

    elif scelta == "2":
        # Se l'utente sceglie "2", stampa un altro messaggio
        print("Hai scelto 'Test'.")
    else:
        # Se l'input non è valido
        print("Scelta non valida, prova di nuovo.")

if __name__ == "__main__":
    main()
