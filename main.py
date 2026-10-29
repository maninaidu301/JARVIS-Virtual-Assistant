import requests
import pyttsx3
import speech_recognition as sr

from decouple import config
from datetime import datetime
from random import choice
from pprint import pprint

from functions.online_ops import (
    find_my_ip,
    get_latest_news,
    get_random_advice,
    get_random_joke,
    get_trending_movies,
    get_weather_report,
    play_on_youtube,
    search_on_google,
    search_on_wikipedia,
    send_email,
    send_whatsapp_message
)

from functions.os_ops import (
    open_calculator,
    open_camera,
    open_cmd,
    open_notepad,
    open_discord
)

from utils import opening_text


# =========================
# CONFIGURATION
# =========================

USERNAME = "Mani"
BOTNAME = "Friday"


# =========================
# TEXT-TO-SPEECH SETUP
# =========================

engine = pyttsx3.init("sapi5")

engine.setProperty("rate", 190)
engine.setProperty("volume", 1.0)

# Set female voice when available
voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
elif len(voices) > 0:
    engine.setProperty("voice", voices[0].id)


# =========================
# TEXT-TO-SPEECH FUNCTION
# =========================

def speak(text):
    """Convert text into speech."""

    print(f"{BOTNAME}: {text}")

    engine.say(str(text))
    engine.runAndWait()


# =========================
# GREET THE USER
# =========================

def greet_user():
    """Greet the user according to the time of day."""

    hour = datetime.now().hour

    if 6 <= hour < 12:
        speak(f"Good morning, {USERNAME}!")

    elif 12 <= hour < 16:
        speak(f"Good afternoon, {USERNAME}!")

    elif 16 <= hour < 19:
        speak(f"Good evening, {USERNAME}!")

    else:
        speak(f"Hello, {USERNAME}!")

    speak(f"I am {BOTNAME}. How may I assist you?")


# =========================
# TAKE VOICE INPUT
# =========================

