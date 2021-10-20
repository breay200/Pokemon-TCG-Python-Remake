import tkinter as tk

master = tk.Tk()
master['background'] ='#4682B4'

width_size= master.winfo_screenwidth() * 0.75
height_size = master.winfo_screenheight() * 0.75

game_area = tk.Frame(master, width=width_size, height=height_size)

player_area = tk.Frame(game_area)
opponent_area = tk.Frame(game_area)

player_bench = tk.Frame(player_area)
opponent_bench = tk.Frame(opponent_area)

player_deck = tk.Frame(player_area)
opponent_deck = tk.Frame(opponent_area)

player_prize = tk.Frame(player_area)
opponent_prize = tk.Frame(opponent_area)

player_active = tk.Frame(player_area)
opponent_active = tk.Frame(opponent_area)

player_bench_1 = tk.Button(player_bench)
player_bench_2 = tk.Button(player_bench)
player_bench_3 = tk.Button(player_bench)
player_bench_4 = tk.Button(player_bench)
player_bench_5 = tk.Button(player_bench)

opponent_bench_1 = tk.Button(opponent_bench)
opponent_bench_2 = tk.Button(opponent_bench)
opponent_bench_3 = tk.Button(opponent_bench)
opponent_bench_4 = tk.Button(opponent_bench)
opponent_bench_5 = tk.Button(opponent_bench)

player_area.pack()
opponent_area.pack()
player_bench.pack()
opponent_bench.pack()
player_deck.pack()
opponent_deck.pack()
player_prize.pack()
opponent_prize.pack()
player_active.pack()
opponent_active.pack()
player_bench_1.pack()
player_bench_2.pack()
player_bench_3.pack()
player_bench_4.pack()
player_bench_5.pack()
opponent_bench_1.pack()
opponent_bench_2.pack()
opponent_bench_3.pack()
opponent_bench_4.pack()
opponent_bench_5.pack()
game_area.pack()


width = master.winfo_screenwidth() * 0.75
height = master.winfo_screenheight() * 0.75
master.geometry("%dx%d" % (width, height))
master.title("TCG REMAKE")

master.mainloop()