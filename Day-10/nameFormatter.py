def format_name(f_name, l_name):
    if f_name == "" or l_name == "": return "Invalid Input"
    return f"{f_name.title()} {l_name.title()}"

print(format_name("mEet", "tHUmmar"))