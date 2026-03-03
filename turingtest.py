"""
Turing Test Simulation – Version 2
Multi-turn evaluation with conversation scoring
"""

import random


class Machine:

    replies = [
        "I analyze input before producing output.",
        "My computations are optimized.",
        "Emotion simulation module active.",
        "Processing complete.",
        "Query acknowledged."
    ]

    def respond(self, question):
        return random.choice(self.replies)


class Human:

    replies = [
        "Haha that’s interesting!",
        "I’m honestly a bit tired today.",
        "That reminds me of something funny.",
        "I don’t really know, what do you think?",
        "Yeah, I totally agree."
    ]

    def respond(self, question):
        return random.choice(self.replies)


class Judge:

    def evaluate(self, responses):
        suspicion = 0
        for r in responses:
            if any(word in r.lower() for word in ["process", "module", "compute", "query"]):
                suspicion += 25
            if len(r.split()) < 4:
                suspicion += 10
        return min(suspicion, 100)

    def verdict(self, score):
        return "BOT" if score > 40 else "HUMAN"


def run_test():
    print("\n" + "="*60)
    print("TURING TEST – MULTI TURN")
    print("="*60)

    machine = Machine()
    human = Human()
    judge = Judge()

    questions = ["Hello!", "How are you?", "What do you think about life?"]

    machine_responses = []
    human_responses = []

    for q in questions:
        machine_responses.append(machine.respond(q))
        human_responses.append(human.respond(q))

    m_score = judge.evaluate(machine_responses)
    h_score = judge.evaluate(human_responses)

    print("Machine Responses:")
    for r in machine_responses:
        print(" ", r)

    print("\nHuman Responses:")
    for r in human_responses:
        print(" ", r)

    print("\nJudge Verdict:")
    print("Machine →", judge.verdict(m_score), f"({m_score}%)")
    print("Human   →", judge.verdict(h_score), f"({h_score}%)")
    print("="*60)


if __name__ == "__main__":
    run_test()