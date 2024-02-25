''' 
For Die A:
If a face on Die A originally had more than 4 spots, we change it to have exactly 4 spots.
If a face had 4 or fewer spots, we leave it as it is.
This ensures that no face on Die A ends up with more than 4 spots.
For Die B:
We don't put any restrictions on Die B. It can have as many spots as it originally had, even more than 6 if necessary.
Die B can be exactly the same as before; we don't limit the number of spots on its faces. 
For Die A, we make sure no face has more than 4 spots, and for Die B, we keep it as it is.'''


def undoom_dice(die_a, die_b):
    new_die_a = []
    new_die_b = die_b.copy()

    for face_a in die_a:
        if face_a > 4:
            new_die_a.append(4)
        else:
            new_die_a.append(face_a)

    return new_die_a, new_die_b

die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

new_die_a, new_die_b = undoom_dice(die_a, die_b)
print(f"New Die A: {new_die_a}")
print(f"New Die B: {new_die_b}")
