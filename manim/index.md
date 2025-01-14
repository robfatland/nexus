# [manim](https://github.com/3b1b/manim)


manim [(community documentation link)](https://docs.manim.community) is a Python package created by educator 
Grant Sanderson for building video content (particularly on mathematics) for publication on YouTube. A good 
sign of longevity: There is a lot of [community activity building plugins](https://plugins.manim.community/).


- [Install `manim` out of `conda-forge`]()
- For rendering equations also [install LaTeX](). 
- Create Python code and save as `myvideo.py`

```
import manim as m
class Scene1(m.Scene):
    def construct(self):
        c = m.Circle(2, color = m.RED, fill_opacity = 0.6)
        self.play(m.DrawBorderThenFill(c), run_time = 1.0)
        title = m.Text("Bumpkin", font_size = 60, slant = "ITALIC").shift(m.UP * 0.3)
        subtitle = m.Text("Dynamics", font_size = 40, slant = "ITALIC").shift(m.DOWN * 0.3)
        self.play(m.Write(title), m.Write(subtitle))
        self.wait(1)
        a = m.Arc(3.0, m.TAU * (1/2), -m.TAU * (3/4), color = m.GREEN, stroke_width = 30)
        self.play(m.Create(a))
        self.wait(3)
        return
```


Instructive facets of manim syntax are found in this simple example.
[(Source: this intro video](https://youtu.be/rIgOfmcd1iA?si=t8BqPVyawcqyPXg2)
by Mitko Nikov.) 


- Use the `manim` utility to render the Python (cinematography!) file as a video:


```
python -m manim myvideo.py Scene1
```


Locate and view the output, in my case at `/home/myusername/manim/media/videos/myvideo/1080p60/Scene1.mp4`.
