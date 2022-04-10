# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
score_player_0 = "Ruud Gullit"
score_player_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = score_player_0 + " " + str(goal_0) + ", " + score_player_1 + " " + str(goal_1)
print(scorers) 

report = f"{score_player_0} scored in the {goal_0}nd minute" "\n" + f"{score_player_1} scored in the {goal_1}th minute"
print(report)


player = "Rinat Dasayev"
first_name = player[0:player.find(" ")]
first_name_len = len(first_name)

last_name_player = player[player.find(" "):]
last_name_len = len(last_name_player)-1

name_short = player[0] + "." + last_name_player
chant =  (first_name_len - 1) * (first_name + "! ") + (first_name + "!")
good_chant = chant != 5
#print(first_name)
#print(last_name_player)
#print(last_name_len)
#print(name_short)
print(chant)
print(good_chant)
