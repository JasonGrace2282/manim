from manim import *


class TrigTheorem(Scene):
    def construct(self):
        # formulae
        eq1 = MathTex("a^2+b^2=c^2")
        eq2 = MathTex(r"\frac{a^2+b^2}{c^2}=1")
        eq3 = MathTex(r"\frac{a^2}{c^2}+\frac{b^2}{c^2}=1")
        eq4 = MathTex(r"\left(\frac{a}{c}\right)^2+\left(\frac{b}{c}\right)^2=1")
        eq5 = MathTex(r"(\sin\theta)^2+(\cos\theta)^2=1")
        eq6 = MathTex(r"\sin^2\theta+\cos^2\theta=1")
        eq7 = MathTex(r"\frac{\sin^2\theta+\cos^2\theta}{\cos^2\theta}=\frac{1}{\cos^2\theta}")
        eq8 = MathTex(r"\frac{\sin^2\theta}{\cos^2\theta}+\frac{\cos^2\theta}{\cos^2\theta}=(\sec\theta)^2")
        eq9 = MathTex(r"\tan^2\theta+1=\sec^2\theta")
        
        # text
        intro = MathTex(r"\text{The algebraic derivation of }\sin^2\theta+\cos^2\theta=1")
        triangle_txt = Text("Let's start by creating a right triangle")
        step1 = Text("From this, we can use the pythagorean theorem.").to_edge(UP)
        step2 = Text("Now some algebra").to_edge(UP)
        step3 = MathTex(r"\text{Recall our triangle again. Notice that }\sin\theta=\frac{a}{c}\text{ and }\cos\theta=\frac{b}{c}").to_edge(UP)
        conclusion = Text("There we have our theorem!").to_edge(UP)
        bonus = Text("BONUS").to_edge(UP)
        
        
        # triangle
        A, B, C = 2 * UR, 2 * DR, 2 * DL
        triangle = Polygon(A, B, C)             
        angle = Angle.from_three_points(B, C, A, radius=0.75)
        right_angle = Angle.from_three_points(A, B, C, elbow=True)
        theta = MathTex(r"\theta").move_to([-1, -1.5, 0])
        side_labels = [MathTex("a").move_to([3, 0, 0]), MathTex("b").move_to([0, -3, 0]), MathTex("c").move_to([-1, 0, 0])]
        triangle_group = VGroup(triangle, theta, angle, *side_labels, right_angle)
        
        # animation starts
        self.add(intro)
        self.wait(1.5)
        self.play(ShrinkToCenter(intro), Write(triangle_txt))
        self.wait(1.5)
        
        # play triangle
        self.play(
            triangle_txt.animate.to_edge(UP), 
            GrowFromCenter(triangle_group)
            )
        self.wait(1)
        self.play(ShrinkToCenter(triangle_txt), Write(step1))
        self.wait(1.5)
        self.play(
            ShrinkToCenter(step1), 
            triangle_group.animate.scale(0.5).shift(UL*2+LEFT*3)
        )
        
        # Algebra
        self.play(FadeIn(eq1))
        self.wait(1.5)
        self.play(Write(step2))
        self.wait(1.5)
        self.play(ShrinkToCenter(step2), TransformMatchingShapes(eq1, eq2))
        self.wait(1.5)
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1.5)
        self.play(Write(step3))
        self.wait(2.5)
        self.play(ShrinkToCenter(step3), TransformMatchingTex(eq4, eq5))
        self.wait(3)
        self.play(TransformMatchingShapes(eq5, eq6))
        self.play(Wiggle(eq6), Write(conclusion))
        self.wait(2.5)
        self.play(ShrinkToCenter(conclusion), Write(bonus))
        self.wait(2)
        self.play(TransformMatchingShapes(eq6, eq7))
        self.wait(2.5)
        self.play(TransformMatchingShapes(eq7, eq8))
        self.wait(2.5)
        self.play(TransformMatchingShapes(eq8, eq9))
        self.wait(3.5)
        self.play(Wiggle(eq9))