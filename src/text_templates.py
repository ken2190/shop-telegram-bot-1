from settings import Settings

settings = Settings()

line_separator = "➖➖➖➖➖"


# Multiple lines
def get_profile_template(user):
    return f"{line_separator}\n📝 id: {user.get_id()}\n📈 Number of orders: {len(user.get_orders())}\n📅 Date of registration: {user.get_register_date_string()}\n{line_separator}"

def get_faq_template(shop_name):
    return f"{line_separator}\nℹ️ FAQ shop {shop_name}\n{line_separator}"

def get_categories_template():
    return f"{line_separator}\n🛍️ Categories\n{line_separator}"

def get_category_was_created_successfuly(cat_name):
    return f"The category {cat_name} was created successfully."

def get_category_data(cat):
    return f"{line_separator}\nID: {cat.get_id()}\nName: {cat.get_name()}\n{line_separator}"

def get_item_card(item=None, name=None, price=None, desc=None, amount=None):
    if item:
        name = item.get_name()
        price = item.get_price()
        desc = item.get_desc()
        amount = item.get_amount()
        
    return f"{line_separator}\n{name} - {'{:.2f}'.format(price)} usd\nIn stock: {amount} pcs.\n{line_separator}\n{desc}"

def get_order_confirmation_template(item_amount_dict, cart_price, email_adress, additional_message, phone_number=None, home_adress=None):
    item_amount_dict_formatted = '\n'.join([f'\t· {item[0].get_name()} - {item[1]} шт.' for item in item_amount_dict])
    phone_number = f"Phone number: {phone_number}\n" if phone_number else ""
    home_adress = f"Delivery address: {home_adress}\n" if home_adress else ""
    return f"{line_separator}\nItem:\n{item_amount_dict_formatted}\nSum: {cart_price}usd.\nEmail: {email_adress}\n{phone_number}{home_adress}Comment to the order: {additional_message}\n{line_separator}\nAre you sure you want to place an order?"
    
def get_order_template(order):
    item_list_amount_formatted = '\n'.join([f'\t· {item[0].get_name()} - {item[1]} шт.' for item in order.get_item_list_amount()])
    phone_number = f"Phone number: {order.get_phone_number()}\n" if settings.is_phone_number_enabled() else ""
    home_adress = f"Delivery address: {order.get_home_adress()}\n" if settings.is_delivery_enabled() else f"Pickup\n"
    return f"{line_separator}\nID order: {order.get_order_id()}\nID user: {order.get_user_id()}\nItem:\n{item_list_amount_formatted}\nSum: {order.get_item_list_price()}usd.\nEmail: {order.get_email_adress()}\n{phone_number}{home_adress}Order comment: {order.get_additional_message()}\nOrder status: {order.get_status_string()}\ndate: {order.get_date_string()}\n{line_separator}"

# Single phrases
# /start
admin_panel = "🔴 Admin Panel"
faq = "ℹ️ FAQ"
profile = "📁 Profile"
catalogue = "🗄️ Catalog"
cart = "🛒 Cart"
support_menu = "☎ Support Menu"

# Admin panel tabs
item_management = "📦 Item Management"
user_management = "🧍 User Management"
shop_stats = "📈 Store Statistics (BETA)"
bot_settings = "⚙ Bot settings"

# FAQ
contacts = "📞 Contacts"
refund = "🎫 Refund Policy"

# Profile
my_orders = "📂 My Orders"
cancel_order = "❌ Cancel order"
restore_order = "✅ Restore order"
my_support_tickets = "🙋 My support tickets"
enable_notif = "🔔Enable order notifications"
disable_notif = "🔕Turn off order notifications"

# Catalogue / Item / Cart
search = "🔍 Find"
add_to_cart = "🛒 Add to Cart"
cart_is_empty = "Cart is empty."
pickup = "✅Pickup"
def delivery_on(price): return f"✅ Delivery - {price}usd."
def delivery_off(price): return f"❌ Delivery - {price}usd."
cart_checkout = "Checkout"
clear_cart = "Clear Cart"
processing = "Processing"
delivery = "Awaiting delivery"
done = "Ready"
cancelled = "Cancelled"

