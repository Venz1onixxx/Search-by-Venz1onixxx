#!/usr/bin/env python3
"""
Search accounts in social networks
Поиск аккаунтов в соцсетях
Author: Venz1onixxx
Версия: 1.1.1
"""

import sys
from datetime import datetime
from colorama import init, Fore, Style
import locale

# Инициализация colorama для цветного вывода
init(autoreset=True)

# Словари для перевода
TEXTS = {
    'ru': {
        'title': 'ПОИСК АККАУНТОВ В СОЦСЕТЯХ',
        'by': 'by Venz1onixxx',
        'tiktok_author': 'Мой TikTok: @venz1onixxx_python',
        'search_for': 'Ищем аккаунты для:',
        'time': 'Время:',
        'main_social': 'Основные соцсети:',
        'extra_platforms': 'Дополнительные платформы:',
        'messengers': 'Мессенджеры:',
        'gaming': 'Игровые платформы:',
        'total': 'Всего:',
        'platforms': 'платформ',
        'instruction': 'Просто переходите по ссылкам и проверяйте',
        'menu_show': 'Показать ссылки',
        'menu_save': 'Сохранить в файл',
        'menu_lang': 'Сменить язык',
        'menu_author': 'Ссылка на автора',
        'menu_exit': 'Выход',
        'choice': 'Выбор:',
        'enter_username': 'Введите юзернейм:',
        'no_username': 'Введите юзернейм',
        'saved': 'Ссылки сохранены в файл:',
        'exit': 'Выход...',
        'again': 'Еще раз? (да/нет):',
        'wrong_choice': 'Неверный выбор',
        'stopped': 'Остановлено',
        'error': 'Ошибка:',
        'change_lang': 'Выберите язык / Select language:',
        'lang_ru': 'Русский',
        'lang_en': 'English',
        'lang_changed': 'Язык изменен на русский',
        'links_for': 'Ссылки для юзернейма:',
        'date': 'Дата:',
        'author_title': 'Автор инструмента:',
        'author_tiktok': 'TikTok автора:',
        'author_instagram': 'Instagram автора:',
        'author_github': 'GitHub автора:',
        'social_names': {
            'Instagram': 'Instagram',
            'Telegram': 'Telegram',
            'ВКонтакте': 'ВКонтакте',
            'Twitter/X': 'Twitter/X',
            'Facebook': 'Facebook',
            'GitHub': 'GitHub',
            'Steam': 'Steam',
            'Reddit': 'Reddit',
            'YouTube': 'YouTube',
            'TikTok': 'TikTok',
            'LinkedIn': 'LinkedIn',
            'Pinterest': 'Pinterest',
            'Twitch': 'Twitch',
            'OnlyFans': 'OnlyFans',
            'Spotify': 'Spotify',
            'Discord': 'Discord',
            'Tumblr': 'Tumblr',
            'Snapchat': 'Snapchat',
            'Flickr': 'Flickr',
            'SoundCloud': 'SoundCloud',
            'WhatsApp': 'WhatsApp',
            'Viber': 'Viber',
            'Skype': 'Skype',
            'Signal': 'Signal',
            'Epic Games': 'Epic Games',
            'Origin': 'Origin',
            'Ubisoft': 'Ubisoft',
            'Battle.net': 'Battle.net',
            'Xbox': 'Xbox',
            'PSN': 'PSN'
        }
    },
    'en': {
        'title': 'SEARCH ACCOUNTS IN SOCIAL NETWORKS',
        'by': 'by Venz1onixxx',
        'tiktok_author': 'My TikTok: @venz1onixxx_python',
        'search_for': 'Searching accounts for:',
        'time': 'Time:',
        'main_social': 'Main social networks:',
        'extra_platforms': 'Additional platforms:',
        'messengers': 'Messengers:',
        'gaming': 'Gaming platforms:',
        'total': 'Total:',
        'platforms': 'platforms',
        'instruction': 'Just follow the links and check',
        'menu_show': 'Show links',
        'menu_save': 'Save to file',
        'menu_lang': 'Change language',
        'menu_author': 'Author link',
        'menu_exit': 'Exit',
        'choice': 'Choice:',
        'enter_username': 'Enter username:',
        'no_username': 'Enter username',
        'saved': 'Links saved to file:',
        'exit': 'Exit...',
        'again': 'Again? (yes/no):',
        'wrong_choice': 'Wrong choice',
        'stopped': 'Stopped',
        'error': 'Error:',
        'change_lang': 'Select language:',
        'lang_ru': 'Russian',
        'lang_en': 'English',
        'lang_changed': 'Language changed to English',
        'links_for': 'Links for username:',
        'date': 'Date:',
        'author_title': 'Tool author:',
        'author_tiktok': 'Author TikTok:',
        'author_instagram': 'Author Instagram:',
        'author_github': 'Author GitHub:',
        'social_names': {
            'Instagram': 'Instagram',
            'Telegram': 'Telegram',
            'ВКонтакте': 'VKontakte',
            'Twitter/X': 'Twitter/X',
            'Facebook': 'Facebook',
            'GitHub': 'GitHub',
            'Steam': 'Steam',
            'Reddit': 'Reddit',
            'YouTube': 'YouTube',
            'TikTok': 'TikTok',
            'LinkedIn': 'LinkedIn',
            'Pinterest': 'Pinterest',
            'Twitch': 'Twitch',
            'OnlyFans': 'OnlyFans',
            'Spotify': 'Spotify',
            'Discord': 'Discord',
            'Tumblr': 'Tumblr',
            'Snapchat': 'Snapchat',
            'Flickr': 'Flickr',
            'SoundCloud': 'SoundCloud',
            'WhatsApp': 'WhatsApp',
            'Viber': 'Viber',
            'Skype': 'Skype',
            'Signal': 'Signal',
            'Epic Games': 'Epic Games',
            'Origin': 'Origin',
            'Ubisoft': 'Ubisoft',
            'Battle.net': 'Battle.net',
            'Xbox': 'Xbox',
            'PSN': 'PSN'
        }
    }
}


