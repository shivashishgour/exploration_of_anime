import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
df = pd.read_csv('anime_cleaned.csv')

l=[]
for i in range(0,255):
    r = lambda: random.randint(0,255)
    x = '#%02X%02X%02X' % (r(),r(),r()) #creating color palletes
    l.append(x)

while True:
    print("\n+++++++++++++++++++++ EXPLORATION OF ANIME +++++++++++++++++++++ ")
    print("1. ANIME OVERVIEW ")
    print("2. ANIME INTERACTION")
    print("3. RANKING")
    print("4. DATA INTERACTION")
    print("5. EXIT")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    choice= int(input('Enter Your choice : '))

    if(choice == 1):
        print("\nGeneral summary of Anime Dataset : ", len(df))
        print("Average Score by Anime : ", round(df.score.mean(),3))
        print("Average number of people who gave the score : ", round(df.scored_by.mean()) )
        print("\n-----------------------------------------------------------------")
        print("1. Bar Graph of Type of Anime ")
        print("2. Bar Graph of Source of anime")
        print("3. Bar Graph of Top Genres")
        print("4. Bar Graph of Rating")
        print("-----------------------------------------------------------------")
        choice1= int(input('Enter which Graph you want to see :  '))
        if(choice1 == 1):
            df['type'].value_counts().plot.barh(color=l,width=0.9)
            plt.show()
            
        if(choice1 == 2):
            df['source'].value_counts().plot.barh(color=l,width=0.9)
            plt.show()
            
        if(choice1 == 3):
            df.genre.str.split(',').value_counts().head(10).plot(kind='barh',color=l)
            plt.show()
            
        if(choice1 == 4):
            df['rating'].value_counts().plot.barh(color=l,width=0.9)
            plt.show()
     
    if(choice==2):
        print("\n-----------------------------------------------------------------")
        print('1. Anime Type VS Anime Score')
        print('2. Anime Source VS Anime Score')
        print('3. Anime Rating VS Anime Score')
        print('4. Year of release')
        print('5. Anime Duration')
        print('6. Anime Studio')
        print("-----------------------------------------------------------------\n")
        choice2= int(input('Enter which Graph you want to see :  '))
        
        if(choice2 == 1): #this will plot the histogram of ANIME type VS SCORE
            tv=df[df['type'] == 'TV']
            tv['score'].value_counts().plot.hist(label='TV')
            mean_score_tv=round(tv.score.mean(),3)
            min_score_tv=round(tv.score.min(),3)
            max_score_tv=round(tv.score.max(),3)

            Special=df[df['type']=='Special']
            Special['score'].value_counts().plot.hist(label='Special')
            mean_score_special=round(Special.score.mean(),3)
            min_score_special=round(Special.score.min(),3)
            max_score_special=round(Special.score.max(),3)

            OVA=df[df['type']=='OVA']
            OVA['score'].value_counts().plot.hist(label='OVA')
            mean_score_ova=round(OVA.score.mean(),3)
            min_score_ova=round(OVA.score.min(),3)
            max_score_ova=round(OVA.score.max(),3)

            Movie=df[df['type'] == 'Movie']
            Movie['score'].value_counts().plot.hist(label='Movie')
            mean_score_movie=round(Movie.score.mean(),3)
            min_score_movie=round(Movie.score.min(),3)
            max_score_movie=round(Movie.score.max(),3)
         
            Music=df[df['type'] == 'Music']
            Music['score'].value_counts().plot.hist(label='Music')
            mean_score_music=round(Music.score.mean(),3)
            min_score_music=round(Music.score.min(),3)
            max_score_music=round(Music.score.max(),3)

            ONA=df[df['type']=='ONA']
            ONA['score'].value_counts().plot.hist(label='ONA')
            mean_score_ona=round(ONA.score.mean(),3)
            min_score_ona=round(ONA.score.min(),3)
            max_score_ona=round(ONA.score.max(),3)

            tv_score=[mean_score_tv,min_score_tv,max_score_tv]
            special_score=[mean_score_special,min_score_special,max_score_special]
            ova_score=[mean_score_ova,min_score_ova,max_score_ova]
            movie_score=[mean_score_movie,min_score_movie,max_score_movie]
            music_score=[mean_score_music,min_score_music,max_score_music]
            ona_score=[mean_score_ona,min_score_ona,max_score_ona]

            final_score=[tv_score,special_score,ova_score,movie_score,music_score,ona_score]
            print(pd.DataFrame(final_score, index=['TV','SPECIAL','OVA','MOVIE','MUSIC','ONA'],columns=['Mean Score','Minimum Score','Maximum Score']))
            
            plt.legend()
            plt.show()

        if(choice2 == 2):#this will plot the histogram of ANIME SOURCE VS SCORE
            manga=df[df['source'] == 'Manga']
            manga['score'].value_counts().plot.hist(label='Manga')
            mean_score_manga=round(manga.score.mean(),3)
            min_score_manga=round(manga.score.min(),3)
            max_score_manga=round(manga.score.max(),3)

            original=df[df['source']=='Original']
            original['score'].value_counts().plot.hist(label='Original')
            mean_score_original=round(original.score.mean(),3)
            min_score_original=round(original.score.min(),3)
            max_score_original=round(original.score.max(),3)

            lightnovel=df[df['source']=='Light novel']
            lightnovel['score'].value_counts().plot.hist(label='Light novel')
            mean_score_lightnovel=round(lightnovel.score.mean(),3)
            min_score_lightnovel=round(lightnovel.score.min(),3)
            max_score_lightnovel=round(lightnovel.score.max(),3)

            visualnovel=df[df['source'] == 'Visual novel']
            visualnovel['score'].value_counts().plot.hist(label='Visual novel')
            mean_score_visualnovel=round(visualnovel.score.mean(),3)
            min_score_visualnovel=round(visualnovel.score.min(),3)
            max_score_visualnovel=round(visualnovel.score.max(),3)
         
            game=df[df['source'] == 'Game']
            game['score'].value_counts().plot.hist(label='Game')
            mean_score_game=round(game.score.mean(),3)
            min_score_game=round(game.score.min(),3)
            max_score_game=round(game.score.max(),3)

            manga_score=[mean_score_manga,min_score_manga,max_score_manga]
            original_score=[mean_score_original,min_score_original,max_score_original]
            lightnovel_score=[mean_score_lightnovel,min_score_lightnovel,max_score_lightnovel]
            visualnovel_score=[mean_score_visualnovel,min_score_visualnovel,max_score_visualnovel]
            game_score=[mean_score_game,min_score_game,max_score_game]
           
            final_score=[manga_score,original_score,lightnovel_score,visualnovel_score,game_score]
            print(pd.DataFrame(final_score, index=['MANGA','ORIGINAL','LIGHT NOVEL','VISUAL NOVEL','GAME'],columns=['Mean Score','Minimum Score','Maximum Score']))
            
            plt.legend()
            plt.show()

        if(choice2 == 3):#this will plot the histogram of ANIME Rating VS SCORE
            pg13=df[df['rating'] == 'PG-13 - Teens 13 or older']
            pg13['score'].value_counts().plot.hist(label='PG-13 - Teens 13 or older')
            mean_score_pg13=round(pg13.score.mean(),3)
            min_score_pg13=round(pg13.score.min(),3)
            max_score_pg13=round(pg13.score.max(),3)

            g_all=df[df['rating']=='G - All Ages']
            g_all['score'].value_counts().plot.hist(label='G - All Ages')
            mean_score_g_all=round(g_all.score.mean(),3)
            min_score_g_all=round(g_all.score.min(),3)
            max_score_g_all=round(g_all.score.max(),3)

            r17=df[df['rating']=='R - 17+ (violence & profanity)']
            r17['score'].value_counts().plot.hist(label='R - 17+ (violence & profanity)')
            mean_score_r17=round(r17.score.mean(),3)
            min_score_r17=round(r17.score.min(),3)
            max_score_r17=round(r17.score.max(),3)

            rmild=df[df['rating'] == 'R+ - Mild Nudity']
            rmild['score'].value_counts().plot.hist(label='R+ - Mild Nudity')
            mean_score_rmild=round(rmild.score.mean(),3)
            min_score_rmild=round(rmild.score.min(),3)
            max_score_rmild=round(rmild.score.max(),3)
         
            pgchild=df[df['rating'] == 'PG - Children']
            pgchild['score'].value_counts().plot.hist(label='PG - Children')
            mean_score_pgchild=round(pgchild.score.mean(),3)
            min_score_pgchild=round(pgchild.score.min(),3)
            max_score_pgchild=round(pgchild.score.max(),3)

            pg13_score=[mean_score_pg13,min_score_pg13,max_score_pg13]
            g_all_score=[mean_score_g_all,min_score_g_all,max_score_g_all]
            r17_score=[mean_score_r17,min_score_r17,max_score_r17]
            rmild_score=[mean_score_rmild,min_score_rmild,max_score_rmild]
            pgchild_score=[mean_score_pgchild,min_score_pgchild, max_score_pgchild]
           
            final_score=[pg13_score,g_all_score,r17_score,rmild_score,pgchild_score]
            print(pd.DataFrame(final_score, index=['PG-13','G- All Ages','R-17+','R+','PG-Children'],columns=['Mean Score','Minimum Score','Maximum Score']))
            
            plt.legend()
            plt.show()
                
        if(choice2 == 4):
            df.aired_from_year.value_counts().plot(kind='line',color=l)
            plt.show()

        if(choice2==5):
            df.duration_min.value_counts().head(15).plot(kind='barh',color=l)
            plt.show()

        if(choice2 == 6):
            df.studio.value_counts().head(10).plot(kind='barh',color=l)
            plt.show()

    if(choice == 3):
        print("\n-----------------------------------------------------------------")
        print('1. Based on popularity')
        print('2. Based on Score')
        print('3. Based on Rank')
        print('4. Based on Favourites')
        print("-----------------------------------------------------------------\n")
        choice3= int(input('Enter your choice :  '))

        if(choice3 == 1):
            print(df.sort_values(by=['members','popularity'],ascending=False).head(10).loc[: ,['title','members','popularity']])

        if(choice3 == 2):
            print(df.sort_values(by=['scored_by','score'],ascending=False).head(10).loc[: ,['title','score','scored_by']])

        if(choice3 == 3):
            print(df.sort_values(by=['popularity','rank']).head(10).loc[: ,['title','rank','popularity']])

        if(choice3 == 4):
            print(df.sort_values(by=['favorites','members'],ascending=False).head(10).loc[: ,['title','members','favorites']])
            
    if(choice ==4):
        print("\n-----------------------------------------------------------------")
        print("This Section will print the Scatter Plot with respect to columns you chose ")
        print('1. Episode')
        print('2. Year')
        print('3. Duration')
        print('4. Score')
        print('5. Raters')
        print('6. Members')
        print('7. Favorites')    
        print("-----------------------------------------------------------------\n")

        value1= int(input("Enter for X axis : "))
        value2= int(input("Enter for Y axis : "))

        if(value1 == 1):
            X='episodes'
        if(value1 == 2):
            X='aired_from_year'
        if(value1 == 3):
            X='duration'
        if(value1 == 4):
            X='score'
        if(value1 == 5):
            X='scored_by'
        if(value1 == 6):
            X='members'
        if(value1 == 7):
            X='favorites'

        if(value2 == 1):
            Y='episodes'
        if(value2 == 2):
            Y='aired_from_year'
        if(value2 == 3):
            Y='duration'
        if(value2 == 4):
            Y='score'
        if(value2 == 5):
            Y='scored_by'
        if(value2 == 6):
            Y='members'
        if(value2 == 7):
            Y='favorites'
        
                                    
        for i in df:
            for j in df:
                if(i==X and j==Y):
                    df.plot(x=X, y=Y, kind='scatter')
                    plt.show()

    if(choice==5):
        print("----------------------THANK YOU !-----------------------")
        break;







    
