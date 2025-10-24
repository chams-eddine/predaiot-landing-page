# engine.py
# The core logic of the PREDAIOT Economic Decision Engine™

import config

def analyze_asset(asset):
    """
    يحلل أصلاً واحداً لتحديد ما إذا كانت الصيانة مجدية اقتصاديًا.
    """
    asset_id = asset['asset_id']
    degradation_pct = asset['degradation_pct']
    
    # 1. التحقق مما إذا كان تدهور الأصل يستدعي التحليل
    if degradation_pct < config.DEGRADATION_THRESHOLD_PCT:
        return {"decision": "NO_ACTION", "reason": f"Degradation ({degradation_pct}%) is below threshold."}
        
    # 2. حساب الطاقة المفقودة (Value Leakage)
    current_output_kw = asset['output_kw']
    lost_output_kw = current_output_kw / (1 - degradation_pct / 100) - current_output_kw
    
    # 3. حساب الطاقة التي يمكن استعادتها بالصيانة
    recoverable_kw = lost_output_kw * config.PERFORMANCE_UPLIFT_AFTER_MAINTENANCE
    
    # 4. تحويل الطاقة القابلة للاسترداد إلى قيمة نقدية (الربح المحتمل)
    potential_gain_omr = recoverable_kw * config.ELECTRICITY_PRICE_OMR_PER_KWH
    
    # 5. حساب درجة الربحية (مقارنة الربح بالتكلفة)
    try:
        profitability_score = potential_gain_omr / config.MAINTENANCE_COST_OMR_PER_ASSET
    except ZeroDivisionError:
        profitability_score = float('inf')

    # 6. اتخاذ القرار الاقتصادي النهائي
    if profitability_score > config.PROFITABILITY_THRESHOLD:
        decision = "DISPATCH_MAINTENANCE"
        reason = (f"High-Profit Opportunity. Gain (OMR {potential_gain_omr:.2f}) "
                  f"is {profitability_score:.2f}x the cost.")
    else:
        decision = "MONITOR"
        reason = f"Not Profitable Yet. Score: {profitability_score:.2f}x. Threshold: {config.PROFITABILITY_THRESHOLD}x."
                  
    return {"asset_id": asset_id, "decision": decision, "reason": reason}
