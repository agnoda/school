#1. Count the number of words and characters in a string using a list data structure. Create a histogram of words in any software of your choice.
#2. Repeat step 1 and use a dictionary data structure.
#3. Use regular expressions and extract phone numbers and email addresses in a string. The phone numbers and email addresses should be saved in a separate
# list data structure.
#4. Extract the username from the email addresses saved in a list data structure in step 3 and append @hotmail.com at the end of the extracted usernames.
#Your code clearly shows the working of the tasks mentioned above. Include comments in the code to improve readability. Use meaningful variable names.
# Upload the python code (with a file extension .py).


import re
story = ('Once on a time and twice on a time, and all times together as ever I heard tell of, there was a tiny lassie who would weep all day to have the stars in the sky to play with; she wouldn’t have this, and she wouldn’t have that, but it was always the stars she would have. So one fine day off she went to find them. And she walked and she walked and she walked, till by-and-by she came to a mill-dam.'
         '“Goode’en to ye,” says she, “I’m seeking the stars in the sky to play with. Have you seen any?”)'
         '“Oh, yes, my bonnie lassie,” said the mill-dam. “They shine in my own face o’ nights till I can’t sleep for them. Jump in and perhaps you’ll find one.”'
         'So she jumped in, and swam about and swam about and swam about, but ne’er a one could she see. So she went on till she came to a brooklet.'
         '“Goode’en to ye, Brooklet, Brooklet,” says she; “I’m seeking the stars in the sky to play with. Have you seen any?”'
         '“Yes, indeed, my bonny lassie,” said the Brooklet. “They glint on my banks at night. Paddle about, and maybe you’ll find one.”'
         'So she paddled and she paddled and she paddled, but ne’er a one did she find. So on she went till she came to the Good Folk.'
         '“Goode’en to ye, Good Folk,” says she; “I’m looking for the stars in the sky to play with. Have ye seen e’er a one?”'
         '“Why, yes, my bonny lassie,” said the Good Folk. “They shine on the grass here o’ night. Dance with us, and maybe you’ll find one.”'
         'And she danced and she danced and she danced, but ne’er a one did she see. So down she sate; I suppose she wept.'
         '“Oh dearie me, oh dearie me,” says she, “I’ve swam and I’ve paddled and I’ve danced, and if ye’ll not help me I shall never find the stars in the sky to play with.”'
         'But the Good Folk whispered together, and one of them came up to her and took her by the hand and said, “If you won’t go home to your mother, go forward, go forward; mind you take the right road. Ask Four Feet to carry you to No Feet at all, and tell No Feet at all to carry you to the stairs without steps, and if you can climb that—”'
         '“Oh, shall I be among the stars in the sky then?” cried the lassie.'
         '“If you’ll not be, then you’ll be elsewhere,” said the Good Folk, and set to dancing again.'
         'So on she went again with a light heart, and by-and-by she came to a saddled horse, tied to a tree.'
         '“Goode’en to ye, Beast,” said she; “I’m seeking the stars in the sky to play with. Will you give me a lift, for all my bones are an-aching.”'
         '“Nay,” said the horse, “I know nought of the stars in the sky, and I’m here to do the bidding of the Good Folk, and not my own will.”'
         '“Well,” said she, “it’s from the Good Folk I come, and they bade me tell Four Feet to carry me to No Feet at all.”'
         '“That’s another story,” said he; “jump up and ride with me.”'
         'So they rode and they rode and they rode, till they got out of the forest and found themselves at the edge of the sea. And on the water in front of them was a wide glistening path running straight out towards a beautiful thing that rose out of the water and went up into the sky, and was all the colours in the world, blue and red and green, and wonderful to look at.'
         '“Now get you down,” said the horse; “I’ve brought ye to the end of the land, and that’s as much as Four Feet can do. I must away home to my own folk.”'
         '“But,” said the lassie, “where’s No Feet at all, and where’s the stair without steps?”'
         '“I know not,” said the horse, “it’s none of my business neither. So goode’en to ye, my bonny lassie;” and off he went.'
         'So the lassie stood still and looked at the water, till a strange kind of fish came swimming up to her feet.'
         '“Goode’en to ye, big Fish,” says she, “I’m looking for the stars in the sky, and for the stairs that climb up to them. Will ye show me the way?”'
         '“Nay,” said the Fish, “I can’t unless you bring me word from the Good Folk.”'
         '“Yes, indeed,” said she. “They said Four Feet would bring me to No Feet at all, and No Feet at all would carry me to the stairs without steps.”'
         '“Get on my back and hold fast.”'
         '“Ah, well,” said the Fish; “that’s all right then. Get on my back and hold fast.”'
         'And off he went—Kerplash!—into the water, along the silver path, towards the bright arch. And the nearer they came the brighter the sheen of it, till she had to shade her eyes from the light of it.'
         'And as they came to the foot of it, she saw it was a broad bright road, sloping up and away into the sky, and at the far, far end of it she could see wee shining things dancing about.'
         '“Now,” said the Fish, “here you are, and yon’s the stair; climb up, if you can, but hold on fast. I’ll warrant you find the stair easier at home than by such a way; ‘t was ne’er meant for lassies’ feet to travel;” and off he splashed through the water.'
         'So she clomb and she clomb and she clomb, but ne’er a step higher did she get: the light was before her and around her, and the water behind her, and the more she struggled the more she was forced down into the dark and the cold, and the more she clomb the deeper she fell.'
         'But she clomb and she clomb, till she got dizzy in the light and shivered with the cold, and dazed with the fear; but still she clomb, till at last, quite dazed and silly-like, she let clean go, and sank down—down—down.'
         'And bang she came on to the hard boards, and found herself sitting, weeping and wailing, by the bedside at home all alone.'
         '-----'
         'The story is written by'
         'Roger Federer &'
         'Serina Williams'
         'You can connect with the author at [rfederer@tennis.com] and [swilliams@tennis.com]'
         'Admin contact number: 1-888-111-2222')


# list of words to look up in the story
search_list = ['about', 'maybe', 'said', 'right']
# use the append function to create a list of counts of each word in the search list
word_counts = []
for word in search_list:
    word_counts.append(story.count(word))
#print(story.count('he'))
print (word_counts)

word_counts_dict = {}
# use the dictionary data structure instead to store the word counts
# the dictionary should look like {'word': count, etc.}
for word in search_list:
    word_counts_dict[word] = story.count(word)

print(word_counts_dict)
# extract all email addresses and phone numbers found
emails = re.findall(r'[\w\.-]+@[\w.-]+', story)
emails_in_a_list = []              # to be used for storing the emails found in the story
for email in emails:
    emails_in_a_list.append(email) # append all emails found by the re.findall function into a list
print("Emails Found:", emails_in_a_list)

phone_numbers = re.findall(r'\d-\d\d\d-\d\d\d-\d\d\d\d', story)
for phone_number in phone_numbers:
    print("Phone Number Found", phone_number)

# extract only the usernames found in the story and append them with @hotmail.com
emails_split = re.findall(r'([\w\.-]+)@([\w.-]+)', story)
usernames = []                      # to be used for storing the usernames in the email addresses;
                                    # #the usernames are the characters in group 1 (within the first parentheses)
new_emails = []                     # to be used for storing the list after appending  @hotmail.com for all emails found
for email_split in emails_split:
#    print(email_split[0])
    usernames.append(email_split[0])
    new_emails.append(email_split[0]+'@hotmail.com')
print('Email Usernames Found:', usernames)
print('Hotmail Addresses:', new_emails)

