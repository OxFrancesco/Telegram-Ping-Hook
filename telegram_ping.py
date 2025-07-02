#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.25.0",
# ]
# ///

import os
import sys
import argparse
import requests
from typing import Optional


def send_telegram_message(token: str, chat_id: str, message: str) -> bool:
    """Send a message to a Telegram chat using the Bot API."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}", file=sys.stderr)
        return False


def get_env_var(name: str) -> Optional[str]:
    """Get environment variable with helpful error message if missing."""
    value = os.environ.get(name)
    if not value:
        print(f"Error: {name} environment variable is required", file=sys.stderr)
        return None
    return value


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send a message to a Telegram user via bot",
        epilog="Environment variables required: TELEGRAM_BOT_TOKEN_PING, TELEGRAM_CHAT_ID_PING"
    )
    parser.add_argument(
        "message",
        nargs="?",
        default="Hello from telegram-ping!",
        help="Message to send (default: 'Hello from telegram-ping!')"
    )
    
    args = parser.parse_args()
    
    # Get required environment variables
    bot_token = get_env_var("TELEGRAM_BOT_TOKEN_PING")
    chat_id = get_env_var("TELEGRAM_CHAT_ID_PING")
    
    if not bot_token or not chat_id:
        print("\nTo get started:", file=sys.stderr)
        print("1. Create a bot with @BotFather on Telegram to get TELEGRAM_BOT_TOKEN_PING", file=sys.stderr)
        print("2. Get your chat ID using @userinfobot to get TELEGRAM_CHAT_ID_PING", file=sys.stderr)
        print("3. Export both variables and run the script", file=sys.stderr)
        sys.exit(1)
    
    # Send the message
    print(f"Sending message: {args.message}")
    success = send_telegram_message(bot_token, chat_id, args.message)
    
    if success:
        print("Message sent successfully!")
        sys.exit(0)
    else:
        print("Failed to send message", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
