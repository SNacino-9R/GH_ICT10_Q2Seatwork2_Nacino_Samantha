from pyscript import display 


def calculate_gwa(e):
    fname = Element("fname").value
    lname = Element("lname").value


    science = float(Element("science").value or 0)
    math = float(Element("math").value or 0)
    english = float(Element("english").value or 0)
    filipino = float(Element("filipino").value or 0)
    ict = float(Element("ict").value or 0)
    pe = float(Element("pe").value or 0)

    
    grades = [science, math, english, filipino, ict, pe]
    units = (3, 3, 3, 3, 3, 2)

    
    total = 0
    total_units = 0
    for g, u in zip(grades, units):
        total += g * u
        total_units += u
    gwa = total / total_units

    summary = f"""
    Student: {fname} {lname}<br>
    Science: {science}<br>
    Math: {math}<br>
    English: {english}<br>
    Filipino: {filipino}<br>
    ICT: {ict}<br>
    PE: {pe}<br><br>
    <b>General Weighted Average:</b> {gwa:.2f}
    """

    Element("result").element.innerHTML = summary