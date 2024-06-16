def chapter_1():
    print("Chapter 1: The Mysterious Whisper")
    print("You wake up to the sound of whispering. The room is dark, but you can feel a cold breeze brushing against your face. Sitting up in bed, you strain your ears to catch the words. It sounds like a child, but you can't make out what they're saying.")
    print("As you rub your eyes and glance around, the whispering stops. You feel a shiver run down your spine. You’ve always heard stories about your house being haunted, but you never believed them. Until now.")
    print("\n1: Investigate the Whispering\n2: Ignore the Whispering")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_2()
    elif choice == '2':
        chapter_3()
    else:
        print("Invalid choice, please try again.")
        chapter_1()

def chapter_2():
    print("\nChapter 2: Investigate the Whispering")
    print("You get out of bed and follow the sound. The whispers lead you to the attic door. Your heart races as you climb the creaky stairs. The attic is filled with old furniture and dusty boxes. In the far corner, you see a faint, glowing light.")
    print("\n1: Approach the Light\n2: Call for Help")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_4()
    elif choice == '2':
        chapter_5()
    else:
        print("Invalid choice, please try again.")
        chapter_2()

def chapter_3():
    print("\nChapter 3: Ignore the Whispering")
    print("You pull the covers over your head and try to fall back asleep, but the whispering haunts your thoughts. The next morning, you wake up feeling exhausted and uneasy. You decide to do some research about the house's history.")
    print("\n1: Go to the Library\n2: Search Online")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_6()
    elif choice == '2':
        chapter_7()
    else:
        print("Invalid choice, please try again.")
        chapter_3()

def chapter_4():
    print("\nChapter 4: Approach the Light")
    print("As you move closer to the light, you see the figure of a small child. The child turns to you, their eyes filled with sadness.")
    print("\"Help me,\" the child whispers.")
    print("\n1: Ask How You Can Help\n2: Run Away")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_8()
    elif choice == '2':
        chapter_9()
    else:
        print("Invalid choice, please try again.")
        chapter_4()

def chapter_5():
    print("\nChapter 5: Call for Help")
    print("You rush downstairs and call your friend, Alex. Alex arrives quickly and you both head to the attic. The light is still there, but it seems to be fading.")
    print("\"We need to find out what's causing this,\" Alex says.")
    print("\n1: Investigate Together\n2: Leave and Call the Authorities")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_10()
    elif choice == '2':
        chapter_11()
    else:
        print("Invalid choice, please try again.")
        chapter_5()

def chapter_6():
    print("\nChapter 6: Go to the Library")
    print("At the library, you find old records about your house. You discover that a child named Emily died there under mysterious circumstances many years ago.")
    print("\n1: Search for More Information About Emily\n2: Go Home and Investigate")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_12()
    elif choice == '2':
        chapter_13()
    else:
        print("Invalid choice, please try again.")
        chapter_6()

def chapter_7():
    print("\nChapter 7: Search Online")
    print("You find articles about the history of your house and the ghost stories associated with it. One name keeps appearing: Emily, a child who died tragically.")
    print("\n1: Contact a Paranormal Expert\n2: Try to Communicate with the Ghost Yourself")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_14()
    elif choice == '2':
        chapter_8()
    else:
        print("Invalid choice, please try again.")
        chapter_7()

def chapter_8():
    print("\nChapter 8: Ask How You Can Help")
    print("Emily looks at you with hopeful eyes. \"Find my locket. It’s the key to setting me free.\"")
    print("\n1: Search the Attic for the Locket\n2: Ask Emily for More Clues")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_10()
    elif choice == '2':
        chapter_9()
    else:
        print("Invalid choice, please try again.")
        chapter_8()

def chapter_9():
    print("\nChapter 9: Run Away")
    print("You bolt down the stairs, your heart pounding. You know you can't handle this alone.")
    print("\n1: Tell Your Parents\n2: Call a Friend for Help")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_11()
    elif choice == '2':
        chapter_10()
    else:
        print("Invalid choice, please try again.")
        chapter_9()

def chapter_10():
    print("\nChapter 10: Investigate Together")
    print("You and Alex approach the light together. Emily appears and tells you both about her lost locket. Alex suggests checking the old family records for clues.")
    print("\n1: Search the House Records\n2: Look for Hidden Compartments in the Attic")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_13()
    elif choice == '2':
        chapter_12()
    else:
        print("Invalid choice, please try again.")
        chapter_10()

def chapter_11():
    print("\nChapter 11: Leave and Call the Authorities")
    print("You decide it's too dangerous and leave the house. The authorities arrive and conduct an investigation, but they find nothing unusual. The whispering stops, but you can’t shake the feeling that something was left unresolved.")
    print("\nThe End")

def chapter_12():
    print("\nChapter 12: Search for More Information About Emily")
    print("You find out that Emily’s locket went missing around the time of her death. It's said to hold a secret that could explain everything.")
    print("\n1: Search Your House for the Locket\n2: Visit the Cemetery Where Emily is Buried")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        chapter_13()
    elif choice == '2':
        chapter_14()
    else:
        print("Invalid choice, please try again.")
        chapter_12()

def chapter_13():
    print("\nChapter 13: Go Home and Investigate")
    print("Armed with the knowledge of Emily's tragic past, you return home. You sense that Emily’s spirit is trying to communicate something important. You find a dusty chest in the attic. Inside, there's a small, ornate locket.")
    print("\n1: Open the Locket\n2: Take the Locket to Emily's Grave")
    choice = input("Choose 1 or 2: ")
    if choice == '1' or choice == '2':
        chapter_14()
    else:
        print("Invalid choice, please try again.")
        chapter_13()

def chapter_14():
    print("\nChapter 14: Contact a Paranormal Expert")
    print("The expert arrives and sets up equipment to communicate with Emily. After a tense session, Emily's voice comes through. \"Thank you,\" she whispers. The locket opens, revealing a hidden photograph and a note explaining her tragic death. With this revelation, Emily’s spirit finally finds peace, and the haunting ceases.")
    print("\nThe End")

def start_adventure():
    chapter_1()

# Start the adventure
start_adventure()
