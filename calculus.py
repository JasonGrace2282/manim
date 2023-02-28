from manim import *

class Derivative(Scene):
    def d_dx(self):
        # Setup
        # Text
        text2 = MathTex(r"\text{How would you find the slope of this curve at the point }\left(3, f\left(3\right)\right)\text{?}", font_size=20).to_edge(UP)
        text3 = Text("Lets start by taking a simpler example: a line", font_size=20).to_edge(UP)
        text4 = MathTex(r"\text{The slope of a line is given by }\frac{y_2-y_1}{x_2-x_1}", font_size=20).to_edge(UP)
        text5 = Text("Notably, the slope of this line is the same as the slope of the line tangent to each point", font_size=20).to_edge(UP)
        # text6 = Text("Remember that the slope of a line shows how the line is changing at a point", font_size=20).to_edge(UP)
        # text7 = Text("And that the slope of the line tangent to it, given by our slope formula, does the same thing").to_edge(UP)
        # text8 = Text("Lets try not finding the slope of the curve at a point, but rather the slope of the tangent line at that point", font_size=20).to_edge(UP)
        # text9 = Text("Lets start by approximating that point as the change in two nearby points to the point we want to find, (x, y).", font_size=20).to_edge(UP)
        # bonus_txt = MathTex(r"\text{Lets make the first point the point we want to find, }\left(x, f(x)\right)\text{, and the other point x plus some distance: }\left(x+\Delta x, f(x+\Delta x)\right)", font_size=20).to_edge(UP)
        # text10 = MathTex(r"\text{The slope will be the slope of the secant line passing through those points, given by }\frac{f(x+\Delta x)-f(x)}{(x+\Delta x)-x}", font_size=20).to_edge(UP)
        # text11 = Text("But what if we move those points closer to the actual point, (x,y)?", font_size=20).to_edge(UP)
        # text12 = Text("Notice that the slope of the secant line approaches the slope of the tangent line!", font_size=20).to_edge(UP)
        # text13 = MathTex(r"\text{Therefore if we evauluate }\lim{\Delta x\to0}\text{, we can find the slope of the tangent line!}", font_size=20).to_edge(UP)
        # text14 = Text("And that is the definition of the derivative!", font_size=20).to_edge(UP)
        
        ax = Axes([-2, 5, 1], [-2, 5, 1])
        func = MathTex("y=x^3-4x^2+3x+1")
        
        
        
        
        # Linear
        graph_line = ax.plot(lambda x: x, color=RED)
        tan_line_linear = DashedVMobject(ax.plot(lambda x: x, color=BLUE))
        
        
        # Curved
        f1 = lambda x: x**3-4*x*x+3*x+1
        graph = ax.plot(f1, x_range=[-5, 10], use_smoothing = False, color = BLUE)
        t_0 = ValueTracker(0)
        t_1 = ValueTracker(1)
        point = Dot([2.9, f1(3), 0], color=RED)

        dot_0 = Dot(point=ax.coords_to_point(t_0.get_value(), f1(t_0.get_value())), color=RED)
        dot_1 = Dot(point=ax.coords_to_point(t_1.get_value(), f1(t_1.get_value())), color=RED)

        dot_0.add_updater(lambda x: x.move_to(ax.c2p(t_0.get_value(), f1(t_0.get_value()))))
        dot_1.add_updater(lambda x: x.move_to(ax.c2p(t_1.get_value(), f1(t_1.get_value()))))

        line_0 = Line(dot_0.get_center(),dot_1.get_center(), color=RED).scale(4)
        line_0.add_updater(lambda z: z.become(Line(dot_0.get_center(), dot_1.get_center(), color=RED).scale(25)))
        
        # Animations
        self.play(Write(text2))
        self.play(FadeIn(ax), Create(graph), FadeIn(point))
        self.wait(2)
        self.play(FadeOut(text2), Write(text3), FadeOut(graph), FadeOut(point))
        self.wait(2)
        self.play(Create(graph_line))
        self.wait(2)
        self.play(ShrinkToCenter(text3), Write(text4))
        self.wait(2)
        self.play(FadeOut(text4), Write(text5), Create(tan_line_linear), FadeOut(graph_line))
        self.wait(2)
        self.play(FadeOut(graph_line), FadeOut(tan_line_linear), Create(graph))
        self.wait(2)
        self.play(FadeIn(dot_0, dot_1), FadeIn(line_0))
        self.play(t_1.animate.set_value(0.5))
        
    def construct(self):
        # Text
        intro= Tex(r"{8cm}What does a derivative mean? What is an integral? Lets take a look", tex_environment="minipage",)
        derivative = Text("Let's start with the derivative")
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(intro.animate.to_edge(UP), Write(derivative))
        self.wait(2)
        self.play(FadeOut(intro), ShrinkToCenter(derivative))
        self.d_dx()
        