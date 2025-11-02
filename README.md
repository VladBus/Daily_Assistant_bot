<div style="text-align: center;">
  <a href="https://t.me/DailyInformationAssistant_bot">
    <img src="assets/readme/banner.png" alt="Banner_image_and_URL_for_tg">
  </a>
</div>

<h1 style="text-align: center;">Daily Assistant bot</h1>

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Telegram-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Last Commit](https://img.shields.io/github/last-commit/VladBus/Daily_Assistant_bot)
![Repo Size](https://img.shields.io/github/repo-size/VladBus/Daily_Assistant_bot)
![Code Size](https://img.shields.io/github/languages/code-size/VladBus/Daily_Assistant_bot)
![Top Language](https://img.shields.io/github/languages/top/VladBus/Daily_Assistant_bot)
![API](https://img.shields.io/badge/API-Telegram%20Bot-blue)
![Activity](https://img.shields.io/badge/activity-high-green)
![Code Style](https://img.shields.io/badge/code%20style-pep8-orange)
![Stars](https://img.shields.io/github/stars/VladBus/Daily_Assistant_bot)
![Watchers](https://img.shields.io/github/watchers/VladBus/Daily_Assistant_bot)

<hr>

## ***🔗 [Link to Daily_Assistant_bot](https://t.me/DailyInformationAssistant_bot)***

> ***A bot designed to provide users with daily insights into various aspects of their lives.***

## 📑 Table of Contents

- [📋 Description](#-description)
- [✨ Features](#-features)
- [🚀 Installation and Setup](#-installation-and-setup)
- [⌨️ Bot Commands](#-bot-commands)
- [🔧 API Integration](#-api-integration)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)
- [🙏 Acknowledgments](#-acknowledgments)
- [🗺️ Roadmap](#-roadmap)
- [❓ FAQ](#-faq)

## 📋 Description

>
>**Daily_Assistant_bot is an intelligent assistant that notifies users about daily attributes of our lives, such as
> weather, currency exchange rates, traffic information, and more. The bot adapts to your location to provide
personalized
> information.**

## ✨ Features

+ 🌤️ Real-time weather updates based on your location
+ 💱 Current currency exchange rates
+ 🚗 Traffic information and road conditions
+ 📅 Personalized daily notifications
+ ⚙️ Customizable notification settings
+ 🎯 Location-based recommendations
+ 📊 Daily statistics and insights

## 🚀 Installation and Setup

### Prerequisites

> + Python 3.8+
> + pyTelegramBotAPI 4.29.1
> + python-dotenv 1.2.1

### Installation Steps

***1*** **Clone the repository**

```bash
git clone https://github.com/VladBus/Daily_Assistant_bot.git
cd Daily_Assistant_bot
```

***2*** **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate
```

***3*** **Install dependencies**

```bash
pip install -r requirements.txt
```

***4*** **Set up environment variables**

Create a ```.env``` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token_here
WEATHER_API_KEY=your_weather_api_key_here
CURRENCY_API_KEY=your_currency_api_key_here
```

***5*** **Run the bot**

```bash
python main.py
```

## ⌨️ Bot Commands

+ ```/start``` - Initialize the bot and get welcome message
+ ```/help``` - Get help with available commands
+ ```/site``` - Get link to associated website
+ ```/weather``` - Get current weather in your location
+ ```/rates``` - Get current currency exchange rates
+ ```/traffic``` - Get traffic information for your area
+ ```/settings``` - Configure notification preferences
+ ```/location``` - Set or update your location

## 🔧 API Integration

The bot integrates with multiple APIs to provide comprehensive information:

+ [OpenWeatherMap API](https://openweathermap.org/api) for weather data
+ [Currency API](https://www.exchangerate-api.com/) for exchange rates
+ [Google Maps API](https://developers.google.com/maps?hl=ru) for traffic information

## 🤝 Contributing

We welcome contributions to the project! Please follow these steps:

1. Fork the repository
2. Create a new branch (```git checkout -b feature/AmazingFeature```)
3. Commit your changes (```git commit -m 'Add some AmazingFeature'```)
4. Push to the branch (```git push origin feature/AmazingFeature```)
5. Open a Pull Request

## 📞 Support

If you have any questions or issues:

1. Check the [Issues](https://github.com/VladBus/Daily_Assistant_bot/issues) section
2. Create a new issue if your question hasn't been addressed
3. Contact us directly:

    + GitHub: [VladBus](https://github.com/VladBus)
    + Telegram: [Vlad Busev](https://t.me/pankmomon)
    + Email: [buvlad2002@gmail.com](https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to=buvlad2002@gmail.com)

## 🙏 Acknowledgments

+ [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for the excellent Telegram bot library
+ [OpenWeatherMap](https://openweathermap.org/) for weather data API
+ [ExchangeRate-API](https://www.exchangerate-api.com/) for currency exchange rates
+ The developer community for valuable contributions and suggestions

## 🗺️ Roadmap

+ Multi-language support
+ Integration with additional APIs
+ Web interface for bot management
+ Advanced usage analytics
+ Plugin system for extended functionality
+ Machine learning for personalized recommendations
+ Voice command support
+ Integration with smart home devices

## ❓ FAQ

| Questions                                                | Answers                                                                                                         |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| :arrow_forward: Q: How do I add the bot to my chat?      | :arrow_backward: A: Find the bot by username @DailyInformationAssistant_bot and click "Start" or "Add to Chat". |
| :arrow_forward: Q: Can I customize notification times?   | :arrow_backward: A: Yes, use the /settings command to configure your personalized schedule.                     |
| :arrow_forward: Q: How often is the information updated? | :arrow_backward: A: Information is updated in real-time, but you can set custom update intervals in settings.   |
| :arrow_forward: Q: Is my location data secure?           | :arrow_backward: A: Yes, all location data is encrypted and used solely for providing personalized information. |

<hr>

⭐ **If you find this project useful, please give it a star!**
