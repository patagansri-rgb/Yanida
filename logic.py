def validate_and_classify(subject, duration_str):
    # ตรวจสอบชื่อวิชา
    if not subject or subject.strip() == "":
        return False, "กรุณากรอกชื่อวิชา", None

    # ตรวจสอบเวลาเรียนว่าเป็นตัวเลขจำนวนเต็มหรือไม่
    try:
        duration = int(duration_str)
    except ValueError:
        return False, "เวลาเรียนต้องเป็นตัวเลขจำนวนเต็มเท่านั้น", None

    # ตรวจสอบช่วงเวลา 1 - 240 นาที
    if not (1 <= duration <= 240):
        return False, "เวลาเรียนต้องอยู่ระหว่าง 1 ถึง 240 นาที", None

    # จำแนกประเภทตามเงื่อนไขโจทย์
    if duration < 30:
        category = "Short"
    elif 30 <= duration <= 59:
        category = "Medium"
    else:
        category = "Long"

    return True, "บันทึกสำเร็จ", category