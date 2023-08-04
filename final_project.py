import pandas as pd
nfl_salaries = pd.read_csv("NFL_Salary_Cap_2018_2020-Table 1.csv")

player_names = []
player_franchises = []
base_salaries = []
positions = []

for index, row in nfl_salaries.iterrows():
    player_names.append(row['Player'])
    player_franchises.append(row['Franchise'])
    base_salaries.append(row['Base Salary'])
    positions.append(row['Pos.'])

def find_player_team(player_name):
    for index, each_row in nfl_salaries.iterrows():
        if player_name in each_row["Player"]:
            return each_row["Franchise"]

# User chooses a player
# Make the user guess the player's team

player_name_input = input("Enter the player's name: ").title()
team = find_player_team(player_name_input)

if player_name_input in player_names:
    print(f"{player_name_input} plays for {team}.")
else:
    print(f"{player_name_input} is not found in the dataset.")
    exit()

# Make the user guess the player's position

def find_position (player_name):
    for index, each_row in nfl_salaries.iterrows():
        if player_name in each_row["Player"]:
            return each_row["Pos."]


while True:
    pos_guess = input(f"""
Guess the position of {player_name_input} from the following:
C - center; DB - defensive back; DE - defensive end
DL - defensive lineman; DT - defensive tackle; E - end
FB - fullback; FL - flanker; G - guard
HB - halfback; K - kicker; LB - linebacker
MLB - middle linebacker; NG - nose guard; NT - nose tackle
OG - offensive guard; OL - offensive lineman; OLB - outside linebacker
OT - offensive tackle; P - punter; QB - quarterback
RB - running back; S - safety; SE - split end
T - tackle; TB - tailback; TE - tight end
WB - wingback; WR - wide receiver """).upper()
    position = find_position(player_name_input)

    if pos_guess == position:
        print(f"You're correct! {player_name_input}'s position is {position}. ")
        break
    else:
        print(f"You're wrong! {player_name_input}'s position is not {pos_guess}. Try again. ")

# Make the user guess the player's salary

def find_base_salary (player_name):
    for index, each_row in nfl_salaries.iterrows():
        if player_name in each_row["Player"]:
            return each_row["Base Salary"]

def is_valid_number(num_str):
    return num_str.isdigit()

def is_number_in_range(salary, lower_bound, upper_bound, player_name_input):
    if int(lower_bound) <= salary <= int(upper_bound):
        print(f"You're correct! {player_name_input}'s base salary is {base_salary}.")
        return True
    else:
        print(f"You're wrong! {player_name_input}'s base salary is not in {bs_guess}. Try again.")
        return False



while True:
    base_salary = find_base_salary(player_name_input)
    base_salary_converted = int(base_salary.replace('$', '').replace(",",""))
    #updated_list_bs = []
   # if is_valid_number(base_salary):
    #    updated_list_bs.append(base_salary)

    #updated_bs = ([int(num.replace('$', '').replace(",","")) for num in updated_list_bs])

    #A = range(1000, 7851001)
   # B = range(7851001, 15703001)
   # C = range(15703001, 23554001)
   # D = range(23554001, 31409001)

    if base_salary is None: 
        print(f"Sorry, the base salary of {player_name_input} is not in our dataset.")
        break
    else:
        bs_guess = input(f'''
Guess how much {player_name_input} makes.
A: $1,000 - $7,851,000
B: $7,851,001 - $15,703,000
C: $15,703,001 - $23,554,000
D: $23,554,001 - $31,409,000 
Please only input A, B, C, or D: ''').upper()

        if bs_guess == "A":
            if is_number_in_range(base_salary_converted, 1000, 7851001, player_name_input):
                break
        elif bs_guess == "B":
            if is_number_in_range(base_salary_converted, 7851001, 15703001, player_name_input):
                break
        elif bs_guess == "C":
            if is_number_in_range(base_salary_converted, 15703001, 23554001, player_name_input):
                break
        elif bs_guess == "D":
            if is_number_in_range(base_salary_converted, 23554001, 31409001, player_name_input):
                break
        else:
            print("Invalid input. Please try again.")
    
