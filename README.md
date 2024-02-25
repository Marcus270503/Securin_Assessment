# Securin_Assessment
Securin Python Assessment

<h2>Part - A</h2>

1. Combinations<br>
  The total combinations when rolling two six-sided dice can be calculated by multiplying the number of faces on each die. In this case, <br> it's 6 * 6 = 36.<br><br>
   <img width="553" alt="Screenshot 2024-02-25 224759" src="https://github.com/Marcus270503/Securin_Assessment/assets/103208421/e74a5854-32f8-4498-9ffa-8d5c832e6f4d">
2. Distribution of Combinations<br>
  To display the distribution of all possible combinations, we can create a 6x6 matrix where the element at position (i, j) represents the sum of Die A's i-th face and Die B's j-th face.<br><br>
   <img width="701" alt="Screenshot 2024-02-25 224819" src="https://github.com/Marcus270503/Securin_Assessment/assets/103208421/198a4da4-bfd8-426f-ae9a-708cf3de0a1f">
3. Probability of Sums<br>
  Calculate the probability of each sum by counting the occurrences and dividing by the total number of combinations.<br><br>
   <img width="661" alt="Screenshot 2024-02-25 224834" src="https://github.com/Marcus270503/Securin_Assessment/assets/103208421/9f46270e-8750-4071-bed0-9fd1b0925d58">

<h2>Part - B</h2>

Undoom Dice<br>
   I devised a function called undoom_dice. I iterated through each face of Die A, checking if the number of spots exceeded 4. If it did, I replaced it with 4, ensuring that no face had more than 4 spots. Die B was simply copied as is since it could have any number of spots.<br><br>
    <img width="633" alt="Screenshot 2024-02-25 224852" src="https://github.com/Marcus270503/Securin_Assessment/assets/103208421/0b73acb6-d92c-44ea-8d26-60e4550bbfcf">


