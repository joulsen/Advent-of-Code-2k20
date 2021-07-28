# Advent of Code 2020 - Day 9

## Explanation of get_sums()

This small document explains how `get_sums()` calculates the sum of all the numbers inputted. This is a bit troublesome to describe in the source, which is why it will happen here.

For simplicity's sake, assume a list of 4 numbers which we will call `number`:
$$
\texttt{number} = \left[ x_1, x_2, x_3, x_4 \right]
$$
The numpy command `np.meshgrid(number, number)` is called in line 35 and will create the 2D grid that spans from `number` to `number` such that it will create the points in $\mathfrak{V}$
$$
\mathfrak{V} = \left\{ (x_1, x_1), (x_1, x_2), (x_1,x_3), \dots (x_2, x_1), (x_2, x_2),\dots (x_4, x_4) \right\}
$$
In practice it exports the following two arrays
$$
A_1 = \begin{bmatrix}
x_1 & x_1 & x_1 & x_1 \\ 
x_2 & x_2 & x_2 & x_2 \\
x_3 & x_3 & x_3 & x_3 \\
x_4 & x_4 & x_4 & x_4 \\
\end{bmatrix}
,\qquad
A_2 = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 \\ 
x_1 & x_2 & x_3 & x_4 \\
x_1 & x_2 & x_3 & x_4 \\
x_1 & x_2 & x_3 & x_4 \\
\end{bmatrix}
$$

Notice that $A_1 = A_2^\top$ (transposed) since `np.meshgrid` receives the same argument for both axes.

Next these to matrices are added using `np.add()` also on line 35. This produces the matrix we will call $B$
$$
B = A_1 + A_2 =
\begin{bmatrix}
x_1 + x_1 & x_1 + x_2 & x_1 + x_3 & x_1 + x_4 \\ 
x_2 + x_1 & x_2 + x_2 & x_2 + x_3 & x_2 + x_4 \\
x_3 + x_1 & x_3 + x_2 & x_3 + x_3 & x_3 + x_4 \\
x_4 + x_1 & x_4 + x_2 & x_4 + x_3 & x_4 + x_4 \\
\end{bmatrix}
$$
You may notice that all possible products of the values in `numbers` are present in this matrix $B$. You may also notice that all the elements except the diagonal elements are present twice. The [upper triangular](https://en.wikipedia.org/wiki/Triangular_matrix) part of the matrix is the same as the lower and as such we merely seperate out the upper triangular part using the function `np.triu()` on line 36.

Now we notice that the diagonal entries are useless for us in this exercise as they represent adding a number to itself which is not permitted. Therefore we set the diagonals to zero using `np.fill_diagonals()` on line 37 which does this operation in-place. By doing `np.triu()` followed by `np.fill_diagonals()` we acquire the new matrix $C$ 
$$
C =
\begin{bmatrix}
0 & x_1 + x_2 & x_1 + x_3 & x_1 + x_4 \\ 
0 & 0 & x_2 + x_3 & x_2 + x_4 \\
0 & 0 & 0 & x_3 + x_4 \\
0 & 0 & 0 & 0 \\
\end{bmatrix}
$$
The last three lines 38-40 simply flatten this array and mask away all the zeros. This leaves us with all sums of any two numbers in `number` which was what we wanted from this function anyways.