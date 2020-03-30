def change_case(in_text):
    out_text = ""
    for i in range(len(in_text)-1):
        current_letter = in_text[i]
        if current_letter.isupper():
            out_text += current_letter.lower()
        elif current_letter.islower():
            out_text += current_letter.upper()
        else:
            out_text += current_letter
    return out_text

in_text = "I`m eaTinG BaNaNa."
out_text = change_case(in_text)
print(out_text)
