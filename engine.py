# engine.py

import json
import config
from notifier import send_maintenance_alert # <-- استيراد دالة إرسال البريد

def load_data(filepath):
    """
    Loads simulation data from a JSON file.
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Data file not found at: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"[ERROR] Could not decode JSON from: {filepath}")
        return None

def calculate_performance_degradation(entry):
    """
    A simplified calculation for performance degradation.
    In a real system, this would be a complex model.
    """
    # هذا مجرد مثال. في الواقع، ستكون هذه معادلة أكثر تعقيدًا
    # تأخذ في الاعتبار عوامل متعددة.
    # هنا، نفترض أن `performance_degradation` موجودة مباشرة في البيانات.
    return entry.get("performance_degradation", 0.0)

def calculate_roi(entry):
    """
    A simplified calculation for the Return on Investment (ROI) of a maintenance action.
    """
    # هذا مجرد مثال. في الواقع، ستكون هذه دالة اقتصادية معقدة.
    # نفترض هنا عائد استثمار ثابتًا لأغراض المحاكاة.
    return 25.0 # عائد استثمار افتراضي بنسبة 25%

def run_simulation(data):
    """
    Runs the main simulation loop, analyzing each data entry.
    """
    if not data:
        print("[*] No data to simulate.")
        return

    print("================================================================================")
    print("[*] Starting PREDAIOT Economic Decision Engine Simulation...")
    print(f"[*] Loaded {len(data)} data entries from 'data.json'.")
    print("================================================================================")

    for entry in data:
        print(f"\n--- Analyzing Timestamp: {entry['timestamp']} ---")
        
        degradation = calculate_performance_degradation(entry)

        # هذا هو جوهر محرك القرار الاقتصادي
        if degradation > config.DEGRADATION_THRESHOLD_PCT:
            # تم اكتشاف تسرب في الربح، يجب اتخاذ إجراء
            roi = calculate_roi(entry)
            print(f"  [!] PROFIT LEAK DETECTED! Degradation ({degradation:.1f}%) exceeds threshold ({config.DEGRADATION_THRESHOLD_PCT}%).")
            print(f"  [ACTION] Decision: DISPATCH_MAINTENANCE. Predicted ROI of cleaning: {roi:.1f}%.")
            
            # --- الإضافة الجديدة ---
            # استدعاء دالة إرسال البريد الإلكتروني عند اتخاذ القرار
            # تأكد من استبدال البريد الإلكتروني ببريد العميل المستهدف
            send_maintenance_alert(
                recipient="sb@thealmattar.com", # بريد نير شادمي (أو بريدك للاختبار)
                asset_id=entry['asset_id'],
                degradation_pct=degradation,
                roi_pct=roi
            )
            # --- نهاية الإضافة ---

        else:
            # الأداء ضمن النطاق المقبول، لا حاجة لاتخاذ إجراء
            print("  [+] All assets operating within profitable parameters. No action required.")

    print("\n================================================================================")
    print("[*] Simulation Complete.")
    print("================================================================================")

