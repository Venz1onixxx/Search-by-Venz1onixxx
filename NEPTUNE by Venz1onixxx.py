"""
Neptune - Инструмент поиска аккаунтов
Автор: Venz1onixxx
TikTok: @venz1onixxx_python
Версия: 1.1
"""

import os
import sys
from datetime import datetime

class Neptune:
    def __init__(self):
        # Включаем цвета в CMD
        os.system('')
        
        # ТОЛЬКО синие цвета для Нептуна
        self.BLUE_DARK = '\033[38;5;27m'      # Темно-синий
        self.BLUE = '\033[94m'                # Синий
        self.CYAN = '\033[96m'                # Голубой
        self.BLUE_LIGHT = '\033[38;5;117m'    # Светло-синий
        self.WHITE = '\033[97m'               # Белый
        self.BOLD = '\033[1m'                 # Жирный
        self.RESET = '\033[0m'                # Сброс
        
    def show_logo(self):
        """Показать синий лого Neptune"""
        os.system('cls')
        
        logo = f"""
{self.BLUE_DARK}{self.BOLD}╔══════════════════════════════════════════════════════════╗
{self.BLUE_DARK}║                                                          ║
{self.BLUE}║    ███╗   ██╗███████╗██████╗ ████████╗██╗   ██╗███╗   ██╗███████╗║
{self.BLUE}║    ████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██╔════╝║
{self.BLUE_LIGHT}║    ██╔██╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██╔██╗ ██║█████╗  ║
{self.BLUE_LIGHT}║    ██║╚██╗██║██╔══╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║██╔══╝  ║
{self.CYAN}║    ██║ ╚████║███████╗██║        ██║   ╚██████╔╝██║ ╚████║███████╗║
{self.CYAN}║    ╚═╝  ╚═══╝╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝║
{self.BLUE_DARK}║                                                          ║
{self.BLUE_DARK}║                ИНСТРУМЕНТ ПОИСКА АККАУНТОВ               ║
{self.WHITE}║                   by Venz1onixxx                          ║
{self.CYAN}║              TikTok: @venz1onixxx_python                  ║
{self.BLUE_DARK}╚══════════════════════════════════════════════════════════╝{self.RESET}
        """
        print(logo)
    
    def printc(self, text, color='white'):
        """Упрощенный вывод цвета"""
        colors = {
            'blue_dark': self.BLUE_DARK,
            'blue': self.BLUE,
            'blue_light': self.BLUE_LIGHT,
            'cyan': self.CYAN,
            'white': self.WHITE
        }
        color_code = colors.get(color, self.WHITE)
        print(f"{color_code}{text}{self.RESET}")
    
    def search(self):
        """Основная функция поиска"""
        self.show_logo()
        
        self.printc("🔍 Neptune - поиск аккаунтов в социальных сетях", 'white')
        self.printc("🌊 Версия 1.1 | Автор: Venz1onixxx", 'cyan')
        self.printc("📱 TikTok: @venz1onixxx_python", 'blue_light')
        self.printc("══════════════════════════════════════════════════", 'blue')
        print()
        
        while True:
            username = input(f"{self.CYAN}🎯 Введите юзернейм (или 'exit' для выхода): {self.WHITE}").strip()
            
            if username.lower() == 'exit':
                self.printc("\n👋 Выход из Neptune...", 'blue')
                break
            
            if not username:
                self.printc("⚠️ Введите юзернейм!", 'blue_light')
                continue
            
            # Показываем результат
            self.show_results(username)
            
            # Спросить продолжить
            choice = input(f"\n{self.CYAN}🔍 Искать другой юзернейм? (да/нет): {self.WHITE}").lower()
            if choice not in ['да', 'yes', 'y', 'д']:
                self.printc("\nСпасибо за использование Neptune!", 'blue')
                break
    
    def show_results(self, username):
        """Показать результаты поиска"""
        print(f"\n{self.BLUE}══════════════════════════════════════════════════{self.RESET}")
        self.printc(f"🌌 Neptune находит аккаунты для: {username}", 'cyan')
        self.printc(f"🕐 Время поиска: {datetime.now().strftime('%H:%M:%S')}", 'blue_light')
        print(f"{self.BLUE}══════════════════════════════════════════════════{self.RESET}\n")
        
        # Список платформ
        platforms = [
            ("🌐 Instagram", f"https://instagram.com/{username}"),
            ("📱 Telegram", f"https://t.me/{username}"),
            ("👥 ВКонтакте", f"https://vk.com/{username}"),
            ("🐦 Twitter/X", f"https://twitter.com/{username}"),
            ("📘 Facebook", f"https://facebook.com/{username}"),
            ("💻 GitHub", f"https://github.com/{username}"),
            ("🎥 YouTube", f"https://youtube.com/@{username}"),
            ("🎵 TikTok", f"https://tiktok.com/@{username}"),
            ("📰 Reddit", f"https://reddit.com/user/{username}"),
            ("🎮 Steam", f"https://steamcommunity.com/id/{username}"),
            ("💼 LinkedIn", f"https://linkedin.com/in/{username}"),
            ("🎬 Twitch", f"https://twitch.tv/{username}"),
            ("🎧 Spotify", f"https://open.spotify.com/user/{username}"),
            ("💬 Discord", f"https://discord.com/users/{username}"),
            ("💚 WhatsApp", f"https://wa.me/{username}"),
            ("📸 Snapchat", f"https://snapchat.com/add/{username}"),
            ("🎨 Pinterest", f"https://pinterest.com/{username}"),
            ("📝 Tumblr", f"https://{username}.tumblr.com"),
            ("🔊 SoundCloud", f"https://soundcloud.com/{username}"),
            ("📷 Flickr", f"https://flickr.com/people/{username}"),
        ]
        
        # Группируем вывод
        self.printc("📊 ОСНОВНЫЕ ПЛАТФОРМЫ:", 'blue_dark')
        print(f"{self.BLUE}──────────────────────────────────────────────────{self.RESET}")
        
        for i in range(0, min(10, len(platforms))):
            name, url = platforms[i]
            print(f"{self.CYAN}[{i+1:2d}] {self.WHITE}{name}")
            print(f"     {self.BLUE}🔗 {url}{self.RESET}")
        
        if len(platforms) > 10:
            print(f"\n{self.BLUE_DARK}📋 ДОПОЛНИТЕЛЬНЫЕ ПЛАТФОРМЫ:{self.RESET}")
            print(f"{self.BLUE}──────────────────────────────────────────────────{self.RESET}")
            
            for i in range(10, len(platforms)):
                name, url = platforms[i]
                print(f"{self.CYAN}[{i+1:2d}] {self.WHITE}{name}")
                print(f"     {self.BLUE}🔗 {url}{self.RESET}")
        
        # Сохраняем в файл
        self.save_results(username, platforms)
        
        print(f"\n{self.BLUE}══════════════════════════════════════════════════{self.RESET}")
        self.printc("📈 Статистика:", 'blue_dark')
        self.printc(f"   • Найдено платформ: {len(platforms)}", 'cyan')
        self.printc(f"   • Юзернейм: {username}", 'blue_light')
        self.printc(f"   • Время: {datetime.now().strftime('%H:%M:%S')}", 'blue_light')
        print(f"{self.BLUE}══════════════════════════════════════════════════{self.RESET}")
    
    def save_results(self, username, platforms):
        """Сохранить результаты в файл - ИСПРАВЛЕННАЯ ВЕРСИЯ"""
        try:
            filename = f"neptune_{username}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write(f"Neptune - Результаты поиска\n")
                f.write(f"Юзернейм: {username}\n")
                f.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                for name, url in platforms:
                    f.write(f"{name}\n")
                    f.write(f"URL: {url}\n")
                    f.write("-" * 40 + "\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("Инструмент: Neptune\n")
                f.write("Автор: Venz1onixxx\n")
                f.write("TikTok: @venz1onixxx_python\n")
                f.write("=" * 60 + "\n")
            
            # ИСПРАВЛЕНО: используем синий цвет вместо GREEN
            print(f"\n{self.BLUE}💾 Результаты сохранены в файл: {filename}{self.RESET}")
            
        except Exception as e:
            # ИСПРАВЛЕНО: используем синий цвет для ошибки
            print(f"\n{self.BLUE_LIGHT}⚠️ Не удалось сохранить файл: {e}{self.RESET}")

# Запуск программы
if __name__ == "__main__":
    try:
        tool = Neptune()
        tool.search()
    except KeyboardInterrupt:
        print(f"\n{Neptune().BLUE}👋 Neptune завершает работу...{Neptune().RESET}")
    except Exception as e:
        print(f"\n{Neptune().BLUE_LIGHT}❌ Ошибка: {e}{Neptune().RESET}")
    
    input(f"\n{Neptune().CYAN}Нажмите Enter для выхода...{Neptune().RESET}")