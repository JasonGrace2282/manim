from manim import *
from typing import Callable


class LT(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )
        
    def long_text(self, text: str):
        return Tex(r"{8cm}"+text, tex_environment="minipage",)
    
    def packages(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")
        
    def do(self, func, *args, **kwargs):
        '''Performs a function and resets self.moving_mobjects to an empty list.'''
        assert isinstance(func, Callable)
        func(*args, **kwargs)
        self.moving_mobjects = []
    
    def BraceFromPoints(self, point_a, point_b, label, buff):
        dummy = Line(point_a, point_b)
        alpha = dummy.get_angle()+PI/2
        brace = BraceLabel(dummy, label, brace_direction=[np.cos(alpha),np.sin(alpha),0], buff=buff)
        return brace    
    
    def construct(self):
        self.packages()
        
        # Shapes
        background = FullScreenRectangle(fill_color=BLACK, color=BLACK, fill_opacity=1)
        transformation_matrix = ((1, 2), (2, 1))
        inverse = ((-1/3, 2/3), (2/3, -1/3))
        
        iBrace = BraceBetweenPoints([0, 0, 0], [1, 0, 0])
        jBrace = BraceBetweenPoints([0, 1, 0], [0, 0, 0])
        iText = iBrace.get_tex(r"\hat{i}")
        jText = jBrace.get_tex(r"\hat{j}")
        
        xy = Matrix((('x'), ('y')), include_background_rectangle=True).set_column_colors([RED, BLUE], [RED, BLUE])
        matrix = Matrix(((0, 0), (0, 0)), include_background_rectangle=True).to_edge(DR).set_column_colors([RED, BLUE], [RED, BLUE])
        initial_matrix = Matrix(((1, 0), (0, 1)), include_background_rectangle=True).to_edge(DR).set_column_colors([RED, BLUE], [RED, BLUE])
        postMatrix = Matrix(((1, 0), (0, 1)), include_background_rectangle=True).to_edge(DL).set_column_colors([RED, BLUE], [RED, BLUE])
        postMatrixFilled = Matrix(transformation_matrix, include_background_rectangle=True).to_edge(DL).set_column_colors([RED, BLUE], [RED, BLUE])
        postXY = Matrix((('x'), ('y')), include_background_rectangle=True).set_column_colors([RED, BLUE], [RED, BLUE])
        xy.next_to(matrix, LEFT, buff=0.5)
        postXY.next_to(postMatrix, RIGHT)
        
        vector = Vector([2, 2], color=YELLOW)
        iHat = Vector([1, 0])
        jHat = Vector([0, 1])
        iCoords = iHat.coordinate_label()
        jCoords = jHat.coordinate_label()
        iAfter = Vector((1, 2))
        jAfter = Vector([2, 1])
        iCoordsAfter = iAfter.coordinate_label()
        jCoordsAfter = jAfter.coordinate_label()
        i = self.BraceFromPoints(iAfter.get_start(), iAfter.get_end(), r"\hat{i}", buff=0.1).set_color(GREEN)
        j = self.BraceFromPoints(jAfter.get_end(), jAfter.get_start(), r"\hat{j}", buff=0.1).set_color(RED)
        
        # Text
        vec = MathTex(r"\vec{v}").next_to(vector)
        intro = self.long_text("What does a matrix represent?")
        text1 = self.long_text("To learn what they are, let's learn about vectors")
        text2 = self.long_text("Vectors are something with both direction and magnitude, and are typically represented as arrows").to_edge(UP)
        text3 = self.long_text(r"The unit vectors are vectors with magnitude 1 unit and are always along a single axis. In this case, the red vector is called $\hat{j}$ and the green $\hat{i}$").to_edge(UP)
        text4 = self.long_text(r"Now lets take a look at matricies. Matricies are a way of writing a linear transformation").to_edge(UP)
        text5 = self.long_text(r"Let's take an example. First let's record the initial positions of $\hat{i}$ and $\hat{j}$").to_edge(UP)
        initial_pos_txt = self.long_text(r"Let's record the $\hat{i}$ coordinates in the first column, and the $\hat{j}$ coordinates in the second column").to_edge(UP)
        initial_pos = self.long_text(r"We get the matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$").to_edge(UP)
        text6 = self.long_text(r"Watch what happens to $\hat{i}$ and $\hat{j}$ when we apply the linear transformation $\begin{bmatrix}1 & 2\\ 2 & 1\end{bmatrix}$").to_edge(UP)
        text7 = self.long_text(r"Now take a look at the new location of $\hat{i}$ and $\hat{j}$").to_edge(UP)
        text8 = self.long_text(r"Lets now record the final position of $\hat{i}$ and $\hat{j}$").to_edge(UP)
        text9 = self.long_text(r"We get the matrix $\begin{bmatrix}1 & 2\\ 2 & 1\end{bmatrix}$, which is the same matrix we applied the transformation as.").to_edge(UP)
        text10 = self.long_text(r"So now we know that the left column of a matrix represents where the $\hat{i}$ unit vector lands, and the right column where the $\hat{j}$ unit vector lands").to_edge(UP)
        text11 = self.long_text("And that is what a matrix is! A way of saying where the unit vectors land! But what does multiplying a matrix with a vector mean?")
        text12 = self.long_text(r"Let's see what happens to a vector when we apply the transformation $\begin{bmatrix}1 & 2\\ 2 & 1\end{bmatrix}$").to_edge(UP)
        
        self.remove(self.plane)
        self.do(self.add, background)
        self.play(Write(intro))
        self.wait(4)
        self.play(Write(text1), Uncreate(intro))
        self.wait(4)
        self.do(self.remove, background)
        self.play(Write(text2),
                  Uncreate(text1),
                  Create(vec),
                  Create(vector)
                  )
        self.wait(4)
        self.play(Write(text3),
                Uncreate(text2),
                Create(iBrace),
                Create(jBrace),
                Create(iText),
                Create(jText)
                )
        self.wait(4)
        self.play(Write(text4),
                  Uncreate(text3),
                  Uncreate(iText),
                  Uncreate(jText),
                  Uncreate(iBrace),
                  Uncreate(jBrace),
                  Uncreate(vec),
                  Uncreate(vector)
                  )
        self.wait(4)
        self.play(Write(text5),
                  Uncreate(text4),
                  Create(matrix),
                  Create(xy),
                  Create(iCoords),
                  Create(jCoords)
                  )
        self.wait(4)
        self.play(Write(initial_pos_txt), Uncreate(text5))
        self.wait(4)
        self.do(self.remove, matrix, jCoords, iCoords)
        self.play(Create(initial_matrix))
        self.wait(4)
        self.play(Write(initial_pos), Uncreate(initial_pos_txt))
        self.wait(4)
        self.play(Write(text6),
                  Uncreate(initial_pos),
                  Create(postMatrix),
                  Create(postXY)
                  )
        self.wait(4)
        self.do(self.add, self.plane)
        self.do(self.apply_matrix, transformation_matrix)
        self.wait(4)
        self.play(Create(text7),
                  Uncreate(text6),
                  Create(iCoordsAfter),
                  Create(jCoordsAfter),
                  )
        self.wait(4)
        self.play(
            Uncreate(text7),
            Create(text8),
            Uncreate(postMatrix),
            Create(postMatrixFilled),
            Create(i),
            Create(j)
        )
        self.wait(4)
        self.play(Uncreate(text8), Create(text9))
        self.wait(4)
        self.play(Uncreate(text9), Create(text10))
        self.wait(4)
        self.do(self.add, background)
        self.do(self.remove, postMatrix, postXY, iCoordsAfter, jCoordsAfter, initial_matrix, xy)
        self.play(Uncreate(text10), Create(text11))
        self.do(self.remove, self.plane)
        self.do(self.apply_matrix, inverse, run_time = 0)
        self.wait(4)
        self.play(Uncreate(text11), Create(text12))
        self.do(self.add, self.plane)
        self.do(self.add_vector, vector)
        self.wait(2)
