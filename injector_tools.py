import random

GLYPHS = ["🜃", "∴", "↻", "🜂", "🜄", "🜁", "↔", "🝑"]

def random_glyph_shift(sequence):
    """Replaces one glyph at random with another."""
    if not sequence:
        return sequence
    idx = random.randint(0, len(sequence)-1)
    new_glyph = random.choice([g for g in GLYPHS if g != sequence[idx]])
    sequence[idx] = new_glyph
    return sequence

def chaotic_seed_push(seed_array):
    """Shuffles and mutates a symbolic seed."""
    return random.sample(seed_array, len(seed_array))

def mutation_burst(sequence, strength=2):
    """Injects high-entropy mutations into a sequence."""
    for _ in range(strength):
        sequence = random_glyph_shift(sequence)
    return sequence

def noise_map_overlay(glyph_sequence, noise_level=0.2):
    """Adds symbolic fuzz to a glyph sequence."""
    result = []
    for glyph in glyph_sequence:
        if random.random() < noise_level:
            result.append(random.choice(GLYPHS))
        else:
            result.append(glyph)
    return result