# Item management
add_cat = "🛍️ Add Category"
add_item = "🗃️ Add Item"
edit_cat = "✏️ Edit Category"
edit_item = "✏️ Edit Item"
change_name = "📋 Change Name"
change_image = "🖼️ Change Image"
hide_image = "🙈 Hide Image"
show_image = "🐵 Show Image"
change_desc = "📝 Change Description"
change_price = "🏷️ Change Price"
change_item_cat = "🛍️ Change Category"
change_stock = "📦 Change Stock"

# User management
user_profile = "📁User Profile"
notify_everyone = "🔔Notify all users"
orders = "📁 Orders"
remove_manager_role = "👨‍💼 Remove manager role"
add_manager_role = "👨‍💼 Make Manager"
remove_admin_role = "🔴 Remove admin role"
add_admin_role = "🔴 Make Admin"
def change_order_status(status): return f"Change status to \"{status}\""

# Shop stats
registration_stats = "👥 Registration Statistics"
order_stats = "📦 Order Statistics"
all_time = "All time"
monthly = "Last 30 days"
weekly = "Last 7 days"
daily = "Last 24 hours"

# Shop settings
main_settings = "🛠️ Main Settings"
item_settings = "🗃️ Item Settings"
additional_settings = "📖 Additional Settings"
custom_commands = "📖 Commands"
add_command = "📝 Add Command"
clean_logs = "📖 Clean Logs"
clean_logs_text = "⚠️ Are you sure you want to clean the logs? They will be permanently deleted!\n(Today's logs will not be deleted)"
backups = "💾 Backup"
update_backup = "🔄 Update Backup"
load_backup = "💿 Load Backup"
clean_backups = "🧹 Cleanup Backups"
system_settings = "💻 System"
clean_images = "🗑️ Delete Unused Images"
clean_images_text = "⚠️ Are you sure you want to delete unused images? They will be permanently deleted!"
clean_database = "📚 Clean Database"
clean_database_text = "⚠️ Are you sure you want to clean the database? All data will be permanently deleted!"
reset_settings = "⚙️ Reset Settings"
reset_settings_text = "⚠️ Are you sure you want to reset your settings? All data will be permanently deleted!"
disable_item_image = "✅ Product Images"
enable_item_image = "❌ Product Images"
checkout_settings = "💳 Checkout Settings"
stats_settings = "📈 Statistics Settings"
graph_color = "🌈 Graph Color"
border_width = "🔲 Stroke Width"
title_font_size = "ℹ️ Graph title size"
axis_font_size = "↔️Axis text size"
tick_font_size = "🔢Tick Text Size"
unavailable = "⛔️"
minus = "➖"
plus = "➕"
enable_sticker = "❌ Welcome Sticker"
disable_sticker = "✅ Welcome Sticker"
enable_phone_number = "❌ Order phone number"
disable_phone_number = "✅ Order phone number"
enable_delivery = "❌ Delivery"
disable_delivery = "✅ Delivery"
def delivery_price(price): return f"🚚 Shipping cost: {price}usd."
enable_captcha = "❌ CAPTCHA on order"
disable_captcha = "✅ CAPTCHA on order"
enable_debug = "❌ Debug mode"
disable_debug = "✅ Debug mode"

# Manager tab
view_order = "📂 View Order"

# Misc buttons
skip = "⏭ Skip"
back = "🔙 back"
confirm = "✅ Yes"
deny = "❌ No"
error = "An error has occurred!"
or_press_back = "or press the \"Back\" button."
hide = "🙈 Hide"
show = "🐵 Show"
delete = "❌ Delete"
reset = "❌ Reset"

if __name__ == "__main__":
    print(delivery_on)
