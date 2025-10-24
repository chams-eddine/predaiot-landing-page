# config.py
# Economic and Operational Parameters

# سعر الكهرباء لكل كيلوواط/ساعة (بالريال العماني)
# تم تعديله لمحاكاة سعر وقت الذروة لزيادة الأثر المالي.
ELECTRICITY_PRICE_OMR_PER_KWH = 0.060

# تكلفة إرسال فريق صيانة لتنظيف أصل واحد (بالريال العماني)
# تم تخفيضه لمحاكاة عملية صيانة فعالة.
MAINTENANCE_COST_OMR_PER_ASSET = 25.0

# نسبة تحسن الأداء المتوقعة بعد الصيانة
PERFORMANCE_UPLIFT_AFTER_MAINTENANCE = 0.98

# عتبة الربحية (أبقيناها منخفضة)
PROFITABILITY_THRESHOLD = 1.1

# عتبة التدهور: نسبة التدهور التي يبدأ عندها المحرك في تحليل الأصل.
DEGRADATION_THRESHOLD_PCT = 5.0
