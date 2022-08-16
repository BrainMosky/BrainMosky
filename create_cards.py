import sqlite3

def main():
    """
    Add a new card to spacegame database
    CREATE TABLE cards (
        id INTEGER,
        card_name TEXT,
        strength INTEGER,
        life INTEGER,
        card_type INTEGER,
        PRIMARY KEY(id)
    );
    """
    con = sqlite3.connect('spacegame.db')
    cur = con.cursor()

    card_name = input('Enter card name:')
    card_strength = input('Enter card strength :')
    card_life = input('Enter card life:')
    card_type = input('Enter card card_type (1 for spaceship, 2 for commander):')
    try:
        int(card_strength)
        int(card_life)
        int(card_type)
    except:
        raise ValueError('Wrong input')

    data = [card_name, card_strength, card_life, card_type]

    cur.execute("INSERT INTO cards (card_name, strength, life, card_type) VALUES(?, ?, ?, ?)", data)
    con.commit()
    con.close()

if __name__ == '__main__':
    main()