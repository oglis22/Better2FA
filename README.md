# Better2FA

Better2FA secures your Discord server from multi-accounting and enhances the overall security by checking the 2FA status of users.

## How It Works

- **2FA Verification**: Automatically checks if a user has Two-Factor Authentication enabled on their account.
- **Suspension and Quarantine of Suspects**: New or suspicious accounts are placed in a quarantine role until further verification.
- **IP Bans**: Ban users based on their IP address if they are identified as suspicious or violating server rules.
- **IP Tables**: Identifies VPN and Proxy usage to prevent fake or manipulated account data.
- **Rate Limiting**: Limits requests to prevent abuse or spamming of commands.
- **Captcha**: Additional CAPTCHA verification for new accounts to verify if the user is human.
- **IP White and Blacklists**: Manages trusted and untrusted IP addresses for added security.
- **Browser Cache and Fingerprint Checking**: Ensures the integrity of user browsers by checking their cache and fingerprints for suspicious activity.

## Features

- **2FA Protection**: Verifies that users have 2FA enabled before allowing full access to the server.
- **Quarantine Mechanism**: Users without 2FA are assigned to a quarantine role until verified.
- **IP-based Security**: Blocks suspicious IP addresses, including VPN and proxies, and manages whitelists and blacklists.
- **Security Measures**: CAPTCHA verification, browser fingerprinting, and rate limiting to secure your server.

## Installation

### Prerequisites

- Python 3.12 or higher
- Discord Developer account and bot token
- Server access to configure environment variables

### Steps to Install

1. **Configuration**:

   ```env
    DISCORD_TOKEN=
    DEBUG=
    SUSPICIOUSLY_NEW_ACCOUNT_IN_DAYS=
    QUARANTINE_ROLE=
    LOG_CHANNEL_ID=
    VERIFY_ROLE=
    VERIFY_LINK_CHANNEL=
    CLIENT_ID=
    CLIENT_SECRET=
    DISCORD_AUTH_LINK=
    REDIRECT_URI=
    GUILD_ID=
    INVITE_LINK=
   ```
(still in development)
