"""This module created using AI"""
import sys, time



def main():
    return 0


# Frames
def skull_loading():
    
    skull_frames = [
        """
          LOADING...
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
          LOADING...
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

    # Animation settings
    loading_duration = 8
    frame_duration = 0.7
    steps = int(loading_duration / frame_duration)

    # Main cycle
    for i in range(steps):
        # Screen cleaning
        sys.stdout.write('\033[H\033[J')  # Очищает экран

        # Current frame
        print(skull_frames[i % len(skull_frames)])
        sys.stdout.flush()

        # Waiting for the next frame
        time.sleep(frame_duration)

def skull_congrats(message="WORK DONE!"):
    print(f"""
     CONGRADULATIONS!
         ______
      .-"      "-.
     /            \\
    |              |
    |,  .-.  .-.  ,|
    | )(_o/  \\o_)( |
    |/     /\\     \\|
    (_     ^^     _)
     \\__ \\____/ __/
      |          |
      \\          /
       `--------`
        
{message}
    """)


if __name__ == "__main__":
    main()
