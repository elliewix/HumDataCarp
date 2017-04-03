with open('raven.txt', 'r') as file_in:
    poem = file_in.read()
    
stanzas = poem.split("\n\n")

raven_count = [s.count("Raven") + s.count("bird") + s.count("fowl") for s in stanzas]
lenore_count = [s.count("Lenore") for s in stanzas]
chamber_count = [s.count("chamber") for s in stanzas]
door_count= [s.count("door") for s in stanzas]

print("Counts of 'bird'/'Raven'/'fowl' as \U0001F426 and \n"
      "Lenore as \U0001F452 and 'chamber' as \U0001F6AA\n"
      "in stanzas of The Raven")
print()
for stanza_num, bird_count in enumerate(raven_count):
    print(str(stanza_num).zfill(2) + ": ", end = "") 
    print(u'\U0001F3E0' * chamber_count[stanza_num], end = "")
    print(u'\U0001F6AA' * door_count[stanza_num], end = "")
    print(u'\U0001F426' * bird_count, end = "")
    print(u'\U0001F452' * lenore_count[stanza_num])