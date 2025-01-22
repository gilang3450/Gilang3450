import time
from threading import Thread
import sys

def animate_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nKu ingin kau jadi milikku", 0.5, 0.15),
        ("Temani diriku seumur hidupku", 4.5, 0.14),
        ("Dan ku berjanji tak akan sakiti", 9, 0.15),
        ("Kau yang kucinta sepenuh hati", 14.5, 0.13),
        ("\nBiarkan semua manusia", 18.3, 0.15),
        ("Jadi saksi nyata", 21.7, 0.12),
        ("Bahwa memilikimu adalah", 24, 0.13),
        ("Anug'rah terindah untuk diriku", 28.8, 0.2),
        
    ]

    threads = [Thread(target=sing_lyric, args=lyric) for lyric in lyrics]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

if __name__ == "__main__":
    sing_song()
