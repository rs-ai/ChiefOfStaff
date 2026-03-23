#!/usr/bin/env python3
"""
Chief of Staff — Email Notification System

Sends email alerts for intelligence, contacts, and briefings.
Uses Resend API — no email passwords, just a revocable API key.

Setup:
  1. Sign up at https://resend.com (free tier: 100 emails/day)
  2. Copy your API key from the dashboard
  3. Create scripts/.env with:
       RESEND_API_KEY=re_xxxxxxxxx
       NOTIFY_TO=your.real.email@gmail.com
  4. Test: python scripts/notify.py --test

Optional: Verify a custom domain in Resend for a branded sender
  (e.g. chief@yourdomain.com). Without it, sends from onboarding@resend.dev.
"""

import json
import sys
import resend
from datetime import datetime, timezone
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
ENV_FILE = Path(__file__).parent / ".env"

# Sender address — change after verifying your own domain in Resend
DEFAULT_FROM = "Chief of Staff <onboarding@resend.dev>"


def load_env():
    """Load config from scripts/.env file."""
    config = {}
    if not ENV_FILE.exists():
        print(f"ERROR: {ENV_FILE} not found. Create it with:")
        print("  RESEND_API_KEY=re_xxxxxxxxx")
        print("  NOTIFY_TO=your.real.email@gmail.com")
        sys.exit(1)
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    required = ["RESEND_API_KEY", "NOTIFY_TO"]
    missing = [k for k in required if k not in config]
    if missing:
        print(f"ERROR: Missing keys in .env: {', '.join(missing)}")
        sys.exit(1)

    resend.api_key = config["RESEND_API_KEY"]
    return config


def load_json(filename):
    """Load a JSON data file."""
    path = DATA_DIR / filename
    if not path.exists():
        return []
    with open(path) as f:
        return json.load(f)


def send_email(config, subject, html_body):
    """Send an email via Resend API."""
    sender = config.get("FROM_ADDRESS", DEFAULT_FROM)
    params = {
        "from": sender,
        "to": [config["NOTIFY_TO"]],
        "subject": subject,
        "html": html_body,
    }
    email = resend.Emails.send(params)
    print(f"Email sent: {subject} (id: {email.get('id', 'unknown')})")
    return email


def format_intel_email(intel_items):
    """Format intelligence items into an HTML email."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    items_html = ""
    for item in intel_items:
        source_link = f'<a href="{item.get("url", "#")}" style="color:#3b82f6;">Source</a>' if item.get("url") else ""
        items_html += f"""
        <div style="padding:12px;border-bottom:1px solid #e2e8f0;">
            <strong>{item.get('title', 'Unknown')}</strong>
            <span style="background:#e2e8f0;padding:2px 6px;border-radius:3px;font-size:12px;margin-left:8px;">{item.get('domain', '')}</span>
            <p style="margin:6px 0;color:#334155;">{item.get('summary', '')}</p>
            {source_link}
        </div>"""

    return f"""
    <html>
    <body style="font-family:system-ui,-apple-system,sans-serif;max-width:700px;margin:0 auto;padding:20px;">
        <div style="background:#0f172a;color:white;padding:16px 20px;border-radius:8px 8px 0 0;">
            <h2 style="margin:0;">Chief of Staff — Intelligence Brief</h2>
            <p style="margin:4px 0 0;color:#94a3b8;">{today} — {len(intel_items)} item{'s' if len(intel_items) != 1 else ''}</p>
        </div>
        <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:4px 16px;">
            {items_html}
        </div>
    </body>
    </html>"""


def format_briefing_email(briefing_text):
    """Format a morning briefing into an HTML email."""
    today = datetime.now(timezone.utc).strftime("%A, %B %d, %Y")
    return f"""
    <html>
    <body style="font-family:system-ui,-apple-system,sans-serif;max-width:700px;margin:0 auto;padding:20px;">
        <div style="background:#0f172a;color:white;padding:16px 20px;border-radius:8px 8px 0 0;">
            <h2 style="margin:0;">Chief of Staff — Morning Briefing</h2>
            <p style="margin:4px 0 0;color:#94a3b8;">{today}</p>
        </div>
        <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:16px;">
            <pre style="white-space:pre-wrap;font-family:system-ui,-apple-system,sans-serif;font-size:14px;line-height:1.6;">{briefing_text}</pre>
        </div>
    </body>
    </html>"""


def format_contacts_email(contacts):
    """Format contact recommendations into an HTML email."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows = ""
    for c in contacts:
        linkedin_url = c.get("linkedin", "")
        linkedin_link = f'<a href="https://{linkedin_url}" style="color:#3b82f6;">LinkedIn</a>' if linkedin_url else "—"
        tier_color = "#ef4444" if c.get("tier") == 1 else "#eab308" if c.get("tier") == 2 else "#94a3b8"
        notes_snippet = (c.get("notes", "")[:120] + "...") if len(c.get("notes", "")) > 120 else c.get("notes", "")
        rows += f"""
        <tr>
            <td style="padding:8px;border-bottom:1px solid #e2e8f0;">
                <strong>{c.get('name', '?')}</strong>
                <span style="background:{tier_color};color:white;padding:1px 5px;border-radius:3px;font-size:11px;margin-left:4px;">T{c.get('tier', '?')}</span>
            </td>
            <td style="padding:8px;border-bottom:1px solid #e2e8f0;">{c.get('role', '')}<br><span style="color:#64748b;font-size:12px;">{c.get('company', '')}</span></td>
            <td style="padding:8px;border-bottom:1px solid #e2e8f0;">{linkedin_link}</td>
        </tr>
        <tr>
            <td colspan="3" style="padding:4px 8px 12px;color:#64748b;font-size:12px;border-bottom:2px solid #e2e8f0;">{notes_snippet}</td>
        </tr>"""

    return f"""
    <html>
    <body style="font-family:system-ui,-apple-system,sans-serif;max-width:700px;margin:0 auto;padding:20px;">
        <div style="background:#0f172a;color:white;padding:16px 20px;border-radius:8px 8px 0 0;">
            <h2 style="margin:0;">Chief of Staff — Contacts to Reach Out To</h2>
            <p style="margin:4px 0 0;color:#94a3b8;">{today} — {len(contacts)} contact{'s' if len(contacts) != 1 else ''}</p>
        </div>
        <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:16px;">
            <table style="width:100%;border-collapse:collapse;">
                <tr style="background:#f8fafc;">
                    <th style="padding:8px;text-align:left;">Name</th>
                    <th style="padding:8px;text-align:left;">Role</th>
                    <th style="padding:8px;text-align:left;">LinkedIn</th>
                </tr>
                {rows}
            </table>
        </div>
    </body>
    </html>"""


