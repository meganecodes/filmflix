import sqlite3 as sql
import time
from prettytable import from_db_cursor


try:
# creating a connection
    conn = sql.connect("filmflix.db")
    print("Connected to SQLite")
except sql.error as error:
    print("Failed to connect to SQLite")


# creating a cursor - to make the connection for executing sql queries
with conn:
    c = conn.cursor()
    c.execute("SELECT * FROM Films")
    x = from_db_cursor(c)


# creating table
#c.execute("""Create #Table Films(
#"FilmID" INTEGER NOT NULL,
#"Title" TEXT,
#"Year" INTEGER,
#"Rating" TEXT,
#"Franchise" TEXT,
#"Duration" INTEGER,
#"Genre" TEXT,
#PRIMARY KEY("filmID" AUTOINCREMENT)
#) """)

conn.commit()


# READ FILMS
read = ""
def read_films(read):
    c.execute("SELECT * FROM Films") 
    print(x)

    #return read
  
#if __name__ == '__main__':
  #read_films(read)


# ADD FILMS
add = ""
def add_film(add):

# film array
    films = []

    film_title = input("What's your film name? \n")
    while True:
        try:
            film_year = int(input("\nWhat year was the film released? \n"))
            break
        except ValueError:
            print("\nInvalid characters. Please make sure the year only contains numbers.")
            continue

    while True:
        film_rating = input("\nFrom the options listed, enter your film rating by letter: \n\nG (General Audience) \nPG (Parental Guidance) \nR (Restricted) \n\n")
        if film_rating not in ('R', 'r', 'PG', 'pg', 'G', 'g'):
            print("Please choose if your film is either rated G, PG or R.")
        else:
            break
              
    while True:
        film_franchise = input(" \nWhich media franchise is your film from? \n\nDC \nDreamWorks \nMarvel \nPixar \nOther \n\n")
        if film_franchise not in ('DC', 'DreamWorks', 'Marvel', 'Pixar', 'Other'):
            print("Please only enter one option from the list")
        else:
            break
        
    while True:
        try:
            film_duration = int(input("\nHow long is the duration of your film in minutes? \n"))
            break
        except ValueError:
            print("\nInvalid characters. Please make sure the duration only contains numbers.")
            continue

    film_genre = input("\nWhat's the genre of your film?\n")

    film_title = film_title.title()
    film_rating = film_rating.upper()
    film_franchise = film_franchise.title()
    film_genre = film_genre.title()

# add user's answers to list
    films.append(film_title)
    films.append(film_year)
    films.append(film_rating)
    films.append(film_franchise)
    films.append(film_duration)
    films.append(film_genre)

# insert user's answer onto film table
    c.execute("INSERT INTO Films(Title, Year, Rating, Franchise, Duration, Genre) VALUES (?,?,?,?,?,?)", films)
    conn.commit()
    print(f"\n{film_title} has been added!")
    time.sleep(3)

  #return add

#if __name__ == '__main__':
    #add_film(add)


# UPDATE FILMS
update = ""
def update_film(update):
    while True:
        try:
            id_field = int(input("Enter the Film ID of the film you want to update.\n"))
            break
        except ValueError:
            print("\nInvalid characters. Please make sure the number entered is correct.\n")
            continue

    while True:
        field_name = input("\nEnter which category you would like to update from the list: \n\nTitle\nYear\nRating\nFranchise\nDuration\nGenre\n\n")
        if field_name not in ('title', 'year', 'rating', 'franchise', 'duration', 'genre', 'Title', 'Year', 'Rating', 'Franchise', 'Duration', 'Genre'):
            print("\nCan only choose one of the categories listed to be updated.\n")
        else:
            break
    
    field_value = input(f"\nPlease enter what you would like the {field_name} to be updated to. (If updating film rating, select from either G, PG or R.)\n")

    match field_name:
        case "title":
            field_value = field_value.title()
        case "rating":
            field_value = field_value.upper()
        case "franchise":
            field_value = field_value.title()
        case "genre":
            field_value = field_value.title()

    field_value = "'" + field_value + "'"

    c.execute(f"UPDATE Films SET {field_name} = {field_value} WHERE FilmID = {id_field}")
    conn.commit()

    print(f"\nFilm ID {id_field} has been updated!")
    time.sleep(3)

  #return update

