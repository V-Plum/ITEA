butt_lo = [0] * 5
for i in range(5):
    print(i)
    butt_lo[i] = [[1],[2]
        [sg.Button("X", key=("rm" + str(i)), tooltip=rm_tooltip)],
        [sg.Button("∧", key=("up" + str(i)), tooltip=up_tooltip)],
        [sg.Button("∨", key=("dn" + str(i)), tooltip=down_tooltip)],
        [sg.Button("Shuffle", key=("sh" + str(i)), tooltip=shuffle_tooltip)]
    ]
print(butt_lo)