class SearchTool:
    def __init__(self, lang='ru'):
        self.lang = lang
        self.t = TEXTS[lang]

    def banner(self):
        """Показывает баннер / Shows banner"""
        return f"""
{Fore.RED}╔══════════════════════════════════════════════════════════╗
{Fore.RED}║                                                          ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗   {Fore.RED}    ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║   {Fore.RED}    ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ███████╗█████╗  ███████║██████╔╝██║     ███████║   {Fore.RED}    ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║   {Fore.RED}    ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║   {Fore.RED}    ║
{Fore.RED}║    {Style.BRIGHT}{Fore.WHITE} ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   {Fore.RED}    ║
{Fore.RED}║                                                          ║
{Fore.RED}║            {Style.BRIGHT}{Fore.CYAN}{self.t['title']:<40} {Fore.RED}║
{Fore.RED}║                 {Style.BRIGHT}{Fore.YELLOW}{self.t['by']:<40} {Fore.RED}║
{Fore.RED}║            {Style.BRIGHT}{Fore.MAGENTA}{self.t['tiktok_author']:<40} {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════════════════════╝
"""

    def show_author_info(self):
        """Показывает информацию об авторе / Shows author info"""
        print(self.banner())
        print(f"\n{Fore.CYAN}{'=' * 60}")
        print(f"{Fore.YELLOW}✨ {self.t['author_title']}")
        print(f"{Fore.CYAN}{'=' * 60}\n")

        author_links = [
            (f"{Fore.YELLOW}[1] {Fore.MAGENTA}{self.t['author_tiktok']}", "https://tiktok.com/@venz1onixxx_python"),
            (f"{Fore.YELLOW}[2] {Fore.MAGENTA}{self.t['author_instagram']}", "https://instagram.com/venz1onixxx"),
            (f"{Fore.YELLOW}[3] {Fore.WHITE}{self.t['author_github']}", "https://github.com/venz1onixxx"),
        ]

        for label, url in author_links:
            print(f"{label}")
            print(f"    {Fore.WHITE}URL: {Fore.BLUE}{url}")

        print(f"\n{Fore.YELLOW}💡 Подписывайтесь для новых инструментов!")
        print(f"{Fore.YELLOW}💡 Follow for more tools!")
        print(f"{Fore.CYAN}{'=' * 60}")

        input(f"\n{Fore.YELLOW}[?] Нажмите Enter чтобы вернуться... ")

    def show_links(self, username):
        """Показывает ссылки / Shows links"""
        print(self.banner())
        print(f"{Fore.YELLOW}[*] {self.t['search_for']} {Fore.GREEN}{username}")
        print(f"{Fore.YELLOW}[*] {self.t['time']} {datetime.now().strftime('%H:%M:%S')}")
        print(f"{Fore.YELLOW}[*]{'=' * 60}\n")

        # Основные соцсети / Main social networks
        print(f"{Fore.CYAN}{self.t['main_social']}")
        print(f"{Fore.CYAN}{'-' * 40}")

        social_links = [
            (f"{Fore.YELLOW}[1]  {Fore.MAGENTA}{self.t['social_names']['Instagram']}",
             f"https://instagram.com/{username}"),
            (f"{Fore.YELLOW}[2]  {Fore.CYAN}{self.t['social_names']['Telegram']}", f"https://t.me/{username}"),
            (f"{Fore.YELLOW}[3]  {Fore.BLUE}{self.t['social_names']['ВКонтакте']}", f"https://vk.com/{username}"),
            (f"{Fore.YELLOW}[4]  {Fore.CYAN}{self.t['social_names']['Twitter/X']}", f"https://twitter.com/{username}"),
            (f"{Fore.YELLOW}[5]  {Fore.BLUE}{self.t['social_names']['Facebook']}", f"https://facebook.com/{username}"),
            (f"{Fore.YELLOW}[6]  {Fore.WHITE}{self.t['social_names']['GitHub']}", f"https://github.com/{username}"),
            (f"{Fore.YELLOW}[7]  {Fore.BLUE}{self.t['social_names']['Steam']}",
             f"https://steamcommunity.com/id/{username}"),
            (f"{Fore.YELLOW}[8]  {Fore.RED}{self.t['social_names']['Reddit']}", f"https://reddit.com/user/{username}"),
            (f"{Fore.YELLOW}[9]  {Fore.RED}{self.t['social_names']['YouTube']}", f"https://youtube.com/@{username}"),
            (f"{Fore.YELLOW}[10] {Fore.CYAN}{self.t['social_names']['TikTok']}", f"https://tiktok.com/@{username}"),
        ]

        for label, url in social_links:
            print(f"{label}")
            print(f"    {Fore.WHITE}URL: {Fore.BLUE}{url}")

        # Дополнительные платформы / Additional platforms
        print(f"\n{Fore.CYAN}{self.t['extra_platforms']}")
        print(f"{Fore.CYAN}{'-' * 40}")

        extra_links = [
            (f"{Fore.YELLOW}[11] {Fore.BLUE}{self.t['social_names']['LinkedIn']}",
             f"https://linkedin.com/in/{username}"),
            (f"{Fore.YELLOW}[12] {Fore.RED}{self.t['social_names']['Pinterest']}", f"https://pinterest.com/{username}"),
            (f"{Fore.YELLOW}[13] {Fore.BLUE}{self.t['social_names']['Twitch']}", f"https://twitch.tv/{username}"),
            (f"{Fore.YELLOW}[14] {Fore.MAGENTA}{self.t['social_names']['OnlyFans']}",
             f"https://onlyfans.com/{username}"),
            (f"{Fore.YELLOW}[15] {Fore.GREEN}{self.t['social_names']['Spotify']}",
             f"https://open.spotify.com/user/{username}"),
            (f"{Fore.YELLOW}[16] {Fore.BLUE}{self.t['social_names']['Discord']}",
             f"https://discord.com/users/{username}"),
            (f"{Fore.YELLOW}[17] {Fore.MAGENTA}{self.t['social_names']['Tumblr']}", f"https://{username}.tumblr.com"),
            (f"{Fore.YELLOW}[18] {Fore.RED}{self.t['social_names']['Snapchat']}",
             f"https://snapchat.com/add/{username}"),
            (f"{Fore.YELLOW}[19] {Fore.BLUE}{self.t['social_names']['Flickr']}",
             f"https://flickr.com/people/{username}"),
            (f"{Fore.YELLOW}[20] {Fore.GREEN}{self.t['social_names']['SoundCloud']}",
             f"https://soundcloud.com/{username}"),
        ]

        for label, url in extra_links:
            print(f"{label}")
            print(f"    {Fore.WHITE}URL: {Fore.BLUE}{url}")

        # Мессенджеры / Messengers
        print(f"\n{Fore.CYAN}{self.t['messengers']}")
        print(f"{Fore.CYAN}{'-' * 40}")

        messenger_links = [
            (f"{Fore.YELLOW}[21] {Fore.GREEN}{self.t['social_names']['WhatsApp']}", f"https://wa.me/{username}"),
            (f"{Fore.YELLOW}[22] {Fore.BLUE}{self.t['social_names']['Viber']}", f"viber://chat?number={username}"),
            (f"{Fore.YELLOW}[23] {Fore.BLUE}{self.t['social_names']['Skype']}", f"skype:{username}?chat"),
            (f"{Fore.YELLOW}[24] {Fore.CYAN}{self.t['social_names']['Signal']}", f"signal.me/#p/{username}"),
        ]

        for label, url in messenger_links:
            print(f"{label}")
            print(f"    {Fore.WHITE}URL: {Fore.BLUE}{url}")

        # Игровые платформы / Gaming platforms
        print(f"\n{Fore.CYAN}{self.t['gaming']}")
        print(f"{Fore.CYAN}{'-' * 40}")

        game_links = [
            (f"{Fore.YELLOW}[25] {Fore.GREEN}{self.t['social_names']['Epic Games']}",
             f"https://epicgames.com/account/{username}"),
            (f"{Fore.YELLOW}[26] {Fore.RED}{self.t['social_names']['Origin']}", f"https://origin.com/{username}"),
            (f"{Fore.YELLOW}[27] {Fore.GREEN}{self.t['social_names']['Ubisoft']}",
             f"https://ubisoft.com/user/{username}"),
            (f"{Fore.YELLOW}[28] {Fore.BLUE}{self.t['social_names']['Battle.net']}", f"https://battle.net/{username}"),
            (f"{Fore.YELLOW}[29] {Fore.BLUE}{self.t['social_names']['Xbox']}",
             f"https://xboxgamertag.com/search/{username}"),
            (f"{Fore.YELLOW}[30] {Fore.BLUE}{self.t['social_names']['PSN']}", f"https://psnprofiles.com/{username}"),
        ]

        for label, url in game_links:
            print(f"{label}")
            print(f"    {Fore.WHITE}URL: {Fore.BLUE}{url}")

        print(f"\n{Fore.YELLOW}[*]{'=' * 60}")
        print(f"{Fore.YELLOW}[*] {self.t['total']} 30 {self.t['platforms']}")
        print(f"{Fore.YELLOW}[*] {self.t['instruction']}")
        print(f"{Fore.YELLOW}[*]{'=' * 60}")

        # Добавляем ссылку на автора в конце
        print(f"\n{Fore.MAGENTA}💻 Автор: Venz1onixxx")
        print(f"{Fore.MAGENTA}📱 TikTok: https://tiktok.com/@venz1onixxx_python")

    def save_to_file(self, username):
        """Сохраняет ссылки в файл / Saves links to file"""
        filename = f"links_{username}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=" * 60 + "\n")
            f.write(f"{self.t['links_for']} {username}\n")
            f.write(f"{self.t['date']} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"=" * 60 + "\n\n")

            # Все ссылки / All links
            links = [
                (self.t['social_names']['Instagram'], f"https://instagram.com/{username}"),
                (self.t['social_names']['Telegram'], f"https://t.me/{username}"),
                (self.t['social_names']['ВКонтакте'], f"https://vk.com/{username}"),
                (self.t['social_names']['Twitter/X'], f"https://twitter.com/{username}"),
                (self.t['social_names']['Facebook'], f"https://facebook.com/{username}"),
                (self.t['social_names']['GitHub'], f"https://github.com/{username}"),
                (self.t['social_names']['Steam'], f"https://steamcommunity.com/id/{username}"),
                (self.t['social_names']['Reddit'], f"https://reddit.com/user/{username}"),
                (self.t['social_names']['YouTube'], f"https://youtube.com/@{username}"),
                (self.t['social_names']['TikTok'], f"https://tiktok.com/@{username}"),
                (self.t['social_names']['LinkedIn'], f"https://linkedin.com/in/{username}"),
                (self.t['social_names']['Pinterest'], f"https://pinterest.com/{username}"),
                (self.t['social_names']['Twitch'], f"https://twitch.tv/{username}"),
                (self.t['social_names']['OnlyFans'], f"https://onlyfans.com/{username}"),
                (self.t['social_names']['Spotify'], f"https://open.spotify.com/user/{username}"),
                (self.t['social_names']['Discord'], f"https://discord.com/users/{username}"),
                (self.t['social_names']['Tumblr'], f"https://{username}.tumblr.com"),
                (self.t['social_names']['Snapchat'], f"https://snapchat.com/add/{username}"),
                (self.t['social_names']['Flickr'], f"https://flickr.com/people/{username}"),
                (self.t['social_names']['SoundCloud'], f"https://soundcloud.com/{username}"),
                (self.t['social_names']['WhatsApp'], f"https://wa.me/{username}"),
                (self.t['social_names']['Viber'], f"viber://chat?number={username}"),
                (self.t['social_names']['Skype'], f"skype:{username}?chat"),
                (self.t['social_names']['Signal'], f"signal.me/#p/{username}"),
                (self.t['social_names']['Epic Games'], f"https://epicgames.com/account/{username}"),
                (self.t['social_names']['Origin'], f"https://origin.com/{username}"),
                (self.t['social_names']['Ubisoft'], f"https://ubisoft.com/user/{username}"),
                (self.t['social_names']['Battle.net'], f"https://battle.net/{username}"),
                (self.t['social_names']['Xbox'], f"https://xboxgamertag.com/search/{username}"),
                (self.t['social_names']['PSN'], f"https://psnprofiles.com/{username}"),
            ]

            for name, url in links:
                f.write(f"[{name}]\n")
                f.write(f"URL: {url}\n")
                f.write(f"-" * 40 + "\n")

            # Добавляем информацию об авторе
            f.write(f"\n{'=' * 60}\n")
            f.write("АВТОР ИНСТРУМЕНТА / TOOL AUTHOR:\n")
            f.write(f"{'=' * 60}\n")
            f.write("Venz1onixxx\n")
            f.write("TikTok: https://tiktok.com/@venz1onixxx_python\n")
            f.write("Instagram: https://instagram.com/venz1onixxx\n")
            f.write("GitHub: https://github.com/venz1onixxx\n")

        return filename

    def change_language(self):
        """Меняет язык / Changes language"""
        print(f"\n{Fore.CYAN}{self.t['change_lang']}")
        print(f"{Fore.YELLOW}[1] {TEXTS['ru']['lang_ru']} (Russian)")
        print(f"{Fore.YELLOW}[2] {TEXTS['en']['lang_en']} (English)")

        lang_choice = input(f"\n{Fore.YELLOW}[?] {self.t['choice']} {Fore.GREEN}").strip()

        if lang_choice == '1':
            self.lang = 'ru'
            self.t = TEXTS['ru']
            print(f"{Fore.GREEN}[+] {self.t['lang_changed']}")
        elif lang_choice == '2':
            self.lang = 'en'
            self.t = TEXTS['en']
            print(f"{Fore.GREEN}[+] {self.t['lang_changed']}")
        else:
            print(f"{Fore.RED}[!] {self.t['wrong_choice']}")

        return self.lang

    def main_menu(self):
        """Главное меню / Main menu"""
        print(self.banner())

        while True:
            print(f"\n{Fore.YELLOW}[1] {self.t['menu_show']}")
            print(f"{Fore.YELLOW}[2] {self.t['menu_save']}")
            print(f"{Fore.YELLOW}[3] {self.t['menu_lang']}")
            print(f"{Fore.YELLOW}[4] {self.t['menu_author']}")
            print(f"{Fore.YELLOW}[5] {self.t['menu_exit']}")

            choice = input(f"\n{Fore.YELLOW}[?] {self.t['choice']} {Fore.GREEN}").strip()

            if choice == '5':
                print(f"{Fore.YELLOW}[*] {self.t['exit']}")
                print(f"{Fore.MAGENTA}[*] Подписывайтесь: https://tiktok.com/@venz1onixxx_python")
                break

            elif choice == '4':
                self.show_author_info()
                print(self.banner())
                continue

            elif choice == '3':
                self.change_language()
                print(self.banner())
                continue

            elif choice in ['1', '2']:
                username = input(f"{Fore.YELLOW}[?] {self.t['enter_username']} {Fore.GREEN}").strip()

                if not username:
                    print(f"{Fore.RED}[!] {self.t['no_username']}")
                    continue

                if choice == '1':
                    self.show_links(username)
                else:
                    filename = self.save_to_file(username)
                    print(f"{Fore.GREEN}[+] {self.t['saved']} {filename}")

                again = input(f"\n{Fore.YELLOW}[?] {self.t['again']} {Fore.GREEN}").lower().strip()
                if self.lang == 'ru':
                    if again not in ['да', 'yes', 'y', 'д']:
                        print(f"{Fore.YELLOW}[*] {self.t['exit']}")
                        print(f"{Fore.MAGENTA}[*] Подписывайтесь: https://tiktok.com/@venz1onixxx_python")
                        break
                else:
                    if again not in ['yes', 'y', 'да', 'д']:
                        print(f"{Fore.YELLOW}[*] {self.t['exit']}")
                        print(f"{Fore.MAGENTA}[*] Follow: https://tiktok.com/@venz1onixxx_python")
                        break

            else:
                print(f"{Fore.RED}[!] {self.t['wrong_choice']}")


def detect_language():
    """Определяет язык системы без устаревших функций"""
    try:
        # Пробуем получить локаль
        current_locale = locale.getlocale()

        if current_locale and current_locale[0]:
            lang_code = current_locale[0].lower()
            if 'ru' in lang_code:
                return 'ru'

        # Если не получилось определить, пробуем через переменные окружения
        import os
        env_lang = os.environ.get('LANG', '').lower()
        if 'ru' in env_lang:
            return 'ru'

        # По умолчанию английский
        return 'en'

    except:
        # В случае ошибки - английский по умолчанию
        return 'en'


def main():
    """Главная функция / Main function"""
    # Определяем язык системы без устаревших функций
    default_lang = detect_language()

    tool = SearchTool(default_lang)

    try:
        tool.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] {tool.t['stopped']}")
        print(f"{Fore.MAGENTA}[*] TikTok автора: https://tiktok.com/@venz1onixxx_python")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] {tool.t['error']} {e}")
        print(f"{Fore.MAGENTA}[*] Автор: https://tiktok.com/@venz1onixxx_python")
        sys.exit(1)


if __name__ == "__main__":
    main()