#if __name__ == '__main__':
    #update_film(update)


# DELETE FILMS
delete = ""
def delete_film(delete):
    while True:
        try:
            id_field = int(input("Enter the Film ID of the film you wish to delete.\n"))
            break
        except ValueError:
            print("\nInvalid characters. Please enter the Film ID you wish to delete. \n")
            continue
        
    while True:
        try:
            delete_val = int(input(f"\nYou are about to delete Film ID {id_field}, do you wish to continue? Type 1 for 'Yes' or 2 for 'No'.\n"))
        except ValueError:
            print("\nInavlid characters. Please enter either 1 for 'Yes' or 2 for 'No'")
            continue

        if delete_val not in (1,2):
            print("\nPlease enter either 1 for 'Yes' or 2 for 'No'")
        else:
            break
    
    while True:
        if delete_val == 1:
            print(f"Film ID {id_field} has been deleted!")
            c.execute(f"DELETE FROM Films WHERE FilmID = {id_field}")
            conn.commit()
            break
        else:
            break

    while True:
        if delete_val == 2:
            print("\nFilm ID has not been deleted.")
            break
        else:
            break
   
    time.sleep(3)  
        
    #return delete

#if __name__ == '__main__':
    #delete_film(delete)


# REPORT OF FILMS
report = ""
def read_report(report):
    report_data = True
    while report_data:

# Main menu
        report = input("Welcome to the Film Flix Database \n\nEnter which report you would like to view by number:\n\n1. View all films\n2. View all data from selected column\n3. View all films from selected media franchise\n4. View all films from selected genre\n5. View all films from selected year\n6. View all films from selected rating\n7. Exit\n\n")
        options = True
        while options:
            match report:

# 1. View all films
                case '1':
                    c.execute("SELECT * FROM Films")
                    x = from_db_cursor(c)
                    print(x)
     
                    options = False

# 2. Filter and view films
                case '2':
                    filter_view = input("\nFilter to view film data by entering the first letter of your option:\n\nT. Title\nY. Year\nR. Rating\nF. Franchise\nD. Duration\nG. Genre\n\n")
                    #make options upper when entered
                    filter_view = filter_view.upper()

                    # Sub-menu for filtering videos
                    match filter_view:
                        case 'T':
                            c.execute("SELECT Title FROM Films")
                            x = from_db_cursor(c)
                            print(x)
                        
                        case 'Y':
                            c.execute("SELECT Year FROM Films")
                            x = from_db_cursor(c)
                            print(x)

                        case 'R':
                            c.execute("SELECT Rating FROM Films")
                            x = from_db_cursor(c)
                            print(x)

                        case 'F':
                            c.execute("SELECT Franchise FROM Films")
                            x = from_db_cursor(c)
                            print(x)

                        case 'D':
                            c.execute("SELECT Duration FROM Films")
                            x = from_db_cursor(c)
                            print(x)

                        case 'G':
                            c.execute("SELECT Genre FROM Films")
                            x = from_db_cursor(c)
                            print(x)

                    options = False

