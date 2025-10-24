# main.py
# Main simulation script for the PREDAIOT EDE v1.0 Demo

import json
from engine import analyze_asset

def run_simulation(data_filepath='data.json'):
    """
    يقوم بتحميل البيانات وتشغيل المحاكاة الكاملة.
    """
    print("="*80)
    print("[*] Starting PREDAIOT Economic Decision Engine Simulation...")
    
    with open(data_filepath, 'r') as f:
        data = json.load(f)
    
    print(f"[*] Loaded {len(data)} data entries from '{data_filepath}'.")
    print("="*80)
    
    for entry in data:
        timestamp = entry['timestamp']
        print(f"\n--- Analyzing Timestamp: {timestamp} ---")
        
        has_actionable_insight = False
        for asset in entry['assets']:
            result = analyze_asset(asset)
            
            if result['decision'] == "DISPATCH_MAINTENANCE":
                print(f"  [!] DECISION for {result['asset_id']}: {result['decision']}")
                print(f"      └── REASON: {result['reason']}")
                has_actionable_insight = True

        if not has_actionable_insight:
            print("  [+] All assets operating within profitable parameters. No action required.")

    print("\n" + "="*80)
    print("[*] Simulation Complete.")
    print("="*80)

if __name__ == "__main__":
    run_simulation()
