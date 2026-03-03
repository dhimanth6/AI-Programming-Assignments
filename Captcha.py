"""
Advanced CAPTCHA System
AI Assignment – Version 2

Architecture:
Client → Request CAPTCHA → Server creates challenge → 
User response → Server validates → Grant / Deny
"""

import random
import string
import hashlib
import time


# ──────────────────────────────────────────────────────────────
# Challenge Factory
# ──────────────────────────────────────────────────────────────

class ChallengeFactory:

    @staticmethod
    def generate(level="easy"):
        if level == "easy":
            return ChallengeFactory._math()
        elif level == "medium":
            return ChallengeFactory._pattern()
        else:
            return ChallengeFactory._text()

    @staticmethod
    def _math():
        x = random.randint(5, 30)
        y = random.randint(5, 30)
        question = f"What is {x} + {y}?"
        return question, str(x + y)

    @staticmethod
    def _pattern():
        sequence = [2, 4, 8, 16]
        question = "Find the next number: 2, 4, 8, 16, ?"
        return question, "32"

    @staticmethod
    def _text():
        code = ''.join(random.choices(string.ascii_uppercase + "23456789", k=6))
        scrambled = " ".join(code)
        question = f"Enter the code: [{scrambled}]"
        return question, code


# ──────────────────────────────────────────────────────────────
# CAPTCHA Session
# ──────────────────────────────────────────────────────────────

class CaptchaSession:

    def __init__(self, level="easy", max_attempts=3):
        self.challenge, self.answer = ChallengeFactory.generate(level)
        self.created = time.time()
        self.max_attempts = max_attempts
        self.attempts = 0
        self.session_id = self._create_session_id()

    def _create_session_id(self):
        raw = f"{self.challenge}{self.created}"
        return hashlib.sha256(raw.encode()).hexdigest()[:10]

    def verify(self, user_input):
        if self.is_expired():
            return False, "Session expired."

        self.attempts += 1

        if user_input.strip().lower() == self.answer.lower():
            return True, "Access Granted."

        if self.attempts >= self.max_attempts:
            return False, "Too many attempts. Blocked."

        return False, "Incorrect. Try again."

    def is_expired(self):
        return (time.time() - self.created) > 90


# ──────────────────────────────────────────────────────────────
# Demo
# ──────────────────────────────────────────────────────────────

def run_demo():
    print("\n" + "="*60)
    print("ADVANCED CAPTCHA SYSTEM")
    print("="*60)

    session = CaptchaSession(level="medium")

    print(f"Session ID : {session.session_id}")
    print(f"Challenge  : {session.challenge}")

    # Simulated user
    simulated_answer = session.answer  # pretend human solved it

    status, message = session.verify(simulated_answer)
    print(f"Response   : {simulated_answer}")
    print(f"Result     : {message}")
    print("="*60)


if __name__ == "__main__":
    run_demo()