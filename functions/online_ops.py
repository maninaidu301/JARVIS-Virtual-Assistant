import requests
import wikipedia
import pywhatkit as kit
import smtplib

from email.message import EmailMessage


# ==========================================
# API KEYS AND CONFIGURATION
# ==========================================

NEWS_API_KEY = ""
OPENWEATHER_APP_ID = ""
TMDB_API_KEY = ""
EMAIL = ""
PASSWORD = ""


# ==========================================
# FIND PUBLIC IP ADDRESS
# ==========================================

def find_my_ip():
    """Retrieve the public IP address."""

    try:
        response = requests.get(
            "https://api64.ipify.org?format=json",
            timeout=10
        )
        response.raise_for_status()

        return response.json()["ip"]

    except requests.RequestException as error:
        print(f"IP address error: {error}")
        return None


# ==========================================
# SEARCH WIKIPEDIA
# ==========================================

def search_on_wikipedia(query):
    """Search Wikipedia and return a short summary."""

    try:
        return wikipedia.summary(
            query,
            sentences=2,
            auto_suggest=True
        )

    except wikipedia.exceptions.DisambiguationError as error:
        return (
            "Your search matches multiple topics. "
            f"Please be more specific. Options include: "
            f"{', '.join(error.options[:5])}"
        )

    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find a Wikipedia page for that topic."

    except Exception as error:
        print(f"Wikipedia error: {error}")
        return "Sorry, Wikipedia search is unavailable right now."


# ==========================================
# PLAY YOUTUBE VIDEO
# ==========================================

def play_on_youtube(video):
    """Search for and play a video on YouTube."""

    try:
        kit.playonyt(video)
        return True

    except Exception as error:
        print(f"YouTube error: {error}")
        return False


# ==========================================
# SEARCH GOOGLE
# ==========================================

def search_on_google(query):
    """Open Google search results for the given query."""

    try:
        kit.search(query)
        return True

    except Exception as error:
        print(f"Google search error: {error}")
        return False


# ==========================================
# SEND WHATSAPP MESSAGE
# ==========================================

def send_whatsapp_message(number, message):
    """Open WhatsApp and prepare an instant message."""

    try:
        number = str(number).strip().replace(" ", "")

        if not number.startswith("+"):
            number = f"+91{number}"

        kit.sendwhatmsg_instantly(
            number,
            message,
            wait_time=15,
            tab_close=True
        )

        return True

    except Exception as error:
        print(f"WhatsApp error: {error}")
        return False


# ==========================================
# SEND EMAIL
# ==========================================

def send_email(receiver_address, subject, message):
    """Send an email using a Gmail account."""

    if not EMAIL or not PASSWORD:
        print("Email configuration is missing from the .env file.")
        return False

    try:
        email = EmailMessage()

        email["To"] = receiver_address
        email["Subject"] = subject
        email["From"] = EMAIL

        email.set_content(message)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(EMAIL, PASSWORD)
            server.send_message(email)

        return True

    except Exception as error:
        print(f"Email error: {error}")
        return False


# ==========================================
# GET LATEST NEWS
# ==========================================

def get_latest_news():
    """Retrieve the five latest general news headlines from India."""

    if not NEWS_API_KEY:
        print("NEWS_API_KEY is missing from the .env file.")
        return []

    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={
                "country": "in",
                "category": "general",
                "apiKey": NEWS_API_KEY
            },
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if data.get("status") != "ok":
            print(f"News API error: {data.get('message', 'Unknown error')}")
            return []

        return [
            article["title"]
            for article in data.get("articles", [])
            if article.get("title")
        ][:5]

    except (requests.RequestException, ValueError) as error:
        print(f"News error: {error}")
        return []


# ==========================================
# GET WEATHER REPORT
# ==========================================

def get_weather_report(city):
    """Retrieve the current weather for a city."""

    if not OPENWEATHER_APP_ID:
        print("OPENWEATHER_APP_ID is missing from the .env file.")
        return "Unavailable", "Unavailable", "Unavailable"

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": OPENWEATHER_APP_ID,
                "units": "metric"
            },
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        return (
            weather,
            f"{temperature}°C",
            f"{feels_like}°C"
        )

    except requests.RequestException as error:
        print(f"Weather API error: {error}")

    except (KeyError, IndexError, TypeError, ValueError) as error:
        print(f"Weather data error: {error}")

    return "Unavailable", "Unavailable", "Unavailable"


# ==========================================
# GET TRENDING MOVIES
# ==========================================

def get_trending_movies():
    """Retrieve the five trending movies."""

    if not TMDB_API_KEY:
        print("TMDB_API_KEY is missing from the .env file.")
        return []

    try:
        response = requests.get(
            "https://api.themoviedb.org/3/trending/movie/day",
            params={"api_key": TMDB_API_KEY},
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        return [
            movie.get("title") or movie.get("original_title")
            for movie in data.get("results", [])
            if movie.get("title") or movie.get("original_title")
        ][:5]

    except (requests.RequestException, ValueError) as error:
        print(f"Trending movies error: {error}")
        return []


# ==========================================
# GET A RANDOM JOKE
# ==========================================

def get_random_joke():
    """Retrieve a random joke."""

    try:
        response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"},
            timeout=10
        )

        response.raise_for_status()

        return response.json().get(
            "joke",
            "Sorry, I could not find a joke right now."
        )

    except (requests.RequestException, ValueError) as error:
        print(f"Joke API error: {error}")
        return "Sorry, I could not fetch a joke right now."


# ==========================================
# GET RANDOM ADVICE
# ==========================================

def get_random_advice():
    """Retrieve a random piece of advice."""

    try:
        response = requests.get(
            "https://api.adviceslip.com/advice",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "slip", {}
        ).get(
            "advice",
            "Always keep learning and moving forward."
        )

    except (requests.RequestException, ValueError) as error:
        print(f"Advice API error: {error}")
        return "Always keep learning and moving forward."

