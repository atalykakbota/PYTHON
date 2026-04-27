import psycopg2              # библиотека для работы с PostgreSQL
import json                  # модуль для работы с JSON
from connect import get_connection  # функция подключения из файла connect.py


def filter_by_group(group_name):
    # выводит контакты, принадлежащие указанной группе
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group_name,))
    for row in cur.fetchall():
        print(row)
    conn.close()


def search_by_email(query):
    # ищет контакты по email (частичное совпадение)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE email ILIKE %s", ('%' + query + '%',))
    for row in cur.fetchall():
        print(row)
    conn.close()


def sort_contacts(by="name"):
    # сортирует контакты по имени, дате рождения или дате добавления
    conn = get_connection()
    cur = conn.cursor()
    allowed = {"name":"c.name","birthday":"c.birthday","date":"c.id"}
    if by not in allowed:
        by = "name"
    cur.execute(f"SELECT * FROM contacts ORDER BY {allowed[by]}")
    for row in cur.fetchall():
        print(row)
    conn.close()


def paginate_contacts(limit=5):
    # постраничный вывод контактов с навигацией (next / prev / quit)
    conn = get_connection()
    cur = conn.cursor()
    offset = 0
    while True:
        cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if not rows:
            print("No more contacts.")
            break
        for r in rows:
            print(r)
        cmd = input("Next / Prev / Quit: ").lower()
        if cmd == "next":
            offset += limit
        elif cmd == "prev" and offset >= limit:
            offset -= limit
        elif cmd == "quit":
            break
    conn.close()


def export_to_json(filename="contacts.json"):
    # экспортирует все контакты (с телефонами и группами) в JSON файл
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               json_agg(json_build_object('number', p.phone, 'type', p.type)) AS phones
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, c.name, c.email, c.birthday, g.name
    """)
    rows = cur.fetchall()
    data = []
    for r in rows:
        data.append({
            "name": r[1],
            "email": r[2],
            "birthday": str(r[3]) if r[3] else None,
            "group": r[4],
            "phones": r[5] if r[5] else []
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    conn.close()


def import_from_json(filename="contacts.json"):
    # импортирует контакты из JSON файла в базу данных
    conn = get_connection()
    cur = conn.cursor()
    with open(filename) as f:
        data = json.load(f)

    for contact in data:
        # проверяем наличие группы
        cur.execute("SELECT id FROM groups WHERE name=%s", (contact["group"],))
        g = cur.fetchone()
        if not g:
            cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (contact["group"],))
            g_id = cur.fetchone()[0]
        else:
            g_id = g[0]

        # проверяем наличие контакта
        cur.execute("SELECT id FROM contacts WHERE name=%s", (contact["name"],))
        existing = cur.fetchone()

        if existing:
            choice = input(f"Contact {contact['name']} exists. Skip or overwrite? ").lower()
            if choice == "skip":
                continue
            elif choice == "overwrite":
                # обновляем данные контакта
                cur.execute("UPDATE contacts SET email=%s, birthday=%s, group_id=%s WHERE id=%s",
                            (contact["email"], contact["birthday"], g_id, existing[0]))
                cid = existing[0]

                # удаляем старые телефоны и добавляем новые
                cur.execute("DELETE FROM phones WHERE contact_id=%s", (cid,))
                for ph in contact.get("phones", []):
                    cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES (%s,%s,%s)",
                                (cid, ph["number"], ph["type"]))
        else:
            # создаём новый контакт
            cur.execute("INSERT INTO contacts(name,email,birthday,group_id) VALUES (%s,%s,%s,%s) RETURNING id",
                        (contact["name"], contact["email"], contact["birthday"], g_id))
            cid = cur.fetchone()[0]

            # добавляем телефоны
            for ph in contact.get("phones", []):
                cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES (%s,%s,%s)",
                            (cid, ph["number"], ph["type"]))

    conn.commit()  # сохраняем изменения
    conn.close()