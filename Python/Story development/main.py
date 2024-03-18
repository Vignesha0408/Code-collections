import random

# Define some lists of words for different parts of speech
a =["Ragav", "Raghu", "Ramesh","Seenu", "Vignesh","Chetan"]
b =["Radhe", "Ramya","Radhika", "Geeta","Gouri","Pallavi"]
c = ["Maya","Gana","Scarlett","Rashmi"]
d = ["Subbi","kulli","Dummi"]
e = ["Pop","Rock","Country","Classical","Hip hop","Rhythm","blues (R&B)",
                 "Soul","Reggae","Funk","Folk","Jazz","Disco","Electronic dance music (EDM)","Blues",]
f = ["Harmonica","Mouth organ","Guiter","Drums" ,"bass drum",  
 "crash cymbal", "ride cymbal", "hi-hat cymbals"  ,
"Xylophone ","Tambourine","Flute","Saxophone","Trumpet","Trombone","French Horn","Tuba","Bagpipe","Violin","Viola",
"Cello","Double Bass","Guitar"  ,"Mandolin","Harp","Sitar","Veena"]


names =  random.choice(a)
frinds1= random.choice(b)
frinds2 = random.choice(c)
frinds3 = random.choice(d)
types_of_song = random.choice(e)
instruments=random.choice(f)
 
 
 
# Generate a story with some sentences
 
def story():
    
    random.choice(types_of_song)
    return   f'''
{names} loves to sing a song.
His voice was very nice and he has deep love for singing.
he loves to sing { types_of_song } music.
His best friends name are { frinds1 },{ frinds2 } and { frinds3 }.
They are very close friends.
:)
One sunny afternoon, {names} was strumming his {instruments} on a park bench,
humming a new tune. { frinds3 }, with her infectious laughter,
strolled by. "Wow, Seenu! That sounds amazing!
What are you working on?" she exclaimed.
{names}'s face lit up. "Just messing around with a new melody," he replied shyly.
'''

# Print the story
 
print(story())