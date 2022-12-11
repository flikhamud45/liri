import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes ="sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

iterable_notes = notes.split("-")

for note in iterable_notes:
    x = note.split(",")
    frequency=freqs[x[0]]
    duration =x[1]
    winsound.Beep(int(frequency), int(duration))


print(iterable_notes)

