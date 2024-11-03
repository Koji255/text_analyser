import sys
import time



def main():
    return 0


# Кадры с черепом, где челюсть открывается и закрывается
def skull_loading():
    # Кадры с черепом
    skull_frames = [
        """
           ______
        .-"      "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__|IIIIII|__/
        | \\IIIIII/ |
        \\          /
         `--------`
        """,
        """
           ______
        .-"      "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__|IIIIII|__/
        | |      | |
        | |      | |
        | \\IIIIII/ |
         `--------`
        """,
    ]

    # Время на один кадр и продолжительность
    loading_duration = 11
    frame_duration = 0.7
    steps = int(loading_duration / frame_duration)

    # Основной цикл
    for i in range(steps):
        # Очистка экрана
        sys.stdout.write('\033[H\033[J')  # Очищает экран

        # Показ текущего кадра
        print(skull_frames[i % len(skull_frames)])
        sys.stdout.flush()

        # Ожидание перед следующим кадром
        time.sleep(frame_duration)

    print("""
      CONGRADULATIONS!
           ______
        .-"      "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__ \____/ __/
        |          |
        \\          /
         `--------`
          
      LOADING COMPLITED!
          """)



if __name__ == "__main__":
    main()
