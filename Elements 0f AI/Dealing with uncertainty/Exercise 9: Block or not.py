def bot8(pbot, p8_bot, p8_human):
    pbot_8 = p8_bot * pbot / (p8_bot * pbot + p8_human * (1 - pbot))

    print(pbot_8)

# you can change these values to test your program with different values
pbot = 0.12
p8_bot = 0.617
p8_human = 0.02

bot8(pbot, p8_bot, p8_human)
