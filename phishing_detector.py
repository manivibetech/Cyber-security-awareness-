# phishing_detector.py
# School Project - Phishing Email Detector (Educational Purpose)

import re


def check_phishing(email_text, sender_email=""):
    score = 0
    reasons = []

    # 1. Check for urgent / scare words
    urgent_words = [
        "urgent", "immediately", "account suspended",
        "verify now", "action required", "click here"
    ]
    for word in urgent_words:
        if word.lower() in email_text.lower():
            score += 1
            reasons.append(f"Contains urgent phrase: '{word}'")

    # 2. Check for suspicious links
    links = re.findall(
        r'http[s]?://\S+|bit\.ly/\S+',
        email_text,
        re.IGNORECASE
    )
    if links:
        score += 2
        reasons.append(f"Contains suspicious links: {links}")

    # 3. Check sender domain
    if sender_email:
        if not re.match(
            r"^[^@]+@(gmail\.com|yahoo\.com|outlook\.com|school\.edu|company\.com)$",
            sender_email.lower()
        ):
            # Demo rule: add trusted school/company domains as needed.
            if "support" in sender_email.lower() or "security" in sender_email.lower():
                score += 1
                reasons.append(f"Suspicious sender: {sender_email}")

    # 4. Check for requests for personal information
    info_keywords = ["password", "otp", "credit card", "bank account", "ssn"]
    for keyword in info_keywords:
        if keyword in email_text.lower():
            score += 2
            reasons.append(f"Asks for sensitive info: '{keyword}'")

    # Final decision
    is_phishing = score >= 3
    return is_phishing, score, reasons


if __name__ == "__main__":
    print("=== Phishing Detector - School Project ===\\n")

    sample1 = (
        "Dear user, your account has been suspended. Please click here "
        "http://bit.ly/secure-login urgently to verify your password immediately."
    )
    sample2 = (
        "Hi Ali, meeting tomorrow at 10am in class. "
        "Please bring your science notes."
    )

    for index, email in enumerate([sample1, sample2], 1):
        result, score, reasons = check_phishing(
            email,
            sender_email="support@secure-login-alert.com"
        )
        print(f"Email {index}: {email[:60]}...")
        print(f" -> Score: {score} | Phishing? {result}")
        if reasons:
            print(f" -> Reasons: {reasons}")
        print()
