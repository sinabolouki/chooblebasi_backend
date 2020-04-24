genders = {"male", "female"}
skin_tones = {"warm", "cool", "neutral", "meh"}
m_body_shapes = {"triangle", "inverted triangle", "rectangle"}
f_body_shapes = {"apple", "pear", "rectangle", "hourglass"}
eye_colors = {"brown", "blue", "green", "dark brown", "honey"}
temp = int(input("are you AGHA DAQIQ?\n1. yes\n2. no\n"))
is_daqiq = False
if temp == 1:
    is_daqiq = True
if not is_daqiq:
    height = int(input("enter your height in cm\n"))
    # height = 180
    weight = int(input("enter your weight in kg\n"))
    # weight = 63
    temp = int(input("what is your gender?\n1. male\n2. female\n(choose 1 or 2)\n"))
    # temp = 1
    if temp == 1:
        gender = "male"
    else:
        gender = "female"
    temp = int(input("what is your skin tone?\n1. warm\n2. cool\n3. neutral\n4. none\n"))
    # temp = 1
    if temp == 1:
        skin_tone = "warm"
    elif temp == 2:
        skin_tone = "cool"
    elif temp == 3:
        skin_tone = "neutral"
    else:
        skin_tone = "meh"
    if gender == "male":
        temp = int(input("what is your body shape?\n1. triangle\n2. inverted triangle\n3. rectangle\n"))
        # temp = 2
        if temp == 1:
            body_shape = "triangle"
        elif temp == 2:
            body_shape = "inverted triangle"
        else:
            body_shape = "rectangle"
    else:
        temp = int(input("what is your body shape?\n1. apple\n2. pear\n3. rectangle\n4. hourglass\n"))
        # temp = 4
        if temp == 1:
            body_shape = "apple"
        elif temp == 2:
            body_shape = "pear"
        elif temp == 3:
            body_shape = "rectangle"
        else:
            body_shape = "hourglass"
    temp = int(input("what color are your eyes?\n1. brown\n2. blue\n3. green\n4. dark brown\n5. honey\n"))
    # temp = 1
    if temp == 1:
        eye_color = "brown"
    elif temp == 2:
        eye_color = "blue"
    elif temp == 3:
        eye_color = "green"
    elif temp == 4:
        eye_color = "dark brown"
    else:
        eye_color = "honey"

    print(gender, "\n", weight, "kg", "\n", height, "cm", "\n", "body shape: ", body_shape, "\n", "skin tone: ",
          skin_tone, "\n", "eye color: ", eye_color, "\n")

    bmi = weight / ((height / 100) ** 2)

    print("bmi: ", bmi)

    body_conditions = {"underweight", "fit", "overweight", "obese"}
    if bmi < 18.5:
        body_condition = "underweight"
    elif 18.5 <= bmi <= 24.9:
        body_condition = "fit"
    elif 24.9 < bmi <= 29.9:
        body_condition = "overweight"
    else:
        body_condition = "obese"
    print(body_condition)

    suggested_clothes = []
    avoid = []
    if gender == "female":
        if body_shape == "apple":
            suggested_clothes.append("V-neck empire waist dresses and tops")
            suggested_clothes.append("wrap dresses")
            suggested_clothes.append("A-line dresses")
            suggested_clothes.append("tops that cover the entire belly area and extend just below your hips")
            suggested_clothes.append("layered tops")
            suggested_clothes.append("ruched tops")
            suggested_clothes.append("tunics")
            suggested_clothes.append("Flared or boot cut pants with back pockets")
            suggested_clothes.append("belt below your bust")

            avoid.append("double breasted jackets")
            avoid.append("bulky tops")
            avoid.append("clingy silhouettes")
            avoid.append("skinny jeans")
            avoid.append("straight leg pants")
            avoid.append("belt around the waist")
        elif body_shape == "pear":
            suggested_clothes.append("scarves")
            suggested_clothes.append("pashminas")
            suggested_clothes.append("colorful necklaces")
            suggested_clothes.append("patterned and embellished tops and dresses")
            suggested_clothes.append("bateau neckline")
            suggested_clothes.append("cap")
            suggested_clothes.append("puff sleeves")
            suggested_clothes.append("tailored, flared pants")
            suggested_clothes.append("A-line skirts")
            suggested_clothes.append("dark, solid colors for your bottom half")
            suggested_clothes.append("lighter, brightly colored tops")

            avoid.append("tight pants")
            avoid.append("capri pants")
            avoid.append("short skirts")
            avoid.append("pencil skirts")
        elif body_shape == "rectangle":
            suggested_clothes.append("belt at the narrowest part of your waist")
            suggested_clothes.append("empire-waist and wrap dresses")
            suggested_clothes.append("tops that end at the mid-section of the hips")
            suggested_clothes.append("ruffled or pleated tops")
            suggested_clothes.append("accessories that add volume to your upper part")
            suggested_clothes.append("underwear that provides good breast support and makes your waist more defined")
            suggested_clothes.append("Peplum jackets, tops, dresses and skirts")
        elif body_shape == "hourglass":
            suggested_clothes.append("clothes that draw attention to your waist")
            suggested_clothes.append("undergarments that fit correctly")

            avoid.append("baggy clothing")
            avoid.append("padded cups")
            avoid.append("unstructured bras")
    else:
        if body_shape == "triangle":
            suggested_clothes.append("Tailored patterned blazers")
            suggested_clothes.append("fitted waistcoats")
            suggested_clothes.append("solid trousers")
            suggested_clothes.append("mix of prints and solid colors")
            suggested_clothes.append("Vertical stripes")
            suggested_clothes.append("Horizontal stripes (only if they are visible from the chest upward)")
            suggested_clothes.append("Jackets with structured shoulders")
            suggested_clothes.append("Single-breasted suits")
            suggested_clothes.append(" jackets tailored for a structured fit on the top,"
                                     " but with extra room around the waist")
            suggested_clothes.append("Brighter color panels")
            suggested_clothes.append("Patterns and detailing across the chest and shoulders")
            suggested_clothes.append("jumpers")
            suggested_clothes.append("crew neck tees")
            suggested_clothes.append("color panels across the chest but a slimming darker color like gray, "
                                     "navy or black around the mid-section")
            suggested_clothes.append("wide and straight leg fits")

            avoid.append("Fitted polo shirts and roll necks")
            avoid.append("Brighter colors and busy prints")
            avoid.append("Bold belts")
            avoid.append("Skinny fits and extreme tapers")
            avoid.append("Narrowing trousers")
        elif body_shape == "inverted triangle":
            suggested_clothes.append("Horizontal stripes (Especially from the chest down)")
            suggested_clothes.append("Slim-fit shirts")
            suggested_clothes.append("Slim cotton polo shirt")
            suggested_clothes.append("spandex")
            suggested_clothes.append("Regular V-neck T-shirts")
            suggested_clothes.append("Regular V-neck T-shirts")
            suggested_clothes.append("Straight-leg trousers and jeans")
            suggested_clothes.append("Slim fit pants")
            suggested_clothes.append("Trousers with larger seat drop")
            suggested_clothes.append("Slim-fit jackets that follow the natural line of your silhouette")

            avoid.append("collar shape")
            avoid.append("plunging V-neck t-shirts")
            avoid.append("skinny jeans")
            avoid.append("Structured tailoring")
            avoid.append("Suit jackets and blazers with shoulder padding")
            avoid.append("Prints, patterns and scoop necklines")
            avoid.append("Any kind of detailing, especially around the shoulders")
        elif body_shape == "rectangle":
            suggested_clothes.append("Horizontal stripes (Especially across your upper torso)")
            suggested_clothes.append("Structured tailoring")
            suggested_clothes.append("Layered looks")
            suggested_clothes.append("button-down shirt and fine-gauge crew neck jumper")
            suggested_clothes.append("Scarves")
            suggested_clothes.append("Prints, color pops, and detailing")

            avoid.append("Double-breasted jackets")

    suggested_colors = []
    if skin_tone == "warm":
        suggested_colors.append("honey")
        suggested_colors.append("olive")
        suggested_colors.append("coral")
        suggested_colors.append("cream")
    elif skin_tone == "cool":
        suggested_colors.append("blue")
        suggested_colors.append("lavender")
        suggested_colors.append("rose")
        suggested_colors.append("grey")
    elif skin_tone == "neutral":
        suggested_colors.append("med. blue")
        suggested_colors.append("jade")
        suggested_colors.append("red")
        suggested_colors.append("white")
    elif skin_tone == "meh":
        suggested_colors.append("pure white")
        suggested_colors.append("light blush pink")
        suggested_colors.append("teal")
        suggested_colors.append("eggplant purple")
    suggested_colors.append(eye_color)

    print("these are your recommendations:")
    for i in suggested_clothes:
        print(i)
    print("\navoid these:")
    for i in avoid:
        print(i)
    print("\nalso use these colors:")
    for i in suggested_colors:
        print(i)
else:
    print("these are your recommendations:\neverything")
    print("\navoid these:\nnothing")
    print("\nalso use these colors:\nall of them")
