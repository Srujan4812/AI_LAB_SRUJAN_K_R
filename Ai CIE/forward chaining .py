
# --- Initial Facts ---
facts = {
    ("food", "apple"),
    ("food", "vegetable"),
    ("eats", "anil", "peanuts"),
    ("alive", "anil")
}


def rule2(facts):
    """
    Rule 2: Anything anyone eats and is not killed (alive) is food.
    (Eats(X, Y) ∧ Alive(X)) → Food(Y)
    """
    new_facts = set()
    for fact in facts:
        if len(fact) == 3:
            predicate, x, y = fact
            if predicate == "eats":
                if ("alive", x) in facts and ("food", y) not in facts:
                    print(f"[Rule2 Fired] Because {x} eats {y} and {x} is alive → {y} is food")
                    new_facts.add(("food", y))
    return new_facts


def rule4(facts):
    """
    Rule 4: Harry eats everything that Anil eats.
    (Eats(Anil, Y)) → Eats(Harry, Y)
    """
    new_facts = set()
    for fact in facts:
        if len(fact) == 3:
            predicate, x, y = fact
            if predicate == "eats" and x == "anil":
                if ("eats", "harry", y) not in facts:
                    print(f"[Rule4 Fired] Because Anil eats {y} → Harry eats {y}")
                    new_facts.add(("eats", "harry", y))
    return new_facts




def forward_chaining(facts, rules, query):
    print("Initial Facts:")
    for f in sorted(facts):
        print("   ", f)

    print("\n--- Starting Forward Chaining ---")

    new_inferences = True
    iteration = 0

    while new_inferences:
        iteration += 1
        print(f"\nIteration {iteration}")
        new_facts = set()

        
        for rule in rules:
            derived = rule(facts)
            new_facts |= derived

        
        if new_facts - facts:
            print("\nNew facts derived in this iteration:")
            for f in new_facts - facts:
                print("   ", f)
            facts |= new_facts
        else:
            print("\nNo new facts derived. Stopping inference.")
            new_inferences = False

    print("\n--- Final Knowledge Base ---")
    for f in sorted(facts):
        print("   ", f)

    print("\nQuery:", query)
    if query in facts:
        print(" Query proven TRUE by forward chaining!")
    else:
        print(" Query could NOT be proven.")

# --- Run the system ---
rules = [rule2, rule4]
query = ("food", "peanuts")

forward_chaining(facts, rules, query)
