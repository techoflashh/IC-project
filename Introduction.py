from manim import *


class Constant(Scene):
    def construct(self):
        name = Tex("DMC", color = RED).scale(0.8).to_edge(UR).shift(LEFT*2.5)
        box = SurroundingRectangle(
            name, color=BLACK, fill_opacity=0.5, fill_color=WHITE, buff=0.2)
        for i in range(10):
            sublist = ['1','2','i','n']
            padx = 1.1
            pady = 0.9
            for e in sublist:
                x1 = MathTex(f"x_{e}").next_to(box, LEFT, buff=1.5)
                self.bring_to_back(name)
                self.bring_to_front(box)
                self.bring_to_back(x1)
                joint = Line(color = PURPLE, buff = 0.1)
                joint.put_start_and_end_on(x1.get_right(), box.get_left())
                self.bring_to_front(joint)
                tri = Triangle(fill_color = BLUE, fill_opacity = 0.75).scale(0.2).rotate(270*DEGREES).next_to(box, LEFT, buff=padx)
                self.play(tri.animate.shift(RIGHT*padx))
                self.remove(x1)
                self.remove(tri)
                y1 = MathTex(f"y_{e}").next_to(box, RIGHT, buff = 1.5)
                self.bring_to_back(y1)
                joint.put_start_and_end_on(y1.get_left(), box.get_right())
                tri = Triangle(fill_color = BLUE, fill_opacity = 0.75).scale(0.2).rotate(270*DEGREES).next_to(box, RIGHT)
                self.play(tri.animate.shift(RIGHT*pady))
                self.remove(y1)
                self.remove(tri)
                self.remove(joint)

class intro(Scene):
    def construct(self):
        Topic = Tex("Capacity Theorems For the Relay Channel").scale(1.5)
        constant_scene = Constant()
        constant_scene.construct()
        self.play(Write(Topic))
        self.play(Topic.animate.to_edge(UL).scale(0.5).shift(LEFT*4),run_time = 2)
        self.add(constant_scene)
        name = Tex("DMC", color=RED).scale(0.8)
        box = always_redraw(lambda:SurroundingRectangle(
            name, color=BLACK, fill_opacity=0.5, fill_color=WHITE, buff=0.2))
        self.bring_to_back(name,box)
        self.wait()

class combined(Scene):
    def construct(self):
        Topic = Tex("Capacity Theorems For the Relay Channel").scale(1.5)
        self.play(Write(Topic))
        self.play(Topic.animate.to_edge(UL).scale(0.5).shift(LEFT*4),run_time = 2)
        self.wait()
        name = Tex("DMC", color=RED).scale(0.8)
        box = always_redraw(lambda:SurroundingRectangle(
            name, color=BLACK, fill_opacity=0.5, fill_color=WHITE, buff=0.2))
        sublist = ['1', '2', 'i', 'n']
        padx = 1.1
        pady = 0.9
        for e in sublist:
            x1 = MathTex(f"x_{e}").next_to(box, LEFT, buff=1.5)
            self.bring_to_back(name)
            self.bring_to_front(box)
            self.bring_to_back(x1)
            joint = Line(color=PURPLE, buff=0.1)
            joint.put_start_and_end_on(x1.get_right(), box.get_left())
            self.bring_to_front(joint)
            tri = Triangle(fill_color=BLUE, fill_opacity=0.75).scale(0.2).rotate(270 * DEGREES).next_to(box, LEFT, buff=padx)
            self.play(tri.animate.shift(RIGHT * padx))
            self.remove(x1)
            self.remove(tri)
            y1 = MathTex(f"y_{e}").next_to(box, RIGHT, buff=1.5)
            self.bring_to_back(y1)
            joint.put_start_and_end_on(y1.get_left(), box.get_right())
            tri = Triangle(fill_color=BLUE, fill_opacity=0.75).scale(0.2).rotate(270 * DEGREES).next_to(box, RIGHT)
            self.play(tri.animate.shift(RIGHT * pady))
            self.remove(y1)
            self.remove(tri)
            self.remove(joint)
        self.play(name.animate.to_edge(UR).shift(LEFT*2.5))
        self.wait()


# class Constant(Scene):
#     @AlwaysRepeat
#     def construct(self):
#         name = Tex("DMC", color=RED).scale(0.8).to_edge(UL).shift(RIGHT * 2.5)
#         box = SurroundingRectangle(
#             name, color=BLACK, fill_opacity=0.5, fill_color=WHITE, buff=0.2)
#         i = 0
#         sublist = ['1', '2', 'i', 'n']
#         padx = 1.1
#         pady = 0.9
#         for e in sublist:
#             x1 = MathTex(f"x_{e}").next_to(box, LEFT, buff=1.5)
#             self.bring_to_back(name)
#             self.bring_to_front(box)
#             self.bring_to_back(x1)
#             joint = Line(color=PURPLE, buff=0.1)
#             joint.put_start_and_end_on(x1.get_right(), box.get_left())
#             self.bring_to_front(joint)
#             tri = Triangle(fill_color=BLUE, fill_opacity=0.75).scale(0.2).rotate(270 * DEGREES).next_to(box, LEFT, buff=padx)
#             self.play(tri.animate.shift(RIGHT * padx))
#             self.remove(x1)
#             self.remove(tri)
#             y1 = MathTex(f"y_{e}").next_to(box, RIGHT, buff=1.5)
#             self.bring_to_back(y1)
#             joint.put_start_and_end_on(y1.get_left(), box.get_right())
#             tri = Triangle(fill_color=BLUE, fill_opacity=0.75).scale(0.2).rotate(270 * DEGREES).next_to(box, RIGHT)
#             self.play(tri.animate.shift(RIGHT * pady))
#             self.remove(y1)
#             self.remove(tri)
#             self.remove(joint)

# class Intro(Scene):
#     def construct(self):
#         topic = Tex("Capacity Theorems For the Relay Channel").scale(1.5)
#         topic.to_edge(UL).shift(LEFT * 4)



#         self.play(Write(topic))
#         self.wait()
#         self.add(constant_scene)  # Add the constant_scene to the scene
#         self.wait()
