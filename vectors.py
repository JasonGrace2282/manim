from manim import *


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
        func(*args, **kwargs)
        self.moving_mobjects = []
        
    
    def construct(self):
        self.packages()
        
        # Shapes
        background = FullScreenRectangle(fill_color=BLACK, color=BLACK, fill_opacity=1)
        transformation_matrix = ((1, 2), (2, 1))
        
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
        postXY.next_to(postMatrix, LEFT)
        
        vector = Vector([2, 2], color=YELLOW)
        iHat = Vector([1, 0])
        jHat = Vector([0, 1])
        iCoords = iHat.coordinate_label()
        jCoords = jHat.coordinate_label()
        iCoordsAfter = Vector([1, 2]).coordinate_label()
        jCoordsAfter = Vector([2, 1]).coordinate_label()
        i, j = BraceBetweenPoints([1, 2, 0], [0, 0, 0]), BraceBetweenPoints([0, 0, 0], [2, 1, 0])
        iTextAfter = i.get_tex(r"\hat{i}")
        jTextAfter = j.get_tex(r"\hat{j}")
        
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
        self.add(background)
        self.play(Write(intro))
        self.wait(4)
        self.play(Write(text1), Uncreate(intro))
        self.wait(4)
        self.remove(background)
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
        self.remove()
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
        self.remove(matrix, jCoords, iCoords)
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
            Create(j),
            Create(iTextAfter),
            Create(jTextAfter)
        )
        self.wait(4)
        self.play(Uncreate(text8), Create(text9))
        self.wait(4)
        self.play(Uncreate(text9), Create(text10))
        self.wait(4)
        self.add(background)
        self.remove(postMatrix, postXY, self.plane, iCoordsAfter, jCoordsAfter, initial_matrix, xy)
        self.play(Uncreate(text10), Create(text11))
        self.do(self.apply_inverse, transformation_matrix)
        self.wait(4)
        self.play(Uncreate(text11), Create(text12))
        self.do(self.add, self.plane)
        self.do(self.add_vector, vector)
        self.wait(2)
