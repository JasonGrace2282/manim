from manim import *


class Addition(Scene):
    def construct(self):
        # Setup
        ax = Axes(
            y_range=[-1, 5],
            axis_config={'include_numbers': True}
            )
        
        title = Title("Vector Addition")
        title_geo = Title("Vector Addition Geometrically")
        title_alg = Title("Vector Addition Algebraically")
        
        v1 = Vector((-1, 2), color=YELLOW).shift(2*DOWN)
        v2 = Vector((2, 1), color=GREEN).shift(2*DOWN)
        v1_label = MathTex(r"\vec{a}=\begin{bmatrix}-1\\2\end{bmatrix}").next_to(v1, LEFT)
        v2_label = MathTex(r"\vec{b}=\begin{bmatrix}2\\1\end{bmatrix}").next_to(v2, RIGHT)
        v3 = MathTex(r"\vec{a}+\vec{b}=\begin{bmatrix}1\\3\end{bmatrix}")
        
        vec_eq = MathTex(r"\vec{a}+\vec{b}=\vec{c}").next_to(title_alg, DOWN)
        eq = MathTex(
                r"\begin{bmatrix}-1\\2\end{bmatrix}+\
                \begin{bmatrix}2\\1\end{bmatrix}\\", r"\
                =\begin{bmatrix}-1+2\\2+1\end{bmatrix}\\", r"\
                    =\begin{bmatrix}1\\3\end{bmatrix}").next_to(vec_eq, DOWN)
        
        
        ax_transformation_val = [0, 2, 0]
        
        self.play(Create(title))
        self.wait(3)
        self.play(Uncreate(title))
        self.play(
            Create(ax),
            Create(title_geo)
        )
        self.play(
            Create(v1),
            Create(v2),
            Create(v1_label),
            Create(v2_label)
            )
        self.wait(5)
        self.play(
            v1_label.animate.to_edge(LEFT).shift(3*UP),
            v2_label.animate.to_edge(LEFT).shift(2*UP)
            )
        self.wait(3)
        self.play(v1.animate.shift(2*RIGHT+UP))
        self.wait(3)
        self.play(
            Create(ab:=Vector(v1.get_end()+ax_transformation_val,
                              color=RED).shift(2*DOWN)),
            Create(v3_coord:=MathTex(r"\begin{bmatrix}1\\3\end{bmatrix}").move_to(v1.get_end()+[0, 1, 0])),
            Write(MathTex(r"\vec{a}+\vec{b}").next_to(ab, LEFT))
            )
        self.wait(3)
        self.remove(v3_coord)
        self.play(
            v3.animate.to_edge(LEFT).shift(DOWN/1.5),
            )
        self.wait(3)
        self.clear()
        self.play(
            Write(vec_eq),
            Write(eq[0]),
            Write(title_alg)
            )
        self.wait(2)
        self.play(Write(eq[1]))
        self.wait(2)
        self.play(Write(eq[2]))
        self.wait(4)