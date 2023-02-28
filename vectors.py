from manim import *


class LT(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_foreground_plane=False,
        )
        
    def long_text(self, text: str):
        return Tex(r"{8cm}"+text, tex_environment="minipage",)
    
    def packages(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")
    
    def construct(self):
        self.packages()
        
        # Shapes
        background = FullScreenRectangle(fill_color=BLACK, color=BLACK, fill_opacity=1)
        iBrace = BraceBetweenPoints([0, 0, 0], [1, 0, 0])
        jBrace = BraceBetweenPoints([0, 1, 0], [0, 0, 0])
        iText = iBrace.get_tex(r"||\hat{i}||=1")
        jText = jBrace.get_tex(r"||\hat{j}||=1")
        xy = Matrix((('x'), ('y')), include_background_rectangle=True).set_column_colors([RED, BLUE], [RED, BLUE])
        matrix = Matrix(((0, 0), (0, 0)), include_background_rectangle=True).to_edge(DR).set_column_colors([RED, BLUE], [RED, BLUE])
        initial_matrix = Matrix(((1, 0), (0, 1)), include_background_rectangle=True).to_edge(DR).set_column_colors([RED, BLUE], [RED, BLUE])
        xy.next_to(matrix, LEFT, buff=0.5)
        vector = Vector([2, 2], color=YELLOW)
        iHat = Vector([1, 0])
        jHat = Vector([0, 1])
        iCoords = iHat.coordinate_label()
        jCoords = jHat.coordinate_label()
        transformation_matrix = ((1, 2), (2, 2))
        
        # Text
        vec = MathTex(r"\vec{v}").next_to(vector)
        intro = self.long_text("What does a matrix represent?")
        text1 = self.long_text("To learn what they are, let's learn about vectors")
        text2 = self.long_text("Vectors are something with both direction and magnitude, and are typically represented as arrows").to_edge(UP)
        text3 = self.long_text("The unit vectors are vectors with magnitude 1 unit and are always along a single axis").to_edge(UP)
        text4 = self.long_text("Now lets take a look at matricies. Matricies are a way of writing a linear transformation").to_edge(UP)
        text5 = Tex(r"{8cm}Let's take an example. First let's record the initial positions of $\hat{i}$ and $\hat{j}$", tex_environment="minipage",).to_edge(UP)
        initial_pos_txt = Tex(r"{8cm}Let's record the $\hat{i}$ coordinates in the first column, and the $\hat{j}$ coordinates in the second column", tex_environment="minipage",).to_edge(UP)
        initial_pos = Tex(r"{8cm}We get the matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$"
                          , tex_environment="minipage",).to_edge(UP)
        text6 = Tex(r"{8cm}Watch what happens to $\hat{i}$ and $\hat{j}$ when we apply the linear transformation", tex_environment="minipage",).to_edge(UP)
        
        self.add(background)
        self.play(Write(intro))
        self.wait(2)
        self.play(Write(text1), Uncreate(intro))
        self.wait(2)
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
        self.wait(2)
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
        self.wait(2)
        self.play(Write(text5),
                  Uncreate(text4),
                  Create(matrix),
                  Create(xy),
                  Create(iCoords),
                  Create(jCoords)
                  )
        self.wait(2)
        self.play(Write(initial_pos_txt), Uncreate(text5))
        self.wait(2)
        self.remove(matrix, jCoords, iCoords)
        self.play(Create(initial_matrix))
        self.wait(2)
        self.play(Write(initial_pos), Uncreate(initial_pos_txt))
        self.wait(2)
        self.play(Write(text6), Uncreate(initial_pos))
        self.wait(2)
        self.add(NumberPlane())
        self.moving_mobjects = []
        self.apply_matrix(transformation_matrix)
        self.play(ApplyMatrix(transformation_matrix, NumberPlane()))
