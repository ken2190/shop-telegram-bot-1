from settings import Settings

settings = Settings()

line_separator = "➖➖➖➖➖➖➖➖➖➖"


# Multiple lines
def get_profile_template(user):
    return f"{line_separator}\n📝 id: {user.get_id()}\n📈 Кол-во заказов: {len(user.get_orders())}\n📅 Дата регистрации: {user.get_register_date()}\n{line_separator}"

def get_faq_template(shop_name):
    return f"{line_separator}\nℹ️ FAQ магазина {shop_name}\n{line_separator}"

def get_categories_template():
    return f"{line_separator}\n🛍️ Категории\n{line_separator}"

def get_category_was_created_successfuly(cat_name):
    return f"Категория {cat_name} была успешно создана."

def get_category_data(cat):
    return f"{line_separator}\nID: {cat.get_id()}\nНазвание: {cat.get_name()}\n{line_separator}"

def get_item_card(item=None, name=None, price=None, desc=None, amount=None):
    if item:
        name = item.get_name()
        price = item.get_price()
        desc = item.get_desc()
        amount = item.get_amount()
        
    return f"{line_separator}\n{name} - {'{:.2f}'.format(price)} руб.\nВ наличии: {amount} шт.\n{line_separator}\n{desc}"

def get_order_confirmation_template(item_amount_dict, cart_price, email_adress, additional_message, phone_number=None, home_adress=None):
    item_amount_dict_formatted = '\n'.join([f'\t· {item[0].get_name()} - {item[1]} шт.' for item in item_amount_dict])
    phone_number = f"Номер телефона: {phone_number}\n" if phone_number else ""
    home_adress = f"Адрес доставки: {home_adress}\n" if home_adress else ""
    return f"{line_separator}\nТовары:\n{item_amount_dict_formatted}\nСумма: {cart_price}руб.\nEmail: {email_adress}\n{phone_number}{home_adress}Комментарий к заказу: {additional_message}\n{line_separator}\nВы уверены, что хотите оформить заказ?"
    
def get_order_template(order):
    item_list_amount_formatted = '\n'.join([f'\t· {item[0].get_name()} - {item[1]} шт.' for item in order.get_item_list_amount()])
    phone_number = f"Номер телефона: {order.get_phone_number()}\n" if settings.is_phone_number_enabled() else ""
    home_adress = f"Адрес доставки: {order.get_home_adress()}\n" if settings.is_home_adress_enabled() else ""
    return f"{line_separator}\nТовары:\n{item_list_amount_formatted}\nСумма: {order.get_item_list_price()}руб.\nEmail: {order.get_email_adress()}\n{phone_number}{home_adress}Комментарий к заказу: {order.get_additional_message()}\nСтатус заказа: {order.get_status_string()}\n{line_separator}"

# Single phrases
# /start
admin_panel = "🔴 Админ панель"
faq = "ℹ️ FAQ"
profile = "📁 Профиль"
catalogue = "🗄️ Каталог"
cart = "🛒 Корзина"
support_menu = "☎ Меню тех. поддержки"

# Admin panel tabs
item_management = "📦 Управление товаром"
user_management = "🧍 Управление пользователями"
shop_stats = "📈 Статистика магазина (BETA)"
bot_settings = "⚙ Настройки бота"

# FAQ
contacts = "📞 Контакты"
refund = "🎫 Политика возврата"

# Profile
my_orders = "📂 Мои заказы"
cancel_order = "❌ Отменить заказ"
restore_order = "✅ Восстановить заказ"
my_support_tickets = "🙋 Мои тикеты в тех. поддержку"
enable_notif = "🔔Включить ововещения о кол-ве товара"
disable_notif = "🔕Выключить ововещения о кол-ве товара"

# Catalogue / Item / Cart
add_to_cart = "🛒 Добавить в корзину"
cart_is_empty = "Корзина пуста."
pickup = "✅Самовывоз"
delivery_on= f"✅Доставка - {'{:.2f}'.format(float(settings.get_delivery_price()))}руб."
delivery_off = f"❌ Доставка - {'{:.2f}'.format(float(settings.get_delivery_price()))}руб."
cart_checkout = "Оформить заказ"
clear_cart = "Отчистить корзину"
processing = "Обрабатывается"
delivery = "Ожидает доставки"
done = "Готов"
cancelled = "Отменён"

# Item management
add_cat = "🛍️ Добавить категорию"
add_item = "🗃️ Добавить товар"
edit_cat = "✏️ Редактировать категорию"
edit_item = "✏️ Редактировать товар"
change_name = "📋 Изменить название"
change_desc = "📝 Изменить описание"
change_price = "🏷️ Изменить цену"
change_item_cat = "🛍️ Изменить категорию"
change_stock = "📦 Изменить кол-во"
hide = "🙈 Скрыть"
show = "🐵Показать"
delete = "❌ Удалить"

# User management
user_profile = "📁Профиль пользователя"
notify_everyone = "🔔Оповещение всем пользователям"
orders = "📁 Заказы"
remove_admin_role = "🔴 Убрать роль администратора"
add_admin_role = "🔴 Сделать администратором"
remove_support_role = "☎️ Убрать роль оператора тех. поддержки"
add_support_role = "☎️ Сделать оператором тех. поддержки"

# Shop stats
registration_stats = "👥Статистика регистраций"
order_stats = "📦Статистика заказов"
all_time = "За всё время"
monthly = "За последние 30 дней"
weekly = "За последние 7 дней"
daily = "За последние 24 часа"

# Shop settings
main_settings = "🛠️ Основные настройки"
checkout_settings = "💳 Настройки оформления заказа"
stats_settings = "📈 Настройки статистики"
graph_color = "🌈 Цвет графика"
border_width = "🔲 Ширина обводки"
title_font_size = "ℹ️ Размер названия графика"
axis_font_size = "↔️Размер текста для осей"
tick_font_size = "🔢Размер текста для делений"
unavailable = "⛔️"
minus = "➖"
plus = "➕"
enable_sticker = "✅ Включить стикер в приветствии"
disable_sticker = "❌ Выключить стикер в приветствии"
enable_phone_number = "✅ Включить номер телефона при заказе"
disable_phone_number = "❌ Выключить номер телефона при заказе"
enable_delivery = "✅ Включить доставку"
disable_delivery = "❌ Выключить доставку"
enable_captcha = "✅ Включить CAPTCHA при заказе"
disable_captcha = "❌ Выключить CAPTCHA при заказе"
enable_debug = "✅ Включить режим отладки"
disable_debug = "❌ Выключить режим отладки"

# Misc buttons
back = "🔙 Назад"
confirm = "✅ Да"
deny = "❌ Нет"
error = "Произошла ошибка!"
