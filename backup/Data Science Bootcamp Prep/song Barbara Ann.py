import ploty

lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"

k={x: lyrics.count(x) for x in lyrics.split()}
# for x in lyrics.split():
#     k[x]=lyrics.count(x)

for x in k:
    print(x, k[x],"\n")
print(k)
print("-" * 50)
print(lyrics.split(" "))