def take_user_input():
    """
    Listen to the user's voice and convert it into text.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        query = query.lower().strip()

        print(f"You said: {query}")

        # Check exit commands
        exit_commands = {
            "exit",
            "stop",
            "quit",
            "goodbye",
            "shutdown assistant",
            "stop assistant"
        }

        if query in exit_commands:
            hour = datetime.now().hour

            if hour >= 21 or hour < 6:
                speak("Good night! Take care.")
            else:
                speak("Have a good day! Goodbye.")

            raise SystemExit

        # Random introductory response
        if opening_text:
            speak(choice(opening_text))

        return query

    except SystemExit:
        raise

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Could you please say that again?")
        return ""

    except sr.RequestError:
        speak("Speech recognition is currently unavailable. Please check your internet connection.")
        return ""

    except OSError:
        speak("Microphone not found. Please check your microphone connection.")
        return ""


# =========================
# MAIN ASSISTANT
# =========================

if __name__ == "__main__":

    greet_user()

    while True:

        try:
            query = take_user_input()

            if not query:
                continue

            # -------------------------
            # OPEN APPLICATIONS
            # -------------------------

            if "open notepad" in query:
                open_notepad()

            elif "open discord" in query:
                open_discord()

            elif "open command prompt" in query or "open cmd" in query:
                open_cmd()

            elif "open camera" in query:
                open_camera()

            elif "open calculator" in query:
                open_calculator()

            # -------------------------
            # FIND IP ADDRESS
            # -------------------------

            elif "ip address" in query:
                ip_address = find_my_ip()

                if ip_address:
                    speak(f"Your IP address is {ip_address}.")
                    print(f"IP Address: {ip_address}")
                else:
                    speak("Sorry, I could not retrieve your IP address.")

            # -------------------------
            # WIKIPEDIA SEARCH
            # -------------------------

            elif "wikipedia" in query:
                speak("What would you like to search for on Wikipedia?")

                search_query = take_user_input()

                if search_query:
                    results = search_on_wikipedia(search_query)

                    if results:
                        speak(f"According to Wikipedia, {results}")
                        print("\nWikipedia Results:")
                        print(results)
                    else:
                        speak("Sorry, I could not find any results.")

            # -------------------------
            # YOUTUBE
            # -------------------------

            elif "youtube" in query:
                speak("What would you like to play on YouTube?")

                video = take_user_input()

                if video:
                    play_on_youtube(video)

            # -------------------------
            # GOOGLE SEARCH
            # -------------------------

            elif "search on google" in query or "google search" in query:
                speak("What would you like to search for on Google?")

                search_query = take_user_input()

                if search_query:
                    search_on_google(search_query)

            # -------------------------
            # WHATSAPP MESSAGE
            # -------------------------

            elif "send whatsapp message" in query:
                speak("Please enter the recipient's phone number in the console.")

                number = input("Enter phone number with country code: ").strip()

                speak("What message would you like to send?")

                message = take_user_input()

                if number and message:
                    send_whatsapp_message(number, message)
                    speak("The WhatsApp message request has been processed.")

            # -------------------------
            # SEND EMAIL
            # -------------------------

            elif "send an email" in query or "send email" in query:
                speak("Please enter the recipient's email address in the console.")

                receiver_address = input("Enter email address: ").strip()

                speak("What should be the email subject?")

                subject = take_user_input()

                speak("What message would you like to send?")

                message = take_user_input()

                if receiver_address and subject and message:

                    try:
                        result = send_email(
                            receiver_address,
                            subject,
                            message
                        )

                        if result:
                            speak("The email was sent successfully.")
                        else:
                            speak("Something went wrong while sending the email. Please check the error logs.")

                    except Exception as error:
                        print(f"Email error: {error}")
                        speak("Sorry, I could not send the email.")

            # -------------------------
            # RANDOM JOKE
            # -------------------------

            elif "joke" in query:
                speak("Here is a joke for you!")

                joke = get_random_joke()

                if joke:
                    speak(joke)
                    pprint(joke)
                else:
                    speak("Sorry, I could not fetch a joke right now.")

            # -------------------------
            # RANDOM ADVICE
            # -------------------------

            elif "advice" in query:
                speak("Here is some advice for you!")

                advice = get_random_advice()

                if advice:
                    speak(advice)
                    pprint(advice)
                else:
                    speak("Sorry, I could not fetch advice right now.")

            # -------------------------
            # TRENDING MOVIES
            # -------------------------

            elif "trending movies" in query:
                movies = get_trending_movies()

                if movies:
                    speak("Here are some trending movies.")

                    for movie in movies:
                        print(movie)
                        speak(movie)
                else:
                    speak("Sorry, I could not fetch trending movies.")

            # -------------------------
            # LATEST NEWS
            # -------------------------

            elif "news" in query:
                speak("Fetching the latest news headlines.")

                news = get_latest_news()

                if news:
                    for headline in news:
                        print(headline)
                        speak(headline)
                else:
                    speak("Sorry, I could not fetch the latest news.")

            # -------------------------
            # WEATHER REPORT
            # -------------------------

            elif "weather" in query:
                try:
                    ip_address = find_my_ip()

                    if not ip_address:
                        speak("Sorry, I could not determine your location.")
                        continue

                    response = requests.get(
                        f"https://ipapi.co/{ip_address}/city/",
                        timeout=10
                    )

                    response.raise_for_status()

                    city = response.text.strip()

                    if not city or "error" in city.lower():
                        speak("Sorry, I could not determine your city.")
                        continue

                    speak(f"Getting the weather report for {city}.")

                    weather, temperature, feels_like = get_weather_report(city)

                    speak(f"The current temperature is {temperature}.")
                    speak(f"It feels like {feels_like}.")
                    speak(f"The weather condition is {weather}.")

                    print("\nWeather Report")
                    print("-------------------------")
                    print(f"City: {city}")
                    print(f"Description: {weather}")
                    print(f"Temperature: {temperature}")
                    print(f"Feels like: {feels_like}")

                except requests.RequestException as error:
                    print(f"Location request error: {error}")
                    speak("Sorry, I could not retrieve your location.")

                except Exception as error:
                    print(f"Weather error: {error}")
                    speak("Sorry, I could not retrieve the weather report.")

            # -------------------------
            # UNKNOWN COMMAND
            # -------------------------

            else:
                speak("Sorry, I do not know how to perform that task yet.")

        except SystemExit:
            break

        except KeyboardInterrupt:
            speak("Assistant stopped. Goodbye!")
            break

        except Exception as error:
            print(f"Unexpected error: {error}")
            speak("Something went wrong. Please try again.")
