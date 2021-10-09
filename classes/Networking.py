import socket
import threading

def connect():
    #need to input the username var
    connect_to_server("PlayerName")

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR, your_name
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name) # Send name to server after connecting

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        print("Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    global your_name, opponent_name, game_round
    global your_choice, opponent_choice, your_score, opponent_score

    while True:
        from_server = sck.recv(4096)

        if not from_server: break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                print("Server says: Welcome " + your_name + "! Waiting for player 2")
            elif from_server == "welcome2":
                print("Server says: Welcome " + your_name + "! Game will start soon")


        elif from_server.startswith("opponent_name$"):
            opponent_name = from_server.replace("opponent_name$", "")
            print("Opponent: " + opponent_name)

            # we know two users are connected so game is ready to start
            threading._start_new_thread(count_down, (game_timer, ""))


        elif from_server.startswith("$opponent_choice"):
            # get the opponent choice from the server
            opponent_choice = from_server.replace("$opponent_choice", "")

            '''BELIEVE THAT i NEEDS TO CUSTOMISE THIS'''
            # figure out who wins in this round
            who_wins = game_logic(your_choice, opponent_choice)
            round_result = " "
            if who_wins == "you":
                your_score = your_score + 1
                round_result = "WIN"
            elif who_wins == "opponent":
                opponent_score = opponent_score + 1
                round_result = "LOSS"
            else:
                round_result = "DRAW"

            print("Opponent choice: " + opponent_choice)
            print("Result: " + round_result)

            # is this the last round e.g. Round 5?
            if game_round == TOTAL_NO_OF_ROUNDS:
                # compute final result
                final_result = ""
                color = ""

                if your_score > opponent_score:
                    final_result = "(You Won!!!)"
                    color = "green"
                elif your_score < opponent_score:
                    final_result = "(You Lost!!!)"
                    color = "red"
                else:
                    final_result = "(Draw!!!)"
                    color = "black"

                print("FINAL RESULT: " + str(your_score) + " - " + str(opponent_score) + " " + final_result)

                game_round = 0

            # Start the timer
            threading._start_new_thread(count_down, (game_timer, ""))
    sck.close()


def count_down(my_timer, nothing):
    global game_round
    if game_round <= TOTAL_NO_OF_ROUNDS:
        game_round = game_round + 1

    print("Game round " + str(game_round) + " starts in")

    while my_timer > 0:
        my_timer = my_timer - 1
        print("game timer is: " + str(my_timer))
        lbl_timer["text"] = my_timer
        sleep(1)

    print("Round - " + str(game_round))