# --- CLI Commands ---

def cmd_test(config):
    """Send a test email."""
    send_email(config, "Chief of Staff — Test Email",
        """<div style="font-family:system-ui;max-width:500px;margin:0 auto;padding:20px;">
        <div style="background:#0f172a;color:white;padding:16px 20px;border-radius:8px 8px 0 0;">
            <h2 style="margin:0;">Chief of Staff</h2>
        </div>
        <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:20px;">
            <h3>Notification system is online.</h3>
            <p>You will receive alerts for:</p>
            <ul>
                <li>Intelligence briefs (with source links)</li>
                <li>Contacts to reach out to (with LinkedIn links)</li>
                <li>Morning briefings</li>
            </ul>
        </div></div>""")


def cmd_intel(config):
    """Send recent intelligence email."""
    intel = load_json("intelligence.json")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    recent = [i for i in intel if i.get("captured_date") == today]
    if not recent:
        print("No intel from today to send.")
        return
    send_email(config, f"Chief of Staff — {len(recent)} Intelligence Item{'s' if len(recent) != 1 else ''}",
        format_intel_email(recent))


def cmd_contacts(config):
    """Send contacts to reach out to."""
    contacts = load_json("contacts.json")
    target = [c for c in contacts if c.get("relationship") in ("target-network", "mentor", "sponsor") and not c.get("last_interaction")]
    if not target:
        print("No uncontacted targets to send.")
        return
    send_email(config, f"Chief of Staff — {len(target)} Contacts to Reach Out To",
        format_contacts_email(target))


def cmd_briefing(config):
    """Send the latest briefing if it exists."""
    briefing_path = DATA_DIR / "briefing-latest.md"
    if not briefing_path.exists():
        print("No briefing file found.")
        return
    text = briefing_path.read_text()
    send_email(config, "Chief of Staff — Morning Briefing", format_briefing_email(text))


def cmd_all(config):
    """Send everything: intel, contacts."""
    cmd_intel(config)
    cmd_contacts(config)


if __name__ == "__main__":
    commands = {
        "--test": cmd_test,
        "--intel": cmd_intel,
        "--contacts": cmd_contacts,
        "--briefing": cmd_briefing,
        "--all": cmd_all,
        "--help": None,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands or sys.argv[1] == "--help":
        print("Chief of Staff — Email Notification System")
        print()
        print("Usage: python scripts/notify.py [command]")
        print()
        print("Commands:")
        for cmd, fn in commands.items():
            if fn:
                print(f"  {cmd:15s} {fn.__doc__}")
        print(f"  {'--help':15s} Show this help message")
        print()
        print("Setup:")
        print("  1. pip install -r requirements.txt")
        print("  2. Copy scripts/.env.example to scripts/.env")
        print("  3. Add your RESEND_API_KEY and NOTIFY_TO email")
        print("  4. Run: python scripts/notify.py --test")
        sys.exit(0 if sys.argv[1:] == ["--help"] else 1)

    config = load_env()
    commands[sys.argv[1]](config)
