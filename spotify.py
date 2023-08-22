import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# #database-table creation
# def create_database():
#     mydb=mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
#     createcursor=mydb.cursor()
#     createcursor.execute("create database if not exists spotify")
#     mydb.commit()
#     createcursor.close()
#     mydb.close()
#     print('Database created successfully')
# create_database()

# def create_table_songs():
#         mydb=mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
#         create_table_cursor=mydb.cursor()
#         create_table_cursor.execute("use spotify")
#         create_table_cursor.execute("create table if not exists songs(id varchar(100) primary key,name varchar(100),artist varchar(100),release_date date,popularity int,danceability Float,energy float)")
#         mydb.commit()
#         create_table_cursor.close()
#         mydb.close()
#         print("table created")
# create_table_songs()

# def create_table_Genres():
#         mydb=mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
#         create_table_cursor=mydb.cursor()
#         create_table_cursor.execute("use spotify")
#         create_table_cursor.execute("create table if not exists genres(id varchar(100) primary key,Genre varchar(100))")
#         mydb.commit()
#         create_table_cursor.close()
#         mydb.close()
#         print("table created")
# create_table_Genres()

# def create_table_songGenre():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Ramdevi#2",
#         port=3306,
#         database="testdb"
#     )
    
#     create_table_cursor = mydb.cursor()
#     create_table_cursor.execute("use spotify")
    
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS songgenres (
#             song_id varchar(100),
#             genre_id varchar(100),
#             FOREIGN KEY (song_id) REFERENCES songs (id),
#             FOREIGN KEY (genre_id) REFERENCES genres (id)
#         )
#     """
#     create_table_cursor.execute(create_table_query)
    
#     mydb.commit()
#     create_table_cursor.close()
#     mydb.close()
#     print("Table created")
# create_table_songGenre()

def insert():
    while True:
        try:
            id=input("Enter ID of the Song : ")
            name=input("Enter name of the Song : ").upper()
            artist=input("Enter the name of the Artist : ")
            genre=input("Enter Genre of the song : ")
            g_id=input("Enter Genre id of the song : ")
            date=input("Enter the Release Date : ")
            popularity=int(input("Enter the Popularity value : "))
            danceability=float(input("Enter the Danceability value : "))
            energy=float(input("Enter Energy value : "))

            mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
            insertcursor=mydb.cursor()
            insertcursor.execute('insert into songs(id,name,artist,release_date,popularity,danceability,energy) values(%s,%s,%s,%s,%s,%s,%s)',(id,name,artist,date,popularity,danceability,energy))
            mydb.commit()
            insertcursor.close()
            mydb.close()

            mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
            insertcursor=mydb.cursor()
            insertcursor.execute('insert into genres(id,Genre) values(%s,%s)',(g_id,genre))
            mydb.commit()
            insertcursor.close()
            mydb.close()


            mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
            insertcursor=mydb.cursor()
            insertcursor.execute('insert into songgenres(song_id, genre_id) values(%s,%s)',(id,g_id))
            mydb.commit()
            insertcursor.close()
            mydb.close()
            print("Song added to your Playlist 💚")
            break
        except Exception as e:
            print("/nEnter Valid data/format ... ")

def show():

        try:
            print("\nYour play list:\n")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
            showcursor=mydb.cursor()
            print("==============PLAY-LIST==============\n")
            showcursor.execute("SELECT * from songs")
            match_songs=showcursor.fetchall()
            for i in match_songs:
                print(i[0]+":"+i[1])
            print("===================================== ")
            mydb.commit()
            showcursor.close()
            mydb.close()
        except mysql.connector.Error as err:
            print("An error occurred:", err)

def search():
    while True:
        print("You can search song by \n 1.Song \n 2.Artist \n 3.Year\n 4.Exit ")
        choice=int(input("Enter your Choice"))
        if choice==1:
            try:
                name=input("Search Query(Song name) 🔍︎ : ")
                mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
                insertcursor=mydb.cursor()
                insertcursor.execute('SELECT * FROM songs WHERE name=%s', (name,))

                matching_songs = insertcursor.fetchall()

                if matching_songs:
                    print(f"\n{len(matching_songs)} song(s) found with the name '{name}':")
                    for song in matching_songs:
                        print("\n ====================================\n\n Song:", song[1]+ "    "+ "Artist:", song[2]+ "\n\n         ◁     ||     ▷  \n ====================================")  
                    mydb.commit()
                else:  
                    print("No songs found with the name", name)      
            except mysql.connector.Error as err:
                    print("Error:", err)



            
        elif choice==2:
            try:
                artist=input("Search Query(Artist Name) 🔍︎ : ")
                mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
                insertcursor=mydb.cursor()
                insertcursor.execute("select * from songs where artist=%s", (artist,))
                matching_songs=insertcursor.fetchall()
                

                if matching_songs:
                    print(f"\n{len(matching_songs)} song(s) found with the artist name '{artist}':")
                    for i in matching_songs:
                        print("\n ====================================\n\n Song:", i[1]+ "    "+ "Artist:", i[2]+ "\n\n         ◁     ||     ▷  \n ====================================")  
                    mydb.commit()
                else:
                    print("No songs found with the artist name", artist)
            except mysql.connector.Error as err:
                    print("Error:", err)

        
        elif choice==3:
            try:
                year=input("Search Query( Year(YYYY) ) 🔍︎ : ")
                mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
                insertcursor=mydb.cursor()
                insertcursor.execute("select * from songs where year(release_date)=%s", (year,))
                matching_songs=insertcursor.fetchall()
                print(matching_songs)
                if matching_songs:
                    print(f"\n{len(matching_songs)} song(s) found with the Release date '{year}':")
                    for song in matching_songs:
                        print("\n ======================================================\n\n Song:", song[1]+ "    "+ "Artist:", song[2]+"    "+ "Year:",str(song[3])+"\n\n             ◁     ||     ▷  \n ======================================================")  
                    mydb.commit()
                else:
                    print("No songs found with the year", year)
            except mysql.connector.Error as err:
                print("Error:", err)
        elif choice==4:
            print("Exiting...")
            break
        else:
            print("Enter Valid Choice")


def remove():
    while True:
        try:
            id=input("Enter the id of song do you want to delete : ")
            g_id=input("Enter the id of Gener do you want to delete : ")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
            remcursor=mydb.cursor()
            remcursor.execute("DELETE FROM songgenres WHERE song_id = %s", (id,))
            remcursor.execute("DELETE FROM songs WHERE id = %s", (id,))
            remcursor.execute("\nDELETE FROM genres WHERE id = %s", (g_id,))
            print(f"\nSong with id {id} removed from the Playlist 👋")
            mydb.commit()
            remcursor.close()
            mydb.close()
            break
        except Exception as e:
            print("The item cant fetch from Database")

def data_analysis():
    # mydb=mysql.connector.connect(host="localhost",user="root",password="Ramdevi#2",port=3306,database="spotify")
    # analyscursor=mydb.cursor()
    query = "SELECT * FROM songs"

    #creating SQLalchemi engine for databse connection
    engine = create_engine('mysql+mysqlconnector://root:Ramdevi#2@localhost:3306/spotify')

    # Load data into a Pandas DataFrame
    df=pd.read_sql_query(query,engine)

    avg_popularity=df["popularity"].mean()
    avg_danceabilty=df["danceability"].mean()
    avg_energy=df["energy"].mean()
    

    print("The Average Popularity 💫 : ",avg_popularity)
    print("The Average Danceability 💃 : ",avg_danceabilty)
    print("The Average Energy ⚡ : ",avg_energy)
    
    print("==============Additional-Information==============\n")
    most_popular=df[df["popularity"]==df["popularity"].max()]
    most_popular_subset =most_popular.iloc[:,[0,1,4]]
    print("\nMost Popular Song in Your Playlist is : \n")
    print(most_popular_subset)
    print("\n--------------------------------------------------\n")

    most_dance=df[df["danceability"]==df["danceability"].max()]
    most_dance_subset =most_dance.iloc[:,[0,1,5]]
    print("\nMost Danceability Song in Your Playlist is : \n")
    print(most_dance_subset)
    print("\n--------------------------------------------------\n")

    most_energy=df[df["energy"]==df["energy"].max()]
    most_energy_subset =most_energy.iloc[:,[0,1,5]]
    print("\nMost Energetic Song in Your Playlist is : \n")
    print(most_energy_subset)
    print("\n--------------------------------------------------\n")
    print("==================================================\n")
        
    
    
    # mydb.commit()
    # analyscursor.close()
    # mydb.close() 

def visualization():
    query = "SELECT * FROM songs"

    #creating SQLalchemi engine for databse connection
    engine = create_engine('mysql+mysqlconnector://root:Ramdevi#2@localhost:3306/spotify')

    # Load data into a Pandas DataFrame
    df=pd.read_sql_query(query,engine)
    while True:
        choice=int(input("Enter the Aspect of your Playlist to do you want to Visualize... :) \n 1.Poplarity-Song \n 2.Danceability-Song\n 3.Energy-Song\n 4.Exit\nEnter Your Choice : "))
        if choice==1:
            plt.figure(figsize=(10, 6))
            # plt.pie(df["name"].tolist(),df["popularity"])
            plt.pie(df["popularity"], labels=df["name"], autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            # plt.xlabel("name")
            # plt.ylabel("popularity")
            # plt.xticks(rotation=45,ha='right')
            # plt.tight_layout()
            # plt.legend(loc="upper left",fontsize=10)
            plt.title("Popularity-Song\n\n")
            plt.show()
        elif choice==2:
            plt.figure(figsize=(10,6))
            plt.pie(df["danceability"], labels=df["name"],autopct=('%1.1f%%'),startangle=140)
            plt.axis('equal')
            plt.title("Song-Danceability\n\n")
            plt.show()
        elif choice==3:

            plt.figure(figsize=(10,6))
            plt.pie(df["energy"], labels=df["name"],autopct=('%1.1f%%'),startangle=140)
            plt.axis('equal')
            plt.title("Song-Energy\n\n")
            plt.show()
        elif choice==4:
            print("Exiting....")
            break
        else:
            print("Enter Valid Choice....")



   

def statistics():
    while True:
         choice=int(input("What Statistics do you want to Check\n 1.Analysis\n 2.Visualization\n 3.Exit\nEnter Your Choice : "))
         if choice==1:
            print("====================ANALYSIS====================\n")
            data_analysis()
         elif choice==2:
             visualization()
         elif choice==3:
             print("Exiting...")
             break
         else:
             print("Enter Valid Choice....")


             
    
 
   

  
            
def main():
    while True:
        choice=int(input("\n Hey Welcome Musicophile, What do you want to do today.....?\n 1.Show Playlist\n 2.Search song\n 3.Add Song\n 4.Remove Song\n 5.Check Statitics\n 6.Exit\nEnter your Choice : "))
        if choice==1:
            show()
        elif choice==2:
            search()
        elif choice==3:
          print("Let's add your Favourite songs to your Playlist")
          insert()
        elif choice==4:
            remove()
        elif choice==5:
            statistics()
        elif choice==6:
            print("Exiting....")
            break
        else:
            print("Enter Valid choice.... :)")

            
main()

      
      
