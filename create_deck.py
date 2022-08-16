import sqlite3

def main():
    """
    Add a new deck to spacegame database
    CREATE TABLE decks (
        deck_id INTEGER,
        card_id INTEGER,
        FOREIGN KEY(card_id) REFERENCES cards(id)
        FOREIGN KEY(deck_id) REFERENCES deck_names(deck_id)
    );
    CREATE TABLE deck_names (
        deck_id INTEGER,
        name TEXT,
        FOREIGN KEY(deck_id) REFERENCES decks(deck_id)
    );
    """
    con = sqlite3.connect('spacegame.db')
    cur = con.cursor()
    action = input("Create deck (1) or fill deck with cards (2)")
    try:
        int(action)
    except:
        raise ValueError('Wrong input')
    if int(action) == 1:
        deck_name = input('Enter deck name:')
        if len(deck_name) > 0:
            cur.execute("INSERT INTO deck_names (name) VALUES(?)", (deck_name,))
            con.commit()
    if int(action) == 2:
        for deck in cur.execute("SELECT * FROM deck_names"):
            print(deck)
        deck_id = input('Choose deck id:')
        try:
            cur.execute("SELECT deck_id FROM deck_names WHERE deck_id = (?)",  (int(deck_id),))
        except:
            raise ValueError('Deck not found')
        for card in cur.execute("SELECT * FROM cards"):
            print(card)

        card_id = input('Enter card id:')
        try:
            cur.execute("SELECT id FROM cards WHERE id = (?)",  (int(card_id),))
        except:
            raise ValueError('Card not found')


    cur.execute("INSERT INTO decks VALUES(?, ?)", (deck_id, card_id))
    con.commit()
    con.close()

if __name__ == '__main__':
    main()