def calculate_score():
    module_scores = {"mobilité": 0.8, "eau": 0.7, "déchets": 0.9, "solaire": 0.6}
    final = sum(module_scores.values()) / len(module_scores)
    grade = "A" if final >= 0.85 else "B" if final >= 0.7 else "C" if final >= 0.5 else "D" if final >= 0.3 else "E"
    return grade, f"Score basé sur {len(module_scores)} modules."