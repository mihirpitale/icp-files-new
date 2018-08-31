output_str="";
for hori in range(0,7):
    for vertical in range(0,7):
        if (vertical == 1 or vertical == 5 or (hori == 2 and (vertical == 2 or vertical == 4)) or (hori == 3 and vertical == 3)):
            output_str=output_str+"* "
        else:
            output_str=output_str+"  "
    output_str=output_str+"\n"
print(output_str);
