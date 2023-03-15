from os import system, name, remove, mkdir, rmdir, listdir
from os.path import exists

import sqlite3


def clearConsole():
    system("cls" if name in ("nt", "dos") else "clear")

def create_config(token, main_admin_id, config_path="config.ini"):
    DEFAULT_CONFIG_TEXT = f"""[main_settings]
token = {token}
mainadminid = {main_admin_id}
debug = 0

[shop_settings]
name = Store name
greeting = Welcome!
refundpolicy = Text for "Refund Policy" tab
contacts = Text for the "Contacts" tab
enableimage = 1
enablesticker = 0
enablephonenumber = 0
enabledelivery = 0
delivery_price = 0.0
enablecaptcha = 1

[stats_settings]
barcolor = 3299ff
borderwidth = 1
titlefontsize = 20
axisfontsize = 12
tickfontsize = 8
"""
    with open(config_path, "w") as config:
        config.write(DEFAULT_CONFIG_TEXT)


CREATE_CATS_TEXT = """
CREATE TABLE "cats" (
	"id" INTEGER,
	"name" TEXT NOT NULL,
	PRIMARY KEY("id")
)
"""
CREATE_ITEMS_TEXT = """
CREATE TABLE "items" (
	"id" INTEGER,
	"name" TEXT NOT NULL,
	"price" FLOAT NOT NULL,
	"cat_id" INTEGER NOT NULL,
	"desc" TEXT,
	"active" INTEGER,
	"amount" INTEGER,
	"image_id" INTEGER,
    "hide_image" INTEGER,
	PRIMARY KEY("id")
)
"""
CREATE_ORDERS_TEXT = """
CREATE TABLE "orders" (
	"order_id" INTEGER,
	"user_id" INTEGER,
	"item_list" TEXT,
	"email_adress" TEXT,
	"phone_number" TEXT,
	"home_adress" TEXT,
	"additional_message" TEXT,
	"date" TEXT,
    "status" INTEGER
    )
"""
CREATE_USERS_TEXT = """
CREATE TABLE "users" (
	"user_id" INTEGER NOT NULL,
	"is_admin" INTEGER,
	"is_manager" INTEGER,
	"notification" INTEGER,
	"date_created" TEXT,
    "cart" TEXT, 
    "cart_delivery" INTEGER
)
"""
CREATE_COMMANDS_TEXT = """
CREATE TABLE "commands" (
    "id" INTEGER NOT NULL,
    "command" TEXT,
    "response" TEXT,
    PRIMARY KEY("id")
)
"""

def create_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(CREATE_CATS_TEXT)
    c.execute(CREATE_ITEMS_TEXT)
    c.execute(CREATE_ORDERS_TEXT)
    c.execute(CREATE_USERS_TEXT)
    c.execute(CREATE_COMMANDS_TEXT)
    conn.commit()
    conn.close()    


if __name__ == "__main__":
    clearConsole()
    if any(list(map(exists, ["config.ini", "images", "data.db"]))):
        while True:
            confirmation = input("Are you sure you want to rerun the installation process? All data will be lost! (y/N) ")
            if confirmation.lower() in ["y", "yes", "n", "no", ""]:
                break
    else:
        confirmation = "y"


    if confirmation.lower() in ["y", "yes"]:
        print("You can learn how to get a bot token by following the link: https://youtu.be/fyISLEvzIec")
        token = input("Enter bot token: ")
        print("You can get your ID by writing \"/start\" to @userinfobot")
        main_admin_id = input("Enter the main admin ID: ")
        if main_admin_id.isalnum():
            if exists("data.db"):
                remove("data.db")
                print("The database has been deleted.")
            create_db()
            print("The database has been created.")
            if exists("config.ini"):
                remove("config.ini")
                print("Settings file has been deleted.")
            create_config(token, main_admin_id)
            print("Settings file has been created.")
            if exists("images"):
                for file in listdir("images"):
                    remove("images/" + file)
                rmdir("images")
                print("The \"images\" folder has been deleted.")
            mkdir("images")
            print("The \"images\" folder has been created.")
            if exists("backups"):
                for folder in listdir("backups"):
                    for file in listdir("backups/" + folder):
                        remove(f"backups/{folder}/{file}")
                    rmdir(f"backups/{folder}")
                rmdir("backups")
                print("The \"backups\" folder has been deleted.")
            mkdir("backups")
            print("The folder \"backups\" has been created.")
        else:
            print("Invalid main admin ID.")
    else:
        print("The installation was canceled.")


    input("Press ENTER to continue...")
