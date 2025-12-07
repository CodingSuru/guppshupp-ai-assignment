from utils.file_loader import load_messages
from memory_engine.extractor import extract_memory
from personality_engine.transformer import apply_personality
from personality_engine.templates import PERSONALITIES
import json

def main():
    print("=" * 60)
    print("=== GUPPSHUPP AI ENGINEER ASSIGNMENT ===")
    print("=== Memory Extraction + Personality Engine ===")
    print("=" * 60)
    
    # Load messages
    print("\n[1] Loading messages from data/sample_input.txt...")
    messages = load_messages("data/sample_input.txt")
    print(f"✓ Loaded {len(messages)} messages")

    # Memory extraction
    print("\n[2] Extracting memory (preferences, emotions, facts)...")
    memory = extract_memory(messages)
    
    print("\n" + "=" * 60)
    print("EXTRACTED MEMORY (JSON FORMAT):")
    print("=" * 60)
    print(json.dumps(memory, indent=2, ensure_ascii=False))
    
    # Save memory to JSON file
    with open("data/output_memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)
    print("\n✓ Memory saved to data/output_memory.json")

    # Personality application
    print("\n" + "=" * 60)
    print("[3] PERSONALITY ENGINE - BEFORE/AFTER DEMONSTRATION")
    print("=" * 60)
    
    neutral_response = "You should take a break and manage your time better. Try focusing on one task at a time."
    
    print("\n>>> BEFORE (Neutral Response):")
    print("-" * 60)
    print(neutral_response)
    print("-" * 60)

    output_responses = []
    output_responses.append("BEFORE (Neutral Response):\n" + neutral_response + "\n\n")

    for style in PERSONALITIES:
        transformed = apply_personality(neutral_response, style)
        print(f"\n>>> AFTER (Personality: {style.upper()}):")
        print("-" * 60)
        print(transformed)
        print("-" * 60)
        output_responses.append(f"AFTER (Personality: {style.upper()}):\n{transformed}\n\n")

    # Save responses to file
    with open("data/output_responses.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_responses))
    print("\n✓ Responses saved to data/output_responses.txt")

    print("\n" + "=" * 60)
    print("✓✓✓ PROJECT EXECUTED SUCCESSFULLY! ✓✓✓")
    print("=" * 60)
    print("\nOutput files created:")
    print("  - data/output_memory.json")
    print("  - data/output_responses.txt")

if __name__ == "__main__":
    main()