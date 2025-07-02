# Telegram Ping 📱

A simple Python script to send messages to Telegram users via bot using UV and PEP 723 inline dependencies.

## ✨ Features

- 🚀 **Single file script** with inline dependencies (PEP 723)
- 🔒 **Secure** - no hardcoded tokens or sensitive data
- ⚡ **Fast execution** with UV's dependency management
- 🛡️ **Error handling** with helpful setup instructions
- 📝 **Command line arguments** for custom messages

## 🚀 Quick Start

### 1. Get Your Credentials

1. **Bot Token**: Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot`
   - Follow instructions to create your bot
   - Copy the bot token

2. **Chat ID**: Message [@userinfobot](https://t.me/userinfobot) on Telegram
   - Copy your user ID

### 2. Set Environment Variables

```bash
export TELEGRAM_BOT_TOKEN_PING="your_bot_token_here"
export TELEGRAM_CHAT_ID_PING="your_chat_id_here"
```

### 3. Run the Script

```bash
# Send custom message
uv run telegram_ping.py "Hello from my script!"

# Send default message
uv run telegram_ping.py

# One-liner with environment variables
TELEGRAM_BOT_TOKEN_PING="token" TELEGRAM_CHAT_ID_PING="chat_id" uv run telegram_ping.py "Test message"
```

## 📋 Requirements

- [UV](https://docs.astral.sh/uv/) (for dependency management)
- Python 3.8+
- Telegram bot token and chat ID

## 🔧 Installation

No installation needed! UV automatically handles dependencies via PEP 723 inline metadata.

```bash
# Clone or download the script
# Set environment variables
# Run with UV
```

## 📖 Usage Examples

### Basic Usage
```bash
uv run telegram_ping.py "Server deployment complete!"
```

### Help
```bash
uv run telegram_ping.py --help
```

### Make Executable
```bash
chmod +x telegram_ping.py
./telegram_ping.py "Direct execution!"
```

### Persistent Environment Variables
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export TELEGRAM_BOT_TOKEN_PING="your_token"' >> ~/.bashrc
echo 'export TELEGRAM_CHAT_ID_PING="your_chat_id"' >> ~/.bashrc
source ~/.bashrc
```

## 🔒 Security

- ✅ No hardcoded credentials
- ✅ Environment variable configuration
- ✅ HTTPS-only API calls
- ✅ Request timeouts and error handling
- ✅ Input validation

## 🛠️ Technical Details

- **Dependencies**: `requests>=2.25.0` (managed via PEP 723)
- **Python Version**: >=3.8
- **Package Manager**: UV
- **API**: Telegram Bot API v6+

## 🐛 Troubleshooting

### "Environment variable required" error
Make sure both environment variables are set:
```bash
echo $TELEGRAM_BOT_TOKEN_PING
echo $TELEGRAM_CHAT_ID_PING
```

### "Failed to send message" error
- Verify bot token is correct
- Ensure chat ID is valid
- Check internet connection
- Verify bot can send messages to the user

### UV not found
Install UV:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 📝 License

MIT License - feel free to modify and use as needed.

## 🤝 Contributing

This is a simple utility script. Feel free to fork and customize for your needs!
