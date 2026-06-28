#!/bin/bash
# Quick test — run this after setting up your Telegram bot
# Requires ~/.env with TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID

source ~/.env

if [[ -z "$TELEGRAM_BOT_TOKEN" || -z "$TELEGRAM_CHAT_ID" ]]; then
  echo "ERROR: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set in ~/.env"
  exit 1
fi

curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -d chat_id="${TELEGRAM_CHAT_ID}" \
  -d text="VulnForge is online — scanners ready."

echo ""
echo "Message sent. Check your Telegram."
