from PIL import Image, ImageDraw, ImageFont, ImageColor
import os
working_directory = os.getcwd()
#os.chdir("/home/stephen/Pictures/flameshot_pics/")
print(f"Current working directory is {working_directory}, ")
print("please ensure all images and fonts are in this directory")

char_side = False
while not char_side:
    evil_or_good = input("Is your character evil or good? Please enter either evil or good: ")
    evil_or_good = evil_or_good.lower().strip()
    if evil_or_good in ["evil", "good"]:
        char_side = True
        break
    else:
        print("\nPlease enter either evil or good \n")

if evil_or_good == "good":
    font_colour = "#397DAC"
elif evil_or_good == "evil":
    font_colour = "#A02509"

def drawing_dicts(x, y, draw_image, dict_name):
    for key, values in dict_name.items():
        draw_image.text((x, y), text=key,
                        font=ImageFont.truetype('VeraSe.ttf',
                                                size=12), fill="#A02509")
        values_y = y+17
        if isinstance(values, list):
            for item in values:
                draw_image.text((x-4, values_y), text=u"\u2022",
                                font=ImageFont.truetype('VeraSe.ttf',
                                size=10), fill=font_colour)
                draw_image.text((x+4, values_y), text=item,
                                font=ImageFont.truetype('VeraSe.ttf',
                                size=11), fill="#2C2929")
                values_y = values_y + 12
        return values_y


def numbers_only_input(stat_level):
    while True:
        try:
            character_stat = int(input(f"Enter you characters {stat_level} value: "))
        except ValueError:
            print("Sorry, Please enter numbers only (1,2,3 etc..)")
            # better try again... Return to the start of the loop
            continue
        else:
            break
    return str(character_stat)

def dicts_from_user_input(dict_name):
    while True:
        try:
            number_of_inputs = int(input(f"Enter number of unique {dict_name}: "))
        except ValueError:
            print("Sorry, Please enter numbers only (1,2,3 etc..)")
            # better try again... Return to the start of the loop
            continue
        else:
            break
    list_of_inputs = []
    for i in range(0, number_of_inputs):
        inputs = input(f"Enter the names of the characters {dict_name}: ")
        list_of_inputs.append(inputs)  # adding the element
    dict_output = {f"{dict_name}": list_of_inputs}
    return dict_output


# base card image
#images_folder = input("Enter the full path to the folder where the images are saved: ")


one_ring_image = Image.open("One_Ring_Blender_Render.png").resize((520, 300))
one_ring_image_rgba = one_ring_image.convert("RGBA")
new_rect = Image.new("RGBA", (520, 300), color=(238, 235, 208, 160))
final = Image.alpha_composite(one_ring_image_rgba, new_rect)
new_rect = Image.new("RGBA", (520, 300), color=(238, 235, 208, 175))
bottom_rectangle = Image.open("sand_bottom.png").resize((520, 30))
bottom_rectangle_rgba = bottom_rectangle.convert("RGBA")
final.paste(bottom_rectangle, (0, 270))
final2 = Image.alpha_composite(final, new_rect)


draw = ImageDraw.Draw(final2)
name = input("Enter name of the character: ")
name = name.upper()


#(left, top, right, bottom) bounding box
hero_name_bbox = draw.textbbox((95, 5), name)

hero_status_location = ((hero_name_bbox[0] + (draw.textlength(name)/2)), 25)

draw.text((hero_status_location[0], hero_status_location[1]-20), text=name,
          font=ImageFont.truetype('VeraSeBd.ttf', 18),
          fill=font_colour,
          anchor="mt")

hero_status = input("Enter hero status (HERO OF LEGEND etc.): ")
hero_status = hero_status.upper()
hero_description = input("Enter description of character e.g. for Saruman = WIZARD,ISENGARD,INFANTRY,HERO: ")
hero_description = hero_description.upper()

draw.text(hero_status_location, text=hero_status, font=ImageFont.truetype('VeraSe.ttf', 10),
          fill=font_colour,
          anchor="mt")
draw.text((hero_status_location[0], (hero_status_location[1]+12)), text=hero_description, font=ImageFont.truetype('VeraSe.ttf', 10),
          fill=font_colour,
          anchor="mt")

draw.rounded_rectangle(((15, 60), (270, 75)),
                             radius=8,
                             fill=(192, 167, 136, 130),
                             width=4)

stats_dict = {"Mv": (numbers_only_input("Movement") + '"'),
              "F": (numbers_only_input("Fight") + '/' + (numbers_only_input("Shooting")) + '+'),
              "S": (numbers_only_input("Strength")),
              "D": (numbers_only_input("Defence")),
              "A": (numbers_only_input("Attacks")),
              "W": (numbers_only_input("Wounds")),
              "C": (numbers_only_input("Courage"))}
the_x = 20
for key, value in stats_dict.items():
    the_name_y = 60
    the_stats_y = 75
    the_font = ImageFont.truetype('VeraSe.ttf', size=12)
    draw.text((the_x, the_name_y), text=key, font=the_font, fill="#2C2929", align="center")
    draw.text((the_x, the_stats_y), text=value, font=the_font, fill="#2C2929", align="center")
    the_x = the_x + 40

spec_stats = {"MIGHT": input("Enter Might value: "),
              "WILL": input("Enter Will value: "),
              "FATE": input("Enter Fate value: "),
              "WOUNDS": stats_dict["W"]}