# 3.  View films from a selected media franchise
                case '3':
                    franchise_view = input("\nTo view films from a particular franchise, choose using the letter code:\n\ndc. DC\ndw. DreamWorks\nmr. Marvel\npx. Pixar\nor. Other\n\n")
                    franchise_view = franchise_view.upper()

                    #franchise sub-menu
                    match franchise_view:
                        case 'DC':
                            c.execute("SELECT * FROM Films WHERE Franchise = \'DC\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'DW':
                            c.execute("SELECT * FROM Films WHERE Franchise = \'DreamWorks\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'MR':
                            c.execute("SELECT * FROM Films WHERE Franchise = \'Marvel\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'PX':
                            c.execute("SELECT * FROM Films WHERE Franchise = \'Pixar\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'OR':
                            c.execute("SELECT * FROM Films WHERE Franchise = \'Other\'")
                            x = from_db_cursor(c)
                            print(x)
                        
                    options = False
                            
# 4. View films from a selected genre
                case '4':
                    genre_view = input("\nTo view films from a particular genre, choose using the letter code:\n\na. Action\nac. Action Comedy\nan. Animation\nc. Comedy\nfa. Fantasy\nmu. Musical\n\n")
                    genre_view = genre_view.upper()

                    #genre sub menu
                    match genre_view:
                        case 'A':
                            c.execute("SELECT * From Films WHERE Genre = \'Action\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'AC':
                            c.execute("SELECT * From Films WHERE Genre = \'Action Comedy\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'AN':
                            c.execute("SELECT * From Films WHERE Genre = \'Animation\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'C':
                            c.execute("SELECT * From Films WHERE Genre = \'Comedy\'")
                            x = from_db_cursor(c)
                            print(x)
                        
                        case 'FA':
                            c.execute("SELECT * From Films WHERE Genre = \'Fantasy\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'MU':
                            c.execute("SELECT * From Films WHERE Genre = \'Musical\'")
                            x = from_db_cursor(c)
                            print(x)
                        
                    options = False

# 5. View films from a selected year
                case '5':
                    year_view = input("\nEnter a year to view films released in selected year.\n\n")
                    year_view = "'" + year_view + "'"
                    c.execute(f"SELECT * FROM Films WHERE Year = {year_view}")
                    x = from_db_cursor(c)
                    print(x)

                    options = False
                
# 6. View film with a selected rating
                case '6':
                    rating_view = input("\nTo view films with a selected rating, choose using the letter code:\n\nG. General Audience\nPG. Parental Guidance\nR. Restricted\n\n")
                    rating_view = rating_view.upper()

                    # rating sub menu
                    match rating_view:
                        case 'G':
                            c.execute("SELECT * FROM Films WHERE Rating = \'G\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'PG':
                            c.execute("SELECT * FROM Films WHERE Rating = \'PG\'")
                            x = from_db_cursor(c)
                            print(x)

                        case 'R':
                            c.execute("SELECT * FROM Films WHERE Rating = \'R\'")
                            x = from_db_cursor(c)
                            print(x)

                    options = False

# 7. Exit
                case '7':
                    print("You have exited the Film Flix Database")

                    options = False
                    report_data = False

# If anything other than the value listed above is entered
                case _:
                    print(f"{report} is invalid")
                    report = input("Film Flix Database \n\nEnter which report you would like to view by number:\n\n1. View all films\n2. View all films from selected column\n3. View all films from selected media franchise\n4. View all films from selected genre\n5. View all films from selected year\n6. View all films from selected rating\n7. Exit\n\n")

    #return report
#if __name__ == '__main__':
    #read_report(report)

# FILM MENU
main_menu = ""
def menu(main_menu):
    menu_data = True
    while menu_data:

# Welcome message
        menu_options = input("Welcome to Film Flix! Select an option by number to continue:\n\n1. Add Film\n2. Update Film\n3. Delete Film\n4. View All Films\n5. View Reports\n6. Exit\n\n")

        menu_ops = True
        while menu_ops:
            
            # Menu - link files with their function names
            match menu_options:
                case '1':
                    add.add_film()
                    menu_ops = False

                case '2':
                    update_film(update)
                    menu_ops = False

                case '3':
                    delete_film(delete)
                    menu_ops = False

                case '4':
                    read_films(read)
                    menu_ops = False

                case '5':
                    read_report(report)
                    menu_ops = False
                
                case '6':
                    print("Thank You for stopping by!")
                    menu_ops = False
                    menu_data = False
                
                case _:
                    print(f"{menu_options} is invalid.")
                    menu_options = input("Welcome to the Film Flix Database! Select an option by number to continue:\n\n1. Add Film\n2. Update Film\n3. Delete Film\n4. View All Films\n5. View Reports\n6. Exit\n\n")

menu(main_menu)

