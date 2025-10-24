# main.py

# نستورد فقط الدوال التي نحتاجها من ملف المحرك
from engine import load_data, run_simulation

def main():
    """
    نقطة الدخول الرئيسية للتطبيق.
    هذه هي الدالة التي تبدأ كل شيء.
    """
    
    # الخطوة 1: تحميل بيانات المحاكاة من ملف data.json
    # نستخدم الدالة load_data التي استوردناها من engine.py
    simulation_data = load_data('data.json')
    
    # الخطوة 2: تشغيل المحرك لاتخاذ القرارات
    # نتأكد أولاً من أن البيانات تم تحميلها بنجاح لتجنب الأخطاء
    if simulation_data:
        # إذا كانت البيانات موجودة، نستدعي الدالة run_simulation
        # التي استوردناها من engine.py ونمرر لها البيانات
        run_simulation(simulation_data)

# هذا السطر القياسي في بايثون يضمن أن دالة main() هي التي تعمل
# عند تشغيل الملف مباشرة من الطرفية (python3 main.py)
if __name__ == "__main__":
    main()