the_spec_stat_name_x = 60
for key, value in spec_stats.items():
    the_spec_stat_value_y = 280
    the_spec_stat_name_y = 295
    draw.text((the_spec_stat_name_x, the_spec_stat_name_y),
                    text=key,
                    font=ImageFont.truetype('VeraSeBd.ttf', 10),
                    fill="#F1F1E2", stroke_width=2, stroke_fill="#888886",
                    anchor="ms")
    if int(value) > 7:
        first_row = int(value)//2
        second_row = int(value) - first_row
        draw.text((the_spec_stat_name_x, the_spec_stat_name_y-15),
                        text=(u"\u2022" * first_row),
                        font=ImageFont.truetype('VeraSeBd.ttf',
                        12), fill="#F1F1E2", stroke_width=2, stroke_fill="#888886",
                        anchor="ms")
        draw.text((the_spec_stat_name_x, the_spec_stat_name_y-7),
                        text=(u"\u2022" * second_row),
                        font=ImageFont.truetype('VeraSeBd.ttf',
                        12), fill="#F1F1E2", stroke_width=2, stroke_fill="#888886",
                        anchor="ms")
    else:
        draw.text((the_spec_stat_name_x, the_spec_stat_value_y),
                        text=(u"\u2022" * int(value)),
                        font=ImageFont.truetype('VeraSeBd.ttf', 20),
                        fill="#F1F1E2", stroke_width=2, stroke_fill="#888886",
                        anchor="ms")
    the_spec_stat_name_x = the_spec_stat_name_x + 130

#draw_categories = ImageDraw.Draw(final2)

heroic_actions = dicts_from_user_input("HEROIC ACTIONS")
heroics_y = drawing_dicts(4, 94, draw, heroic_actions)

wargear = dicts_from_user_input("WARGEAR")
wargears_y = drawing_dicts(190, 94, draw, wargear)

special_rules = dicts_from_user_input("SPECIAL RULES")
drawing_dicts(4, heroics_y+5, draw, special_rules)

char_options = dicts_from_user_input("OPTIONS")
drawing_dicts(190, wargears_y+5, draw, char_options)


while True:
    try:
        number_of_powers = int(input(f"Enter number of powers you character has \n if your character has no powers please enter 0: "))
    except ValueError:
        print("Sorry, Please enter numbers only (1,2,3 etc..)")
        # better try again... Return to the start of the loop
        continue
    else:
        break

# creating an empty list
powers_dict = {"POWER": [], "RANGE": [], "CAST": []}
# iterating till the range

if number_of_powers < 1:
    pass
else:
    for i in range(0, number_of_powers):
        powers_dict["POWER"].append(input("Enter the Powers Name: "))
        powers_dict["RANGE"].append(input("Enter the Powers Range: "))
        powers_dict["CAST"].append(input("Enter the Powers Cast Requirement: "))


power_name_x = 300
power_name_y = 150
if number_of_powers < 1:
    pass
else:
    for key in powers_dict.keys():
        draw.text((power_name_x, power_name_y), text=key,
                         font=ImageFont.truetype('VeraSe.ttf', size=13),
                         fill=font_colour,
                         align="left")
        power_name_x = power_name_x + 75

    power_stat_x = 300
    power_stat_y = 165
    for value in powers_dict["POWER"]:
        draw.text((power_stat_x, power_stat_y), text=value,
                         font=ImageFont.truetype('VeraSe.ttf', size=11),
                         fill="#2C2929",
                         align="left")
        power_stat_y = power_stat_y + 13

    power_stat_x = 385
    power_stat_y = 165
    for value in powers_dict["RANGE"]:
        draw.text((power_stat_x, power_stat_y), text=value,
                         font=ImageFont.truetype('VeraSe.ttf', size=11),
                         fill="#2C2929",
                         align="left")
        power_stat_y = power_stat_y + 13

    power_stat_x = 465
    power_stat_y = 165
    for value in powers_dict["CAST"]:
        draw.text((power_stat_x, power_stat_y), text=value,
                         font=ImageFont.truetype('VeraSe.ttf', size=11),
                         fill="#2C2929",
                         align="left")
        power_stat_y = power_stat_y + 13

images_folder = ("/home/stephen/Pictures/flameshot_pics/")

character_image_file = input("Enter the name of the character image file without the extension (image must be .png)")
character_image = Image.open(f"{character_image_file}.png").resize((120, 120))
final2.paste(character_image, (330, 25))
#.replace(" ", "")

faction_available = False

while not faction_available:
    faction = input("""
Which faction does your character belong to? \nEnter the number beside the faction name e.g enter 1 for gondor
                1: gondor       2: rohan,
                3: dol armoth   4: moria evil 
                5: isengard     6: mordor
                7: easterlings  8: harad 
                9: angmar       10: not available :""")
    faction_dict = {"1": "gondor", "2": "rohan", "3":"dolarmoth", "4": "moriaevil", "5": "isengard",
                    "6": "mordor", "7": "easterlings", "8": "harad", "9":"angmar", "10": "notavailable"}

    if faction in faction_dict.keys():
        faction_available = True
        faction_image=Image.open(f"{images_folder}{faction_dict[faction]}.png").resize((20,20))
        break
    else:
        print("\nPlease enter the number which corresponds to your faction \n")



#faction_image = Image.open(images_folder + input("Name of faction image file: ")).resize((20, 20))
final2.paste(faction_image, (430, 25))
final2.show()
